import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL': "https://faceattendacerealtimebyputra-default-rtdb.firebaseio.com/"})

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
    "2":
        {
            "name": "Bule",
            "major": "Manajemen",
            "starting_year": 2019,
            "total_attendance": 3,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-2-23 21:41:49",

        },
    "3":
        {
            "name": "Mas Elon",
            "major": "Teknik Kedokteran",
            "starting_year": 2018,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-2-23 21:41:49",

        },
    "4":
        {
            "name": "Tri Putra Satriawan",
            "major": "Teknik Politik",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-2-23 21:41:49",

        },
    "5":
        {
            "name": "Fadil",
            "major": "Perternakan Dinosaurus",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2023-2-23 21:41:49",

        },
    "6":
        {
            "name": "Femmy",
            "major": "Guru Besar Batujajar",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-2-23 21:41:49",

        },
    "7":
        {
            "name": "Aura",
            "major": "Dkv",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2023-2-23 21:41:49",

        },


}

for key,value in data.items():
    ref.child(key).set(value)