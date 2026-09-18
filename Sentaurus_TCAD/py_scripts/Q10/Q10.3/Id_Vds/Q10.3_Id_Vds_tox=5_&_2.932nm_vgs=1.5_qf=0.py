import pandas as pd, matplotlib.pyplot as plt, numpy as np
df1 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_no_qf_idvd_vgs_1.5.csv'
)
df2 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_2.93nm_no_qf_idvd_vgs_1.5.csv'
)

#For setting up the figure to show all the plots
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)

#Plotting
plt.plot(
    df1['drain TotalCurrent(IdVg_n127_des) X'],
    df1['drain TotalCurrent(IdVg_n127_des) Y']*1e3,
    linewidth=2,
    label = f'$t_{{ox}}$ = 5.000 nm'
)
plt.plot(
    df2['drain TotalCurrent(IdVg_n127_des) X'],
    df2['drain TotalCurrent(IdVg_n127_des) Y']*1e3,
    linewidth=2,
    label = f'$t_{{ox}}$ = 2.932 nm'
)
plt.xlabel(
    r'$V_{DS}$,  (V) $\longrightarrow$'
)
plt.ylabel(
    r'$I_D$,  (mA) $\longrightarrow$'
)
plt.title(
    r'$I_D - V_{DS}$ for different $t_{ox}$ at $V_{GS}$ = 1.5V and no $Q_f$ ',
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
#     'Q10.3_Id_Vds_tox=5_&_2.932nm_vgs=1.5_qf=0.png',
#     dpi = 300
# )
plt.show()
