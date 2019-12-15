import json
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib import style

headersFB = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'FB',
    'interval': '60min',
    'dataype': 'json',
    'outputsize': 'compact',
    'apikey': '727KJOLRT2S75RPT'
}

headersAAPL = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'AAPL',
    'interval': '5',
    'dataype': 'json',
    'outputsize': 'compact',
    'apikey': '727KJOLRT2S75RPT'
}

headersNFLX = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'NFLX',
    'interval': '60min',
    'dataype': 'json',
    'outputsize': 'compact',
    'apikey': '727KJOLRT2S75RPT'
}

headersGOOGL = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'GOOGL',
    'interval': '60min',
    'dataype': 'json',
    'outputsize': 'compact',
    'apikey': '727KJOLRT2S75RPT'
}

url = 'https://www.alphavantage.co/query?'

dataFBPrice = list()
dataAAPLPrice = list()
dataNFLXPrice = list()
dataGOOGLPrice = list()

dataFBDate = list()
dataAAPLDate = list()
dataNFLXDate = list()
dataGOOGLDate = list()

def getData(company):
    try:
        response = requests.get(url, company)
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    d = response.json()
    return d

def setDataPrice(p, data, c):
    for n in data[c].keys():
        p.append(float(data[c][n]['1. open']))
    return p

def setDataDate(d, data, c):
    for m in data[c]:
        d.append(str(m))
    return d

def setAllData(stock, d, p):
    data = getData(stock)
    tagK = data.keys()[1]
    choice = tagK
    setDataDate(d, data, choice)
    setDataPrice(p, data, choice)

setAllData(headersFB, dataFBDate, dataFBPrice)
setAllData(headersAAPL, dataAAPLDate, dataAAPLPrice)
setAllData(headersNFLX, dataNFLXDate, dataNFLXPrice)
setAllData(headersGOOGL, dataGOOGLDate, dataGOOGLPrice)

plt.style.use('dark_background')

fig, axs = plt.subplots(2, 2)

axs[0, 0].get_xaxis().set_visible(False)
axs[0, 1].get_xaxis().set_visible(False)
axs[1, 0].get_xaxis().set_visible(False)
axs[1, 1].get_xaxis().set_visible(False)

axs[0, 0].get_yaxis().set_visible(False)
axs[0, 1].get_yaxis().set_visible(False)
axs[1, 0].get_yaxis().set_visible(False)
axs[1, 1].get_yaxis().set_visible(False)

#
# # #####DANGER###################################
# def animate(i):
#     graph_data = open('example.txt','r').read()
#     lines = graph_data.split('\n')
#     xs = []
#     ys = []
#     for line in lines:
#         if len(line) > 1:
#             x, y = line.split(',')
#             xs.append(float(x))
#             ys.append(float(y))
#     axs.clear()
#     ax1.plot(xs, ys)
#     axs[0, 0].plot(dataFBDate, dataFBPrice, 'tab:blue' )
#     axs[0, 1].plot(dataAAPLDate, dataAAPLPrice, 'tab:green')
#     axs[1, 0].plot(dataNFLXDate, dataNFLXPrice, 'tab:red')
#     axs[1, 1].plot(dataGOOGLDate, dataGOOGLPrice, 'tab:orange')
# # #####//DANGER###################################

axs[0, 0].plot(dataFBDate, dataFBPrice, 'tab:blue' )
axs[0, 1].plot(dataAAPLDate, dataAAPLPrice, 'tab:green')
axs[1, 0].plot(dataNFLXDate, dataNFLXPrice, 'tab:red')
axs[1, 1].plot(dataGOOGLDate, dataGOOGLPrice, 'tab:orange')

# ani = animation.FuncAnimation(fig, animate, interval=1000)
fig.show()

####INFO#####
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=FB&interval=5min&apikey=demo
#function options:  -TIME_SERIES_DAILY
#                   -TIME_SERIES_WEEKLY
#                   -TIME_SERIES_MONTHLY
#                   -TIME_SERIES_INTRADAY

#symbol: name of stock

#interval: time between data sets

#api key: 727KJOLRT2S75RPT


#####SAVE FOR LATES#######


#


# with requests.Session() as s:
#     download = s.get(url, headers=headers)
#
#     decoded_content = download.content.decode('utf-8')
#
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)
#
# fig = go.Figure([go.Scatter(x=cr['timestamp'], y=cr['open'])])
# fig.show()


# # #get data from API for #
# # try:
# #     response = requests.get(url, headers)
# # except requests.exceptions.RequestException as e:
# #     print e
# #     sys.exit(1)
# #
# # data = response.json()
#

# data_json = json.loads(response)





###recursive search###
#def extract_element_from_json(obj, path):
#    def extract(obj, path, ind, arr):
#        key = path[ind]
#        if ind + 1 < len(path):
#            if isinstance(obj, dict):
#                if key in obj.keys():
#                    extract(obj.get(key), path, ind + 1, arr)
#                else:
#                    arr.append(None)
#            elif isinstance(obj, list):
#                if not obj:
#                    arr.append(None)
#                else:
#                    for item in obj:
#                        extract(item, path, ind, arr)
#            else:
#                arr.append(None)
#        if ind + 1 == len(path):
#            if isinstance(obj, list):
#                if not obj:
#                    arr.append(None)
#                else:
#                    for item in obj:
#                        arr.append(item.get(key, None))
#            elif isinstance(obj, dict):
#                arr.append(obj.get(key, None))
#            else:
#                arr.append(None)
#        return arr
#    if isinstance(obj, dict):
#        return extract(obj, path, 0, [])
#    elif isinstance(obj, list):
#        outer_arr = []
#        for item in obj:
#            outer_arr.append(extract(item, path, 0, []))
#        return outer_arr
######






###TRASHHHHHHHH###

#data = json.dumps(response.content.decode('utf-8'), indent = 4, sort_keys=True)

#json_data = json.loads(response.content.decode('utf-8'))

#
#for x in data:
#    print(json_data['Time Series (Daily)'][x]['1. open'])

###works###
#print(extract_element_from_json(json_data, ['Time Series (Daily)','2019-12-11']))

#json_data = json.loads(response.text)
#print(json_data)
