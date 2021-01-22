import numpy as np
import pandas as pd
import os

sets = ['train_x', 'train_y', 'val_x', 'val_y']
year = '108'
for set in sets:
    file_path = os.path.join(r'D:\dataset\lilium_price', set, year)
    file_name = os.listdir(file_path)

    df1 = pd.read_csv(os.path.join(file_path, file_name[0]))
    df2 = pd.read_csv(os.path.join(file_path, file_name[1]))
    df3 = pd.read_csv(os.path.join(file_path, file_name[2]))
    df4 = pd.read_csv(os.path.join(file_path, file_name[3]))
    df5 = pd.read_csv(os.path.join(file_path, file_name[4]))
    df6 = pd.read_csv(os.path.join(file_path, file_name[5]))
    df7 = pd.read_csv(os.path.join(file_path, file_name[6]))
    df8 = pd.read_csv(os.path.join(file_path, file_name[7]))
    df9 = pd.read_csv(os.path.join(file_path, file_name[8]))
    df10 = pd.read_csv(os.path.join(file_path, file_name[9]))

    data = pd.concat((df1, df2, df3, df4, df5, df6, df7, df8, df9, df10), axis=1)
    data.to_csv(os.path.join(os.path.join(r'D:\dataset\lilium_price', set), (year+'all.csv')), header=None, index=None)