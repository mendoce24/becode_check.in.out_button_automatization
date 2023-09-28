import requests
from enum import Enum
from datetime import datetime
import os
import logging

# Get your personal token on: 
# mybecode --> inspect --> network --> 
# fetch/xhr --> name (graph.becode.org) --> headers (request headers) --> authorization


log_filename = 'my_script.log'
log_level = logging.INFO

logging.basicConfig(filename=log_filename, level=log_level, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')



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
    
    logging.info(f'Status Code request get_junior_today_attendance -> {resp.status_code}')
    logging.info(f'Request response get_junior_today_attendance -> {resp.json()}')

# Request that "push the hour button". It passes the request with a personal token and the status (bool) of where the student is
def record_attendance(at_home, token):
    hour = datetime.now().hour
    minute = datetime.now().minute
    logging.info(f'Running record_attendace at {hour}:{minute}')
    if hour == 8 or hour == 9:
        time_period = AttendanceTimePeriod.Morning
        # When calling this function here, the first request is sent and then the scheduler is going to trigger and start job for the current request right after
        get_junior_today_attendance(token)
    elif hour == 12:
        time_period = AttendanceTimePeriod.Lunch
    elif hour == 13:
        time_period = AttendanceTimePeriod.Noon
    elif hour == 17 or hour == 18:
        time_period = AttendanceTimePeriod.Evening
    else:
        logging.warning(f'No time period found for hour {hour}')
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
    
    logging.info(f'Status Code request record_attendance -> {resp.status_code}')
    logging.info(f'Request response record_attendance -> {resp.json()}')
    logging.info('Congratulations! You have successfully recorded your attendance!')

def main():
    # Access the environment variable and convert it to a boolean
    at_home = os.environ.get("AT_HOME", "").lower() == "true"
    token = os.environ.get("TOKEN")
    logging.info(f'at_home: {at_home}')

    try:
        record_attendance(at_home, token)
    except requests.exceptions.RequestException as req_error:
        logging.error(f'Request error occurred: {req_error}')
        raise  # Re-raise the exception for further handling
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        raise  # Re-raise the exception for further handling

if __name__ == "__main__":
    main()

logging.shutdown()
