 ## Installation
```shell
git clone https://github.com/eano23333/zhao_agcn.git
cd zhao_agcn
conda env create -f environment.yaml
conda activate zhao_agcn
pip install -e .
```

# Data Preparation

 - Preprocess the data with
  
    `python data/prepare.py`


​     
# Training & Testing

Change the config file depending on what you want.


    `python main.py --config ./config/train_joint.yaml`
    
    `python main.py --config ./config/train_bone.yaml`
