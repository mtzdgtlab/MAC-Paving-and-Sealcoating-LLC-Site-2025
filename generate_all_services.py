#!/usr/bin/env python3
import pandas as pd
import os

# Rutas de archivos y directorios
CSV_PATH = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/Base_de_Datos_de_Servicios.csv'
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

# Lista de placeholders a reemplazar
PLACEHOLDERS = [
    'title', 'description', 'canonical', 'keywords', 'breadcrumb_title', 'breadcrumb_path',
    'breadcrumb_bg', 'block_title_1', 'block_description_1', 'img_alt_1', 'img_alt_2',
    'block_title_2', 'block_description_2', 'block_title_3', 'block_description_3',
    'img_alt_3', 'block_title_4', 'block_description_4', 'img_alt_4',
    'list_areas', 'img_1', 'img_2', 'img_3', 'img_4'
]

def load_template(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_file(row, template_str, output_path):
    content = template_str
    for ph in PLACEHOLDERS:
        val = str(row.get(ph, ''))
        
        # Procesamiento especial para list_areas
        if ph == 'list_areas' and val:
            # Dividir por comas y crear elementos <li>
            areas = [area.strip() for area in val.split(',')]
            val = '\n'.join([f'                        <li>{area}</li>' for area in areas])
        
        # Reemplazar con espacios dentro y sin espacios
        content = content.replace(f"{{{{ {ph} }}}}", val)
        content = content.replace(f"{{{{{ph}}}}}", val)
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Cargar CSV (saltando la primera línea si es necesario)
    df = pd.read_csv(CSV_PATH, skiprows=1)

    # Cargar plantillas
    tmpl_map = load_template(TEMPLATE_MAP)
    tmpl_test = load_template(TEMPLATE_TEST)

    # Generar archivos para PlantillaServMap
    for file_id in MAP_FILES:
        row = df[df['file'] == file_id]
        if row.empty:
            print(f"Advertencia: '{file_id}' no encontrado en CSV.")
            continue
        row = row.iloc[0]
        
        # Determinar carpeta de destino usando el mapeo
        folder = FOLDER_MAPPING.get(file_id, 'other')
        output_dir = os.path.join(BASE_OUTPUT_DIR, folder)
        out_path = os.path.join(output_dir, f"{file_id}.astro")
        
        generate_file(row, tmpl_map, out_path)
        print(f"Generado: {out_path}")

    # Generar archivos para PlantillaServTest
    for file_id in TEST_FILES:
        row = df[df['file'] == file_id]
        if row.empty:
            print(f"Advertencia: '{file_id}' no encontrado en CSV.")
            continue
        row = row.iloc[0]
        
        # Determinar carpeta de destino usando el mapeo
        folder = FOLDER_MAPPING.get(file_id, 'other')
        output_dir = os.path.join(BASE_OUTPUT_DIR, folder)
        out_path = os.path.join(output_dir, f"{file_id}.astro")
        
        generate_file(row, tmpl_test, out_path)
        print(f"Generado: {out_path}")

if __name__ == "__main__":
    main()
