# Installation

    git clone https://github.com/cb12372/zhao_agcn.git
    cd zhao_agcn
    pip install -r requirements.txt

# Original Data：

保存在以下目录：zhao_agcn/data/ntu/xview

链接：https://pan.baidu.com/s/1rAUVhd54MAHIbt7U6DRm0w?pwd=sebi 

提取码：sebi 

# Data Preparation

Preprocess the data with

    cd data/ntu/xview
    python prepare.py
    cd ..
    cd ..
    cd ..


​     
# Training

Change the config file depending on what you want.


    python main.py --config ./config/nturgbd-cross-view/train_joint.yaml
