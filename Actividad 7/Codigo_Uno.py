import requests
import json
from collections import namedtuple
from contextlib import closing
import sqlite3
import logging

from prefect import task, Flow

# Cambio 1: Configuración de la URL de la API y el nombre de la base de datos
API_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"
DATABASE_NAME = "cfpbcomplaints.db"

# Cambio 2: Configuración de registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cambio 3: Función para realizar solicitudes HTTP de manera segura
def safe_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error en la solicitud HTTP: {e}")
        raise

@task
def get_complaint_data():
    # Cambio 4: Uso de la función safe_request para solicitudes HTTP
    response_text = safe_request(API_URL, params={'size': 10})
    response_json = json.loads(response_text)
    return response_json['hits']['hits']

@task
def parse_complaint_data(raw):
    complaints = []
    Complaint = namedtuple('Complaint', ['data_received', 'state', 'product', 'company', 'complaint_what_happened'])
    for row in raw:
        source = row.get('_source')
        this_complaint = Complaint(
            data_received=source.get('date_received'),
            state=source.get('state'),
            product=source.get('product'),
            company=source.get('company'),
            complaint_what_happened=source.get('complaint_what_happened')
        )
        complaints.append(this_complaint)
    return complaints

@task
def store_complaints(parsed):
    create_script = 'CREATE TABLE IF NOT EXISTS complaint (timestamp TEXT, state TEXT, product TEXT, company TEXT, complaint_what_happened TEXT)'
    insert_cmd = "INSERT INTO complaint VALUES (?, ?, ?, ?, ?)"

    try:
        # Cambio 5: Manejo de errores al interactuar con la base de datos
        with closing(sqlite3.connect(DATABASE_NAME)) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.executescript(create_script)
                cursor.executemany(insert_cmd, parsed)
                conn.commit()
    except sqlite3.Error as e:
        logger.error(f"Error al interactuar con la base de datos: {e}")
        raise

with Flow("my etl flow") as f:
    raw = get_complaint_data()
    parsed = parse_complaint_data(raw)
    store_complaints(parsed)

if __name__ == "__main__":
    f.run()
