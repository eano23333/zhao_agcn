# Installation
 
    git clone https://github.com/cb12372/zhao_agcn.git
    cd zhao_agcn
    pip install -r requirements.txt

# Data Preparation
Preprocess the data with
  
    cd data/ntu/xview
    python prepare.py
    cd ..
    cd ..
    cd ..
 

     
# Training

Change the config file depending on what you want.


    python main.py --config ./config/nturgbd-cross-view/train_joint.yaml
