import numpy as np
from scipy.io.wavfile import write

import functions

parser = functions.parse("note_sequence.csv")

a = functions.track2wav(parser[0], master_tune=220)

write("output.wav", 48000, a)
