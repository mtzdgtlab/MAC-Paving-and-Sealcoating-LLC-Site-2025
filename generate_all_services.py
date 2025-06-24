#!/usr/bin/env python3
import pandas as pd
import os

# Rutas de archivos y directorios
CSV_PATH = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/Base_de_Datos_de_Servicios.csv'
TEMPLATE_MAP = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/PlantillaServMap.astro'
TEMPLATE_TEST = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/data/PlantillaServTest.astro'
OUTPUT_DIR = '/Users/ismrtinez/Sites/astro-textos-mac-repo/src/pages/services/all-services'

# Archivos a generar por plantilla
MAP_FILES = [
    '2 Installation', '4 Replacement', '6 Sealcoating', '8 Line Striping',
    '10 Paver Maintenance', '12 Walkways', '14 Curbs', '16 Sod Installation',
    '18 Drainage', '20 Hauling'
]
TEST_FILES = [
    '3 Resurfacing', '5 Extension', '7 Crack Filling', '9 Pavers Installation',
    '11 Belgium blocks', '13 Sidewalks', '15 Aprons', '17 Top Soil', '19 Power Wash'
]

# Lista de placeholders a reemplazar
PLACEHOLDERS = [
    'title', 'description', 'canonical', 'keywords', 'breadcrumb_title', 'breadcrumb_path',
    'block_title_1', 'block_description_1', 'img_alt_1', 'img_alt_2',
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
        # Reemplazar con espacios dentro y sin espacios
        content = content.replace(f"{{{{ {ph} }}}}", val)
        content = content.replace(f"{{{{{ph}}}}}", val)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Crear carpeta de salida si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Cargar CSV
    df = pd.read_csv(CSV_PATH)

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
        out_path = os.path.join(OUTPUT_DIR, f"{file_id}.astro")
        generate_file(row, tmpl_map, out_path)
        print(f"Generado: {out_path}")

    # Generar archivos para PlantillaServTest
    for file_id in TEST_FILES:
        row = df[df['file'] == file_id]
        if row.empty:
            print(f"Advertencia: '{file_id}' no encontrado en CSV.")
            continue
        row = row.iloc[0]
        out_path = os.path.join(OUTPUT_DIR, f"{file_id}.astro")
        generate_file(row, tmpl_test, out_path)
        print(f"Generado: {out_path}")

if __name__ == "__main__":
    main()
