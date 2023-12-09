# main.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TipoCambio(Base):
    __tablename__ = 'tipo_cambio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    moneda_origen = Column(String, nullable=False)
    moneda_destino = Column(String, nullable=False)
    tasa_cambio = Column(Float, nullable=False)

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)

def config():
    # Configuración de la base de datos
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ejemplo: Insertar un tipo de cambio
    tipo_cambio = TipoCambio(moneda_origen='USD', moneda_destino='EUR', tasa_cambio=1.2)
    session.add(tipo_cambio)

    # Ejemplo: Insertar un cliente
    cliente = Cliente(nombre='John', apellido='Doe', email='john.doe@example.com')
    session.add(cliente)

    # Guardar los cambios en la base de datos
    session.commit()

if __name__ == "__main__":
    # Llamada a la función config al inicio del programa
    config()

    # Resto del código del menú y opciones...
