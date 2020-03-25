# Scraper Twitter API
## Sobre

API de exemplo para scraping de dados na api do twitter com flask, coleta de métricas via prometheus, dashboard de visualização no grafana e tracking de error/performance com elastic search, kibana e apm-server.

## Setup
Para instalar os pacotes necessários para a execução da aplicação em python é necessário ter:
  - Python 3.6
  - Pip > 9

Exportar as variáveis de ambiente:
Endpoint do banco de dados:
```sh
      $ export DATABASE_URL=mysql+pymysql://user:pass@host:port/database?charset=utf8mb4
```
Credenciais de acesso a api do twitter:
```sh
      $ export CLIENT_KEY=[CREDENCIAL_AQUI] #
      $ export CLIENT_SECRET=[CREDENCIAL_AQUI]
```
Endpoint do apm-server:
```sh
      $ export APM_URL=http://apm-server:8200
```
Executar a aplicação localmente:
 ```sh
$ make setup
$ make run local
```

### Executando a aplicação via compose:

Requisitos:
  - Docker
  - Docker-compose

Editar o arquivo do docker-compose:
 ```sh
$ vim infra/docker/docker-compose.yml
```
E definir as credenciais de acesso a api do twitter:
```
CLIENT_KEY=[CREDENCIAL_AQUI]
CLIENT_SECRET=[CREDENCIAL_AQUI]
```
Executar a aplicação localmente:
 ```sh
$ make docker-run
```
Os serviços estarão disponíveis nas seguintes portas:
| Serviço | Host |
| ------ | ------ |
| API | http://127.0.0.1:5000 |
| Kibana | http://127.0.0.1:5601 |
| Grafana | http://127.0.0.1:3000 |
| Prometheus | http://127.0.0.1:9090 |
| ElasticSearch | http://127.0.0.1:9200 |
| Apm-server  | http://127.0.0.1:8200  |

## Rotas da API

WebUI :
http://127.0.0.1:5000/

Obtem até 100 posts para cada uma das hashtags e armazena no banco de dados:
http://127.0.0.1:5000/populate

Lista os autores mais influentes:
http://127.0.0.1:5000/top

Mostra a lista total dos tweets ordenados por hora:
http://127.0.0.1:5000/tweets

Exibe o total de postagens para cada uma das #tag por idioma/país do usuário que postou:
http://127.0.0.1:5000/total

Exporter para coleta do prometheus:
http://127.0.0.1:5000/metric

