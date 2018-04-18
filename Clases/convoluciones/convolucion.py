#convolucion.py

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage #trae diferentes tipos de convoluciones


plt.style.use('ggplot')


def convolve1d(signal, ir):
    '''
        usamos el metodo same/constant para cero padding, uno np y el otro scipy
    '''

    n = len(signal)
    m = len(ir)
    output = np.zeros(n)
    for i in range(n):
        for j in range(m):

            if i -j <0: continue
            output += signal[i - j] * ir[j]
    return output

def make_square_and_saw_waves(height, start, end, n):

    single_square_wave = []
    single_saw_wave = []

    for i in range(n):

        if start <= i < end:

            single_square_wave.append(height)
            single_saw_wave.append(height * (end - i)/(end -start))
        else:

            single_square_wave.append(0)
            single_saw_wave.append(0)

    return single_square_wave, single_saw_wave


#creamos señal y ir
start,end = 40,60

single_square_wave, single_saw_wave = make_square_and_saw_waves(height = 10,start = start, end = end, n = 100)



#convolucion, comparacion de metodos
np_conv = np.convolve(single_square_wave, single_saw_wave, mode = 'same')

conv1d = convolve1d(single_square_wave, single_saw_wave)

sconv = scipy.ndimage.convolve1d(single_square_wave, single_square_wave, mode = 'constant')


#dibujamos, escalando por altura

plt.clf()
fig, axs = plt.subplots(5, 1, figsize =(12, 6), sharey = True, sharex = True)

axs[0].plot(single_square_wave/np.max(single_square_wave), c = 'r')
axs[0].set_title('single square')
axs[0].set_ylim(-.1, 1.1)

axs[1].plot(single_saw_wave/np.max(single_saw_wave), c = 'r')
axs[1].set_title('single saw')
axs[1].set_ylim(-.1, 1.1)

axs[2].plot(conv1d/np.max(conv1d), c = 'r')
axs[2].set_title('conv1d')
axs[2].set_ylim(-.1, 1.1)

axs[3].plot(np_conv/np.max(np_conv), c = 'r')
axs[3].set_title('np_conv')
axs[3].set_ylim(-.1, 1.1)

axs[4].plot(sconv/np.max(sconv), c = 'r')
axs[4].set_title('sconv')
axs[4].set_ylim(-.1, 1.1)

plt.show()
