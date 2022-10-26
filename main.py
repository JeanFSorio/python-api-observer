import psycopg2
import requests
from datetime import datetime
import time

def loop():   
   #fetch form url
   url = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
   response = requests.get(url)
   #establishing the connection
   conn = psycopg2.connect("postgresql://postgres:EKoXvG1FI2gQe64rpZZg@containers-us-west-27.railway.app:6706/railway")
   cursor = conn.cursor()
   cursor.execute( "INSERT INTO eleicao_log (apuracao, horario) " + 
                        f"VALUES ('{response.text}', '{datetime.now()}');")
   conn.commit()
   conn.close()
   print(f"Done! - {datetime.now()}")
   time.sleep(600)
   
for x in range(0,10):
   loop()
