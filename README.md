# PROJECT TITLE:  AttendEase AI

[Link To Proposal](https://docs.google.com/document/d/1unNH3bXb-GxBl88jow0WgRBcK-YXlXJFcqL31G55IZ0/edit?usp=sharing)


### The Structure of this Readme File

+ Introduction to the Project
+ App Demonstration
+ Dependencies
+ Guide to Set up on local Server
+ Guide to the App's architecture.
+ Guide Cloud Hosting
+ Exceptions Handling
+ Conclusions and Final Words


### Introduction To AttendEase.ai

AttendEase AI is an application that helps teachers to track the attendance of their students through the help of computer vision, A.I. models, and a real-time cloud-based database.

### [Application Demo Video](https://www.loom.com/share/80cd9c787e474ada982bf9bdf5143d94)
### [Link To Cloud DataBase](https://console.firebase.google.com/project/face-attendance-f13a6/database/face-attendance-f13a6-default-rtdb/data)


### Dependencies:
These are the modules and the libraries that support this application. To run this application, you must have these modules installed.

- Cv2, 
- os, 
- pickle,  
- Flask, 
- cvzone, 
- face_recognition, 
- firebase_admin, 
- numpy as np,  
- datetime


### Guide To Setup

This app runs locally, and these are the steps to setting this app up in your local environment.

**Step 1:** Clone the repository / download the project as a zip file




**Step 2:** Open the file Main.py in your preferred Ide, But PyCharm is our preference.



**Step 3:** Install all Modules and run the file.

**Step 4:** The application has three registered students, including Kim Kardashian, and Kendal Jenner. Get a picture of either of these two celebrities and hold it to the view of the camera.



### Guide to App Architechture

Our app is built across four main sections. We have explained the sections in detail, the importance, and the unique features of each.

**Web Cam Set Up:** The most important feature of our app is that it recognizes students' faces. This is only possible by accessing the webcam of the computer. The first part of our algorithm calls the webcam.

**U.I. Graphics:** To make the application understandable to look at, we placed a frame of graphics around it. The user interface you see is a frame that is placed accurately around the webcam pop-up. We also placed text on this graphic. We named these graphics modes, and when a condition is met, like when a student has been marked, a new mode(graphic) comes up. Below is an example of such images.




**Encoding Generator:** Not forgetting that learning part of artificial intelligence, we included the algorithm pictures of the three students: Kim Kardashian, Kendall Jenner, and Adeyemi Testimony. And our code encoded their faces and saved them in a file for our algorithm to refer to it whenever it finds a face. 

**Database Set Up(Cloud Hosting):** Our app will lose its essence without real-time database tracking. Hosted on Firebase, the facilitator can upload new students' details. He can also find the real-time attendance standing of each student. 




### Handling Exceptions: 

This app only takes the student's pictures as input. There are two main errors we can run into. First is No internet access, and the second is the student's face recognition frequency. And we tried to handle these. For no internet access, we made this app to run via the web, and when there is so internet access, the web page indicates so with HTTP connection errors.

To avoid students taking attendance endlessly, we added a restriction that does not allow a student to log another attendance within a 30-minute span from the last attendance recorded.




### Conclusions and Final Words

Reconciliation With  Technical Requirements:

**Platform Technical Requirement**
The desktop application should be compatible with major desktop operating systems, such as Windows, macOS, and Linux. The project will be built with pycharm IDE on a Windows operating system.
**Platform Implementation**
The application was built with Pycharm IDE on a Windows operating system and is compatible with Windows, macOS, and Linux operating systems, provided the required modules are installed.


**Framework Technical Requirement**
The application's G.U.I. should be built using Tkinter.
**Framework Implementation**
The application's GUI was built off image templates. Tinkter was no longer used as the application does not require any input from the students and teachers aside from the student's faces. All other details are pre-encoded and saved on the database.


**User Interface Technical Requirement**
The desktop application should have a user-friendly, responsive interface design with clear and concise instructions. The design must be intuitive.
**User Interface Implementation**
The user interface is clear and concise. It shows when a student has been marked and displays the student’s details neatly.


**Back-End Technical Requirement**
The desktop application should have an easily accessible database management system. Our choice is google sheets for its accessibility and ease of manipulation. This might change in the future to a more complex and robust system like MongoDB.
**Back End Implementation**
The application’s database is hosted on Firebase, a Google-owned cloud service. It is safe and yet easy to use. It is secure and easily accessible.

**In Conclusion:** This project was daunting, starting from learning the basics of computer vision and real-time database management systems. But it worked. Coupling research with trial and error, we set up the app. 
During all of this, we realized the underrated power Artificial Intelligence holds. At some point, we started to consider the risks that our app might pose to society. If we go a step further, add a feature that collects the location where the person's face is detected, this could be a mainstream tracking app that tracks people's faces and the places they have been.
The possibilities and dangers are endless. This project has taught us this.








