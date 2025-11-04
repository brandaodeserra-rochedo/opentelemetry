
# OpenTelemetry coletando logs, trace e metricas

bash src/command.sh 

##  Stack
- OpenTelemetry Collector 
- Prometheus (Coleta de métricas)
- Tempo (Coleta de trace)
- Loki (Coleta de log)
- Grafana (Visualização)


##  Como baixar o projeto
Clone o repositório:

```
Entre na pasta do projeto:
```
cd opentelemetry
```
baixar as imagens e rodar os containers:
```
sudo docker compose up -d
```

##  Como criar e ativar o ambiente virtual
Execute o comando para criar o ambiente virtual:
```
python3 -m venv venv
```
Execute o comando para ativar o ambiente virtual (Linux):
```
source venv/bin/activate
```

##  Como instalar as libs necessárias
```
pip install -r requirements.txt
```

##  Como executar o script para testar a comunicação com o coletor do OpenTelemetry

Todos os arquivos estão na pasta ```src```

##  Como acessar os serviços

### Grafana
localhost:3000 

#### Credenciais Grafana
____________________________

login: admin

password: admin

____________________________

## Prometheus
localhost: 9090

## Referências
https://www.youtube.com/watch?v=9mifCIFhtIQ&list=PLOQgLBuj2-3IL2SzHv1CHaBBHJEvHZE0m

https://hub.docker.com/r/grafana/otel-lgtm

https://docs.docker.com/engine/cli/otel/

https://github.com/open-telemetry

https://grafana.com/

https://grafana.com/oss/opentelemetry/

https://youtu.be/WHJmahuQ3Sw

git clone https://github.com/wlcamargo/opentelemetry
