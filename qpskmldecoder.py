import numpy as np
source=[1+1j,-1+1j,-1-1j,1-1j]
transmitter=np.random.choice(source)
print(transmitter)


noise=np.random.normal(0,1,1)
receiver=transmitter+noise
print(receiver)

if ((receiver.real >0) and (receiver.imag >0)):
    dec_output=1+1j
elif ((receiver.real >0) and (receiver.imag <0)):
    dec_output=1-1j
elif ((receiver.real < 0) and (receiver.imag >0)):
    dec_output=-1+1j
else:
    dec_output=-1+1j

print(dec_output)