import requests

class jsonResponse: 
    def __init__(self, uf, jsonText): 
        self.uf = uf 
        self.jsonText = jsonText


def fecthJson(ufs, codigoCargo, codigoOrdem):
   response = []
   for uf in ufs:
      # para tentar uniformizar o horario posso fazer o fetch de todos e salvar em um objeto e só depois fazer os insert
      url = f"https://resultados.tse.jus.br/oficial/ele2022/{codigoOrdem}/dados-simplificados/{uf}/{uf}-c000{codigoCargo}-e000{codigoOrdem}-r.json"
      #dictResponse = {'jsonResponse':,"uf": uf}
      response.append(jsonResponse( uf, requests.get(url).text ))
   return response;
