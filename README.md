# Kafka-Project

## :wrench: Kafka-Producer
L'objectif ici est de récuperer le prix du BTC/USDT toute les minutes sur la plateforme d'échange Binance et de l'envoyer sur notre serveur kafka.
Les applications qui va nous permettre d'éditer les données dans notre serveur Kafka sont [kafka-python](https://pypi.org/project/kafka-python/) et [cctx](https://pypi.org/project/cctx/).

### :ledger: Librairies utilisées

#### CCTX
Cette librairie va nous permettre d'utiliser l'API Binance et de requeter nos valeurs voulues.
La documentation ce trouve [ici](https://github.com/ccxt/ccxt).

#### Kafka-python
Cette librairie nous permet de se connecter à notre serveur kafka et de pouvoir interagir avec celle-ci.

### Apercu 
Localhost:3030 </br>
<img src="https://github.com/Milojan98/Kafka-Project/blob/main/Images/localhost.png"> </br>

Accéder au [code](https://github.com/Milojan98/Kafka-Project/blob/main/python-kafka/ProducerKafka.py) de la partie producer.

## :gear: Kafka-Consumer

### :chart_with_upwards_trend: Apercu 
 Graphique afficher par le consumer: </br>
<img src="https://github.com/Milojan98/Kafka-Project/blob/main/Images/Figure_1.png"> </br>


