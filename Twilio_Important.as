--Starting

cd Documents/my_tutorial_folder
source bin/activate

Twilio number +16173077805
+15104601941 - purchased heroku ps:scale web=1

Configure Procfile
web: gunicorn run:app

Sending SMS
python send_sms.py

Recovery key
R1LZJxTnLKDwul1tZvtHBNsWqtv0Gn4RuSm0D6ac

How to add something to your bash profile
echo 'export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin' >>~/.bash_profile


How to get into your heroku virtual environment
virtualenv venv
source venv/bin/activate

Website
http://twilio-aadil.herokuapp.com/?From=%2B16175105178


Heroku run one off dynos
heroku run python manage.py shell


Callbaks
http://requestb.in/1h18unm1

import requests, time
r = requests.post('http://requestb.in/1h18unm1', data={"ts":time.time()})
print r.status_code
print r.content