import datetime
import requests
import time
import pandas as pd

class Finnhub:
    def __init__(self, token):
        self.token = token
        self.base = "https://finnhub.io/api/v1"

    def fetch(self, kind, symbol, fromDate, toDate, resolution):
        url = "{}/{}/candle?token={}&symbol={}&resolution={}&from={:.0f}&to={:.0f}".format(
            self.base,
            kind,
            self.token,
            symbol,
            resolution,
            fromDate.timestamp(),
            toDate.timestamp(),
        )
        json = requests.get(url).json()
        df = pd.DataFrame.from_dict(json)
        df.columns = ["Close", "High", "Low", "Open", "S", "t", "Volume"]
        df["Open Time"] = pd.to_datetime(df["t"], unit="s")
        df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]
        df = df.sort_values(by=["Open Time"], ascending=[1])
        df = df.reset_index(drop=True)
                return df

    def fetch_last_days(self, kind, symbol, days):
        toDate = datetime.datetime.now()
        fromDate = toDate - datetime.timedelta(days)
        return self.fetch(kind, symbol, fromDate, toDate, "D")

    def fetch_exchanges(self, kind):
        url = "{}/{}/exchange?token={}".format(self.base, kind, self.token)
        json = requests.get(url).json()
        df = pd.DataFrame.from_dict(json)
                return df

    def fetch_symbols(self, kind, exchange):

        url = "{}/{}/symbol?token={}&exchange={}".format(
            self.base, kind, self.token, exchange
        )
        json = requests.get(url).json()
        df = pd.DataFrame.from_dict(json)
                return df