from typing import Dict
import requests, json, os
from datetime import datetime
from zoneinfo import ZoneInfo

# =========================
# CONFIG
# =========================
DAILY_CAPITAL = 2000
MAX_CAPITAL = 100000

INVEST_STOCKS = {
    # Ultra-strong, compounding machines
    "HDFCBANK": 1333,
    "TCS": 11536,
    "RELIANCE": 2885,
    "INFY": 1594,
    "ICICIBANK": 4963,
    "NESTLEIND": 17963,

    # Strong franchises, slightly cyclical or sector-dependent
    "BHARTIARTL": 10604,
    "ASIANPAINT": 236,
    "ITC": 1660,
    "SUNPHARMA": 3351,
    "HCLTECH": 7229,
    "BAJAJ-AUTO": 16669,
    "APOLLOHOSP": 157,
    "DMART": 19913,

    # Strong but valuation / cyclicality / policy risk
    "SBIN": 3045,
    "AXISBANK": 5900,
    "NTPC": 11630,
    "POWERGRID": 14977,
    "COALINDIA": 20374,
    "CIPLA": 694,

    # Good businesses, higher volatility or execution risk
    "ADANIPORTS": 15083,
    "TRENT": 1964,
    "VBL": 18921,
    "BEL": 383,
    "IRCTC": 13611,
    "CAMS": 342,
    "CDSL": 21174,

    # Financials with mixed quality / leverage sensitivity
    "CHOLAFIN": 685,
    "LTF": 24948,
    "ICICIPRULI": 18652,
    "IDFCFIRSTB": 11184,
    "ABCAPITAL": 21614,

    # Cyclicals and infra-heavy bets
    "TATAMOTORS": 3456,
    "TATASTEEL": 3499,
    "TATAPOWER": 3426,
    "DLF": 14732,
    "GODREJPROP": 17875,
    "ACC": 22,
    "AMBUJACEM": 1270,
    "APLAPOLLO": 25780,

    # High risk / turnaround / speculative
    "JIOFIN": 18143,
    "BDL": 2144,
    "IOC": 1624,
    "NHPC": 17400,
    "GMRINFRA": 13528,
    "ASHOKLEY": 212,
    "IDEA": 14366,
}

INVEST_STOCKS_RISK = {
    "HDFCBANK": 1,
    "TCS": 1,
    "RELIANCE": 1,
    "INFY": 1,
    "ICICIBANK": 1,
    "NESTLEIND": 1,
    "BHARTIARTL": 2,
    "ASIANPAINT": 2,
    "ITC": 2,
    "SUNPHARMA": 2,
    "HCLTECH": 2,
    "BAJAJ-AUTO": 2,
    "APOLLOHOSP": 2,
    "DMART": 2,
    "SBIN": 3,
    "AXISBANK": 3,
    "NTPC": 3,
    "POWERGRID": 2,
    "COALINDIA": 3,
    "MARUTI": 3,
    "CIPLA": 2,
    "ADANIPORTS": 4,
    "TRENT": 4,
    "VBL": 3,
    "BEL": 3,
    "IRCTC": 3,
    "CAMS": 2,
    "CDSL": 3,
    "COLPAL": 2,
    "DIXON": 4,
    "CHOLAFIN": 3,
    "LTF": 4,
    "ICICIPRULI": 3,
    "FEDERALBNK": 3,
    "IDFCFIRSTB": 4,
    "ABCAPITAL": 4,
    "TATAMOTORS": 4,
    "TATASTEEL": 5,
    "TATAPOWER": 4,
    "DLF": 4,
    "GODREJPROP": 4,
    "ACC": 3,
    "AMBUJACEM": 3,
    "APLAPOLLO": 4,
    "JIOFIN": 4,
    "BDL": 3,
    "IOC": 4,
    "NHPC": 3,
    "GMRINFRA": 5,
    "INDUSTOWER": 4,
    "ASHOKLEY": 4,
    "NYKAA": 5,
    "AUROPHARMA": 4,
    "IDEA": 5,
    "SUZLON": 5,
}

ETF_DICT = {
    "ALPHA":        7412,     # Kotak Nifty Alpha 50
    "EVINDIA":      24461,    # EV & new-age mobility theme
    "ITBEES":       19084,    # Nifty IT
    "SML100CASE":   758955,   # Small-cap 100
    "MID150CASE":   24077,    # Mid-cap 150
    "MODEFENCE":    24944,    # Defence sector
    "MOM30IETF":    10585,    # Momentum 30
    "GOLDBEES":     14428,    # Gold hedge
    "OILIETF":      24533,    # Oil & energy
    "TOP20":        760415,   # Top 20 large caps
}

# =========================
# SECRET
# =========================

FIREBASE_URL = os.environ["FIREBASE_URL"]
PAYTM_ORDER_URL = os.environ["PAYTM_ORDER_URL"]
TRADINGVIEW_URL = os.environ["TRADINGVIEW_URL"]

def get_token():
    current_time = datetime.now().strftime('%Y-%m-%d')
    FIREBASE_PTM = FIREBASE_URL + 'ptm.json'
    r = requests.get(FIREBASE_PTM, timeout=100)
    res = r.json()
    dt = datetime.strptime(res.get("dtm"), "%Y-%m-%d").date()
    ist_today = datetime.now(ZoneInfo("Asia/Kolkata")).date()
    if dt == ist_today:
        return res.get("talk")
    return 0

# =========================
# FIREBASE
# =========================
def save_order_to_db(  symbol, ids, datetime, qty, target_price, order_no, off_mkt_flag):
    payload = {order_no:{"symbol": symbol, "ids": ids, 'dtm':datetime, 'qty':qty, 'target_price':target_price,'order_no':order_no,'off_mkt_flag':off_mkt_flag,'status':'Initiated'},}
    r = requests.patch(FIREBASE_URL+"orders.json", json=payload, timeout=50)
    r.raise_for_status()
    print(r.text)

def get_orders():
    r = requests.get(FIREBASE_URL+"orders.json", timeout=200)
    res = r.json()
    Base_res = res
    print("results : ",Base_res)
    if res:
        response = requests.get('https://developer.paytmmoney.com/orders/v1/user/orders', headers={'x-jwt-token': get_token(), 'Content-Type': 'application/json'} )
        responsejson = response.json()
        for book in responsejson.get('data'):
            order_no = book.get('order_no')
            status = book.get('status')
            print(order_no,status)
            if res.get(order_no):
                if res.get(order_no).get('status') != status:
                    print("Oreder Record STATUS**** ", status)
                    res[order_no]['status'] = status
        if Base_res != res:
            r = requests.patch(FIREBASE_URL+"orders.json", payload= res, timeout=500)
            print("Update Status" , r.status_code())

def already_ordered_today(off_mkt_flag):
    r = requests.get(FIREBASE_URL+"orders.json", timeout=200)
    res = r.json()
    symbols = [
        v["symbol"]
        for v in res.values()
        if v.get("status") not in ("O-Cancelled", "Rejected")
           and v.get("off_mkt_flag") == off_mkt_flag
    ]
    return symbols

# =========================
# MARKET DATA
# =========================
def fetch_stock_data(DataDict):
    symbols = [f"NSE:{s}" for s in DataDict]
    columns = [
        "name", "close", "change","change_abs", "high", "low", "ADR","ADRP","ADX-DI",
        "ROC|1W","ROC|1M", "SMA50", "SMA100", "High.3M", "High.6M", "Low.3M",
        "price_target_1y", "price_target_median", "RSI|1","RSI|5","BB.lower",
        "recommendation_buy", "recommendation_sell", "recommendation_total",
    ]
    payload = {
        "symbols": {"tickers": symbols, "query": {"types": []}},
        "columns": columns,
    }
    r = requests.post(TRADINGVIEW_URL, json=payload, timeout=15)
    r.raise_for_status()
    raw = r.json()
    stocks = {}
    for row in raw["data"]:
        stocks[row["s"]] = dict(zip(columns, row["d"]))
    return stocks

# =========================
# STRATEGY
# =========================
def calculate_quantity(price):
    return max(1, int(DAILY_CAPITAL // price))


def evaluate_stock(stock: Dict, ETF = 0 ) -> Dict:
    """
    Evaluates whether a stock is eligible to buy today based on strict
    downtrend + asymmetry logic and computes an intraday buy target.
    """
    now = datetime.now()
    close = stock.get("close", 0)
    high_3m = stock.get("High.3M", 0)
    high_6m = stock.get("High.6M", 0)
    low_3m = stock.get("Low.3M", 0)
    adr = stock.get("ADR", 0)
    adrp = stock.get("ADRP", 0)
    sma50 = stock.get("SMA50", 0)
    sma100 = stock.get("SMA100",0)
    if not sma100:
        sma100=0
    if not sma50:
        sma50=0
    # -------------------------
    #  HARD FILTERS
    #  TIME-BASED TARGET LOGIC
    # -------------------------
    trading_start = now.replace(hour=9, minute=0, second=0, microsecond=0)
    trading_mid = now.replace(hour=12, minute=0, second=0, microsecond=0)
    trading_end = now.replace(hour=15, minute=30, second=0, microsecond=0)
    # Pre-market or post-market → next-day logic
    if now < trading_start or now > trading_end:
        adr_factor = 0.85
        off_mkt_flag = True     #      "next_day_probable_low"
    # Pre-noon aggressive
    elif now <= trading_mid:
        adr_factor = 0.55
        off_mkt_flag = False     #     "intraday_aggressive"
    # Post-noon conservative
    else:
        adr_factor = 0.25
        off_mkt_flag = False    #      "intraday_conservative"

    print("Name:", stock.get("name")," = ",close ,"|Change:", round(stock.get("change"),2),
          "|3M-High:", high_3m, "(", round((high_3m - close)*100/close) ,
          ") |3M-Low:", low_3m," (",round((low_3m - close)*100/close), ") |ADR:",
          adr," (",round(adrp,1), ") |SMA50/100", round(sma50,1), round(sma100,1), "| %SMA50/100% ",
          round((sma50 - close)*100/close) , round((sma100 - close)*100/close)
          )
    print("ROC 1m , 1w - ", stock.get("ROC|1M"), stock.get("ROC|1W")," | ADX-DI +DI", round(stock.get("ADX-DI", 0),2) , round(stock.get("ADX+DI", 0),2))
    # 1. Price moving down
    if not (
            (
                    stock.get("change", 0) < 0.0
                    or off_mkt_flag
            )
            and ( (stock.get("ROC|1W") or 0) < 0
                  or (stock.get("ROC|1M") or 0) < 0) ):
        return {"eligible": False,
                "Reason"  : "Price NOT moving down. Acutally in Uptrend based on ROC."}
    if close > high_3m * 0.95:
        return {"eligible": False,
                "Reason"  : "Near to 3M High. So over Price to invest now. close > high_3m * 0.95"}
    if close > high_6m * 0.93:
        return {"eligible": False,
                "Reason"  : "Near to 3M High. So over Price to invest now. close > high_6m * 0.94"}
    if close > 4000:
        return {"eligible": False,
                "Reason"  : "Out of Budget."}
    if not ETF:
        if stock.get("price_target_1y", 0) < close * 1.10:
            return {"eligible": False,
                    "Reason"  : "No Great sign of Growth(price_target_average). stock.get(price_target_1y, 0) < close * 1.10"}
        if stock.get("price_target_median", 0) < close * 1.10:
            return {"eligible": False,
                    "Reason"  : "No Great sign of Growth(price_target_average). stock.get(price_target_median, 0) < close * 1.10"}
        if not (stock.get("SMA50", 0) > stock.get("close", 0)):
            if not (stock.get("SMA100", 0) > stock.get("close", 0)):
                if stock.get("price_target_median", 0) < close * 1.15:
                    return {"eligible": False,
                            "Reason"  : "Price NOT moving down. Acutally in Uptrend based on SMA."}
        buy = stock.get("recommendation_buy") or 0
        sell = stock.get("recommendation_sell") or 0
        total = stock.get("recommendation_total") or 1
        if buy <= sell or buy <= 0.5 * total:
            return {"eligible": False,
                    "Reason"  : "No Expert Recomendations "
                    }
    if (close - low_3m) >= (high_3m - close):
        return {"eligible": False,
                "Reason"  : "Not Leaning towards 3M Low. (close - low_3m) >= (high_3m - close) "}
    if stock.get("ADX-DI", 0) != 0 and stock.get("ADX+DI", 0) !=0:
        if not (
                stock.get("ADX-DI", 0) > stock.get("ADX+DI", 0)
                and stock.get("ADX-DI", 0) >= 20
        ):
            return {"eligible": False,
                    "Reason"  : "ADX-DI Says no Downwords movement to target."
                    }

    RiskIndex = INVEST_STOCKS_RISK.get(stock.get('name'), 0)
    print(RiskIndex,adr_factor)
    adr_factor+= RiskIndex*0.04
    print(adr_factor)
    vol_target = close - (adr * adr_factor) - (close * 0.02)
    bb_lower = stock.get("BB.lower", vol_target)
    low_3m = stock.get("Low.3M", vol_target)
    structural_target = max(vol_target, bb_lower, low_3m)
    min_move = close - (0.30 * adr)
    target_buy_price = round(min(structural_target, min_move),2)

    return {
        "eligible": True,
        "Reason"  : "All Pass",
        "stock": stock.get("name"),
        "buy_target_price": target_buy_price,
        "off_mkt_flag": off_mkt_flag,
    }

# =========================
# ORDER
# =========================
def place_order(symbol, price, access_token, off_mkt_flag = True , etf = 0):
    price = round(price, 2)
    now = datetime.now()
    print("ORDER -> NOW Time Is : ", now)
    if not etf:
        security_id = INVEST_STOCKS[symbol]
    else:
        security_id = ETF_DICT[symbol]
    qty = calculate_quantity(price)
    payload = {"txn_type": "B", "exchange": "NSE", "segment": "E", "product": "C", "security_id": security_id, "quantity": qty, "validity": "DAY", "order_type": "LMT", "price": price, "source": "N", "off_mkt_flag": off_mkt_flag}
    order_url = 'https://developer.paytmmoney.com/orders/v1/place/regular'
    headers = {'x-jwt-token': access_token, 'Content-Type': 'application/json'}
    print("ORDER -> ", payload, headers, order_url)
    r = requests.post(order_url, headers=headers, json=payload)
    print("ORDER -> ", r.text)
    if not r.text:
        print("ORDER -> Empty response from Paytm")
        raise RuntimeError("Empty response from Paytm")
    return json.loads(r.text)

# =========================
# MAIN
# =========================
def main():
    print("Started...")
    token = get_token()
    if not token:
        print("NO Token Available.")
        exit(0)
    print("Token Fetched...")
    stocks = fetch_stock_data(INVEST_STOCKS)
    investment_threshold = 0
    now = datetime.now()
    trading_start = now.replace(hour=9, minute=0, second=0, microsecond=0)
    trading_end = now.replace(hour=15, minute=30, second=0, microsecond=0)
    if now < trading_start or now > trading_end:
        off_mkt_flag = True     #      "next_day_probable_low"
        print("Out of Market Window")
    else:
        off_mkt_flag = False    #      "intraday_conservative"
        print("Active Market Window")
    already_ordered_today_list = already_ordered_today(off_mkt_flag)
    for full_symbol, data in stocks.items():
        symbol = full_symbol.split(":")[1]
        if symbol in already_ordered_today_list:
            print("Main -> ", symbol , " -> Already Ordered Today")
            continue
        target_dict = evaluate_stock(data, 0)
        if not target_dict.get('eligible'):
            print("Main -> ", symbol , " -> No Target Price | Not Eligible", str(target_dict))
            continue
        target_price = target_dict.get('buy_target_price')
        investment_threshold += target_price
        if investment_threshold > MAX_CAPITAL:
            print("MAX_CAPITAL Reached Exit...")
            continue
        response = place_order(symbol, target_price, token , off_mkt_flag , 0)
        if response.get("status") == "success":
            order_no = response["data"][0]["order_no"]
            save_order_to_db(symbol,INVEST_STOCKS[symbol],datetime.now().strftime("%Y-%m-%d %H:%M:%S"),calculate_quantity(target_price), target_price,order_no, off_mkt_flag)
    print("**ETF World**")
    stocks = fetch_stock_data(ETF_DICT)
    for etf_symbol, data in stocks.items():
        symbol = etf_symbol.split(":")[1]
        print("Main ETF -> ", symbol)
        if symbol in already_ordered_today_list:
            print("Main ETF -> ", symbol , " -> Already Ordered Today")
            continue
        target_dict = evaluate_stock(data, 1)
        if not target_dict.get('eligible'):
            print("Main -> ", symbol , " -> No Target Price | Not Eligible", str(target_dict))
            continue
        target_price = target_dict.get('buy_target_price')
        response = place_order(symbol, target_price, token ,off_mkt_flag , 1)
        if response.get("status") == "success":
            order_no = response["data"][0]["order_no"]
            save_order_to_db(   symbol,ETF_DICT[symbol],datetime.now().strftime("%Y-%m-%d %H:%M:%S"),calculate_quantity(target_price), target_price,order_no, off_mkt_flag)

if __name__ == "__main__":
    main()