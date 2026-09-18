import pandas as pd, matplotlib.pyplot as plt, numpy as np
df1 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_no_qf_idvg_vds_0.4.csv'
)
df2 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_3.5_nm_no_qf_idvg_vds_0.4.csv'
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



#Plotting
x = df1['drain TotalCurrent(IdVg_n128_des) X']
mask = (x >= 0.875) & (x <= 1.15)
y1 = df1['drain TotalCurrent(IdVg_n128_des) Y']
y2 = df2['drain TotalCurrent(IdVg_n128_des) Y']

m1, c1 = np.polyfit(
    x[mask],
    y1[mask],
    1
)
m2, c2 = np.polyfit(
    x[mask],
    y2[mask],
    1
)
x_tang = np.arange(0.25, 1.25, 0.02)
y1_tang = m1*x_tang + c1
y2_tang = m2*x_tang + c2
v_th = {}
v_th[3.5] = float(-c2/m2)
v_th[5.0] = float(-c1/m1)




# print(float(-c1/m1))
# print(float(-c2/m2))



plt.plot(
    x,
    y1*1e3,
    linewidth=2,
    label = r'$t_{ox}$ = 5.0nm'
)
plt.plot(
    x_tang,
    y1_tang*1000,
    linewidth=1,
    linestyle = '-.',
    color = 'black',
    alpha=0.7,
    label = r'Tangent for threshold voltage at $t_{ox}$ = 5.0nm'
)


plt.plot(
    x,
    y2*1e3,
    linewidth=2,
    label = r'$t_{ox}$ = 3.5nm'
)
plt.plot(
    x_tang,
    y2_tang*1000,
    linewidth=1,
    linestyle = '--',
    color = 'black',
    alpha=0.7,
    label = r'Tangent for threshold voltage at $t_{ox}$ = 3.5nm'
)

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
    f'Threshold Voltage ($V_{{TH}}$) for $t_{{ox}}$ = $5.0nm$: '
    f'{v_th[5.0]:1.3f} V\n'
    f'Threshold Voltage ($V_{{TH}}$) for $t_{{ox}}$ = $3.5nm$: '
    f'{v_th[3.5]:1.3f} V ',
    ha='left',
    va='bottom',
    fontsize=9,
    fontweight = 'bold',
    transform=ax.transAxes
    
)












plt.xlabel(
    r'$V_{GS}$,  (V) $\longrightarrow$'
)
plt.ylabel(
    r'$I_D$,  (mA) $\longrightarrow$'
)
plt.title(
    r'$I_D - V_{GS}$ for different $t_{ox}$  at $V_{DS}$ = 0.4V and without $Q_{f}$',
)




plt.grid(
        True,
        linestyle = '--',
        alpha = 0.6
)
plt.legend(
        fontsize = 10
)
plt.tight_layout()
# plt.savefig(
#     'Q10.1_Id_Vgs_tox=5_&_3.5nm_vds=0.4_qf=0.png',
#     dpi = 300
# )
plt.show()
