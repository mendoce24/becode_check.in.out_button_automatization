import requests
from enum import Enum
from datetime import datetime
import os
import logging


# `log_filename = 'my_script.log'` is setting the name of the log file to be created as
# "my_script.log". This file will store the log messages generated by the script.
log_filename = 'my_script.log'
log_level = logging.INFO

# `logging.basicConfig()` is a function from the Python `logging` module that sets up the basic
# configuration for logging.
logging.basicConfig(filename=log_filename, level=log_level, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# The class `AttendanceTimePeriod` is an enumeration that represents different time periods for
# attendance.
class AttendanceTimePeriod(Enum):
    Morning = 'MORNING'
    Lunch = 'LUNCH'
    Noon = 'NOON'
    Evening = 'EVENING'

def day_object():
    """Getting day object for the junior_attendance request"""
    return datetime.timestamp(datetime.now())

def is_at_home():
    """
    The function `is_at_home()` checks if today is Wednesday or Friday.
    :return: The function is_at_home() returns True if today is Wednesday (weekday 2) or Friday (weekday
    4), and False otherwise.
    """
    today = datetime.now().weekday()
    return today in [0, 2, 4]

# Request that pass the object of the day, hour, minute and second to becode graph regarding the time frame which the button was pushed
def get_junior_today_attendance(token):
    """
    The function `get_junior_today_attendance` sends a request to an API to retrieve the attendance of
    junior members for the current day.
    
    :param token: The `token` parameter is a string that represents the authentication token required to
    access the API. It is used in the `Authorization` header of the request to authenticate the user and
    authorize access to the requested resource
    """
    
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
    """
    The function `record_attendance` logs the current time and determines the time period based on the
    hour, and then calls another function based on the time period.
    
    :param at_home: The `at_home` parameter is a boolean value indicating whether the attendance is
    being recorded for students who are attending classes remotely from home. If `at_home` is `True`, it
    means the attendance is being recorded for students who are studying from home. If `at_home` is
    `False`,
    :param token: The `token` parameter is a token that is used for authentication or authorization
    purposes. It is likely used to authenticate the user or verify their access privileges before
    allowing them to record attendance
    :return: None if no time period is found for the current hour.
    """
    hour = datetime.now().hour
    minute = datetime.now().minute
    logging.info(f'Running record_attendace at {hour}:{minute}')
    if hour in [8, 9]:
        time_period = AttendanceTimePeriod.Morning
        # When calling this function here, the first request is sent and then the scheduler is going to trigger and start job for the current request right after
        get_junior_today_attendance(token)
    elif hour == 12:
        time_period = AttendanceTimePeriod.Lunch
    elif hour == 13:
        time_period = AttendanceTimePeriod.Noon
    elif hour in [17, 18]:
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
    """
    The main function accesses an environment variable, converts it to a boolean, logs the value, and
    then calls the record_attendance function, handling any request or unexpected errors that may occur.
    """
    at_home = is_at_home()
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

# The `if __name__ == "__main__":` condition checks if the current script is being run as the main
# module (i.e., directly executed) or if it is being imported as a module into another script.
if __name__ == "__main__":
    main()

# The `logging.shutdown()` function is used to perform a clean shutdown of the logging system. It
# should be called at the end of the script to release any resources used by the logging system. This
# function is optional and not always necessary, but it can be useful in certain situations to ensure
# that all log records are flushed and any open log files are closed properly.
logging.shutdown()
