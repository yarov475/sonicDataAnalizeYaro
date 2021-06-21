from miditime.MIDITime import MIDITime
from datetime import datetime
import random

mymidi = MIDITime(108, 'johnadams1.mid', 3, 4, 1)

my_data = [
{'event_date': datetime(1753,6,8), 'magnitude':0.0024499630},
{'event_date': datetime(1753,6,9), 'magnitude':0.0035766320},
{'event_date': datetime(1753,6,14), 'magnitude':0.0042241550}
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(d['event_date']), 'magnitude': d['magnitude']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'magnitude': d['magnitude']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(magnitude):
    scale_pct = mymidi.linear_scale_pct(0, 1, magnitude)
    # Pick a range of notes. This allows you to play in a key.
    c_major = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_major)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

note_list = []

for d in my_data_timed:
    note_list.append([
        d['beat'] - start_time,
        mag_to_pitch_tuned(d['magnitude']),
        random.randint(0,200),  # attack
        random.randint(1,4)  # duration, in beats
    ])
    # Add a track with those notes
mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()