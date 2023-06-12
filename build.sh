# prepares the runtime and install all dependencies

set -e  # breaks the script if encounters an exception 

sudo apt -y update # update the repo list 
sudo apt -y install python3 python3-pip python3-venv # install python 
python3 -m venv venv  # create a venv
source venv/bin/activate  # activate the venv 
python3 -m pip install --upgrade pip # upgrade pip to its latest version
pip install -r requirements.txt # install dependencies 

echo Build Complete!  # done !