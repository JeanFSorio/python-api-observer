import psycopg2
import requests
from datetime import datetime
import time
import pytz


ufs = ['br', 'ac', 'al', 'ap','am', 'ba', 'ce', 'df', 'es', 'zz', 'go', 'ma', 'mt', 'ms','mg', 'pr', 'pb', 'pa', 'pe', 'pi','rj','rn', 'rs','ro','rr','sc','se','sp','to']
def loop():   
   #fetch form url
   timeNow = datetime.now(pytz.timezone('Brazil/East'))
   for uf in ufs:
      url = f"https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/{uf}/{uf}-c0001-e000545-r.json"
      response = requests.get(url)
      #establishing the connection
      conn = psycopg2.connect("postgresql://postgres:EKoXvG1FI2gQe64rpZZg@containers-us-west-27.railway.app:6706/railway")
      cursor = conn.cursor()
      cursor.execute( "INSERT INTO eleicao_log (apuracao, horario, localidade) " + 
                           f"VALUES ('{response.text}', '{timeNow}', '{uf}');")
      conn.commit()
      conn.close()
      print(f"Done! - {timeNow} - {uf}")
   time.sleep(600)
   
for x in range(0,10):
   loop()
