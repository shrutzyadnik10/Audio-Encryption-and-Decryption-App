from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import random
import string
from Crypto.Cipher import AES

fs, data = wavfile.read('C:/Users/Shruti/Downloads/Recording.wav')
plt.plot(data)            # fs = sampling frequency = 44.1kHz
plt.title("Original Audio Plot")

with open('C:/Users/Shruti/Downloads/Recording.wav', 'rb') as fd:
    contents = fd.read()

sd.play(data, fs)

AES_KEY = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))

AES_IV = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))


print("AES Key is ", AES_KEY)
print("AES Initialization vector is ", AES_IV)

encryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
encrypted_audio = encryptor.encrypt(contents)

with open('encrypted_audio_file.wav', 'wb') as fd:
    fd.write(encrypted_audio)
print("A file titled 'encrypted_audio_file.wav' is generated which is the encrypted audio to be communicated")

with open('encrypted_audio_file.wav', 'rb') as fd:
    contents = fd.read()

fs, data_2 = wavfile.read("C:/Users/Shruti/PycharmProjects/Audio/encrypted_audio_file.wav")
plt.plot(data_2)            # fs = sampling frequency = 44.1kHz
plt.title("Encrypted Audio Plot")

sd.play(data_2,fs)

decryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
decrypted_audio = decryptor.decrypt(contents)

with open('decrypted_audio_file.wav', 'wb') as fd:
    fd.write(decrypted_audio)

fs, data1 = wavfile.read("C:/Users/Shruti/PycharmProjects/Audio/decrypted_audio_file.wav")
plt.plot(data1)            # fs = sampling frequency = 44.1kHz
plt.title("Decrypted Audio Plot")
data_1 = np.asarray(data1, dtype = np.int32)

sd.play(data1, fs)
