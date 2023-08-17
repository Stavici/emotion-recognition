

import opensmile
import audiofile

def smile_create(file):
    signal, sampling_rate = audiofile.read(file, duration=25, )
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPS,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )
    smile_value_df = smile.process_signal(signal, sampling_rate)
    return smile_value_df

