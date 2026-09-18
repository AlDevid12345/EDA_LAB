import matplotlib.pyplot as plt, pandas as pd, numpy as np, math 

#Fundamental Physical Constants
Q         = 1.602 * 1E-19 #C
V_THERMAL = 0.02585      #V
EPS_0 = 8.854 * 1E-14 #F/cm

#Device parameters
N_A = 1E16 #cm^-3
Q_F = 1E12 #cm^-2
T_OX = 10E-7 #cm
MU_N = 400 #cm^2/(V.s)
LAMBDA = 0.1 #V^-1
W = 4 #μm
L = 0.18 #μm

#Material parameters
CHI_SI = 4.05 #eV 
PHI_M = 4.1 #eV
N_I = 1.5E10 #cm^-3
E_G = 1.12 #eV
EPS_SI = 11.7 * EPS_0 #F/cm
EPS_OX = 3.9  * EPS_0 #F/cm
N_C_OVER_N_V = 2.692

phi_f = V_THERMAL * np.log(N_A/N_I)
phi_s = CHI_SI + E_G/2 + V_THERMAL/2 * np.log(N_C_OVER_N_V) + phi_f
phi_ms = PHI_M - phi_s 
psi_sm = 2 * phi_f + 6 * V_THERMAL
c_ox = EPS_OX / T_OX
psi_ox = np.sqrt(2 * Q * N_A * EPS_SI * psi_sm) / c_ox
v_fb = phi_ms - Q_F * Q / c_ox
v_th = v_fb + psi_sm + psi_ox

gamma = np.sqrt(2 * Q * EPS_SI * N_A)/c_ox
alpha = 1 + gamma/(2 * np.sqrt(psi_sm))
fig, ax = plt.subplots(1, 2, figsize = (11, 4.2))
V_DS = np.linspace(0, 4, 1000)

for V_GS in [1, 2, 3]:
    I_D_SPICE1 = 1000*np.where(V_DS <= V_GS-v_th, 
                   MU_N * c_ox * W/L * ((V_GS - v_th)*V_DS - (V_DS**2)/2) * (1 + LAMBDA * V_DS),
                   MU_N * c_ox * W/(2*L) * (V_GS - v_th)**2 * (1 + LAMBDA * V_DS)
    )
    I_D_SPICE3 = 1000*np.where(V_DS <= (V_GS-v_th)/alpha, 
                       MU_N * c_ox * W/L * ((V_GS - v_th)*V_DS - (alpha * V_DS**2)/2) * (1 + LAMBDA * V_DS),
                       MU_N * c_ox * W/(2*L*alpha) * (V_GS - v_th)**2 * (1 + LAMBDA * V_DS)
        )
    ax[0].plot(
        V_DS,
        I_D_SPICE1,
        linewidth = 2,
        label = f'$V_{{GS}}=$ = {V_GS} V'
    )
    ax[1].plot(
        V_DS,
        I_D_SPICE3,
        linewidth = 2,
        label = f'$V_{{GS}}$ = {V_GS} V'
    )
print(f'V_TH = {v_th:0.3f}\n')
for i in range(2):
    ax[i].set_title(f'SPICE {i+1 if i == 0 else i+2}')
    ax[i].set_xlabel(r'Diode Voltage, $V_{DS}$ (V)')
    ax[i].set_ylabel(r'Diode Current, $I_D$ (mA)')
for axis in ax:
    axis.grid(True, 
            linestyle = '--',
            alpha = 0.5
    )
    axis.legend(
        fontsize = 10,
        title = 'Gate to Source Voltage',
        title_fontsize = 11,
        loc = 'upper left'
    )
    
plt.savefig('ID-VDS_using_SPICE_1_and_3.png', dpi = 350)
plt.tight_layout()
plt.show()




