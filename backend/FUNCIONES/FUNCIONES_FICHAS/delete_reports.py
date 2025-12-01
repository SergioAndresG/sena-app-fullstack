import datetime
import os
REPORTS_DIR = "archivos_exportados"



def cleanup_old_reports():
    """Elimina los archivos de reporte con más de 30 días de antigüedad."""
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=30)
    
    if not os.path.exists(REPORTS_DIR):
        return

    for root, dirs, files in os.walk(REPORTS_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_modified_time < cutoff:
                    os.remove(file_path)
                    print(f"Eliminado archivo antiguo: {file_path}")
            except Exception as e:
                print(f"Error eliminando {file_path}: {e}")