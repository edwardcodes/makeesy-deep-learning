# NOTE: Sine is with even positions and Cosine is at odd positions

import matplotlib.pyplot as plt
import numpy as np

d_model = 32
max_positions = 100

i_2 = 2
position_enc_i_2 = np.array(
    [
        [pos / np.power(10000, 2 * i_2 / d_model)]
        for pos in range(max_positions)
    ]
)


i_4 = 4
position_enc_i_4 = np.array(
    [
        [pos / np.power(10000, 2 * i_4 / d_model)]
        for pos in range(max_positions)
    ]
)


i_6 = 6
position_enc_i_6 = np.array(
    [
        [pos / np.power(10000, 2 * i_6 / d_model)]
        for pos in range(max_positions)
    ]
)


x = range(max_positions)
sine_i_2 = np.sin(position_enc_i_2)
sine_i_4 = np.sin(position_enc_i_4)
sine_i_6 = np.sin(position_enc_i_6)
plt.plot(x, sine_i_2, label=f"i={i_2}")
plt.plot(x, sine_i_4, label=f"i={i_4}")
plt.plot(x, sine_i_6, label=f"i={i_6}")
plt.ylabel('Embedding Dimensions')
plt.xlabel('Token Position')
plt.legend()
plt.show()
