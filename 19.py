import base64
import wave
import email

text=open("19_email.txt").read()
mail=email.message_from_string(text)
audio=mail.get_payload(0).get_payload(decode=True)

f=open("19_indian.wav","wb")
f.write(audio)

w=wave.open("19_indian.wav","rb")
h=wave.open("19_rst.wav","wb")

h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())
wave.big_endiana = 1
h.writeframes(frames)
h.close()