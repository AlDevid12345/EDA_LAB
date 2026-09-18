import pandas as pd, matplotlib.pyplot as plt, numpy as np
df = pd.read_csv(
    r'D:\EDA_Lab\25EC01004\Lab1\Electrical Data\Diode_IV_Temperature.csv'
)
V_T_at_temp = {}
for Temperature, group in df.groupby('T (C)'):
    I = group ['I (mA)']
    V = group ['V (V)']
    
    plt.plot(V,
            I,
            linewidth = 2,
            label = f'T = {Temperature} °C'
            )
    m, c = np.polyfit(
        V.iloc[-3:], 
        I.iloc[-3:], 
        1
    )
    V_T_at_temp[Temperature] = float(-c/m)

    V_fit = np.linspace(
        V.iloc[-3]-0.01, 
        V.iloc[-1]+0.01, 
        100
    )

    
    I_fit = m * V_fit + c

plt.title('Diode I - V characteristics')
plt.xlabel(r'Diode Voltage, $V_{D}$')
plt.ylabel(r'Diode Current, $I_{D}$')
plt.grid(
    True, 
    linestyle='--', 
    alpha = 0.5
)
plt.legend(
    title = 'Temperature',
    fontsize = 10,
    title_fontsize = 11,
    loc = 'upper left'
)
for temp in V_T_at_temp:
    print(f'V_T at temperature {temp} °C : {V_T_at_temp[temp]:1.3} V')


plt.savefig('I_V_characteristics.png', dpi = 350)
plt.show()