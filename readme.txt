usage- $ pkg install -y git python

$ git clone https://github.com/sujithreddy001/Loanapp.git

$ cd Loanapp

Install requierments

$ python3 app.py -i

setup configration file ( Flask, apiHASH )

$ python3 setup.py -c

To Genrate User Data

$ python3 scraper.py

( members.csv is default if you changed name use it ) Send Bulk sms To Collected Data

$ python3 smsbot.py members.csv

add users to your group ( in devlopment )

$ python3 groupadd.py members.csv

Update Tool

$ python3 setup.py -u