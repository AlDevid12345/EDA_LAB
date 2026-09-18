import pandas as pd, matplotlib.pyplot as plt, numpy as np
df1 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_no_qf_idvg_vds_0.4.csv'
)
df2 = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Sentaurus_TCAD\data\q_10_5nm_with_3.4_qf_idvg_vds_0.4.csv'
)

#For setting up the figure to show all the plots
manager = plt.get_current_fig_manager()
manager.window.state(
    'zoomed'
)

#Plotting
plt.plot(
    df1['drain TotalCurrent(IdVg_n128_des) X'],
    df1['drain TotalCurrent(IdVg_n128_des) Y']*1e3,
    linewidth=2,
    label = f'Without $Q_f$ ($Q_f$ = 0 $cm^{{-2}}$)'
)
plt.plot(
    df2['drain TotalCurrent(IdVg_n128_des) X'],
    df2['drain TotalCurrent(IdVg_n128_des) Y']*1e3,
    linewidth=2,
    label = r'with $Q_f$ ($Q_f$ =  $3.4 \times 10^{10}$ $cm^{-2}$)'
)
plt.xlabel(
    r'$V_{GS}$,  (V) $\longrightarrow$'
)
plt.ylabel(
    r'$I_D$,  (mA) $\longrightarrow$'
)
plt.title(
    r'$I_D - V_{GS}$ with and without $Q_{f}$ at $V_{DS}$ = 0.4V and $t_{ox}$ = 5nm',
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
#     'Q10.3_Id_Vgs_qf=0_&_3.4e10_vds=0.4_tox=5nm.png',
#     dpi = 300
# )
plt.show()
