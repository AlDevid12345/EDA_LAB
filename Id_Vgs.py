import pandas as pd, matplotlib.pyplot as plt, numpy as np
df = pd.read_csv(r'D:\EDA_Lab\25EC01004\Lab1\Electrical Data\MOSFET_ID_VGS.csv')
fig, ax = plt.subplots(1, 2, figsize = (11, 4.2))

gm_peak_at_Vgs_and_Vds = {}
V_T_at_Vds = {}

for v_ds, group in df.groupby('V_DS (V)'):
    
    i_d =  group ['I_D (mA)']
    v_gs = group ['V_GS (V)']
    dI_d_dV_gs = np.gradient(i_d, v_gs)
    
    idx = np.argmax(dI_d_dV_gs)
    gm_peak_at_Vgs_and_Vds[float(dI_d_dV_gs[idx])] = [float(v_gs.iloc[idx]), float(v_ds)]
    
    m, c = np.polyfit(
        v_gs.iloc[-2:],
        i_d.iloc[-2:],
        1
    )
    V_T_at_Vds[-c/m] = float(v_ds)
   
    


    ax[1].scatter(
        v_gs.iloc[idx],
        dI_d_dV_gs[idx],
        color='red',
        s=80,
        zorder=5
    )

    ax[1].annotate(
        f'Peak $g_m$\n({v_gs.iloc[idx]:.2f} V, {dI_d_dV_gs[idx]:.2f} mS)',
        xy=(v_gs.iloc[idx], dI_d_dV_gs[idx]), 
        xytext=(15, 10),                           
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->'),
        fontsize=9
    )
    ax[0].plot(
        v_gs,
        i_d,
        linewidth = 2,
        label = f'$V_{{DS}}$ = {v_ds} V'
    )
    
    ax[1].plot(
        v_gs,
        dI_d_dV_gs,
        label = f'$V_{{DS}}$ = {v_ds} V'
    )

ax[0].set_title(r'Transfer characteristics',
                fontweight = 'bold')
ax[0].set_xlabel(r'$V_{GS}$ (V)')
ax[0].set_ylabel(r'$I_D$ (mA)')


ax[1].set_title(r'Transconductance $g_m = dI_D/dV_{GS}$', 
                fontweight = 'bold')
ax[1].set_xlabel(r'$V_{GS} (V)$')
ax[1].set_ylabel(r'$g_m$ (mS)')



for gm in gm_peak_at_Vgs_and_Vds :
    print(
        f'gm peak (at V_ds = {gm_peak_at_Vgs_and_Vds[gm][1]} V) : {gm:2.3f} mS (occurred at V_gs = {gm_peak_at_Vgs_and_Vds[gm][0]} V) '
    )
print('=='*20)
for Vt in V_T_at_Vds:
    print(
        f'V_T (at V_ds = {V_T_at_Vds[Vt]:1.2f} V) : {Vt:1.3f} V'
    )





for i in ax:
    i.grid(True, 
            linestyle = '--',
            alpha = 0.6
            )
    i.legend(fontsize = 10)

plt.tight_layout()
plt.savefig('gm_transfer.png', dpi = 300)

plt.show()