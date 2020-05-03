# FinnhubPythonWrapper
A simple Python wrapper for [Finnhub.io](https://finnhub.io/). This library makes use of [requests](https://github.com/psf/requests)
to fetch data from Finnhub.io and returns the [Pandas](https://github.com/pandas-dev/pandas) dataframes

## Examples:

```python
    fh = Finnhub("your-token")
    # Get list of exchanges. `kind` can be one of ["stock", "forex", "crypto"]
    fh.fetch_exchanges(kind = "crypto") 
    # Get list of symbols on the exchange
    fh.fetch_symbols(kind = "crypto", exchange = "Binance")
    # Get list of 1-Day BTCUSDT candles from Binance last 30 days
    fh.fetch_last_days("crypto", "BINANCE:BTCUSDT", 30)
```


## Disclaimer
This library has no association with Finnhub.io and use it at your own risk.