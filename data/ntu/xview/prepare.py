import pickle
import numpy as np
import pandas as pd
import os


num_array = [str(i) for i in range(0, 4599)]  # 从'1'到'4599'
zero_array = [0] * 4599  # 创建4599个0

# 将两个数组放入一个列表中
data_to_save = [num_array, zero_array]
data_to_save = tuple(data_to_save)

# 将数据写入Pickle文件
with open('val_label.pkl', 'wb') as file:
    pickle.dump(data_to_save, file)



#将npy转换pkl
# path处填入npy文件具体路径
np_file = np.load(r'train_label.npy')
# 将npy文件的数据格式转化为csv格式
np_to_csv = pd.DataFrame(data=np_file)
# 存入具体目录下的np_to_csv.csv 文件
np_to_csv.to_csv(r'data_test.csv')
cvs_file = 'data_test.csv'
data = pd.read_csv(cvs_file)
pkl_file = 'data_test.pkl'
data.to_pickle(pkl_file)
with open('data_test.pkl', 'rb') as f:
    load_data = pickle.load(f)
load_data_1 = load_data.T

load_data_1 = load_data_1.values.tolist()
load_data_2 = [str(i) for i in load_data_1[0]]

data = [load_data_2,load_data_1[1]]
data = tuple(data)

with open('train_label.pkl', 'wb') as f:
    pickle.dump(data, f)