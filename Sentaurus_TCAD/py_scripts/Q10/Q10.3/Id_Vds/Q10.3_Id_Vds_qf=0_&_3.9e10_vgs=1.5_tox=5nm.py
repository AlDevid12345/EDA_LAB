import pandas as pd, matplotlib.pyplot as plt, numpy as np
df1 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_no_qf_idvd_vgs_1.5.csv'
)
df2 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_with_qf_idvd_vgs_1.5.csv'
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
    label = f'without $Q_f$'
)
plt.plot(
    df2['drain TotalCurrent(IdVg_n127_des) X'],
    df2['drain TotalCurrent(IdVg_n127_des) Y']*1e3,
    linewidth=2,
    label = f'with $Q_f$'
)
plt.xlabel(
    r'$V_{DS}$,  (V) $\longrightarrow$'
)
plt.ylabel(
    r'$I_D$,  (mA) $\longrightarrow$'
)
plt.title(
    r'$I_D - V_{DS}$ with and without $Q_{f}$ at $V_{GS}$ = 1.5V and $t_{ox}$ = 5nm ',
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
#     'Q10.3_Id_Vds_qf=0_&_3.9e10_vgs=1.5_tox=5nm.png',
#     dpi = 300
# )
plt.show()
