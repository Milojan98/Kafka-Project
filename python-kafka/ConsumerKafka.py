# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:46:53 2020

@author: Miloj
"""

from kafka import KafkaConsumer
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np
import json


consumer = KafkaConsumer('Test',auto_offset_reset='earliest',
                         group_id=None,bootstrap_servers='localhost:9092',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8'))
                        )
print(consumer)
xdata = []
ydata = []

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`

    msg=message.value
    
    print (msg)
    date=msg['date']/1000
    date=datetime.utcfromtimestamp(date).strftime('%H:%M')
    xdata.append(date)
    ydata.append(msg['value'])
    figure=plt.figure()
    figure.patch.set_facecolor('lavender')
    ax = figure.add_subplot(111)
    ax.set_title('BTC/USDT',color='crimson')
    ax.yaxis.tick_right()
    ax.set_facecolor('black')

    figure.autofmt_xdate(bottom=0.2)
    plt.plot(xdata,ydata,color="tomato")
    plt.show()
    
    """
    plt.cla()
    plt.plot(xdata,ydata)
    plt.show()
     ax.pause(1e-17)
    #"""

    
consumer.close()