import matplotlib.pyplot as plt
import cv2
import pandas as pd
import numpy as np




df = pd.read_csv('./meteo.csv')

print(df.head())

lluvia = np.reshape(np.array(df['y'])[:-958], (100,-1))

lluviaM = np.mean(lluvia, axis=0)

plt.plot(lluviaM)
plt.ylabel('lluvia / mm')
plt.xlabel('tiempo/ u.a.')
plt.title('Lluvia en Lisboa frente al tiempo')
plt.show()