import requests
from enum import Enum
from datetime import datetime
import os

# Get your personal token on: 
# mybecode --> inspect --> network --> 
# fetch/xhr --> name (graph.becode.org) --> headers (request headers) --> authorization



class AttendanceTimePeriod(Enum):
    Morning = 'MORNING'
    Lunch = 'LUNCH'
    Noon = 'NOON'
    Evening = 'EVENING'

# Getting day object for the junior_attendance request
def day_object():
    return datetime.timestamp(datetime.now())

# Request that pass the object of the day, hour, minute and second to becode graph regarding the time frame which the button was pushed
def get_junior_today_attendance(token):
    
    junior_payload = {
    "operationName": "get_junior_today_attendance", 
     "variables": {"day": day_object()}, 
     "extensions": {
        "persistedQuery": {
            "version": 1, 
            "sha256Hash": "2d903b4f72e5ce35ab4239a53e48612aec6e5469eaeb76de603b68bac7f6410c"
            }
        }
     }
    resp = requests.post(
    'https://graph.becode.org/',
    json=junior_payload,
    headers={'Authorization': f'Bearer {token}'}
    )

# Request that "push the hour button". It passes the request with a personal token and the status (bool) of where the student is
def record_attendance(at_home, token):
    hour = datetime.now().hour
    minute = datetime.now().minute
    print(f'Running record_attendace at {hour}:{minute}')
    if hour == 9:
        time_period = AttendanceTimePeriod.Morning
        # When calling this function here, the first request is sent and then the scheduler is going to trigger and start job for the current request right after
        get_junior_today_attendance(token)
    elif hour == 12:
        time_period = AttendanceTimePeriod.Lunch
    elif hour == 13:
        time_period = AttendanceTimePeriod.Noon
    elif hour == 17:
        time_period = AttendanceTimePeriod.Evening
    else:
        return None

    
    becode_payload = {
        "operationName": "record_attendance_time",
        "variables": {"period": time_period.value, "atHome": at_home},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "553ae433516c13a97e348d4a48dd0114d1949f791ab21d97bed27030a65e85a8",
            }
        },
    }

    resp = requests.post(
        'https://graph.becode.org/',
        json=becode_payload,
        headers={'Authorization': f'Bearer {token}'}
    )
    
    print(f'Status Code request -> {resp.status_code}')
    print(f'Request response -> {resp.json()}')

def main():
    # Access the environment variable and convert it to a boolean
    at_home = os.environ.get("AT_HOME", "").lower() == "true"
    token = os.environ.get("TOKEN")
    record_attendance(at_home, token)

if __name__ == "__main__":
    main()