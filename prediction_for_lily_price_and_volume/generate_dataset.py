# 取前n天的資料作為特徵
import pandas as pd
import numpy as np
import torch
import utils
import math
from tqdm import tqdm
import os

fold = r'D:\dataset\lilium_price'
year = '105-108'
cloumn = [ '上價', '中價', '平均價', '交易量']
n = 10  # 取前n天的資料作為特徵
train_end = 1040

csv_fold = os.path.join(fold, year)
file_list = os.listdir(csv_fold)
for file_name in file_list:
    path_csv = os.path.join(csv_fold, file_name)
    #切分訓練集、驗證集
    train_df, val_df = utils.read_col_data(path_csv, cloumn, n , train_end=train_end)
    #切分特徵、label
    train_x, train_y = utils.split_xy(train_df, len(cloumn), n)
    val_x, val_y = utils.split_xy(val_df, len(cloumn), n)

    np.savetxt(os.path.join(fold, 'train_x', year, file_name), train_x, delimiter=",", fmt='%.2f')
    np.savetxt(os.path.join(fold, 'train_y', year, file_name), train_y, delimiter=",", fmt='%.2f')
    np.savetxt(os.path.join(fold, 'val_x', year, file_name), val_x, delimiter=",", fmt='%.2f')
    np.savetxt(os.path.join(fold, 'val_y', year, file_name), val_y, delimiter=",", fmt='%.2f')