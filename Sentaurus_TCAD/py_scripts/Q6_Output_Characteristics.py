import pandas as pd, matplotlib.pyplot as plt, numpy as np

#For setting up the figure to show all th plots
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\Q6_id_vd_at_const_vgs.csv'
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
v_gs = {
    0.3: ['vgs_0.3 X', 'vgs_0.3 Y'],
    0.6: ['vgs_0.6 X', 'vgs_0.6 Y'],
    0.9: ['vgs_0.9 X', 'vgs_0.9 Y'],
    1.5: ['vgs_1.5 X', 'vgs_1.5 Y']
}


# For Id-Vd 

v_th = {}
tang_x = np.arange(0.1, 2.8, 0.3)
for v in v_gs:
    I_d = df[v_gs[v][1]]
    V_d = df[v_gs[v][0]]

    ax[0].plot(
        V_d,
        I_d*1e3,
        linewidth=2,
        label = f'$V_{{GS}}$ = {v} V'
    )


ax[0].set_title(
    r'Output Characteristics ($I_D - V_{DS}$)',
    fontweight = 'bold'
)
ax[0].set_xlabel(
    r'$V_{DS}$,  (V) $\longrightarrow$'
)
ax[0].set_ylabel(
    r'$I_D$,  (mA) $\longrightarrow$'
)



# gd-vd
g_o = 0
V_d =  df[v_gs[1.5][0]]
dI_d_dV_d = np.gradient(
    df[v_gs[1.5][1]], 
    V_d
)
ax[1].plot(
    V_d,
    dI_d_dV_d*1e6,
    linewidth=2,
    label = f'$V_{{DS}}$ = {v} V'
)

ax[1].set_title(
    r'$g_D - V_{DS}$ Plot at $V_{GS}$ = 1.5V ',
    fontweight = 'bold'
)
ax[1].set_xlabel(
    r'$V_{DS}$,  (V) $\longrightarrow$'
)
ax[1].set_ylabel(
    r'$g_D$,  (mS) $\longrightarrow$'
)

g_o = (dI_d_dV_d[df[v_gs[1.5][0]] == 3])[0]





for i in ax:
    i.grid(
        True,
        linestyle = '--',
        alpha = 0.6
    )
    i.legend(
        fontsize = 10
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
    f' Output Conductance ($g_o$) at saturation for ($V_{{GS}}$ = 1.5 V): '
    f'{(g_o)*1000:.3f}  $mS \\cdot \\mu m$ \n'
    f' Output Resistance ($r_o$) at saturation for ($V_{{GS}}$ = 1.5 V): $1/g_o$ = '
    f'{(1/g_o)*1e-3:.3f} $k\\Omega$/$\\mu m$\n',
    transform=ax[1].transAxes,
    ha='left',
    va='bottom',
    fontsize=9,
    fontweight='bold'
)


plt.tight_layout()
# plt.savefig(
#     'Q6_Output_Characteristics_and_gd_vd_at_vg=1.5.png',
#     dpi = 300
# )
plt.show()

print(f'g_o = {g_o} S')
print(f'r_o = {1/g_o*1e-3} kOhm/micrometer')