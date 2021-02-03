# 用於智慧農業分身創新中的機器學習的資料切割
import pandas as pd
from pandas import DataFrame
from tqdm import tqdm
import random

# 讀取資料集
df = pd.read_csv(r'D:\dataset\2021智慧農業數位分身創新應用競賽\org\train_data.csv', encoding='utf-8')   #原始資料路徑
# # 刪除重複的資料，並保留出現第一次的
# df.drop_duplicates(keep='first', inplace=True)


val_idx = []    #用於紀錄該日期所有資料在該資料集中的index
date_list = []  #用於儲存所有日期
train_data = [] #用於儲存訓練資料
val_data = []   #用於儲存驗證資料

#隨機選擇驗證日期
for time in df['d.log_time']:
    date = time.split()[0]  #以空白字元切割
    date_list.append(date)
date_set = set(date_list)
val_date = random.choices(tuple(date_set), k=10)

with tqdm(total=len(df)) as pbar:
    for index, row in df.iterrows():
        data_row = df.loc[index].values
        time = data_row[1]
        date = time.split(' ')[0]
        
        if date in  val_date:
            val_data.append(df.loc[index])
        else:
            train_data.append(df.loc[index])

        # 更新進度條
        pbar.update(1)
        pbar.set_description('generate_dataset')


df_val = DataFrame(val_data)
df_train = DataFrame(train_data)
    
# 將資料打亂
# df = df.sample(frac=1.0).reset_index(drop=True)
# cut_idx = int(round(0.9 * df.shape[0]))
# df_train, df_val = df.iloc[:cut_idx], df.iloc[cut_idx:]

# 輸出train.csv與val.csv檔案
df_train.to_csv(r'D:\dataset\2021智慧農業數位分身創新應用競賽\train.csv', index=False)      #生成訓練資料路徑
df_val.to_csv(r'D:\dataset\2021智慧農業數位分身創新應用競賽\val.csv', index=False)      #生成驗證資料路徑