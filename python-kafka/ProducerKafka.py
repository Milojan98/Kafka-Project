# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:17:57 2020

@author: Miloj
"""

from kafka import KafkaProducer
import ccxt
import time
import json

print(ccxt.exchanges) # print a list of all available exchange classes
binance = ccxt.binance()
symbol = 'BTC/USDT'

#ok=binance.fetch_tickers()


producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

"""   
for i in :
    producer.send('Binance_BTC-USDT_1h', str(i).encode('UTF-8'))
 """
while True:
    data=binance.fetch_ohlcv(symbol, '1m')
    print(data[0][:2])
    producer.send('Binance_BTC-USDT_1h', {'date':data[0][0], 'value': data[0][1]})
    time.sleep(60)

producer.close()