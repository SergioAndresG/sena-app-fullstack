from sqlalchemy.orm import Session
from connection import crear
from MODELS.archivo_excel import ArchivoExcel
from MODELS.ficha import Ficha
from datetime import datetime, timedelta

def cleanup_old_db_records():
    """Elimina registros antiguos de la base de datos (ejemplo: archivos_excel > 30 días)."""
    db = Session(bind=crear)
    try:
        cutoff = datetime.now() - timedelta(days=30)
        # Buscar registros viejos
        old_records = db.query(ArchivoExcel).filter(ArchivoExcel.fecha_creacion < cutoff).all()
        for record in old_records:
            db.delete(record)
            print(f"🗑️ Eliminado de BD: {record.nombre_original}")
        db.commit()
    except Exception as e:
        print(f"❌ Error eliminando registros: {e}")
        db.rollback()
    finally:
        db.close()  

def delete_ficha(db: Session, numero_ficha: str):
    """
    Elimina una ficha específica y, gracias a la configuración de cascada,
    a todos sus aprendices asociados.
    """
    # Buscar la ficha por su número
    ficha_a_eliminar = db.query(Ficha).filter(Ficha.numero_ficha == numero_ficha).first()

    if not ficha_a_eliminar:
        # Si no se encuentra la ficha, no se puede eliminar nada
        return None

    # Eliminar la ficha. SQLAlchemy se encargará de la cascada en la sesión.
    db.delete(ficha_a_eliminar)
    db.commit()
    
    return ficha_a_eliminar

def clean_old_db_tokens():
    db = Session(bind=crear)
    try:
        cutoff = datetime.now() - timedelta(days=30)
        # Buscar registros viejos
        old_records = db.query(Ficha).filter(Ficha.fecha_reporte < cutoff).all()
        for record in old_records:
            db.delete(record)
            print(f"🗑️ Eliminado de BD: {record.numero_ficha}")
        db.commit()
    except Exception as e:
        print(f"❌ Error eliminando registros: {e}")
        db.rollback()
    finally:
        db.close()  

