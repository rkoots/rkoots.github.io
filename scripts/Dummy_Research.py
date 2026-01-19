import os
import requests
import json
from datetime import datetime, date

# =========================
# CONFIG
# =========================
DAILY_CAPITAL = 2000
MAX_CAPITAL = 20000
ETF_CAPITAL = 20000

INVEST_STOCKS = {
    'RELIANCE':     2885,
    'HDFCBANK':     1333,
    'ICICIBANK':    4963,
    'BEL':          383,
    'BHARTIARTL':   10604,
    'TRENT':        1964,
    'VBL':          18921,
    'BAJFINANCE':   317,
    'SBIN':         3045,
    'NTPC':         11630,
    'TCS':          11536,
    'SUNPHARMA':    3351,
    'JIOFIN':       18143,
    'DMART':        19913,
    'AXISBANK':     5900,
    'ADANIPORTS':   15083,
    'POWERGRID':    14977,
    'HCLTECH':      7229,
    'ASIANPAINT':   236,
    'DIXON':        21690,
    'ITC':          1660,
    'APOLLOHOSP':   157,
    'COALINDIA':    20374,
    'TATASTEEL':    3499,
    'BAJAJ-AUTO':   16669,
    'INFY':         1594,
    'DLF':          14732,
    'BDL':          2144,
    'CAMS':         342,
    'CDSL':         21174,
    'NYKAA':        6545,
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
    "GROWWPOWER":   758165,   # Power & utilities
    "MONIFTY500":   19237,    # Broad market (Nifty 500)
}

# =========================
# SECRET
# =========================
FIREBASE_URL = os.getenv("FIREBASE_URL")
PAYTM_ORDER_URL = os.getenv("PAYTM_ORDER_URL")
TRADINGVIEW_URL = os.getenv("TRADINGVIEW_URL")
print(TRADINGVIEW_URL)

# =========================
# FIREBASE
# =========================
def fetch_firebase():
    print("Firebase -> fetch_firebase")
    r = requests.get(FIREBASE_URL, timeout=10)
    r.raise_for_status()
    return r.json() or {}

def save_order_to_firebase(symbol, payload):
    print("Firebase -> save_order_to_firebase")
    r = requests.patch(FIREBASE_URL, json={symbol: payload}, timeout=10)
    r.raise_for_status()

def already_ordered_today(symbol, firebase_data):
    record = firebase_data.get(symbol)
    if not record:
        return False
    order_date = datetime.strptime(record["dtm"], "%Y-%m-%d %H:%M:%S").date()
    print("Firebase -> already_ordered_today for the given Symbol -> ", order_date)
    return order_date == date.today()

# =========================
# AUTH
# =========================
def get_access_token():
    data = fetch_firebase()
    dtm = data.get("dtm")
    token = data.get("talk")
    print("Auth -> get_access_token -> ", dtm )
    if not dtm or not token:
        print("Auth -> Missing token or date in Firebase")
        raise RuntimeError("Missing token or date in Firebase")
    firebase_date = datetime.strptime(dtm, "%Y-%m-%d").date()
    if firebase_date < date.today():
        print("Auth -> Token expired")
        raise RuntimeError("Token expired")
    return token

# =========================
# MARKET DATA
# =========================
def fetch_stock_data(DataDict):
    symbols = [f"NSE:{s}" for s in DataDict]
    columns = [
        "name", "close", "change", "high", "low", "ADR",
        "SMA50", "SMA200", "High.3M", "High.6M", "Low.3M",
        "price_target_average", "price_target_1y", "price_target_median",
        "earnings_release_next_date",
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
    print("Market Data -> Stock List -> ", str(stocks))
    return stocks

# =========================
# STRATEGY
# =========================
def calculate_quantity(price):
    return max(1, int(DAILY_CAPITAL // price))

def evaluate_stock(stock , etf = 0):
    close = stock["close"]
    TradingLow_Risk = 0
    adr = stock.get("ADR") or 0
    if stock["High.3M"] and close > stock["High.3M"] * 0.95:
        print("evaluate_stock -> ", stock, "-> 3M High is near 5% of close | ", close , stock["High.3M"] )
        return 0
    if stock["High.6M"] and close > stock["High.6M"] * 0.95:
        print("evaluate_stock -> ", stock, "-> 6M High is near 5% of close | ", close , stock["High.6M"] )
        return 0
    if stock["Low.3M"] and close < stock["Low.3M"]:
        print("evaluate_stock -> ", stock, "-> Below 3M Low  | ", close , stock["Low.3M"] )
        TradingLow_Risk = 1
    range_3m = stock["High.3M"] - stock["Low.3M"]
    position = (close - stock["Low.3M"]) / range_3m
    if position > 0.75:
        print("evaluate_stock -> ", stock, "-> Near to 75%ile of high 3month range  | ",stock["High.3M"], close , stock["Low.3M"] , position )
        return 0
    if not etf :
        buy = stock.get("recommendation_buy") or 0
        sell = stock.get("recommendation_sell") or 0
        total = stock.get("recommendation_total") or 1
        if buy <= sell or buy <= 0.5 * total:
            return 0
    target1 = stock.get("low") - (adr * 0.5)
    target2 = stock.get("close") - (adr * 0.75)
    target3 = stock.get("high") - (adr)
    target =min(target1,target2,target3)
    if TradingLow_Risk:
        target = stock.get("low") - (adr * 0.99)
    print("evaluate_stock -> ", stock, "-> Targetted  -> LOW, Close, High, 3M-High, 3M-Low, T1, T2, T3, Target")
    print(stock.get("low"), stock.get("close"), stock.get("high"), stock["High.3M"] , stock["Low.3M"], target1, target2, target3, target)
    if not etf :
        return round(target * 20) / 20
    else:
        return round(target , 2)

# =========================
# ORDER
# =========================
def place_order(symbol, price, token, etf = 0):
    off_mkt_flag = True
    now = datetime.now()
    print("ORDER -> NOW Time Is : ", now)
    trading_start = now.replace(hour=9, minute=15, second=0, microsecond=0)
    trading_end = now.replace(hour=15, minute=30, second=0, microsecond=0)
    if trading_start <= now <= trading_end:
        off_mkt_flag = False
    if not etf:
        security_id = INVEST_STOCKS[symbol]
    else:
        security_id = ETF_DICT[symbol]
    qty = calculate_quantity(price)
    payload = {
        "txn_type": "B",
        "exchange": "NSE",
        "segment": "E",
        "product": "C",
        "security_id": security_id,
        "quantity": qty,
        "validity": "DAY",
        "order_type": "LMT",
        "price": price,
        "source": "N",
        "off_mkt_flag": off_mkt_flag,
    }
    headers = {
        "x-jwt-token": token,
        "Content-Type": "application/json",
    }
    print("ORDER -> ", payload)
    r = requests.post(PAYTM_ORDER_URL, headers=headers, json=payload, timeout=15)
    print("ORDER -> ", r.text)
    if not r.text:
        print("ORDER -> Empty response from Paytm")
        raise RuntimeError("Empty response from Paytm")
    return json.loads(r.text)

# =========================
# MAIN
# =========================
def main():
    token = get_access_token()
    firebase_data = fetch_firebase()
    stocks = fetch_stock_data(INVEST_STOCKS)
    investment_threshold = 0
    for full_symbol, data in stocks.items():
        symbol = full_symbol.split(":")[1]
        print("Main -> ", symbol)
        if already_ordered_today(symbol, firebase_data):
            print("Main -> ", symbol , " -> Already Ordered Today")
            continue
        target_price = evaluate_stock(data)
        if not target_price:
            print("Main -> ", symbol , " -> No Target Price | Not Eligible")
            continue
        investment_threshold += target_price
        if investment_threshold > MAX_CAPITAL:
            print("MAX_CAPITAL Reached Exit...")
            exit(0)
        response = place_order(symbol, target_price, token)
        if response.get("status") == "success":
            order_no = response["data"][0]["order_no"]
            save_order_to_firebase(
                symbol,
                {
                    "id": INVEST_STOCKS[symbol],
                    "dtm": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "quantity": calculate_quantity(target_price),
                    "price": target_price,
                    "order_id": order_no,
                },
            )

    stocks = fetch_stock_data(ETF_DICT)
    Etf_investment_threshold = 0
    for etf_symbol, data in stocks.items():
        symbol = etf_symbol.split(":")[1]
        print("Main ETF -> ", symbol)
        if already_ordered_today(symbol, firebase_data):
            print("Main ETF -> ", symbol , " -> Already Ordered Today")
            continue
        target_price = evaluate_stock(data, 1)
        if not target_price:
            print("Main ETF -> ", symbol , " -> No Target Price | Not Eligible")
            continue
        Etf_investment_threshold += target_price
        if Etf_investment_threshold > ETF_CAPITAL:
            print("ETF_CAPITAL Reached Exit...")
            continue
        response = place_order(symbol, target_price, token, 1)
        if response.get("status") == "success":
            order_no = response["data"][0]["order_no"]
            save_order_to_firebase(
                symbol,
                {
                    "id": ETF_DICT[symbol],
                    "dtm": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "quantity": calculate_quantity(target_price),
                    "price": target_price,
                    "order_id": order_no,
                },
            )

if __name__ == "__main__":
    main()