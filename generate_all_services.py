#!/usr/bin/env python3
import pandas as pd
import os

# Rutas de archivos y directorios
CSV_PATH = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/BaseDeDatos.csv'
TEMPLATE_MAP = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/PlantillaServMap.astro'
TEMPLATE_TEST = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/PlantillaServTest.astro'
BASE_OUTPUT_DIR = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/pages/services'

# Mapeo de servicios a carpetas de destino
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

# Mapeo de nombres de archivo CSV a nombres reales de archivo
FILE_NAME_MAPPING = {
    'paver-maintenance': 'maintenance',
    'paver-installation': 'installation',
    'belgium-blocks': 'belgium-blocks',
    'sod-installation': 'sod-installation',
    'top-soil': 'top-soil', 
    'power-wash': 'power-wash',
    'crack-filling': 'crack-filling',
    'line-striping': 'line-striping'
}

# Archivos a generar por plantilla
MAP_FILES = [
    'installation', 'replacement', 'sealcoating', 'line-striping',
    'paver-maintenance', 'walkways', 'curbs', 'sod-installation',
    'drainage', 'hauling'
]
TEST_FILES = [
    'resurfacing', 'extension', 'crack-filling', 'paver-installation',
    'belgium-blocks', 'sidewalks', 'aprons', 'top-soil', 'power-wash'
]

# Lista de placeholders a reemplazar - Mapeo correcto según columnas CSV
PLACEHOLDER_MAPPING = {
    'title': 2,  # Columna C (índice 2)
    'meta_description': 3,  # Columna D (índice 3) 
    'description': 3,  # Columna D (índice 3) - mismo que meta_description
    'canonical': 4,  # Columna E (índice 4)
    'keywords': 5,  # Columna F (índice 5)
    'breadcrumb_title': 6,  # Columna G (índice 6)
    'breadcrumb_path': 7,  # Columna H (índice 7)
    'block_title_1': 8,  # Columna I (índice 8)
    'block_description_1': 9,  # Columna J (índice 9)
    'img_alt_1': 10,  # Columna K (índice 10)
    'img_alt_2': 11,  # Columna L (índice 11)
    'block_title_2': 12,  # Columna M (índice 12)
    'block_description_2': 13,  # Columna N (índice 13)
    'block_title_3': 14,  # Columna O (índice 14)
    'block_description_3': 15,  # Columna P (índice 15)
    'img_alt_3': 16,  # Columna Q (índice 16)
    'block_title_4': 17,  # Columna R (índice 17)
    'block_description_4': 18,  # Columna S (índice 18)
    'img_alt_4': 19,  # Columna T (índice 19)
    'list_areas': 20,  # Columna U (índice 20)
    'img_1': 21,  # Columna V (índice 21)
    'img_2': 22,  # Columna W (índice 22)
    'img_3': 23,  # Columna X (índice 23)
    'img_4': 24,  # Columna Y (índice 24)
    'breadcrumb_bg': 25  # Columna Z (índice 25)
}

def load_template(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_file(row_data, template_str, output_path):
    content = template_str
    
    # Debug: mostrar los primeros datos de la fila
    print(f"Procesando archivo para: {row_data[0] if len(row_data) > 0 else 'N/A'}")
    
    # Reemplazar placeholders basado en el mapeo
    for placeholder, col_index in PLACEHOLDER_MAPPING.items():
        if col_index < len(row_data):
            val = str(row_data[col_index]).strip()
            
            # Procesamiento especial para list_areas
            if placeholder == 'list_areas' and val and val != 'nan':
                # Dividir por comas y crear elementos <li>
                areas = [area.strip() for area in val.split(',')]
                val = '\n'.join([f'                        <li>{area}</li>' for area in areas])
            
            # Limpiar valores NaN o vacíos
            if val == 'nan' or val == '' or val == 'nan':
                val = ''
            
            # Reemplazar con diferentes formatos de placeholders
            # Formato con espacios: {{ placeholder }}
            content = content.replace(f"{{{{ {placeholder} }}}}", val)
            # Formato sin espacios: {{placeholder}}
            content = content.replace(f"{{{{{placeholder}}}}}", val)
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Cargar CSV (saltando las dos primeras líneas: título y encabezado)
    df = pd.read_csv(CSV_PATH, skiprows=2, header=None)

    # Cargar plantillas
    tmpl_map = load_template(TEMPLATE_MAP)
    tmpl_test = load_template(TEMPLATE_TEST)

    # Generar archivos para PlantillaServMap
    for file_id in MAP_FILES:
        # Buscar la fila correspondiente en el CSV
        row_found = None
        for index, row in df.iterrows():
            if len(row) > 0 and str(row[0]).strip() == file_id:
                row_found = row.values
                break
        
        if row_found is None:
            print(f"Advertencia: '{file_id}' no encontrado en CSV.")
            continue
        
        # Determinar carpeta de destino y nombre de archivo
        folder = FOLDER_MAPPING.get(file_id, 'other')
        output_dir = os.path.join(BASE_OUTPUT_DIR, folder)
        
        # Usar el mapeo de nombres para obtener el nombre correcto del archivo
        actual_filename = FILE_NAME_MAPPING.get(file_id, file_id)
        out_path = os.path.join(output_dir, f"{actual_filename}.astro")
        
        generate_file(row_found, tmpl_map, out_path)
        print(f"Generado: {out_path}")

    # Generar archivos para PlantillaServTest
    for file_id in TEST_FILES:
        # Buscar la fila correspondiente en el CSV
        row_found = None
        for index, row in df.iterrows():
            if len(row) > 0 and str(row[0]).strip() == file_id:
                row_found = row.values
                break
        
        if row_found is None:
            print(f"Advertencia: '{file_id}' no encontrado en CSV.")
            continue
        
        # Determinar carpeta de destino usando el mapeo
        folder = FOLDER_MAPPING.get(file_id, 'other')
        output_dir = os.path.join(BASE_OUTPUT_DIR, folder)
        
        # Usar el mapeo de nombres para obtener el nombre correcto del archivo
        actual_filename = FILE_NAME_MAPPING.get(file_id, file_id)
        out_path = os.path.join(output_dir, f"{actual_filename}.astro")
        
        generate_file(row_found, tmpl_test, out_path)
        print(f"Generado: {out_path}")

if __name__ == "__main__":
    main()
