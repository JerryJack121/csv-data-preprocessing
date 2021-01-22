import pandas as pd
import numpy as np
import torch
import utils
import math
from tqdm import tqdm
import os

path_csv = r'D:\dataset\lilium_price\108\FS443.csv'
cloumn = [ '上價', '中價', '平均價', '交易量']
n = 5  # 取前n天的資料作為特徵
train_end = 200

#切分訓練集、驗證集
train_df, val_df = utils.read_col_data(path_csv, cloumn, n , train_end=train_end)
#切分特徵、label
train_x, train_y = utils.split_xy(train_df, len(cloumn), n)
val_x, val_y = utils.split_xy(val_df, len(cloumn), n)

np.savetxt(r'D:\dataset\lilium_price\train_x\108_FS443.csv', train_x, delimiter=",", fmt='%.2f')
np.savetxt(r'D:\dataset\lilium_price\train_y\108_FS443.csv', train_y, delimiter=",", fmt='%.2f')
np.savetxt(r'D:\dataset\lilium_price\val_x\108_FS443.csv', val_x, delimiter=",", fmt='%.2f')
np.savetxt(r'D:\dataset\lilium_price\val_y\108_FS443.csv', val_y, delimiter=",", fmt='%.2f')