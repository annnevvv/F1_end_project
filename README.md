Formula One Website
This is a final project of Python bootcamp from Software Developmant Academy (SDA). Our group had 40-class-hours to finish that project. For now it is a MVP realization. Our team plans to develop this project systematically. There are still areas that need to be perfected. The next goal is deployment of  this F1 website project. 
This is a Django-based website project focused on providing information and engagement related to Formula One. The website consists of six individual apps, each serving a specific purpose to enhance the user experience and deliver various functionalities. Below is an overview of each app and its features:
Apps
1. Stats App
The Stats app is responsible for retrieving statistics from the Formula One API. It provides the following features:
•	Driver Standings: Displays the current standings of the drivers in the Formula One championship.
•	Constructor Standings: Shows the current standings of the constructors in the Formula One championship.
•	Races Standings: Provides information about the standings of different races in the Formula One championship.
2. Blog App
The Blog app allows users to read and comment on posts related to Formula One. It offers the following functionalities:
•	Post Display: Shows a list of blog posts, including their titles, authors, and publication dates.
•	Post Details: Enables users to view the full content of a blog post and read other users' comments.
•	Commenting: Allows users to leave comments on blog posts to express their opinions and engage in discussions.
3. Quiz App
The Quiz app offers an interactive quiz about Formula One, comprising 15 multiple-choice questions. It incorporates the following features:
•	Questionnaire: Presents users with a series of questions related to Formula One, allowing them to select one answer from multiple options.
•	Scoring: Calculates the user's score based on their answers and provides feedback on their performance.
•	Result Page: Displays the user's score, along with personalized feedback, once the quiz is completed.
4. Events App
The Events app provides information about upcoming events and allows users to sign up for them. It includes the following capabilities:
•	Event Display: Shows a list of F1 race events, including their dates, locations, and additional details.
•	Event Registration: Enables users to sign up for the events they are interested in attending.
•	User Registration Tracking: Once logged in, users can view the events they have registered for.
5. Members App
The Members app facilitates user registration and login functionality, granting users the ability to personalize their experience. Key features include:
•	User Registration: Allows users to create an account by providing necessary details such as username, email, and password.
•	User Login: Provides a secure login mechanism for registered users to access additional features.
•	User Blog Posts: Logged-in users can create their own blog posts and share their thoughts about Formula One.
6. Homepage App
The Homepage app serves as the main gateway to the entire project, providing a comprehensive overview of all the available apps. It encompasses the following functionalities:
•	Project Overview: Displays a brief introduction and description of the Formula One website project.
•	App Navigation: Provides direct links to each individual app, making it easy for users to access their desired features.

Summary
By combining these six apps, the Formula One website project delivers a comprehensive and immersive experience for Formula One fans, providing access to statistics, news, discussions, quizzes, event information, and personalization features. Whether users are seeking information, entertainment, or community engagement, this website aims to cater to their needs and enhance their passion for Formula One. 




Database app fixtures:

There are four database app fixtures ready for upload: members, events, quiz and blog. You find them in each of app fixture directory and upload them in django.  
Stats Database Upload (MySQL):
In this project there is an implemented module available for creating MySQL database and data upload. In current version developers has achieved MVP status. Database is working correctly with proper triggers and settings. We would like to further develop this code. Our goal is to automate the process of pulling data into the database automatically once race is finished.

To set up and update your local database, please follow the steps below:

Update Project Settings mySQL Database:
•	User: Your local username (default: root)
•	Password
•	Host (default: localhost)
•	Port (default: 3306)

1.	/stats/databaseupload/user_data:
•	Update the following settings:
o	Host (default: 'localhost')
o	User
o	Password
2.	/stats/databaseupload/1.Table_creation:
a.	Execute the file- It will automatically create a database on your local machine with basic data
3.	stats/databaseupload/2.Insert_race_results:
a.	Execute the file-
b.	b) Insert the race number (circuitID) you would like to add to the database. Please refer to the circuits table for ID verification.
 
3.	stats/databaseupload/2.Insert_race_results (Optional):
a.	Execute the file
b.	b) Insert the last race number you would like to add to the database. It will automatically update the races from the beginning of the season. For 7 it will fill the data 1 to 7.

4.	/stats/databaseupload/3.Insert_sprint_results:
a.	Execute the file
b.	b) Insert the sprint number associated with the race. If there was a sprint with the 4th race, type 4, and it will add the sprint results to the database with an 's' on the ID number.

 
