import requests

class jsonResponse: 
    def __init__(self, uf, jsonText): 
        self.uf = uf 
        self.jsonText = jsonText


def fecthJson(ufs):
   response = []
   for uf in ufs:
      # para tentar uniformizar o horario posso fazer o fetch de todos e salvar em um objeto e só depois fazer os insert
      url = f"https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/{uf}/{uf}-c0001-e000545-r.json"
      #dictResponse = {'jsonResponse':,"uf": uf}
      response.append(jsonResponse( uf, requests.get(url).text ))
   return response;
