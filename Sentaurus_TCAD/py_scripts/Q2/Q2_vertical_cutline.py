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
#Plotting
plt.plot(
    df['DopingConcentration_vertical X'],
    df['DopingConcentration_vertical Y']/1e20,
    linewidth=2,
)

plt.xlabel(
    r'x,  ($\mu$m) $\longrightarrow$'
)
plt.ylabel(
    r'Doping concentration  ($10^{20}\,\mathrm{cm}^{-3}$) $\longrightarrow$'
)
plt.title(
    r'Vertical Cutline',
)


peak_doping_conc=max(df['DopingConcentration_vertical Y'])
#print(peak_doping_conc)

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
    f'${peak_doping_conc/1e19:1.3f} \\times 10^{{19}}$ $cm^{{-3}}$',
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
plt.savefig(
    'Q2_vertical_cutline.png',
    dpi = 300
)
plt.show()
