# [Histórico Eleições](https://eleicao-historico.up.railway.app/)

[JeanFSorio/eleicao-rails](https://github.com/JeanFSorio/eleicao-rails) is the website project.

[This project](https://eleicao-historico.up.railway.app/) goal was to make a log of every minute update of an API, [this API](https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json) was showing the current progress in the electoral results.

This project is basically a big recursive function with a 5 minutes sleep, so from time to time it read the API and see if are there changes, if true ir save in the mongodb server a log from that moment. This recursive function had a time to start and a time to stop fetching the API.