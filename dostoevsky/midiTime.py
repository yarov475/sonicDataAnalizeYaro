from miditime.miditime import MIDITime

mymidi = MIDITime(120, '22midi.mid')

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# take only ont

midinotes = [
    [10, 12, 11, 1],
    [4, 3, 19, 89]
    # At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats позитивность
]

mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()
print('midi from 22 created')
print('posInt', posInt)
