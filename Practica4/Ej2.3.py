# Jobs.py
import requests
from sqlalchemy import create_engine, Column, String, Float, Integer  # Añadir Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TipoCambio(Base):
    __tablename__ = 'tipo_cambio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    moneda_origen = Column(String, nullable=False)
    moneda_destino = Column(String, nullable=False)
    tasa_cambio = Column(Float, nullable=False)

def actualizar_tipo_cambio():
    # URL de la API para obtener el tipo de cambio
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

    try:
        # Realizar la solicitud a la API
        response = requests.get(url)
        data = response.json()

        # Obtener los valores necesarios de la respuesta
        moneda_origen = data['moneda_origen']
        moneda_destino = data['moneda_destino']
        tasa_cambio = data['tasa_cambio']

        # Configuración de la base de datos
        engine = create_engine('sqlite:///app.db')
        Base.metadata.create_all(engine)

        # Crear una sesión
        Session = sessionmaker(bind=engine)
        session = Session()

        # Insertar el tipo de cambio en la base de datos
        tipo_cambio = TipoCambio(moneda_origen=moneda_origen, moneda_destino=moneda_destino, tasa_cambio=tasa_cambio)
        session.add(tipo_cambio)
        session.commit()

        print("Tipo de cambio actualizado exitosamente.")

    except Exception as e:
        print(f"Error al actualizar el tipo de cambio: {e}")

if __name__ == "__main__":
    actualizar_tipo_cambio()

{
  "result": {
    "moneda_origen": "USD",
    "moneda_destino": "PEN",
    "tasa_cambio": 3.8
  }
}

import requests

def actualizar_tipo_cambio():
    # Obtener la data de la API
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Obtener el contenido JSON de la respuesta
        data = response.json()

        # Verificar si 'moneda_origen' está en la respuesta
        if 'moneda_origen' in data:
            moneda_origen = data['moneda_origen']
            moneda_destino = data['moneda_destino']
            tasa_cambio = data['tasa_cambio']

            # Continuar con el procesamiento de la información
            print(f"Moneda Origen: {moneda_origen}")
            print(f"Moneda Destino: {moneda_destino}")
            print(f"Tasa de Cambio: {tasa_cambio}")
        else:
            print("La clave 'moneda_origen' no está en la respuesta.")
    else:
        print(f"Error al obtener la respuesta de la API. Código de estado: {response.status_code}")

# Llamar a la función para probar
actualizar_tipo_cambio()


