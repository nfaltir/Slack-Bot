import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import ssl
import requests
import yfinance as yf

#issues with web socket, this is a solution found on github
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



stockObj = yf.Ticker(input("Enter stock ticker: "))
stock = stockObj.info

stockName = stock['longName']
summary = stock['longBusinessSummary']
currentPrice = stock['currentPrice']


client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)
client.chat_postMessage(channel='#bot-test',
                        text=stockName+"\n"+"\nBusiness Summary\n " + summary + "\n" + "\nCurrent Price: "+ str(currentPrice))


