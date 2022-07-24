# face_detection
I have done face detection project using self trained weights , to visit my project click https://github.com/vishnu322010326030/face_detection.git


CREATING A DATASET
__________________
__________________

Before creating a dataset , we much dowmload git to our local system.

METHOD-1:
________

Download git through website:

    https://git-scm.com/downloads


METHOD-2:
________

for download git to local system through pip run the below commands:

Step 1: Download PIP get-pip.py

   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Step 2: Installing PIP on Windows

   python get-pip.py

Step 3: Verify Installation

   pip help

Step 4: To Upgrading PIP for Python on Windows

   python -m pip install --upgrade pip

____________________________________________________________________________________________


After downloading git , download ~ OIDv4 ToolKit ~

run the following command in command prompt , but for this you should hava python3:
    
    # 1.Clone this repository
    git clone https://github.com/EscVM/OIDv4_ToolKit.git

    # 2. Install the required packages
    pip3 install -r requirements.txt


____________________________________________________________________________________________



Now , let's download some bunch of picture set for training.

run the below commands to download the pictures

    ###change directory to OIDV4-Toolkit

    $ cd OIDV4-Toolkit

    $ pip install -r requirements.txt

    $ python main.py

    $ python main.py downloader --classes Ballon Airplane Ball_net --type_csv trian --limit 400

    $ python convert_annotations.py

    $ python main.py downloader --classes Ballon Airplane Ball_net --type_csv trian --limit 400 --multiclasses

_________________________________________________________________________________________________________________



The algorith will take care to download all the necessary files and build the directory structure like this:

```
main_folder
│   main.py
│
└───OID
    │   file011.txt
    │   file012.txt
    │
    └───csv_folder
    |    │   class-descriptions-boxable.csv
    |    │   validation-annotations-bbox.csv
    |
    └───Dataset
        |
        └─── test
        |
        └─── train
        |
        └─── validation
             |
             └───Ballon
             |     |
             |     |0fdea8a716155a8e.jpg
             |     |2fe4f21e409f0a56.jpg
             |     |...
             |     └───Labels
             |            |
             |            |0fdea8a716155a8e.txt
             |            |2fe4f21e409f0a56.txt
             |            |...
             |
             └───Airplane
                   |
                   |0b6f22bf3b586889.jpg
                   |0baea327f06f8afb.jpg
                   |...
                   └───Labels
                          |
                          |0b6f22bf3b586889.txt
                          |0baea327f06f8afb.txt
                          |...
```

____________________________________________________________________________________________________
### Explanation about OIDV4-Toolkit


<img align="right" src="images/rectangle.png">

In the __original__ dataset the coordinates of the bounding boxes are made in the following way:

**XMin**, **XMax**, **YMin**, **YMax**: coordinates of the box, in normalized image coordinates. XMin is in [0,1], where 0 is the leftmost pixel, and 1 is the rightmost pixel in the image. Y coordinates go from the top pixel (0) to the bottom pixel (1).

However, in order to accomodate a more intuitive representation and give the maximum flexibility, every `.txt` annotation is made like:

`name_of_the_class    left    top     right     bottom`

where each coordinate is denormalized. So, the four different values correspond to the actual number of pixels of the related image.

If you don't need the labels creation use `--noLabels`.

### Optional Arguments
The annotations of the dataset has been marked with a bunch of boolean values. This attributes are reported below:
- **IsOccluded**: Indicates that the object is occluded by another object in the image.
- **IsTruncated**: Indicates that the object extends beyond the boundary of the image.
- **IsGroupOf**: Indicates that the box spans a group of objects (e.g., a bed of flowers or a crowd of people). We asked annotators to use this tag for cases with more than 5 instances which are heavily occluding each other and are physically touching.
- **IsDepiction**: Indicates that the object is a depiction (e.g., a cartoon or drawing of the object, not a real physical instance).
- **IsInside**: Indicates a picture taken from the inside of the object (e.g., a car interior or inside of a building).
- **n_threads**: Select how many threads you want to use. The ToolKit will take care for you to download multiple images in parallel, considerably speeding up the downloading process.
- **limit**: Limit the number of images being downloaded. Useful if you want to restrict the size of your dataset.
- **y**: Answer yes when have to download missing csv files.

Naturally, the ToolKit provides the same options as paramenters in order to filter the downloaded images.
For example, with:
  ```bash
   python3 main.py downloader -y --classes Ballon Airplane --type_csv validation --image_IsGroupOf 0
   ```
only images without group annotations are downloaded.

# 3.0 Download images from Image-Level Labels Dataset for Image Classifiction
The Toolkit is now able to acess also to the huge dataset without bounding boxes. This dataset is formed by 19,995 classes and it's already divided into train, validation and test. The command used for the download from this dataset is ```downloader_ill``` (Downloader of Image-Level Labels) and requires the argument ```--sub```. This argument selects the sub-dataset between human-verified labels ```h``` (5,655,108 images) and machine-generated labels ```m``` (8,853,429 images). An example of command is:
```bash
python3 main.py downloader_ill --sub m --classes Ballon Airplane --type_csv train --limit 400
```
The previously explained commands ```Dataset```, ```multiclasses```, ```n_threads``` and ```limit``` are available.
The Toolkit automatically will put the dataset and the csv folder in specific folders that are renamed with a `_nl` at the end.
# Commands sum-up

|                    | downloader | visualizer | downloader_ill |                                                  |
|-------------------:|:----------:|:----------:|:--------------:|--------------------------------------------------|
|            Dataset |      O     |      O     |        O       | Dataset folder name                              |
|            classes |      R     |            |        R       | Considered classes                               |
|           type_csv |      R     |            |        R       | Train, test or validation dataset                |
|                  y |      O     |            |        O       | Answer yes when downloading missing csv files    |
|       multiclasses |      O     |            |        O       | Download classes toghether                       |
|           noLabels |      O     |            |                | Don't create labels                              |
|   Image_IsOccluded |      O     |            |                | Consider or not this filter                      |
|  Image_IsTruncated |      O     |            |                | Consider or not this filter                      |
|    Image_IsGroupOf |      O     |            |                | Consider or not this filter                      |
|  Image_IsDepiction |      O     |            |                | Consider or not this filter                      |
|     Image_IsInside |      O     |            |                | Consider or not this filter                      |
|          n_threads |      O     |            |        O       | Indicates the maximum threads number             |
|              limit |      O     |            |        O       | Max number of images to download                 |
|                sub |            |            |        R       | Human-verified or Machine-generated images (h/m) |

R = required, O = optional

# 4.0 Use the ToolKit to visualize the labeled images
The ToolKit is useful also for visualize the downloaded images with the respective labels.
```bash
   python3 main.py visualizer
   ```
  In this way the default `Dataset` folder will be pointed to search the images and labels automatically. To point
  another folder it's possible to use `--Dataset` optional argument.
```bash
   python3 main.py visualizer --Dataset desired_folder
   ```
Then the system will ask you which folder to visualize (train, validation or test) and the desired class.
Hence with `d` (next), `a` (previous) and `q` (exit) you will be able to explore all the images. Follow the menu for all the other options.

<p align="center">
  <img width="540" height="303" src="images/visualizer_example.gif">
</p>

{
  title={creating custom dataset},
  author={Vishnu},
  year={2022},
  publisher={Github},
  journal={GitHub repository},
  
}
```

Training_Dataset
________________
________________



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
 

Execution part
______________
______________



Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.
The distribution includes data-science packages suitable for Windows, Linux, and macOS.

Why it matters:

it contains conda ,Anaconda Navigator, Python,and many scientific packages for Machine Learning.

Anaconda Navigator is a GUI that allows you to launch applications like Spyder IDE is used for deep learning programming in best way and also easily manage conda packages.

________________________________________________________________________________________________________________________

### How you can install Anaconda

step1: Go to the Anaconda Website and choose a Python 3.x graphical installer (A) or a Python 2.x graphical installer (B)

step2: Locate your download and double click it.

step3: When setup screen appears, click on Next.

step4: Read the license agreement and click on I Agree.

step5: Click on Next.

step6: Note your installation location and then click Next.

step7: The recommended approach is to not check the box to add Anaconda to your path.
        (you can always add Anaconda to your PATH later if you don't check the box)

step8: Click on Next.

step9: You can install Microsoft VSCode if you wish, but it is optional.

step10: Click on Finish.

_________________________________________________________________________________________________________________________

### Add Anaconda to Path

step1: Open a Command Prompt.

step2: Enter the commands below into your Command Prompt:
       
       conda --version

       python --version

step3: If you don't know where your conda and/or python is, open an Anaconda Prompt and type in the following commands:

       where conda

       where python

step4: Add conda and python to your PATH. You can do this by going to your Environment Variables and adding the output of step 3 to your path.

step5: Open a new Command Prompt. Try typing conda --version and python --version into the Command Prompt to check to see if everything went well.

_______________________________________________________________________________________________________________________

