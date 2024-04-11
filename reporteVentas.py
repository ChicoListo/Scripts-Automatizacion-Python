#Genera un repórte simple con visualizacion de datos usando matplotlib y pandas.
import pandas as pd
import matplotlib.pyplot as plt

# Datos de muestra
data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [200, 240, 310, 400]}
df = pd.DataFrame(data)

# Creación del gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Mes'], df['Ventas'], marker='o', color='b', linestyle='-')
plt.title('Reporte Mensual de Ventas', fontsize=16)
plt.xlabel('Mes', fontsize=14)
plt.ylabel('Ventas', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.tight_layout()

# Guardar el gráfico como imagen
plt.savefig(r'C:\Users\user\Downloads\figure.png')

# Mostrar el gráfico
plt.show()
