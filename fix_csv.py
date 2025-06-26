#!/usr/bin/env python3
import pandas as pd

# Mapeo de servicios a carpetas
FOLDER_MAPPING = {
    'installation': 'asphalt-paving',
    'resurfacing': 'asphalt-paving', 
    'replacement': 'asphalt-paving',
    'extension': 'asphalt-paving',
    'sealcoating': 'sealer',
    'crack-filling': 'sealer',
    'line-striping': 'sealer',
    'paver-installation': 'pavers',
    'paver-maintenance': 'pavers',
    'belgium-blocks': 'pavers',
    'walkways': 'concrete',
    'sidewalks': 'concrete',
    'curbs': 'concrete',
    'aprons': 'concrete',
    'sod-installation': 'landscaping',
    'top-soil': 'landscaping',
    'drainage': 'landscaping',
    'power-wash': 'landscaping',
    'hauling': 'landscaping'
}

# Leer CSV
csv_path = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/Base_de_Datos_de_Servicios.csv'

# Leer el archivo línea por línea para mantener el formato
with open(csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Procesar cada línea
new_lines = []
for i, line in enumerate(lines):
    if i == 0:  # Título
        new_lines.append(line)
    elif i == 1:  # Header - agregar output_folder
        line = line.strip()
        if not line.startswith('file,output_folder,'):
            line = line.replace('file,', 'file,output_folder,')
        new_lines.append(line + '\n')
    else:  # Datos
        parts = line.strip().split(',', 1)  # Solo split en la primera coma
        if len(parts) >= 2:
            file_name = parts[0]
            rest = parts[1]
            folder = FOLDER_MAPPING.get(file_name, 'other')
            new_line = f"{file_name},{folder},{rest}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

# Escribir archivo actualizado
with open(csv_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("CSV actualizado con columna output_folder")
