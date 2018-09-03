# RuneMate Credit Tracker

Keeps track of your RuneMate account's credit balance.

**Requires Python 3.6**

### Usage
`python main.py -o path/to/output.csv`

You'll be prompted your login credentials as well as a 2FA key.

The program will append your current credit balance to the specified file every 15 minutes.

Format of the csv file is `unixtime,balance`.
