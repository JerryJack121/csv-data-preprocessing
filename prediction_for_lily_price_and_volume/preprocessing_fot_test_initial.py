import pandas as pd
import os
from tqdm import tqdm
import numpy as np

input_fold = r'D:\dataset\lilium_price\org\for2021test'
outfold = r'D:\dataset\lilium_price\test_x\for2021test'
n = 10

list = os.listdir(input_fold)
new_df = []
for file_name in list:
    df = pd.read_excel(os.path.join(input_fold, file_name), header=4)
    df = df.drop(['日　　期', '市　　場', '產　　品', '增減%', '增減%.1', '殘貨量', 'Unnamed: 12'], axis=1) #刪除特定欄位
    df = df[-1-n:-1].reset_index(drop=True)
    arr1 = df['最高價'].values
    arr2 = df['上價'].values
    arr3 = df['中價'].values
    arr4 = df['下價'].values
    arr5 = df['平均價'].values
    arr6 = df['交易量'].values


    arr_list = [arr1, arr2, arr3, arr4, arr5, arr6]
    
    for arr in arr_list:
        for i in range(n):
            new_df.append(arr[i])
        
new_df = pd.DataFrame(np.array(new_df).reshape(1, -1))
new_df.to_csv(os.path.join(outfold, 'for2021test.csv'), index=None, header=None)
