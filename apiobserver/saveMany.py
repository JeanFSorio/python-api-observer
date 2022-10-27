
import psycopg2

def saveMany(response, timeNow):
    #establishing the connection
	conn = psycopg2.connect(
		"postgresql://postgres:EKoXvG1FI2gQe64rpZZg@containers-us-west-27.railway.app:6706/railway")
	for res in response:
		# TODO: verificar se já existe
		
		if	verifyDuplicate(conn, res.jsonText):
			save = conn.cursor()
			save.execute("INSERT INTO eleicao_log (apuracao, horario, localidade) " +
						f"VALUES ('{res.jsonText}', '{timeNow}', '{res.uf}');")
			conn.commit()
			print(f"Done! - {timeNow} - {res.uf}")
	conn.close()


def verifyDuplicate(conn, jsonText=''):
	#jsonData = json.load(jsonText)
	query = conn.cursor()
	query.execute("SELECT * FROM eleicao_log " +
					f"WHERE apuracao::text = '{jsonText}'")
	fetch = query.fetchone()
	return fetch is None