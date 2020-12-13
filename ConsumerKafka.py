# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:46:53 2020

@author: Miloj
"""

from kafka import KafkaConsumer
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import json


consumer = KafkaConsumer('Test',auto_offset_reset='earliest',
                         group_id=None,bootstrap_servers='localhost:9092',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8'))
                        )
print(consumer)
xdata = []
ydata = []

style.use('fivethirtyeight')

plt.figure()


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`

    msg=message.value
    
    print (msg)

    xdata.append(msg['date'])
    ydata.append(msg['value'])
    
    plt.close()
    plt.plot(xdata,ydata)
    plt.show()
    
    #ax.clear()
    
    #fig.show()

    """
    plt.cla()
    plt.plot(xdata,ydata)
    plt.show()
     ax.pause(1e-17)
    #"""

    
consumer.close()