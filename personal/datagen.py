import requests
from decimal import Decimal, InvalidOperation
from datetime import datetime
from dateutil.relativedelta import relativedelta

FIREBASE_URL = "https://studio-2616610665-59648-default-rtdb.asia-southeast1.firebasedatabase.app/MF.json"
AMFI_URL = "https://www.amfiindia.com/spages/NAVAll.txt"

def fetch_nav_map():
    """Fetch NAV data from AMFI and return a mapping of scheme codes to NAV values."""
    try:
        response = requests.get(AMFI_URL, timeout=30)
        response.raise_for_status()
        lines = response.text.splitlines()
        nav_map = {}
        
        for line in lines:
            parts = line.split(";")
            if len(parts) > 4:
                try:
                    scheme_code = parts[0].strip()
                    nav_str = parts[4].strip()
                    
                    # Skip header row and invalid NAV values
                    if (scheme_code.upper() == 'SCHEME CODE' or 
                        not nav_str or 
                        nav_str.upper() in ['NA', 'N/A', '-', 'NET ASSET VALUE']):
                        continue
                    
                    # Remove any commas and convert to Decimal
                    nav_str = nav_str.replace(',', '')
                    nav = Decimal(nav_str)
                    
                    # Only add if NAV is positive
                    if nav > 0:
                        nav_map[scheme_code] = nav
                        
                except (ValueError, IndexError, InvalidOperation) as e:
                    print(f"Warning: Could not parse line: {line}. Error: {e}")
                    continue
        return nav_map
    except requests.RequestException as e:
        print(f"Error fetching NAV data: {e}")
        return {}

def fetch_firebase_data():
    """Fetch mutual fund data from Firebase."""
    try:
        response = requests.get(FIREBASE_URL, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching Firebase data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing Firebase JSON: {e}")
        return None

def process_funds(data):
    """Process mutual fund data, update SIPs, calculate current values and returns."""
    if not data:
        print("No data to process")
        return data
    
    # Handle both list and dictionary formats
    if isinstance(data, list):
        funds_data = {str(i): fund for i, fund in enumerate(data) if fund is not None}
    else:
        funds_data = data
    
    nav_map = fetch_nav_map()
    if not nav_map:
        print("Warning: Could not fetch NAV data. Using current NAV from fund data.")
    
    today = datetime.today().date()
    updated_funds = []
    
    for fund_id, fund in funds_data.items():
        try:
            # Extract fund data
            scheme_code = str(fund.get("scheme_code", ""))
            total_invested = Decimal(str(fund.get("total_invested", 0)))
            total_units = Decimal(str(fund.get("total_units", 0)))
            sip_amount = Decimal(str(fund.get("sip_amount", 0)))
            
            # Get current NAV from AMFI data
            current_nav = nav_map.get(scheme_code, Decimal(0))
            if current_nav == 0:
                # Fallback to current_nav from fund data
                current_nav = Decimal(str(fund.get("current_nav", 0)))
                print(f"Warning: Using fallback NAV for {fund.get('fund_name', 'Unknown')}: {current_nav}")
            
            # Process SIP if due
            next_sip_due_str = fund.get("next_sip_due_date")
            if next_sip_due_str:
                try:
                    next_sip_due = datetime.strptime(next_sip_due_str, "%Y-%m-%d").date()
                    
                    if next_sip_due <= today and sip_amount > 0:
                        print(f"Processing SIP for {fund.get('fund_name', 'Unknown')}: ₹{sip_amount}")
                        
                        # Add SIP amount to total investment
                        total_invested += sip_amount
                        
                        # Calculate units for SIP purchase
                        sip_units = sip_amount / current_nav if current_nav > 0 else Decimal(0)
                        total_units += sip_units
                        
                        # Update next SIP due date to next month
                        new_due_date = next_sip_due + relativedelta(months=1)
                        fund["next_sip_due_date"] = str(new_due_date)
                        
                        print(f"Updated next SIP due date to: {new_due_date}")
                        
                except ValueError as e:
                    print(f"Error parsing SIP due date {next_sip_due_str}: {e}")
            
            # Calculate current value and returns
            current_value = total_units * current_nav
            returns = current_value - total_invested
            
            # Update fund data
            fund["current_nav"] = float(current_nav)
            fund["total_units"] = float(total_units)
            fund["total_invested"] = float(total_invested)
            fund["current_value"] = float(current_value)
            fund["returns"] = float(returns)
            fund["last_updated"] = str(today)
            
            print(f"Updated: {fund.get('fund_name', 'Unknown')}")
            print(f"  NAV: ₹{current_nav}")
            print(f"  Units: {total_units}")
            print(f"  Current Value: ₹{current_value:,.2f}")
            print(f"  Total Invested: ₹{total_invested:,.2f}")
            print(f"  Returns: ₹{returns:,.2f}")
            print("-" * 50)
            
            updated_funds.append(fund)
            
        except Exception as e:
            print(f"Error processing fund {fund_id}: {e}")
            # Keep original fund if processing fails
            if fund is not None:
                updated_funds.append(fund)
            continue
    
    return updated_funds

def update_firebase(updated_data):
    """Update the processed data back to Firebase."""
    try:
        response = requests.put(FIREBASE_URL, json=updated_data, timeout=30)
        response.raise_for_status()
        print("Firebase updated successfully.")
    except requests.RequestException as e:
        print(f"Error updating Firebase: {e}")

if __name__ == "__main__":
    print("Starting mutual fund data processing...")
    print(f"Current date: {datetime.today().date()}")
    print("=" * 50)
    
    firebase_data = fetch_firebase_data()
    
    if not firebase_data:
        print("No data found or error fetching data.")
    else:
        if isinstance(firebase_data, list):
            fund_count = len([f for f in firebase_data if f is not None])
        else:
            fund_count = len(firebase_data)
            
        print(f"Processing {fund_count} funds...")
        print("=" * 50)
        
        updated = process_funds(firebase_data)
        if updated:
            update_firebase(updated)
        print("Processing complete.")