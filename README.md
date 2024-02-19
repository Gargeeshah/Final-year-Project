**Chapter 1**

**INTRODUCTION**

Measuring the HR of people has multiple applications in telemedicine, Internet-of-Things(IoT),
sports, security, etc. However, sometimes it is difficult to use a classic method for mea-
suring HR or the classical method does not scale. This project presents a solution that
works on live video streams and can measure the HR of multiple people at the same time.
This chapter discusses the overview, motivation, problem definition and objectives of the
project, project scope and its limitations and methods used behind this project.
The heart rate of a person represents the number of heart beats per minute. It is an
essential physiological parameter, a source of information related to the entire cardiovas-
cular system. People who are less physically active are expected to have a higher heart
rate, as their heart muscle has to work harder to maintain a constant cardiac rhythm.
Also, there are situations in which continuous heart rate monitoring is required but skin
contact is problematic, and the patient feels uncomfortable to be continuously connected
to a pulse measuring apparatus. So there is a need to design a system which will continu-
ously monitor the condition of patients heart rate. It is useful for patients/doctors safety
and also reduces the spread of covid-19.
This system is composed of:
• Monitoring Devices like web cam/Camera required at the monitoring environment.
• Web server/ Cloud platforms provide a multiple of services that can be integrated
with web apps to rapidly develop features. These can be hosted on a cloud service
and accessed virtual.

***1.1 Problem Definition***

The problem definition of this project is as follows:
“ To monitor and detect the Heart Rate using Image processing, and wireless networks in
order to provide a real time system in the medical field ”.

***1.2 Objectives***

The list of objectives to be completed for this project are as follows:
• To measure the rate of heartbeat of a person ,without any physical contact.
• To observe multiple persons heart rate at the same time.
• To provide alert message while emergency.
• To develop a flask based web application for GUI.

Activities per Objective
1. To measure the rate of heartbeat of a person ,without any physical contact.
• The subject needs to be relaxed, steady and to be seated in front of the web cam.
• The distance between the camera and the patient can vary between 1 and 3 meters.
• The region of interest to be selected is forehead.
2. To observe multiple persons heart rate at the same time.
• Collecting the data of patients from different rooms to the single destination.
• Examine multiple patients from one location.
3. To provide alert message while emergency.
• Trigger message when the heart rate are abnormal.
• Set the threshold value or range to limit the abnormality.
• Emergency action is to be taken quickly.
4. To develop a Flask based web application for GUI.
• Flask is built in development server and debugger, integrated unit testing support,
RESTful request dispatching, support for secure cookies (client side sessions),uses
Jinja2 templating.
• OpenCV is used as an image processing library in many computer vision real-time
applications. There are thousands of functions available in OpenCV. These simple
techniques are used to shape our images in our required format.

***1.3 Project Scope and Limitations***

No matter what project methodology you choose, it will require you first and foremost to
define the scope of the project. The scope states what the objectives of the project are
and what goals must be met to achieve success.
Scope:

1. Easy to operate like any other website and android app.
2. The purpose of web-platform or website being developed for live monitoring of pa-
tient.
3. Android app is developed for doctor/admin to observe patients.
4. It saves doctor time in going to the each patient and check them.
5. It provide user a single concise about the heart rate.
6. Doctor can monitor and observe individual patient easily by using android app with-
out having to go through each patient .
7. Above all, the web-platform and Android app will provide a comfortable user expe-
rience.
8. It also provides Emergency Alert for patients such as abnormal change in heart rate
There are some limitations to this project which can be worked upon in the future. Some
of them are as follows:
• The subject or patient must be seated in front of the camera.
• Local network is required i.e all the devices must be connected to a same network.
• Poor network connection may lead to inefficiency of the website.

***1.4 Methodologies of Problem solving***

1. Face Detection
The preliminary stage of the system is to detect the subject which needs to be steady
in front of the web camera. The live video streaming must continuously progress so
that face can be detected or it can also detect the absence of subject. The most
important part is to detect the single subject through the camera so that we will be
using a haar cascade classifier which is an effective object detection way and helps to
locate the subject in the live video. Face detection is refined further by extracting
the forehead area specially for better accuracy.
2. Defining Parameter
The different parameters need to be set to increase the accuracy of the system.
The required parameter are discussed below:
• Web Camera parameter: Different parameters are defined based on require-
ments like number of VideoframeRate, Video channel count and some video
capturing parameter. This parameter changes according to the user.
• Color Magnification Parameters: There are a number of frames captured which
need to store for accurate magnification of exact colours. So for that buffer size
and buffer index are needed to set it initially some threshold values like mini-
mum and maximum frequency for defining the range for frequency rate.
• Heart Rate Calculation Parameters: We need to set some limit for beats per
sec to use a specific count of frame frequency to achieve the accuracy.
3. Image Pyramid
This stage is to extract the feature from the face color variant. These images can
be studied deeper using the image pyramid. There are two types of image pyramid.
They are (A) Gaussian Pyramids (B) Laplacian Pyramids. Here we used a gaussian
pyramid which consists of multi scale copies of image and used as a low pass filter for
image blurring. In the gaussian pyramid, the image resolution reduces level by level
to discover the smallest magnifying image. It comprises down sampling of image,
scale search and extract the major characteristics. The gaussian pyramid rectifies
the color changes happening in images and enlarges it level by level. After extracting
features the level again reconstructs into its original size and displays the continuous
streaming.
4. Heart Rate Estimation
The gaussian pyramid gives refined image in the smallest pixel and on that image
the color magnification algorithm is utilized to locate the variant in color alternate in
veins for precise body inside video for getting the change in parameter, the bandpass
filter is used and grab that pulses the amplify it. For finding the frequency, Fourier
transform is used and calculate the mean average of frequency and for best result we
take 15 as a video frame rate. The resultant value of frequency we get is in hertz.
As per the requirement to calculate heart beat per second we need some mathemat-
ical equation to convert hertz into beats per sec. After getting the frequencies we
need to reconstruct the frames. The result based on the frame rate to be chosen for
calculating the frequency. When the first 15 image frames are read, the actual time
Heart rate extraction begins and after that each value is introduced to the firebase
and the approach presents a new Heart Rate.
Till the point the overview of proposed system followed by motivation and problem defi-
nition along with objectives has been known. The studies carried out by various authors
related to proposed system will be figured out in further chapter.

**Chapter 2**

**SYSTEM DESIGN**

This chapter gives all the system designs such as system architecture and all the UML
diagrams e.g. use-case diagram, class diagram, activity diagram, sequence diagram, etc.

![System Architecture](https://github.com/Gargeeshah/Final-year-Project/tree/main/Img/System Architecture.png)

A system architecture or systems architecture is the conceptual model that defines the
structure, behavior, and more views of a system. An architecture description is a formal
description and representation of a system, organized in a way that supports reasoning
about the structures and behaviors of the system.
The architecture of the system is divided into 4 layers Face detection, Image reduction,
Extraction, Backend as shown in 4.1. The face detection layer describes the Haar Cascade
classifier used to detect any object here its is face. Haar Cascade classifier consists of Haar
feature and Cascade filter. After detecting face it will extract the region of interest i.e.
forehead by using this classifier only. The Image Reduction layer uses Gaussian pyramid
for different resolution of image frames. Gaussian pyramid is a two step process -
1. Downward pyramid: Also known as Gaussian pyramid construction which takes input
as frames(i.e. images of face) and breaks down level by level as we want to check
heartrate or colour variation on different levels. As colour variation is not feasible at
normal scaling thus we need to consider different levels.
2. Upward pyramid: Also known as Gaussian pyramid reconstruction which is reverse of
downward pyramid. To maintain the originality of image it is necessary to reconstruct
the image level by level.

Next is to extract RGB features from the ROI, and by applying Euler colour magnification
algorithm on it heart rate is calculated. Bandpass filter will pass the particular frequency
only i.e. heart rate whose frequency range is 1Hz - 2Hz and Fast Fourier Transform is
used to transform an image between the frequency domain. Database connectivity will be
provided for storing each patient’s hear rate. The backend data will be stored in multiple
NoSQL databases. and when heart beat is beyond or above the threshold value text
message will be send to admin’s side through Twilio messaging tool.

**Chapter 3**

**PROJECT IMPLEMENTATION**

Here in this chapter, the project implementation details such as various project modules,
different technologies and tools used to implement system functionalities are discussed.
Also the algorithms of various system modules are stated.

**3.1 Overview of Project Modules**

The proposed system presents the heart rate monitoring system without any physical
contact. The system detects the face of the subject via the digicam and performs image
processing based totally on frames and calculates the coronary heart rate. The aim behind
this system is to avoid physical contact and grant an emergency remedy to the situation
to limit the hazard and additionally alert will set off via textual content message to admin.
The proposed system consists of different modules : (A) Face Detection, (B) Defining
Parameter, (C) Image pyramid, and (D) Heart Rate Estimation.

***3.2 Algorithm Details***

The algorithms used in the project are mentioned in this section.

3.2.1 Algorithm 1
Algorithm Face Detection
1. Start
2. Selecting Haar-like features which is Horizontal,vertical,Diagonal
3. Creating an integral image to the sum of pixel values in an image or rectangular part
of an image.
4. Running AdaBoost training
5. Creating classifier cascades
6. Classifies the face and shows the Green box.
7. End.
3.2.2 Algorithm 2
Algorithm Gaussian Pyramid
1. Start.
2. Start with the original image.
3. Iteratively compute the image at each level of the pyramid, first by smoothing the
image (with the Gaussian filter) and then down-sampling it.
4. Stop at a level where the image size becomes sufficiently small (for example, 1 X 1).
5. The function to implement the previous algorithm is left as an exercise for the reader
6. Stop.
3.2.3 Algorithm 3
Algorithm Colour Magnification
1. Start.
2. Take a standard frame as input and apply spatial decomposition.
3. Apply temporal Filtering to the frames.
4. The resulting signal is then amplified.
5. Reveal hidden colour changes in veins by visualizing the flow of blood.
6. Temporal Frequencies are selected to calculate heart rate.
7. End.
3.2.4 Algorithm 4
Algorithm Heartrate Estimation
1. Start.
2. Result provided by colour magnification is passed to the Mathematical Module.
3. Fast Fourier Transform gives the frequency of heartRate.
4. Then the frequency is convert into beats per sec
5. Estimate the Heart rate and go on updating.
6. End.

This chapter covers the various implementation tools and technologies used for the pro-
posed system in brief. It also describes various modules created for the system and the
algorithms developed to implement the same respectively.

**Chapter 4**

**RESULTS**

The seventh chapter explored the topic software testing. Test cases used for testing the
modules of the project along with their expected and actual outputs are also mentioned.
This chapter describes the final output of the proposed systems. It also is the proof
that all the functional models are efficiently implemented.

***4.1 Outcomes***

According to the plan, the final outcome was supposed to be web-application/website that
a user can access. The web-application is successfully build as planned in the earlier stages.
The proposed system gave following outcomes as a result:
• An interactive, user-friendly interface.
• The user will get to know Heart-rate.
• The user need not go through physical contact of any apparatus to check heart rate.
• The use of heart rate monitor and detector web platform will increase the safety and
reduce considerable amount of time delay in emergency situation.
• The tracking facility to admin through an android app will help the admin/doctor
to monitor and analyze the multiple patients/users depending on the situation and
health status of them.
• The admin/Doctor is not accessing the android app then also he/she will get an
emergency alert on mobile phone through a message about the patient’s emergency.

***WEB APPLICATION***

Figure 4.1 describes the process, designed in such a way to run on a local host server
that is a deployment server which is used for debugging and tracking multiple hosts con-
nected to the server.

The figure 4.2 is a screen shot of the login page which asks the user’s email and password
for authentication.

After successful login, the main interface appears which shows the camera frame and green
frame at the center for the user where face detection is done so heart rate is calculated as
shown in figure 4.3.

The figure 4.4 shows where the face is detected or not in the frame and shows the message-
face Not Detected.

Estimating heart rate and storing, updating in the database as shown in figure 4.5 is done
simultaneously. For each user data is stored in excel sheet.

***ANDROID APP***
Figure 4.6 shows a splash page in android app. A splash page is a page that precedes
any page on your website. A splash screen can appear while a game or program is launch-
ing. It is an introduction page on a website.

The figure 4.7 is a screen shot of the login page which asks the user’s email and password
for authentication in android app.

The image 4.8 shows the dashboard displaying the heart rate of multiple patients, which
is accessible to admin,can continuously keep track of heart rate of each patient and also
heart rate keeps on updating frequently.

The image 4.9 shows the virtual monitoring of user/patient through clicking the check
button of respective person in android app.

The figure 4.10 shows where the face is detected or not in the frame of an android app
and shows the message-face Not Detected.

Text message as shown in figure 4.11 is sent to the given number in case of any abnormality
in heart rate i.e. it goes beyond or below the threshold value.

***4.2.1 Analysis***
In order to measure accuracy of our system, we have calculated heart rate on the system
and compared it with already existing technologies/apparatus like Oximeter, Smartwatch,
Heart rate monitoring(android app), etc. Total for each tool we have mentioned 20 read-
ings i.e. total = 60.

To determine accuracy and error rate we need to know formula and corresponding vari-
ables:

Let x = Average heart beat from oximeter/app/watch.
y = Heart beat from our system.
Error rate:

Errorrate = absolute(x − y)/x ∗ 100 .......................(4.1)
By putting values of x and y i.e. in first case x will be heart rate from oximeter and like
wise. y in all cases will be heart rate from the system, we will get the percentage of error.

Note - Take absolute value of (x - y).
Accuracy:

Accuracy = 100 − error (8.2)
Subtracting error percentage or error rate from 100 will give us accuracy of our system
with respect to the corresponding technology.

As shown in table 4.1 total 20 readings are displayed for each standard method which is
taken at a 2 min interval rate and we got the respective average heart rate value from 20
readings of each tool.
Substituting x and y in both the above equation, we successfully determine the accuracy.
From table 8.2 highest accuracy of the proposed system is achieved in respect with oxim
eter. Also accuracy of our system is directly proportional to intensity of light, so it is highly
recommended to execute this in proper brightness and according to the study made on
wrist-monitor accuracy [12], [13], it is found that smart watches are accurate about 91-94%
with respect to standard measuring heart rate tools. Also, they are less accurate after
doing any activity. Where as oximeters are considered reliable, accurate and portable.

**Chapter 5**

**CONCLUSION**

***5.1 Conclusion***
The purpose of the Heart rate detection system is to help the user to monitor the heart
rate and also monitor multiple people heart rate through an android app .The main aim
behind the proposed system is to provide contactless monitoring and heart rate checkup
that will be displayed at one place which will increase the safety of doctors .among all the
pulse monitoring methods, the non-contact ones are considered to be the safest nowadays.
The approach presented in the proposed system is to solve many problems of heart rate
monitoring like emergency treatment and provide an android app for multi-user heart rate
monitoring to maintain the social distance. An analysis will be performed on the facial
video and frequency beat of heart that directly affect the performance and accuracy of the
application. According to the objectives defined in chapter 1, all of the were implemented
in the order below.
1. Measure the rate of heartbeat of a person ,without any physical contact.
2. Observe multiple persons heart rate at the same time.
3. Monitor and analyze the rate of heart beat in real time condition.
4. Develop a flask based web application for GUI.
5. Develop Android App for multi user Monitoring.
6. Emergency Alert for critical Situation.
7. Maximizing accuracy by reducing error rate.
***5.2 Future Work***
This system can further be extended and can be integrated with more featured treatment

entities like emotions,Blood pressure ,Gesture,Mask detection and any other medical as-
pects that are suitable. Also,automation in the medical field is possible by using this

proposed system with extra added features .