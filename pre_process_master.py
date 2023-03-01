import pandas as pd
import datetime

master_loc = "/mnt/nas_fintech_11/SEC/data/masters/master_10-K.csv"
save_master_loc = "/mnt/nas_fintech_11/SEC/data/masters/FILINGS_METADATA_10K.csv"

master_df = pd.read_csv(master_loc)

def create_new_file_path(local_path, Filename):
    Filename = Filename.split('_')[1]
    Filename = Filename.split('.')[0] + ".txt"
    return local_path[2:] + "/" + Filename

def get_txt_filename(Filename_new):
    return Filename_new.split('/')[-1]


master_df['Date Filed'] = pd.to_datetime(master_df['Date Filed'], format="%Y-%m-%d")

master_df = master_df[(master_df['Date Filed'] > pd.to_datetime("2007-01-01", format="%Y-%m-%d"))]  

master_df["Filename_new"] = master_df.apply(lambda row : create_new_file_path(row['local_path'],
                     row['Filename']), axis = 1)

master_df["Filename_txt"] = master_df.apply(lambda row : get_txt_filename(row['Filename_new']), axis = 1)                     

master_df.head()

master_df.to_csv(save_master_loc, index=False)