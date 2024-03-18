
# Stock Price Extractor

# What it does
The Stock Price extractor is bot on Discord platform. it will return basic responses for user which are already set in script.
but If user wants stock price data ; he must provide stock name with "/"symbol at beginning here's user
demo: Hello -> Hello there! 
time->_Time Right Now is 08:37:48.700330 
roll dice -> _ You rolled: 6_ 
*for user to extract stock-price here's demo *
ask stock name by beginning of "/" symbol like 
/NVDA -> Open High Low Close Adj Close Volume Date 2024-01-30 629.0 634.929993 622.599976 627.73999 627.73999 40746400
this is how you will get your price for right now user can inly fetch US markets data ,will add Indian markets to it

# How It's built 
This is my solo project and I had no experience in bot development before this but somehow I started development. I explored about Discord API and its documentation this step was so stressful and confusing but after overcoming this challenge I moved to the next phase of development where created a python script in which added basic responses for user commands and commands starting with "/" symbol will get stock price returned. It uses Yahoo Finance python library to get real time stock data of US markets and Python Pandas library to arrange data. For price accuracy bot will return "Last price" and its time along with Open High Low Close of stock

# Demo Use

https://github.com/radhe098/stockbot/assets/110740717/90d34a42-34d2-4c57-8bf9-6af1c1986ddf

