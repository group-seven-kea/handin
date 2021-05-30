from os import environ as env
import requests

class Cryptocurrency:

    def get_data(self):
        url = 'https://rest.coinapi.io/v1/ohlcv/BTC/USD/history?period_id=1DAY&time_start=2021-05-01T00:00:00'
        headers = {"X-CoinAPI-Key": env.get("COIN_API_KEY")}
        response = requests.get(url, headers=headers)
        return self.parse_data(response)

    def parse_data(self, response):
        output = [["Date", "Price"]]
        for day in response.json():
            output.append([day['time_period_start'][5:10], day['price_close']])
        return output

