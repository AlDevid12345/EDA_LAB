import pandas as pd, matplotlib.pyplot as plt, numpy as np
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_2_horizontal_cutline_new.csv'
)

#For setting up the figure to show all the plots
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)

#Plotting
plt.plot(
    df['DopingConcentration_horizontal X'],
    df['DopingConcentration_horizontal Y']/1e20,
    linewidth=2,
)

plt.xlabel(
    r'x,  ($\mu$m) $\longrightarrow$'
)
plt.ylabel(
    r'Doping concentration  ($10^{20}\,\mathrm{cm}^{-3}$) $\longrightarrow$'
)
plt.title(
    r'Horizontal Cutline',
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
