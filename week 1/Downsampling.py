from scipy.io import wavfile
fs, x = wavfile.read('/home/apiiit123/Desktop/Week - 1/R.wav')
def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('R.wav',fs,y)
a=int(input("Enter sampling factor:"))
sampling(x, a)
