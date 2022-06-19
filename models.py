#creacion de modelos 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario (db.Model):
    __tablename__= 'Usuario'
    id = db.Colum(db.Integer, primary_key = True)
    primer_nombre = dbColum(db.String(250), nulable = False)
    segundo_nombre = dbColum(db.String(250), nulable = False)
    apellido_paterno = dbColum(db.String(250), nulable = False)
    apellido_materno = dbColum(db.String(250), nulable = False)
    direccion = dbColum(db.String(250), nulable = False)

    def serialize(self):
        return {
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion
        }
        def save(self):
            db.session.add(self)
            db.session.commit()
        def update(self):
            db.session.commit()
        def delete(self):
            db.session.delete(self)
            db.session.commit()
