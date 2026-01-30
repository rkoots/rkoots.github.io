import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import roc_auc_score
pd.set_option('display.max_columns', None)
from xgboost import XGBRegressor, XGBClassifier
import ta

# =========================
# CONFIG
# =========================
DB_PATH = "stocks.db"
TABLE = "stock_history"
LOOKBACK = 60

# =========================
# LOAD DATA
# =========================
def main(TICKER,date_str):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"""
        SELECT Date, Open, High, Low, Close, Volume
        FROM {TABLE}
        WHERE Ticker = '{TICKER}'
        and date<='{date_str}'
        ORDER BY Date
        """,
        conn,
        parse_dates=["Date"]
    )
    conn.close()
    df.set_index("Date", inplace=True)

    # =========================
    # FEATURE ENGINEERING
    # =========================

    # Returns
    df["ret_1d"] = df["Close"].pct_change()
    df["ret_5d"] = df["Close"].pct_change(5)
    df["ret_10d"] = df["Close"].pct_change(10)

    # Volatility
    df["atr"] = ta.volatility.AverageTrueRange(
        df["High"], df["Low"], df["Close"], window=14
    ).average_true_range()

    df["bb_width"] = (
                             ta.volatility.BollingerBands(df["Close"]).bollinger_hband() -
                             ta.volatility.BollingerBands(df["Close"]).bollinger_lband()
                     ) / df["Close"]

    # Trend
    df["adx"] = ta.trend.ADXIndicator(
        df["High"], df["Low"], df["Close"]
    ).adx()

    df["sma_50"] = df["Close"].rolling(50).mean()
    df["sma_200"] = df["Close"].rolling(200).mean()
    df["trend_flag"] = (df["sma_50"] > df["sma_200"]).astype(int)

    # Momentum
    df["roc_5"] = ta.momentum.ROCIndicator(df["Close"], 5).roc()
    df["macd_diff"] = (
        ta.trend.MACD(df["Close"]).macd_diff()
    )

    # Volume
    df["obv"] = ta.volume.OnBalanceVolumeIndicator(
        df["Close"], df["Volume"]
    ).on_balance_volume()

    df["vol_z"] = (
            (df["Volume"] - df["Volume"].rolling(20).mean()) /
            df["Volume"].rolling(20).std()
    )

    # VWAP deviation
    df["vwap"] = ta.volume.VolumeWeightedAveragePrice(
        df["High"], df["Low"], df["Close"], df["Volume"]
    ).volume_weighted_average_price()

    df["vwap_dev"] = (df["Close"] - df["vwap"]) / df["Close"]

    # Regime
    df["vol_regime"] = (
            df["atr"] > df["atr"].rolling(60).median()
    ).astype(int)

    # =========================
    # TARGETS
    # =========================
    df["y_close_next"] = df["Close"].shift(-1)
    df["y_ret_5d"] = df["Close"].shift(-5) / df["Close"] - 1
    df["y_up"] = (df["y_close_next"] > df["Close"]).astype(int)

    df.dropna(inplace=True)

    # =========================
    # FEATURES
    # =========================
    features = [
        "ret_1d", "ret_5d", "ret_10d",
        "atr", "bb_width",
        "adx", "trend_flag",
        "roc_5", "macd_diff",
        "obv", "vol_z",
        "vwap_dev",
        "vol_regime"
    ]

    X = df[features]
    y_close = df["y_close_next"]
    y_ret5 = df["y_ret_5d"]
    y_up = df["y_up"]

    # =========================
    # WALK-FORWARD SPLIT
    # =========================
    tscv = TimeSeriesSplit(n_splits=5)
    train_idx, test_idx = list(tscv.split(X))[-1]

    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_up_train, y_up_test = y_up.iloc[train_idx], y_up.iloc[test_idx]

    # =========================
    # SCALE (for logistic only)
    # =========================
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # =========================
    # MODELS
    # =========================

    # Logistic baseline
    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(X_train_s, y_up_train)

    # XGBoost classifier
    xgb_clf = XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.03,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss"
    )
    xgb_clf.fit(X_train, y_up_train)

    # Calibrated probabilities
    xgb_cal = CalibratedClassifierCV(xgb_clf, method="isotonic", cv=3)
    xgb_cal.fit(X_train, y_up_train)

    # =========================
    # EVALUATION
    # =========================
    log_auc = roc_auc_score(y_up_test, log_model.predict_proba(X_test_s)[:, 1])
    xgb_auc = roc_auc_score(y_up_test, xgb_cal.predict_proba(X_test)[:, 1])



    # =========================
    # FEATURE IMPORTANCE
    # =========================
    imp = pd.Series(
        xgb_clf.feature_importances_,
        index=features
    ).sort_values(ascending=False)

    # =========================
    # LATEST PREDICTION
    # =========================
    latest = X.iloc[[-1]]
    up_prob = xgb_cal.predict_proba(latest)[0, 1]
    return up_prob,log_auc,xgb_auc



conn = sqlite3.connect(DB_PATH)
tickers = pd.read_sql(
    f"""
    SELECT DISTINCT Ticker
    FROM {TABLE}
    ORDER BY Ticker
    """,
    conn
)["Ticker"].tolist()
if 1:
    Counter= 0
    Passer = 0
    Failer = 0
    Passer60 = 0
    Failer60 = 0
    Passer65 = 0
    Failer65 = 0
    Passer_xgb_auc = 0
    Failer_xgb_auc = 0
    from datetime import datetime, timedelta
    start_date = datetime(2025, 10, 1)
    end_date = datetime(2025, 12, 30)
    check_date = start_date
    check_date_1 = check_date - timedelta(days=1)
    while check_date <= end_date:
        date_str_main = check_date.strftime('%Y-%m-%d')
        check_date += timedelta(days=1)
        date_str1 = check_date.strftime('%Y-%m-%d')
        date_str = check_date_1.strftime('%Y-%m-%d')
        check_date_1 += timedelta(days=1)
        for i in tickers:
            Counter +=1
            up_prob,log_auc,xgb_auc = main(i,date_str_main)
            regime = ''
            new = pd.read_sql(f""" SELECT date, Open, High, Low, close FROM {TABLE}_test where Ticker='{i}' and Date>='{date_str}' ORDER BY date ASC LIMIT 2 """,conn)
            new['Prev_Close'] = new['Close'].shift(0)  # current row Close
            new['Next_Open'] = new['Open'].shift(-1)  # next row Open
            trend_df = new[:-1].copy()
            trend_df['Change_Value'] = trend_df['Next_Open'] - trend_df['Prev_Close']
            trend_df['Change_Percent'] = (trend_df['Change_Value'] / trend_df['Prev_Close']) * 100
            trend_df['Trend'] = trend_df['Change_Value'].apply(lambda x: 'Uptrend' if x > 0 else 'Downtrend')
            trend_df = trend_df[['Prev_Close', 'Next_Open', 'Change_Value', 'Change_Percent','Trend']]
            if up_prob > 0.55:
                regime = "Uptrend"
                trend_df['regime'] = regime
                if trend_df.loc[0, 'Trend'] == regime:
                    Passer+=1
                else:
                    Failer+=1
            if up_prob > 0.60:
                regime = "Uptrend"
                trend_df['regime'] = regime
                if trend_df.loc[0, 'Trend'] == regime:
                    Passer60+=1
                else:
                    Failer60+=1
            if up_prob > 0.65:
                regime = "Uptrend"
                trend_df['regime'] = regime
                if trend_df.loc[0, 'Trend'] == regime:
                    Passer65+=1
                else:
                    Failer65+=1
            if xgb_auc > 0.52:
                if up_prob > 0.55:
                    regime = "Uptrend"
                    if trend_df.loc[0, 'Trend'] == regime:
                        Passer_xgb_auc+=1
                    else:
                        Failer_xgb_auc+=1

        print(check_date, Counter, Passer, Failer, Passer_xgb_auc, Failer_xgb_auc , Passer60, Failer60, Passer65, Failer65)
