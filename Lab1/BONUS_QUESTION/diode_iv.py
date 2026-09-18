import numpy as np, matplotlib.pyplot as plt

I_S       = 1E-12 #A
V_THERMAL = 0.02585 #V

ETAS       = [1.0, 1.5, 2.0] #Ideality factors

fig1, ax1 = plt.subplots(1, 3, figsize = (14, 4.2))
fig2, ax2 = plt.subplots(1, 1, figsize = (11, 5.2))
fig3, ax3 = plt.subplots(1, 1, figsize =(11, 5.2))
v_sweep = np.linspace(0, 0.8, 80)
for index in range(3):
    I_D = I_S*(np.exp(v_sweep /(ETAS[index] * V_THERMAL)) - 1)
    I_D_LOG = I_S*(np.exp(v_sweep /(ETAS[index] * V_THERMAL)) - 1)
    G_D = np.gradient(I_D, v_sweep)
    
    if index == 1:
        I_D*=1000
    if index == 2:
        I_D*=1E6
    ax1[index].plot(
        v_sweep,
        I_D,
        linewidth = 2,
        label = f'$\\eta$ = {ETAS[index]}'
    )
    ax3.semilogy(
        v_sweep,
        I_D_LOG,
        linewidth = 2,
        label = f'$\\eta$ = {ETAS[index]}'
    )
    ax2.semilogy(
            v_sweep,
            G_D,
            linewidth = 2,
            label = f'$\\eta$ = {ETAS[index]}'
    )
fig1.suptitle(
    f'I-V characteristics of diode for various values of $\\eta$ (using Shockley Diode Equation)' ,
    fontsize=14, 
    fontweight='bold', 
)
fig2.suptitle(
    f'$g_d$-V graph of diode for various values of $\\eta$ (using Shockley Diode Equation)' ,
    fontsize=14, 
    fontweight='bold', 
)
fig3.suptitle(
    f'I-V characteristics of diode for various values of $\\eta$ (using Shockley Diode Equation)' ,
    fontsize=14, 
    fontweight='bold', 
)
for axis in ax1:
    axis.grid(True, 
            linestyle = '--',
            alpha = 0.5
    )
    axis.legend(
        fontsize = 10,
        title = 'Ideality factor',
        title_fontsize = 11,
        loc = 'upper left'
    )
ax2.grid(
    True, 
    linestyle = '--',
    alpha = 0.5
)
ax2.legend(
    fontsize = 10,
    title = 'Ideality factor',
    title_fontsize = 11,
    loc = 'upper left'
)
ax3.grid(
    True, 
    linestyle = '--',
    alpha = 0.5
)
ax3.legend(
    fontsize = 10,
    title = 'Ideality factor',
    title_fontsize = 11,
    loc = 'upper left'
)



for index in range(3):
    ax1[index].set_xlabel(r'Diode Voltage, $V_{D}$ (V)')
    y = r'$I_D$ (A)' if index == 0 else r'$I_D$ (mA)' if index == 1 else r'$I_D$ ($\mu$A)'
    ax1[index].set_ylabel(f'Diode Current, '+y)

ax2.set_xlabel(r'Diode Voltage, $V_{D}$ (V)')
ax2.set_ylabel(r' Small Signal Diode conductance, $g_d$ (S)')

ax3.set_xlabel(r'Diode Voltage, $V_{D}$ (V)')
ax3.set_ylabel(r'Diode Current, $I_d$ (A)')

plt.tight_layout()
fig1.savefig('I_V_Diode_Graph_Std.png', dpi = 350)
fig2.savefig('gd_V_Diode_Graph.png',    dpi = 350)
fig3.savefig('I_V_Diode_Graph_Log.png', dpi = 350)
plt.show()