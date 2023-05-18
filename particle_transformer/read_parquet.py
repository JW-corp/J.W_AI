import pandas as pd


infile_tr = "/xrootd_user/jiwoongk/xrootd2/TopLandscape/train_file.parquet"
infile_va = "/xrootd_user/jiwoongk/xrootd2/TopLandscape/val_file.parquet"
infile_te = "/xrootd_user/jiwoongk/xrootd2/TopLandscape/test_file.parquet"

df = pd.read_parquet(infile_va)
print(df.shape)

limit = int(df.shape[0] * 0.4)
df = df.loc[:limit,:]
df.to_parquet('/xrootd_user/jiwoongk/xrootd2/TopLandscape/val_file_40.parquet')


#df.to_parquet('myfile.parquet')