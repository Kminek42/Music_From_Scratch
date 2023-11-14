import numpy as np

def parse(filename):
    file = open("note_sequence.csv", "r")
    data = file.read().split("\n")
    file.close()

    tracks = []
    for track in data:
        track = track.split(",")
        tracks.append([
            track[0], [int(num.strip()) for num in track[1:]]
        ])

    return tracks


def track2wav(track, master_tune = 440, sample_rate=48000, note_duration=0.25):
    sequence = np.array(track[1])
    f = master_tune * 2 ** ((sequence - 49) / 12)
    f = np.repeat(f, int(note_duration * sample_rate))

    # generate amplitude
    amplitude = np.linspace(1, 0.5, int(note_duration * sample_rate))
    amplitude = np.tile(amplitude, len(sequence))

    # generate time
    t = np.linspace(0, note_duration * len(sequence), len(f))

    # generate wave
    Y = np.zeros(len(t))

    for k in range(1, 400):
        Y += np.sin(2 * np.pi * f * k * t) / k
        Y += np.sin(2.01 * np.pi * f * k * t) / k
        Y += 0.5 * np.sin(1.0025 * np.pi * f * k * t) / k

    # normalize signal
    Y -= Y.min()
    Y /= Y.max()
    Y *= 1.8
    Y -= 0.9

    # apply amplitude
    Y *= amplitude

    return Y.astype(np.float32)
