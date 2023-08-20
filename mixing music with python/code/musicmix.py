from pydub import AudioSegment

# Load the first audio file
audio1 = AudioSegment.from_file('YUrijj_SHatunov_-_Belye_rozy_49909527.wav')
# Load the second audio file
audio2 = AudioSegment.from_file('YUrijj_SHatunov_-_Rozovyjj_vecher_49909520.wav')

# Combine the two audio files
combined_audio = audio1.overlay(audio2)

# Export the combined audio to a new file
combined_audio.export('123456789.wav', format='wav')
