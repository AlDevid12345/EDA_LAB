import matplotlib.pyplot as plt, pandas as pd, numpy as np
df = pd.read_csv(r"D:\EDA_Lab\25EC01004\Lab1\Electrical Data\MOSFET_ID_VDS.csv")


for i in df.groupby("V_GS (V)"):
    xData = i[1]["V_DS (V)"]
    yDate = i[1]["I_D (mA)"]
    plt.plot(xData, yDate, marker = "o", linewidth = 2, label=f'$V_{{GS}}$ = {i[0]} V')
#print(df["V_GS (V)"])
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$ (V)", fontsize=12, labelpad=10) 
plt.ylabel("Drain Current, $I_D$ (mA)", fontsize=12, labelpad=10)
plt.title('MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)', fontsize=14, fontweight='bold', pad=15)
plt.legend(title='Gate-Source Voltage', title_fontsize='11',  loc='upper left', fontsize='10') 
plt.grid(True, linestyle='--', alpha=0.6) 
plt.savefig('Id-Vds_Plot.png', dpi = 300)
plt.tight_layout()

plt.figure(2, figsize=(10, 6)) 
r0 = 0
for v_gs, group in df.groupby("V_GS (V)"):
    v_ds, i_d = group["V_DS (V)"], group["I_D (mA)"]
    did_dvds = np.gradient(i_d, v_ds)
    
    plt.plot(v_ds, did_dvds, marker='s', linestyle='--', linewidth=2, label=f'$V_{{GS}} = {v_gs} V$')
    if v_gs == 5.0 :
        r0 = 1/did_dvds[-1]
        

print(f'r0 = 1/gd = {r0:1.3f} kOhms')


plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12, labelpad=10) 
plt.ylabel('Conductance, $g_d$ (mS or mA/V)', fontsize=12, labelpad=10) 
plt.legend(title='Gate-Source Voltage', loc='upper right', fontsize='10') 
plt.grid(True, linestyle='--', alpha=0.6) 
plt.tight_layout() 
plt.savefig('gd_vds.png', dpi=300) 









plt.show()
