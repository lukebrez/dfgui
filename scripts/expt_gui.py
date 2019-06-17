import dfgui
import pandas as pd

file = 'X:/data/Brezovec/2P_Imaging/20190101_walking_dataset/master_expt.pkl'
df = pd.read_pickle(file)
dfgui.show(df)