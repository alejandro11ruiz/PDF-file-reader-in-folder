import os
import fitz
import fnmatch
import pandas as pd

# Patrones de búsqueda
patterns = ['*.PDF', '*.pdf']

# Obtener lista de archivos en el directorio
files = os.listdir(".")

# Filtrar archivos que coincidan con cualquiera de los patrones
matching_files = []
for pattern in patterns:
    matching_files.extend(fnmatch.filter(files, pattern))

def get_pdf_properties(file_path):
    # Abrir el archivo PDF
    pdf_document = fitz.open(file_path)

    # Obtener propiedades del PDF
    properties = {
        "Archivo": file_path,
        "No. Paginas":pdf_document.page_count
    }

    # Cerrar el documento PDF
    pdf_document.close()

    return properties

concatInfoFiles=[]

for file in matching_files:
    concatInfoFiles.append(get_pdf_properties(file))
    
df=pd.DataFrame(concatInfoFiles)

df.to_csv('conteo_de_paginas.csv', index=False)
    
