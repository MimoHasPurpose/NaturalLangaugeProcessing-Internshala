# .mp3, lossy
# .flac, lossless
# .wav uncompressed, best audio quality
import wave
# Audio signal parameters
#-number of channels 
#-sample width (no of bytes for each sample)
#-framerate/sample_rate (no of samples/second)
#-number of frames ()
#-values of a frame
obj=wave.open("output.wav","rb")
print("Number of channels",obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number of frames",obj.getnframes())
print("parameters",obj.getparams())

t_audio=obj.getnframes()/obj.getframerate()
print(t_audio)

frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/2)
obj.close()


obj_new=wave.open("output_new.wav","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
obj_new.writeframes(frames)
obj_new.close()