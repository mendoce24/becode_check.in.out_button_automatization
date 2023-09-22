import requests
from enum import Enum
import sys

class AttendanceTimePeriod(Enum):
    Morning = 'MORNING'
    Lunch = 'LUNCH'
    Noon = 'NOON'
    Evening = 'EVENING'    

args = sys.argv
at_home = bool(args[1])
time_period = AttendanceTimePeriod(args[2])

becode_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoib3duZXIiLCJ1aWQiOiI2ZDI4NmYwNy0wMzMzLTQyYTItOTNjNy1hZjhhYzNlNzg1OGYiLCJrZXkiOiI0ZGI1MmI3NyIsImlhdCI6MTY5NTExMTA5OH0.ZSdvZwHKYCA29yg3yEQTWtHqvQyYJNFHhvODRhdkF_s'
becode_payload = {"operationName":"record_attendance_time","variables":{"period":time_period.value,"atHome":at_home},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"553ae433516c13a97e348d4a48dd0114d1949f791ab21d97bed27030a65e85a8"}}}

resp = requests.post('https://graph.becode.org/',
                     json=becode_payload,
                     headers={'Authorization': f'Bearer {becode_token}'})
