from os import environ as env
import requests

class Cryptocurrency:

    def get_data(self):
        #url = 'https://rest.coinapi.io/v1/ohlcv/BTC/USD/history?period_id=1DAY&time_start=2021-05-01T00:00:00'
        #headers = {"X-CoinAPI-Key": env.get("COIN_API_KEY")}
        #response = requests.get(url, headers=headers)
        #if ("error" in response.json()):
        return [['Date', 'Price'], ['05-01', 57859.28], ['05-02', 56625.2], ['05-03', 57212.73], ['05-04', 53241.92], ['05-05', 57508.18], ['05-06', 56440.66], ['05-07', 57380.39], ['05-08', 58958.05], ['05-09', 58317.0], ['05-10', 55866.41], ['05-11', 56753.19], ['05-12', 49451.0], ['05-13', 49690.11], ['05-14', 49893.48], ['05-15', 46775.51], ['05-16', 46450.79], ['05-17', 43580.5], ['05-18', 42877.75], ['05-19', 36742.3], ['05-20', 40623.33], ['05-21', 37335.16], ['05-22', 37476.83], ['05-23', 34718.8], ['05-24', 38878.56], ['05-25', 38361.81], ['05-26', 39293.23], ['05-27', 38579.0], ['05-28', 36870.87]]
        #return self.parse_data(response)

    def parse_data(self, response):
        output = [["Date", "Price"]]
        for day in response.json():
            output.append([day['time_period_start'][5:10], day['price_close']])
        return output

