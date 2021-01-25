import pandas as pd
import os
from tqdm import tqdm
import numpy as np

input_fold = r'D:\dataset\lilium_price\org\for2020test'
outfold = r'D:\dataset\lilium_price\test_x\for2020test'
n = 10
p = 4

list = os.listdir(input_fold)
for file_name in list:
    df = pd.read_excel(os.path.join(input_fold, file_name), header=4)
    df = df.drop(['日　　期', '市　　場', '產　　品', '最高價', '下價', '增減%', '增減%.1', '殘貨量', 'Unnamed: 12'], axis=1) #刪除特定欄位
    df = df[-1-n:-1].reset_index(drop=True)
    arr1 = df['上價'].values
    arr2 = df['中價'].values
    arr3 = df['平均價'].values
    arr4 = df['交易量'].values

    arr_list = [arr1, arr2, arr3, arr4]
    new_df = []
    for arr in arr_list:
        for i in range(n):
            new_df.append(arr[i])
    new_df = pd.DataFrame(np.array(new_df).reshape(1, -1))
    new_df.to_csv(os.path.join(outfold, file_name[:-4]+'.csv'), index=None, header=None)
