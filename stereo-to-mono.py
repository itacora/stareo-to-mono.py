#library import
import os
import glob
import wave
import soundfile as sf


#Specified your folder that stored your own stereo files（depends on you）.
from_dir = "path your folder"
#Specified your folder that you want to save mono files（depends on you）.
to_dir = "path your folder"

#As follows, you do not have to change codes if you want to change to mono only.
os.makedirs(to_dir, exist_ok=True)
for path in glob.glob(os.path.join(from_dir, '*.WAV')):
    wav, fs = sf.read(path)
    # case of stereo 2 ch, just separate Lch and Rch.
    wav_l = wav[:, 0]
    wav_r = wav[:, 1]

    # change to mono
    #initial value 0.5
    xs = (0.5 * wav_l) + (0.5 * wav_r)
    
    #save files
    #defult : sf.write('new_file.wav', xs, fs)
    basename = os.path.basename(path)
    ftitle, fext = os.path.splitext(path)
    sf.write(os.path.join(to_dir, 'mono_' + basename), xs, fs)

    
    
