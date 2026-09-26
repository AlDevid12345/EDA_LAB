import pandas as pd, matplotlib.pyplot as plt, numpy as np
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_2_horizontal_cutline_new.csv'
)
channel_length = 0

#For setting up the figure to show all the plots
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)

#Plotting
x = df['DopingConcentration_horizontal X']
y = df['DopingConcentration_horizontal Y']
plt.plot(
    df['DopingConcentration_horizontal X'],
    df['DopingConcentration_horizontal Y']/1e20,
    linewidth=2,
)


channel_length = -x.iloc[61]+x.iloc[82]
#print(channel_length)

plt.xlabel(
    r'x,  ($\mu$m) $\longrightarrow$'
)
plt.ylabel(
    r'Doping concentration  ($10^{20}\,\mathrm{cm}^{-3}$) $\longrightarrow$'
)
plt.title(
    r'Horizontal Cutline',
)

plt.annotate(
    "",
    xy = (x.iloc[61],0.05),
    xytext= (x.iloc[82], 0.05),
    arrowprops=dict(arrowstyle='<->')
)
plt.text(
    (x.iloc[61] + x.iloc[82])/2,
    0.05,
    f"{channel_length:2.6f} $\\mu m$",
    ha = 'center',
    va = 'bottom'
)


plt.grid(
        True,
        linestyle = '--',
        alpha = 0.6
)

plt.tight_layout()
# plt.savefig(
#     'Q2_horzontal_cutline.png',
#     dpi = 300
# )
plt.show()
