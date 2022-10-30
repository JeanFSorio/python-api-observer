
import psycopg2

def saveMany(response, timeNow, cargo):
    #establishing the connection
	conn = psycopg2.connect(
		"postgresql://postgres:EKoXvG1FI2gQe64rpZZg@containers-us-west-27.railway.app:6706/railway")
	for res in response:
		# TODO: verificar se já existe
		
		if	verifyDuplicate(conn, res.jsonText):
			save = conn.cursor()
			save.execute("INSERT INTO resultados (apuracao, horario, localidade, cargo) " +
						f"VALUES ('{res.jsonText}', '{timeNow}', '{res.uf}', '{cargo}');")
			conn.commit()
			print(f"Done! - {timeNow} - {res.uf} -  '{cargo}'")
		else:
			print(f"Already in db! - {timeNow} - {res.uf} -  '{cargo}'")
	conn.close()


def verifyDuplicate(conn, jsonText=''):
	#jsonData = json.load(jsonText)
	query = conn.cursor()
	query.execute("SELECT * FROM resultados " +
					f"WHERE apuracao::text = '{jsonText}'")
	fetch = query.fetchone()
	return True #fetch is None