
import psycopg2

def saveMany(response, timeNow):
    #establishing the connection
   for res in response:
      conn = psycopg2.connect(
          "postgresql://postgres:EKoXvG1FI2gQe64rpZZg@containers-us-west-27.railway.app:6706/railway")
      cursor = conn.cursor()
      cursor.execute("INSERT INTO eleicao_log (apuracao, horario, localidade) " +
                     f"VALUES ('{res.json}', '{timeNow}', '{res.uf}');")
      conn.commit()
      conn.close()
      print(f"Done! - {timeNow} - {res.uf}")