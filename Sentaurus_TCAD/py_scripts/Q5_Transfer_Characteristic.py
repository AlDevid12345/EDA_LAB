import pandas as pd, matplotlib.pyplot as plt, numpy as np

#For setting up the figure to show all th plots
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q5_idvg.csv'
)
fig, ax = plt.subplots(
    1, 
    2, 
    figsize=(15, 5.345)
)
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)
v_ds = {
    0.05: ['Vd_0.05 X', 'Vd_0.05 Y'],
    0.4 : ['Vd_0.4 X', 'Vd_0.4 Y']
}


# For Linear Graph 

v_th = {}
tang_x = np.arange(0.1, 2.8, 0.3)
for v in [0.05, 0.4]:
    I_d = df[v_ds[v][1]]
    V_g = df[v_ds[v][0]]
    
    mask = (0.5 <= V_g) & (V_g <= 0.73 )
    
    m, c = np.polyfit(
        V_g[mask],
        I_d[mask],
        1
    )
    tang_y = m*tang_x + c
    v_th[v] = float(-c/m)
    ax[0].plot(
        V_g,
        I_d*1e6,
        linewidth=2,
        label = f'$V_{{DS}}$ = {v} V'
    )
    ax[0].plot(
        tang_x,
        tang_y*1e6,
        linewidth = 1,
        linestyle = '--' if v == 0.05 else '-.',
        color = 'black',
        alpha = 0.7,
        label = 
        f'Tangent for $V_{{TH}}$ at $V_{{DS}}$ = {v} V'
    )
ax[0].text(
    0,-0.18,
    r'Observational Data',
    ha='left',
    va='bottom',
    transform=ax[0].transAxes,
    fontsize = '13'
)
ax[0].text(
    0,-0.3,
    f'Threshold Voltage ($V_{{TH}}$) for ($V_{{DS}}$ = {0.05}V): '
    f'{v_th[0.05]:1.3f} V\n'
    f'Threshold Voltage ($V_{{TH}}$) for ($V_{{DS}}$ = {0.4}V): '
    f'{v_th[0.4]:1.3f} V ',
    ha='left',
    va='bottom',
    fontsize=9,
    fontweight = 'bold',
    transform=ax[0].transAxes,
)

ax[0].set_title(
    r'Transfer Characteristics (Linear Graph)',
    fontweight = 'bold'
)
ax[0].set_xlabel(
    r'$V_{GS}$,  (V) $\longrightarrow$'
)
ax[0].set_ylabel(
    r'$I_D$,  ($\mu$ A) $\longrightarrow$'
)



#Logarithmic Graph

v_ss = {}
tang_x = np.arange(0.1, 1.4, 0.3)
for v in [0.05, 0.4]:
    I_d = df[v_ds[v][1]]
    V_g = df[v_ds[v][0]]
    
    
    ax[1].semilogy(
        V_g,
        I_d,
        linewidth = 2,
        label = f'$V_{{DS}}$ = {v} V'
    )
    mask = (0.5 <= V_g) & (V_g <= 0.6 )
    m, c = np.polyfit(
        V_g[mask],
        np.log10(I_d[mask]),
        1
    )

    v_ss[v] = float(1 / m)
    tang_y = m * tang_x + c
    ax[1].plot(
        tang_x,
        10**tang_y,
        linewidth = 1,
        linestyle = '--' if v == 0.05 else '-.',
        color = 'black',
        alpha = 0.7,
        label = 
        f'Tangent for subthreshold at $V_{{DS}}$ = {v} V'
    )
    

ax[1].set_xlabel(
    r'$V_{GS}$,  (V) $\longrightarrow$'
)
ax[1].set_ylabel(
    r'$I_D$,  (A) $\longrightarrow$'
)
ax[1].set_title(
    r'Transfer Characteristics (Logarithmic Graph)',
    fontweight = 'bold'
)


ax[1].text(
    0,
    -0.18,
    'Observational Data',
    transform=ax[1].transAxes,
    ha='left',
    va='bottom',
    fontsize=13
)

ax[1].text(
    0,
    -0.30,
    f'Subthreshold Slope (SS) for ($V_{{DS}}$ = 0.05 V): '
    f'{v_ss[0.05]*1000:.2f} mV/decade\n'
    f'Subthreshold Slope (SS) for ($V_{{DS}}$ = 0.4 V): '
    f'{v_ss[0.4]*1000:.2f} mV/decade',
    transform=ax[1].transAxes,
    ha='left',
    va='bottom',
    fontsize=9,
    fontweight='bold'
)


for i in ax:
    i.grid(
        True,
        linestyle = '--',
        alpha = 0.6
    )
    i.legend(
        fontsize = 10
    )


plt.tight_layout()
plt.savefig(
    'Q5_Transfer_Characteristics.png',
    dpi = 300
)
print(v_th, v_ss)
plt.show()