import pandas as pd

# Leer CSV
df = pd.read_csv('/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/Base_de_Datos_de_Servicios.csv', skiprows=1)

# Encontrar instalaciones
installations = df[df['file'] == 'installation']
print('Instalaciones encontradas:')
for i, row in installations.iterrows():
    print(f'{i}: {row["title"]}')

# Encontrar maintenance
maintenance = df[df['file'] == 'maintenance']
print('\nMaintenance encontrados:')
for i, row in maintenance.iterrows():
    print(f'{i}: {row["title"]}')
