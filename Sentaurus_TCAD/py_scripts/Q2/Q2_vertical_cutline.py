import pandas as pd, matplotlib.pyplot as plt, numpy as np
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_2_vertical_cutline_new.csv'
)

fig, ax = plt.subplots(
    1, 
    1, 
    figsize=(15, 5.345)
)
#For setting up the figure to show all the plots
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)


peak_doping_conc = 0
peak_doping_conc = abs(min(df['DopingConcentration_vertical Y']))
df['DopingConcentration_vertical Y'] = abs( df['DopingConcentration_vertical Y'])
print(df['DopingConcentration_vertical Y'])
#Plotting

x = df['DopingConcentration_vertical X']
y = df['DopingConcentration_vertical Y']
plt.plot(
    x[x >= 0.076],
    y[x >= 0.076]/1e18,
    linewidth=2,
)

plt.xlabel(
    r'x,  ($\mu$m) $\longrightarrow$'
)
plt.ylabel(
    r'Doping concentration  ($10^{18}\,\mathrm{cm}^{-3}$) $\longrightarrow$'
)
plt.title(
    r'Vertical Cutline',
)



# print(abs(peak_doping_conc))

plt.text(
    0,-0.18,
    r'Observational Data',
    ha='left',
    va='bottom',
    fontsize = '13',
    transform=ax.transAxes
)
plt.text(
    0,-0.3,
    f'Peak doping concentration: '
    f'${peak_doping_conc/1e18:1.3f} \\times 10^{{18}}$ $cm^{{-3}}$',
    ha='left',
    va='bottom',
    fontsize=9,
    fontweight = 'bold',
    transform=ax.transAxes
    
)







plt.grid(
        True,
        linestyle = '--',
        alpha = 0.6
)

plt.tight_layout()
# plt.savefig(
#     'Q2_vertical_cutline.png',
#     dpi = 300
# )
plt.show()
