import math
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------
# Importing data into dataframes
# ==================================
# if "space(s)" are used as delimiter in data, add following argument "delim_whitespace=True"
# ex) df1 = pd.read_csv("s1.csv", delim_whitespace=True)

df1 = pd.read_csv("sample.csv")
# df2 = pd.read_csv("2.csv")
# df3 = pd.read_csv("3.csv")
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# Figure configrations
# ==================================
# if you want to set the size of the figure
# use plt.figure(figsize=(width_inch,height_inch))  1inch = 2.54cm
# ==================================

fig = plt.figure()
plt.rcParams['font.family'] = 'Times New Roman'  # fonts
plt.rcParams['font.size'] = 14  # fontsize
plt.rcParams['axes.linewidth'] = 1.5  # linewidth of axes
plt.rcParams['text.usetex'] = True
# usetex = True: latex description can be used in the figure
# ex) ax1.set_xlabel(r'$ LATEX DESCRIPTION $')
# note: if the system says "type1ec.sty or dvipng is not found",
#        install them using "apt install cm-super" or "apt install dvipng." (Ubuntu)
# If errors do not go away, set "plt.rcParams['text.usetex'] = False"

# -----------------------------------------------------------------------
# Add subplots to draw multiple graphs in the same figure
# ==================================
# add_subplots(i,j,k): define the number and places of the graph
# i: number of lines in the figure
# j: number of rows in the figure
# k: order of the graph in the figure
# ==================================

ax1 = fig.add_subplot(4, 1, 1)
ax2 = fig.add_subplot(4, 1, 2)
ax3 = fig.add_subplot(4, 1, 3)
ax4 = fig.add_subplot(4, 1, 4)

# -----------------------------------------------------------------------
# Drawing graphs
# ==================================
xlim = [0, 5]  # xrange for all plots

# 1st plot
ax1.plot(df1["time"], df1["angle"], label="angle", lw=1)
ax1.set_xlim(xlim)  # set xrange of the plot: ax1.set_xlim([a,b])
# ax1.set_ylim()    # set yrange of the plot: ax1.set_ylim([a,b])
# ax1.set_xlabel('time[sec]')
ax1.set_ylabel('Angle [deg]')
ax1.legend()  # add a legend(label) of the plot

# 2nd plot
ax2.plot(df1["time"], df1["velocity"], label="vel.", lw=1)
ax2.set_xlim(xlim)
# ax1.set_ylim()
# ax2.set_xlabel('time[sec]')
ax2.set_ylabel('Velocity [deg/sec]')
ax2.legend()

# 3rd plot
ax3.plot(df1["time"], df1["acceleration"], label="accel.", lw=1)
ax3.set_xlim(xlim)
# ax1.set_ylim()
# ax3.set_xlabel('time[sec]')
ax3.set_ylabel(r'${\rm Acceleration}\ [{\rm deg}/{\rm sec}^2]$')
ax3.legend()

# 4th plot
ax4.plot(df1["time"], df1["state"], label="state", lw=1)
ax4.set_xlim(xlim)
# ax1.set_ylim()
ax4.set_xlabel('Time[sec]')
ax4.set_ylabel('State')
ax4.legend()
# -----------------------------------------------------------------------

fig.align_labels()  # align all labels
plt.show()
