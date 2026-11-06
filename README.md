Smart Attendance and Time Tracking System

A simple attendance management application built with Python and Streamlit.

About the Project

I started this project to explore how Python can be used to solve everyday problems through software development.

The idea is to build a system that makes student attendance management easier, more organized and less dependent on manual record keeping.

The application is still a work in progress, and I'm gradually adding new features as I develop it.

What It Can Do So Far

- Register students with their names and student IDs.
- Prevent students from registering with an ID that already exists.
- Display a list of registered students.
- Remove students from the registration list.

Technologies

- Python – application logic.
- Streamlit – user interface.

Project Structure

smart_attendance_system/
│
├── app.py
├── module/
│   ├── attendance.py
│   └── time_tracking.py
│
├── database/
├── assets/
├── Requirements.txt
├── README.md
└── .gitignore

What's Next?

I'm working towards adding features such as:

- Student attendance check-in and check-out.
- Automatic time tracking.
- Attendance history and records.
- Database integration.
- Attendance reports.

Running the Project

Clone the repository:

git clone https://github.com/IMMNUEL327/smart-attendance-system.git

Install the dependencies:

pip install -r Requirements.txt

Run the application:

python -m streamlit run app.py

A Little Note

This project is part of my journey in learning Python and building practical software applications. I'm using it to improve my programming skills, understand how applications are structured, and gain hands-on experience with software development.
