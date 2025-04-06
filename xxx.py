import mido
from mido import Message, MidiFile, MidiTrack

# 定义《小星星》的音符（音高）
notes = [60, 60, 67, 67, 69, 69, 67,
         65, 65, 64, 64, 62, 62, 60]

# 将音符延长，后半段降调
lowered_notes = [note - 2 for note in notes]  # 降调两个音阶
extended_notes = notes + lowered_notes  # 组合前半段和后半段
durations = [400] * len(extended_notes)  # 更新持续时间

# 定义打击乐音符（音高）
percussion_notes = [35, 38, 42]  # 大鼓、小鼓、踩镲
percussion_durations = [200, 200, 200]  # 持续时间

# 创建一个新的 MIDI 文件和轨道
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 设置乐器（钢琴）
track.append(Message('program_change', program=0, time=0))

# 生成 MIDI 消息
time = 0
for note, duration in zip(extended_notes, durations):
    track.append(Message('note_on', note=note, velocity=64, time=time))
    track.append(Message('note_off', note=note, velocity=64, time=duration))
    time = 0

# 添加打击乐音符
for percussion_note, percussion_duration in zip(percussion_notes, percussion_durations):
    track.append(Message('note_on', note=percussion_note, velocity=64, time=0))
    track.append(Message('note_off', note=percussion_note, velocity=64, time=percussion_duration))

# 创建一个新的音轨用于伴奏
accompaniment_track = MidiTrack()
mid.tracks.append(accompaniment_track)

# 定义伴奏和弦（音高）
chords = [
    [60, 64, 67],  # C 大调和弦
    [62, 65, 69],  # D 小调和弦
    [64, 67, 71],  # E 小调和弦
    [65, 69, 72],  # F 大调和弦
]

# 定义伴奏的持续时间
accompaniment_durations = [800] * len(chords)  # 每个和弦持续时间

# 添加伴奏和弦到伴奏音轨
for chord, duration in zip(chords, accompaniment_durations):
    for note in chord:
        accompaniment_track.append(Message('note_on', note=note, velocity=64, time=0))
    for note in chord:
        accompaniment_track.append(Message('note_off', note=note, velocity=64, time=duration))

# 保存 MIDI 文件
mid.save('twinkle_twinkle.mid')    