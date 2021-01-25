# 取前n天的資料作為特徵
import pandas as pd
import numpy as np
import torch
import utils
import math
from tqdm import tqdm
import os

fold = r'D:\dataset\lilium_price\generate_dataset'
file_name = 'FS443.csv'
cloumn = [ '上價', '中價', '平均價', '交易量']
n = 10  # 取前n天的資料作為特徵
train_end = int(3287*0.9)

path_csv = os.path.join(fold, file_name)
#切分訓練集、驗證集
train_df, val_df = utils.read_col_data(path_csv, cloumn, n , train_end=train_end)
#切分特徵、label
train_x, train_y = utils.split_xy(train_df, len(cloumn), n)
val_x, val_y = utils.split_xy(val_df, len(cloumn), n)

np.savetxt(os.path.join(r'D:\dataset\lilium_price', 'train_x', file_name), train_x, delimiter=",", fmt='%.2f')
np.savetxt(os.path.join(r'D:\dataset\lilium_price', 'train_y', file_name), train_y, delimiter=",", fmt='%.2f')
np.savetxt(os.path.join(r'D:\dataset\lilium_price', 'val_x', file_name), val_x, delimiter=",", fmt='%.2f')
np.savetxt(os.path.join(r'D:\dataset\lilium_price', 'val_y', file_name), val_y, delimiter=",", fmt='%.2f')