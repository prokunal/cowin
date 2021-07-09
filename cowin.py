# Author:	 Kunal Kumar
# Website: 	 https://procoder.in
# Instagram: 	 @prokunal
# twitter: 	 @pr0kunal

import requests
from playsound import playsound
from datetime import datetime
import sys
import json
try:
    pincode = sys.argv[1]
    date= sys.argv[2]
    check_age = sys.argv[3]
except:
    print("Usage:    python3 {} <pincode> <date> <age>".format(sys.argv[0]))
    print("Usage:    python3 {} 842001 {} 18".format(sys.argv[0],datetime.now().strftime("%d-%m-%Y")))
    print("Usage:    python3 {} 842001 {} 18".format(sys.argv[0],datetime.now().strftime("%d-%m-%Y")))
    exit()
print("Checking for available slots on {}".format(date))
print("I will notify you, when {}+ slot is available.".format(sys.argv[3]))



date1 = datetime(int(date.split('-')[2]),int(date.split('-')[1]),int(date.split('-')[0])+1)
date2 = datetime.now()

def date_check(date1,date2):
    if date1 < date2:
        print("\nYOU CAN'T GO IN PAST FOR VACCINATION")
        print("PLEASE CHECK YOUR DATE.")
        exit()
    else:
        pass
date_check(date1,date2)


def message():
    print("slot available for {}+".format(check_age))
    return sound()

def sound():
    playsound('siren.wav')

def notify(pincode,date):
    while True:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:68.7) Gecko/20100101 Firefox/68.7'}
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode,date)
        response = requests.get(url,headers=headers)
        text = response.text
        data = json.loads(text)
        stock = []
        count = 0
        new = data['centers']
        if len(data['centers']) > 0:
            
            for i in range(len(new)):
                for x in range(len(new[i]['sessions'])):
                    
                    age = data['centers'][i]['sessions'][x]['min_age_limit']
                    st = data['centers'][i]['sessions'][x]['available_capacity']
                    if age == int(check_age):
                        stock.append(st)
                    else:
                        pass
            if len(stock) == 0:
                print("slot not available for {}".format(sys.argv[3]))
            else:
                for i in stock:
                    if i == 0:
                        pass
                    else:
                        return message()
        else:
            print("SLOT NOT AVAILABLE")
notify(pincode,date)
