from miditime.miditime import MIDITime
# NOTE: this import works at least as of v1.1.3; for older versions or forks of miditime, you may need to use
# from miditime.MIDITime import MIDITime

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
mymidi = MIDITime(120, 'toneToweight.mid')

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
midinotes = [
    [60, 70, 40, 40],  #At 0 beats (the start), Middle C with attack 200, for 3 beats
    [10, 61, 200, 255],
    #At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats позитивность
]

# (0,0.006*"день"),(1,'0.007*"воиска" ),(2, '0.004*"день" )(3, '0.004*"города"), (4,
#   ' 0.007*"воина"),(5,( '0.005*"дома"), (6,  '0.006*"наши"),(7, '0.004*"дома" ),( 8,(0.004*"день"),(9,
#   '0.004*"дома")]  * 10000
#  день -> {'neutral': 0.8634016513824463, 'positive': 0.014513582922518253}
# воиска -> {'neutral': 0.9991804361343384, 'skip': 0.003085370408371091}
# города -> {'neutral': 0.9976868629455566, 'positive': 0.01972912810742855}
# воина -> {'neutral': 1.0000100135803223, 'skip': 0.003386611817404628}
# дома -> {'neutral': 0.9993638396263123, 'positive': 0.008857354521751404}
# наши -> {'neutral': 0.9995927214622498, 'negative': 1.0000003385357559e-05}
# дома -> {'neutral': 0.9993638396263123, 'positive': 0.008857354521751404}
# день -> {'neutral': 0.8634016513824463, 'positive': 0.014513582922518253}
# дома -> {'neutral': 0.9993638396263123, 'positive': 0.008857354521751404}

# Add a track with those notes
mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()