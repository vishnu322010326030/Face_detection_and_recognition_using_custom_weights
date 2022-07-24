For training we should have a google account with sufficient space in it because, we use google colab for training.

MY Drive
│   
│
└───Colab_Notebooks
    │     
    │
    └───face_detection_project
         │   backup
         │   custom_weights   ---->  Darknet53.conv.74
         │   darknet          ---->  Makefile
         │   trainingset      ---->  Creating-files-data-and-name.py
                                     Creating-train-test-txt-files.py
                                     classes.names.txt

prepare your drive path in this way for better understanding.

________________________________________________________________________________________________________


run the following commands in the colab for training your dataset.

Run every command in different cell to avoid confusion.

#This command connects our google colab to drive. 
    
         $ from google.colab import drive
           drive.mount("/content/drive")


#(ls)list out all directories in it 

         $ !ls '/content/drive/My Drive/Colab_Notebooks/face_detection_project'


#Here we renamed our dataset as trainingset which we have downloaded from (OIDV4_Tool_kit)

#we have zipped the trainingset and uploaded to our drive (absolute path = '/content/drive/My Drive/Colab_Notebook/face_detection_project')

         $ !unzip '/content/drive/My Drive/Colab_Notebooks/face_detection_project/trainingset.zip' -d '/content/drive/My Drive/Colab_Notebooks/face_detection_project'


#Now download the darknet form the github using git clone command and place it in an empty directory
   
         $ !git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/My Drive/Colab Notebooks/face_detection_project/darknet'


#Enter into the darknet directory
        
         $ %cd /content/drive/My Drive/Colab_Notebooks/face_detection_project/darknet


#This make command build executable programs and libraries from the source code.

         $ !make


#Let's go back to the face_detection_project directory to execute some python files.

         $ %cd /content/drive/My Drive/Colab_Notebooks/face_detection_project


#Execute the trainingset/creating-files-data-and-name.py file and trainingset/creating-train-and-test-txt-files.py

         $ !python trainingset/creating-files-data-and-name.py
        
         $ !python trainingset/creating-train-and-test-txt-files.py


#Now download the darknet53.conv.74 with the help of "wget" from pjreddie.com

         $ !wget https://pjreddie.com/media/files/darknet53.conv.74 -O ./darknet/darknet53.conv.74


#Give the permissions to the darknet (make it executable)

         $ !chmod +x ./darknet/darknet


#check the usage , if you are getting ("usage: darknet/darknet <function>") then, every thing is good.

         $ !darknet/darknet

_________________________________________________________________________________________________________

[BEFORE EXECUTNG THE FINAL STEP , YOU MUST MAKE SOME CHANGES FOR THE TRAINING]

#Enable the gpu ,where you can change it in google colab/edit/notebook settings

#In the darknet/cfg/yolov3_custom.cfg , batch=1 should be commented and batch =2 should run for training and for testing batch=2 should be commented and batch=1 should run

#The max_batches should not be below 2000 even though you train for two images (this tells you how many iterations go ahead with the yolov3)  

#In max_step and min_step, you can go around 20% less than batches we have given up like 400000 -> 5800 and 450000 -> 6200 respectively.

#Find a good text editor (I suggest Notepad++) to make changes in yolov3_custom.cfg , which is in darknet/cgf/yolov3_custom.cfg.

             #open the yolov3_custom.cfg with a text editor and search yolo and change the classes count and filter count based on a formula and do the same in three different places in the file
                          #classes = no.of classes
                          #filters = (no.of classes + 5) * 3

#Create a file name classes with the extension .names and add all the classes names into it and place it in the trainingset.

#Make some changes in Makefile which is in the darknet , download it and open with an text editor and change.
                          #GPU = 1
                          #CUDNN = 1
                          #opencv = 1

# Next go to the Creating-files-data-and-name.py , change the full_path_to_images = 'trainingset'

# Next go to the Creating-train-and-test-txt-files.py , change the full_path_to_images = 'trainingset'


_________________________________________________________________________________________________________

#FINAL STEP ! - run the darknet detector train trainingset , yolov3_custom.cfg and darknet53.conv.74 ( which is in custom_weights).
   
         $ !darknet/darknet detector train trainingset/labelled_data.data darknet/cfg/yolov3_custom.cfg custom_weight/darknet53.conv.74 -dont_show
_________________________________________________________________________________________________________

ABOUT FACE DETECTION :-

Face detection technology is used in many fields: entertainment, security, law enforcement, biometrics, and more. 
Over the years, it has progressed from clunky computer vision techniques all the way to advanced artificial neural networks.
Face detection has a key role in face analysis, tracking, and recognition – but the question is, what exactly is face detection and how does it work? Read on, 
and we’ll break down the term for you, provide examples, and show how it is used in today’s society.


HOW DOES FACE DETECTION WORK?

Face detection technology uses machine learning and algorithms in order to extract human faces from larger images; such images typically contain plenty of non-face objects, such as buildings, landscapes, and various body parts.

Facial detection algorithms usually begin by seeking out human eyes, which are one of the easiest facial features to detect. Next, the algorithm might try to find the mouth, nose, eyebrows, and iris.
 After identifying these facial features, and the algorithm concludes that it has extracted a face, it then goes through additional tests to confirm that it is, indeed, a face.

To make algorithms as accurate as possible, they must be trained with huge data sets that contain hundreds of thousands of images. Some of these images contain faces, while others do not. The training procedures help the algorithm’s ability to decide whether an image contains faces, and where those facial regions are located.

Also, now would be a good time to give you definitions of the main types of algorithms – ML, AI, and Deep Learning.

Machine Learning (ML): ML algorithms use statistics to find patterns in huge amounts of data. This data can include words, numbers, images, clicks, and more.
                       ML is the process behind many modern services – voice assistants (Siri and Alexa), search engines (Google and Baidu), and recommendation systems (Spotify and Netflix)

Artificial Intelligence (AI): If an ML solution is programmed to learn how to perform a task, rather than just simple performance, then it is AI. 
                              Systems that use AI demonstrate behaviors similar to human intelligence – for instance, problem solving, planning, learning, perception, manipulation, and reasoning

Deep Learning: This algorithm is a subset of machine learning, and it is what forms deep neural networks; essentially, machines are given a greater ability to find and amplify tiny patterns.
                Such networks have any layers of computational nodes that collaborate to sift through data and deliver predictions.


Now, as for the exact technologies used to develop face detection applications; these include:

OpenCV
Matlab
Tensorflow
Neural Networks

__________________________________________________________________________________________________________
#It take around 2 hours to train.

#After 2 hours the trained weights will be saved in backup which is in colab_notebook. you can consider the yolov3_custom_6000.weights as your final output trained weights.

<p align="center">
  <img width="540" height="303" src="https://www.pinterest.com/pin/771382242417416307/">
</p>

{
  title={creating custom dataset},
  author={Vishnu},
  year={2022},
  publisher={Github},
  journal={GitHub repository},
  
}
 























