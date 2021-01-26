import numpy as np
import pandas as pd
import os

sets = ['train_x', 'train_y', 'val_x', 'val_y']
file_name = ['FS443.csv', 'FS479.csv', 'FS592.csv', 'FS609.csv', 'FS639.csv', 'FS779.csv', 'FS859.csv', 'FS879.csv', 'FS899.csv', 'FS929.csv']
year = '104-108_879-899'
for set in sets:
    file_path = os.path.join(r'D:\dataset\lilium_price', set, year)
    # file_name = os.listdir(file_path)

    # df1 = pd.read_csv(os.path.join(file_path, file_name[0]), header=None)
    # df2 = pd.read_csv(os.path.join(file_path, file_name[1]), header=None)
    # df3 = pd.read_csv(os.path.join(file_path, file_name[2]), header=None)
    # df4 = pd.read_csv(os.path.join(file_path, file_name[3]), header=None)
    # df5 = pd.read_csv(os.path.join(file_path, file_name[4]), header=None)
    # df6 = pd.read_csv(os.path.join(file_path, file_name[5]), header=None)
    # df7 = pd.read_csv(os.path.join(file_path, file_name[6]), header=None)
    df8 = pd.read_csv(os.path.join(file_path, file_name[7]), header=None)
    df9 = pd.read_csv(os.path.join(file_path, file_name[8]), header=None)
    # df10 = pd.read_csv(os.path.join(file_path, file_name[9]), header=None)

    # data = pd.concat((df1, df2, df3, df4, df5, df6, df7, df8, df9, df10), axis=1)
    data = pd.concat((df8, df9), axis=1)
    # data = df7
    data.to_csv(os.path.join(os.path.join(r'D:\dataset\lilium_price', set), (year+'all.csv')), header=None, index=None)