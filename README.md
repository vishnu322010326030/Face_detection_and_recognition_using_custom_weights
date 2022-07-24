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


























