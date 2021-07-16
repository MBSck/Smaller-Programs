import rampy as rp
import matplotlib.pyplot as plt
import numpy as np

filepath = "/media/marten/VERBATIM/Masterarbeit_Marten/Marten/sub_ma1/200512_Raman_RT/" \
           "001_532nm_1mW_20s_RT_ma_sub1_Spot1_unpol.dat"

x_axis = []
y_axis = []

for line in open(filepath, "r"):
    item = line.rstrip()
    x_axis.append(item.rsplit()[0])
    y_axis.append(item.rsplit()[1])

plt.figure()
plt.plot(x_axis, y_axis)
plt.show()





