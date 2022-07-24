$ import cv2

________________________________________________

$ import cv2
$ import numpy as np
$ import matplotlib.pyplot as plt

_________________________________________________

$ import cv2
$ net = cv2.dnn.readNetFromDarknet("Desktop\proj\yolov3_custom.cfg",r"Desktop\proj\yolov3_custom_6000.weights")

__________________________________________________

$ classes = ['Aeroplane','Baloon']

___________________________________________________

cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
while 1:

    _, img = cap.read()
while 1:
    img = cv2.resize(img,(1280,720))
    _, img = cap.read()
    hight,width,_ = img.shape
    img = cv2.resize(img,(1280,720))
    blob = cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)
    hight,width,_ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)
    net.setInput(blob)


    net.setInput(blob)
    output_layers_name = net.getUnconnectedOutLayersNames()


    output_layers_name = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_name)


    layerOutputs = net.forward(output_layers_name)
    boxes =[]

    confidences = []
    boxes =[]
    class_ids = []
    confidences = []

    class_ids = []
    for output in layerOutputs:

        for detection in output:
    for output in layerOutputs:
            score = detection[5:]
        for detection in output:
            class_id = np.argmax(score)
            score = detection[5:]
            confidence = score[class_id]
            class_id = np.argmax(score)
            if confidence > 0.7:
            confidence = score[class_id]
                center_x = int(detection[0] * width)
            if confidence > 0.7:
                center_y = int(detection[1] * hight)
                center_x = int(detection[0] * width)
                w = int(detection[2] * width)
                center_y = int(detection[1] * hight)
                h = int(detection[3]* hight)
                w = int(detection[2] * width)
                x = int(center_x - w/2)
                h = int(detection[3]* hight)
                y = int(center_y - h/2)
                x = int(center_x - w/2)
                boxes.append([x,y,w,h])
                y = int(center_y - h/2)
                confidences.append((float(confidence)))
                boxes.append([x,y,w,h])
                class_ids.append(class_id)
                confidences.append((float(confidence)))

                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.5,.4)


    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.5,.4)
    boxes =[]

    confidences = []
    boxes =[]
    class_ids = []
    confidences = []

    class_ids = []
    for output in layerOutputs:

        for detection in output:
    for output in layerOutputs:
            score = detection[5:]
        for detection in output:
            class_id = np.argmax(score)
            score = detection[5:]
            confidence = score[class_id]
            class_id = np.argmax(score)
            if confidence > 0.5:
            confidence = score[class_id]
                center_x = int(detection[0] * width)
            if confidence > 0.5:
                center_y = int(detection[1] * hight)
                center_x = int(detection[0] * width)
                w = int(detection[2] * width)
                center_y = int(detection[1] * hight)
                h = int(detection[3]* hight)
                w = int(detection[2] * width)

                h = int(detection[3]* hight)
                x = int(center_x - w/2)

                y = int(center_y - h/2)
                x = int(center_x - w/2)

                y = int(center_y - h/2)




                boxes.append([x,y,w,h])

                confidences.append((float(confidence)))
                boxes.append([x,y,w,h])
                class_ids.append(class_id)
                confidences.append((float(confidence)))

                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.8,.4)

    font = cv2.FONT_HERSHEY_PLAIN
    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.8,.4)
    colors = np.random.uniform(0,255,size =(len(boxes),3))
    font = cv2.FONT_HERSHEY_PLAIN
    if  len(indexes)>0:
    colors = np.random.uniform(0,255,size =(len(boxes),3))
        for i in indexes.flatten():
    if  len(indexes)>0:
            x,y,w,h = boxes[i]
        for i in indexes.flatten():
            label = str(classes[class_ids[i]])
            x,y,w,h = boxes[i]
            confidence = str(round(confidences[i],2))
            label = str(classes[class_ids[i]])
            color = colors[i]
            confidence = str(round(confidences[i],2))
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            color = colors[i]
            cv2.putText(img,label + " " + confidence, (x,y+400),font,2,color,2)
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)

            cv2.putText(img,label + " " + confidence, (x,y+400),font,2,color,2)
    cv2.imshow('img',img)

    if cv2.waitKey(1) == ord('q'):
    cv2.imshow('img',img)
        break
    if cv2.waitKey(1) == ord('q'):
    
        break
cap.release()
    
cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()

________________________________________________________________________________________________________________________________