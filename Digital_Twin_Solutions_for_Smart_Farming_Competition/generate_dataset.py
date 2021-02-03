# 用於產生LSTM的訓練資料
import pandas as pd
import os
import numpy as np
from tqdm import tqdm

PATH_org = r'D:\dataset\2021智慧農業數位分身創新應用競賽\org'
PATH_all = r'D:\dataset\2021智慧農業數位分身創新應用競賽\org\train-test.csv'
PATH_generate = r'D:\dataset\2021智慧農業數位分身創新應用競賽\generate_dateset'

train_df = pd.read_csv(os.path.join(PATH_org, 'train_data.csv'), index_col=0)
col_name = train_df.columns.to_list()

# 在測試資料新增label欄位並填入NAN
test_df = pd.read_csv(os.path.join(PATH_org, 'test_data.csv'), index_col=0)
col_num = train_df.shape[1]
data_num = test_df.shape[1]
nan_array = np.full([test_df.shape[0], col_num-data_num], np.nan)
test_df = test_df.reindex(columns = col_name)
test_df.iloc[:, data_num:] = nan_array
# concat 訓練資料與測試資料
all_df = pd.concat([train_df, test_df], axis=0, ignore_index=True)
# 對時間排列
all_df['d.log_time'] = pd.to_datetime(all_df['d.log_time'])
all_df.sort_values('d.log_time', inplace=True)
# all_df.to_csv(PATH_all, index=None)
# print(all_df.iloc[1248])
# 前10個時間點(包含當下)當做訓練資料，若遇到nan則跳過
n = 10
train_data = []
train_label = []
for i in tqdm(range(len(all_df)-n)):
    # print(all_df.iloc[i+n][0], all_df.iloc[i+n]['actuator01'])
    if np.isnan(all_df.iloc[i+n]['actuator01']):
        continue    
    data = all_df.iloc[i:i+n, 0:data_num].values
    label = all_df.iloc[i+n, data_num:].values
    train_data.append(data)
    train_label.append(label)
train_data = np.array(train_data)
train_label = np.array(train_label)
print('train_data:', train_data.shape)
print('train_label:', train_label.shape)

# 存檔.npy
np.save(os.path.join(PATH_generate, 'train-val_data.npy'), train_data)
np.save(os.path.join(PATH_generate, 'train-val_label.npy'), train_label)