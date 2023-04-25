import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-f13a6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "001":
        {
            "name": "Kim Kardashian",
            "major": "Computer Sc",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "002":
        {
            "name": "Kendal Jenner",
            "major": "Computer Sc",
            "starting_year": 2021,
            "total_attendance": 2,
            "standing": "Bad",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "003":
        {
            "name": "Adeyemi Testimony",
            "major": "Computer Sc",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
