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

 Homepage view 1:
 ![homepage1](https://github.com/annnevvv/F1_end_project/assets/118659024/0ab715b5-dc8d-4ca7-978b-6eaeef91049c)
 
 Homepage view 2:
![homepage2](https://github.com/annnevvv/F1_end_project/assets/118659024/a113f436-b4c1-4e72-84af-bb1e53adc991)

Stats view 1:
![stats1](https://github.com/annnevvv/F1_end_project/assets/118659024/083accb7-3772-4b48-835c-00d309c8aa51)

Stats view 2:
![stats2](https://github.com/annnevvv/F1_end_project/assets/118659024/281c5840-b6dd-44ed-9729-b4dc72f5cc6f)

Stats view 3:
![stats4](https://github.com/annnevvv/F1_end_project/assets/118659024/2458d16d-4531-4e52-a30e-3c2f571b596f)

Stats view 4:
![stats5](https://github.com/annnevvv/F1_end_project/assets/118659024/e394a0ed-9356-45b2-8a8d-274e34402506)

Stats view 5:
![stats6](https://github.com/annnevvv/F1_end_project/assets/118659024/929e2474-d4d8-4e70-9e26-15145d30fc3e)

Quiz view 1:
![quiz1](https://github.com/annnevvv/F1_end_project/assets/118659024/f293a37f-e549-47b7-b3b1-9d4a9779b573)

Quiz view 2:
![quiz2](https://github.com/annnevvv/F1_end_project/assets/118659024/a9bc42f4-ee6a-468f-a20e-a1bbf384fb40)

Blog view 1:
![blog1](https://github.com/annnevvv/F1_end_project/assets/118659024/9bbb2a2d-5ccf-49c6-961e-2337196c68ad)

Blog view 2:
![blog2](https://github.com/annnevvv/F1_end_project/assets/118659024/792c1c29-ae07-4362-bdf2-318021c5be59)

Blog view 3:
![blog3](https://github.com/annnevvv/F1_end_project/assets/118659024/91195ff0-5b0f-464c-bc23-80e26aac5185)

Blog view 4:
![blog4](https://github.com/annnevvv/F1_end_project/assets/118659024/e84cc841-0ef2-4928-acc7-1c039ca87708)

Events view 1:
![events1](https://github.com/annnevvv/F1_end_project/assets/118659024/dbe31ed7-b910-46a3-8248-f37fd2eab391)

Events view 2:
![events2](https://github.com/annnevvv/F1_end_project/assets/118659024/75b54b2f-5d02-4ab7-8d51-ecc556f9dc93)

Events view 3:
![events3](https://github.com/annnevvv/F1_end_project/assets/118659024/b1a5e03a-3792-4c63-9bad-fef3342404bc)

Members view 1:
![members1](https://github.com/annnevvv/F1_end_project/assets/118659024/60441cab-c850-46a6-a9f9-891cf290ea0a)

Members view 2:
![members2](https://github.com/annnevvv/F1_end_project/assets/118659024/e9181c01-f13e-4a97-b3a7-7e4e897d95f7)

Members view 3:
![members3](https://github.com/annnevvv/F1_end_project/assets/118659024/4e230c58-6c08-491b-b319-a2e403dfd73d)

About view 1:
![about1](https://github.com/annnevvv/F1_end_project/assets/118659024/3a89de77-c8e6-4aca-ac7d-7c9b13c3a18c)

About view 2:
![about2](https://github.com/annnevvv/F1_end_project/assets/118659024/aa5dd9a4-9ced-4fb9-bf2a-6445b14a5b14)
