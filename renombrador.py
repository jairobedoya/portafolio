import os


carpeta = r"C:\Users\JAIRO BEDOYA\OneDrive\Escritorio\archivos_originales"


archivos = os.listdir(carpeta)


for i, nombre_original in enumerate(archivos, start=1):
    ruta_original = os.path.join(carpeta, nombre_original)
    
  
    nombre_sin_ext, extension = os.path.splitext(nombre_original)
    
    
    nuevo_nombre = f"jairo_{i:03}{extension}"
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)

    os.rename(ruta_original, ruta_nueva)
    print(f"Renombrado: {nombre_original} -> {nuevo_nombre}")