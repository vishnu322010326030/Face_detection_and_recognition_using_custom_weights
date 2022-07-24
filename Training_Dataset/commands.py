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

#FINAL STEP ! - run the darknet detector train trainingset , yolov3_custom.cfg and darknet53.conv.74 ( which is in custom_weights).
   
         $ !darknet/darknet detector train trainingset/labelled_data.data darknet/cfg/yolov3_custom.cfg custom_weight/darknet53.conv.74 -dont_show
_________________________________________________________________________________________________________