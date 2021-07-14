from miditime.miditime import MIDITime
from data_to_sound import positive, negative, neutral


posInt = []
negInt = []

for i in positive:
    posInt.append(int(i))

for b in negative:
    negInt.append(int(b))

mymidi = MIDITime(120, '22midi.mid')

# Create a list of notes. Each note is a list: [time, pitch, attack, duration]
# take only ont

midinotes = [
    posInt,
    negInt,
    # At 10 beats (12 seconds from start), C#5 with attack 200, for 4 beats позитивность
]

mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()
print('midi from 22 created')
print('posInt', posInt)
