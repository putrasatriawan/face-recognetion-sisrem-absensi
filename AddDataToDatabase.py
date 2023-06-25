import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL': ""})

ref = db.reference('Students')

data = {
        "1":
            {
                "name": "Orang India",
                "major": "Robotika",
                "starting_year":2018,
                "total_attendance":6,
                "standing": "G",
                "year":4,
                "last_attendance_time": "2023-2-23 21:41:49",

        },
   

}

for key,value in data.items():
    ref.child(key).set(value)
