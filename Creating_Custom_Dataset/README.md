creating a dataset.

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
























