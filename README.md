# Flask PG Events

Projeto para entender o funcionamento de eventos gerados pelo PostgreSQL em uma aplicação Flask.

## Como usar

O projeto utiliza docker para executar a aplicacao e o PostgreSQL. Portanto o primeiro passo é criar a imagem do PostgreSQL:

```BASH
docker run -d --name flask_pg_events_db \
-e POSTGRES_PASSWORD=secret \
-e POSTGRES_USER=user \
-e POSTGRES_DB=db \
postgres:12.9-alpine 
```

Nao e necessario criar uma porta de acesso externo para o PostgreSQL, pois iremos utilizar a funcionalidade do docker network para conectar a aplicacao ao PostgreSQL na porta padrao do PG 5432.

Agora e necessario criar a imagem da aplicacao:

Primeiro copie as configuracoes da aplicacao do arquivo .env.template para o arquivo .env e substitua os valores de acordo com o ambiente de desenvolvimento.

```BASH
cp .env.template .env
```

Depois crie a imagem:

```BASH
docker build -t flask-pg-events-server .
```

Nao irem rodar o container imediatamente, pois e necessario conectar o container a uma rede para conectar ao PostgreSQL.

Para criar o container execute:

```BASH
docker create -d --name flask_pg_events_server \
-p 3000:5000 \
-v $(pwd):/usr/app \
flask-pg-events-server
```

Agora para criar a rede e conectar o container ao PostgreSQL execute:

```BASH
docker network create --driver bridge flask_pg_events 
docker network connect flask_pg_events flask_pg_events_db 
docker network connect flask_pg_events flask_pg_events_server
```

Finalmente inicie o container:

```BASH
docker start flask_pg_events_server
```

## Migração e seed

Para criar a base de dados e seed com dados iniciais, execute:

```BASH
docker exec -i flask_pg_events_db psql -d db -U user < migrations.sql
docker exec -i flask_pg_events_db psql -d db -U user < initial_seed.sql
```
