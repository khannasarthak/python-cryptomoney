#!/usr/bin/python3
import requests
import json
from urllib.request import urlopen
from gi.repository import Notify
import time


rbtc = requests.get(url='https://blockchain.info/ticker')
objbtc = rbtc.json()

### CHANGE THESE IF NEEDED ###
mybtc = 0.00812164
myeth = 0.13370304
##############################
btc =  float((objbtc['USD']['last']))

reth = requests.get(url='https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
objeth = reth.json()
eth =  (objeth['USD'])

mytotal = round(mybtc*btc + myeth*eth,2)
body = 'My CrytpoMoney - USD :$'+str(mytotal)
summary = 'BTC: $'+str(round(mybtc*btc,2))+'  ETH: $'+str(round(myeth*eth,2))

Notify.init('CryptoMoney')
notification = Notify.Notification.new(body,summary)
notification.show()
Notify.uninit()