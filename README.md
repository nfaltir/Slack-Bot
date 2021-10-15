Python Slack Bot 🐍 
===================================

Project Objective
--------------------
1. Create a slack bot ✅
2. Connect python and slack bot ✅
3. Allow bot to fetch stock data using yfinance and post on slack ✅
4. Allow slack users to interact with bot (request stock data) 🔨
5. Automate bot to post stock reports at specific time 🔨


<br>
Install Python Packages
--------------------------
I am using Python 3.9.7<br>
`pip3 install -r requirements.txt`
<br>

Slack Config
---------------
1. Create a slack work space for testing
2. https://api.slack.com/apps/ click on `create an App` name your app and select workspace.
3. Click on the Slack Bot card, then click on `Review Scopes to Add` 
4. Select `chat:write` for now
5. Click `Install to workspace`
6. Get Oauth token, copy and paste it into a `.env file` in root folder of project


<br><i>Output Figure</i>
<img src="static/report.png"
     alt="example-energy"
     style="float: left; margin-right: 10px; margin-bottom: 50px;" />

<br>
Common issues
------------------
yfinance is a useful but slow library, to circumvent this issue, data requests must be dynamic in nature (ex: current_price) <br>
fixed data, like ticker symbols, address, or data that only change every quarter (cash posistion) can be loaded into api app or a local db. <br>
Essentially, to avoid any issues you will need to split project into pieces. Too mnay requests can lead to yahoo finance flagging your ip,<br> causing slowdowns or no service at all. Websites with data tables are also implementing strategies to block web scrappers from scrapping their data<br> So a solution like Selenium or beautiful soup can work, but not its not a viable solution longterm. Ulitmately, the best solution is to get a finance api from<br> a reputable source.
<hr>

