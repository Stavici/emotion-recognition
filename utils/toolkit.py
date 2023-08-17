import glob
import os

import moviepy.editor as mp
import pandas as pd


def wmv_to_wav(in_path, out_path):
    for filename in os.listdir(in_path):
        if filename.endswith(".wmv"):
            video_clip = mp.VideoFileClip(f'{out_path}/{filename}')
            video_clip.audio.write_audiofile(f'{out_path}/{filename}.wav')
        else:
            continue
    return "wnv_to_wav completed"


def data_consolidation():
    all_filenames = [i for i in glob.glob(f'{config.PATH_CSV}/*.csv')]
    consolidate_df = pd.concat([pd.read_csv(file) for file in all_filenames])
    return consolidate_df


def smile_to_csv():
    for filename in os.listdir(config.PATH_AUDIO):
        if filename.endswith(".wav"):
            file = os.path.join(f'{config.PATH_AUDIO}/{filename}')
            smile_value_df = core.smile_create(file)
            smile_value_df.drop(smile_value_df.tail(1).index, inplace=True)

            if filename.endswith("T.wav"):
                smile_value_df.insert(smile_value_df.shape[1], 'labels', 1)
            else:
                smile_value_df.insert(smile_value_df.shape[1], 'labels', 0)

            smile_value_df.to_csv(f'{config.PATH_CSV}/{filename[:-4]}.csv', index=False)
        else:
            continue
