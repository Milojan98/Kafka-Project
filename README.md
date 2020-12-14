# Kafka-Project

## :wrench: Kafka-Producer
L'objectif de cette partie est qu'à chaque minute une récuperation du prix BTC/USDT soit effectué sur la plateforme d'échange Binance et que par la suite ce dernier, soit envoyé sur notre serveur kafka.
Les applications qui vont nous permettre d'éditer les données dans notre serveur Kafka sont [kafka-python](https://pypi.org/project/kafka-python/) et [cctx](https://pypi.org/project/cctx/).

### :ledger: Librairies utilisées

#### CCTX
Cette librairie nous permettra d'utiliser l'API Binance et de receuillir les valeurs voulues.
La documentation ce trouve [ici](https://github.com/ccxt/ccxt).

#### Kafka-python : KafkaProducer
Cette librairie nous permet de se connecter à notre serveur kafka et de pouvoir interagir avec cette derniere.

### Aperçu 
Localhost:3030 </br>
<img src="https://github.com/Milojan98/Kafka-Project/blob/main/Images/localhost.png"> </br>

Accéder au [code](https://github.com/Milojan98/Kafka-Project/blob/main/python-kafka/ProducerKafka.py) de la partie producer.

## :gear: Kafka-Consumer
Au sein de cette partie, la récuparation des messages stokés sera effectué sur notre serveur kafka et pour pouvoir ensuite afficher un graphique dynamique qui représentera le cours actuel du BTC/USDT. 

### :ledger: Librairies utilisées

#### Kafka-python : KafkaConsumer
Cette librairie nous permet de se connecter à notre serveur kafka et de pouvoir récuperer les messages.

#### Matplotlib 
Cette librairie nous permettra d'afficher un graphique en live, qui s'actualisera au fil des données reçues. 

### :chart_with_upwards_trend: Aperçu 
 Graphique affiché par le consumer: </br>
<img src="https://github.com/Milojan98/Kafka-Project/blob/main/Images/Figure_1.png"> </br>

Accéder au [code](https://github.com/Milojan98/Kafka-Project/blob/main/python-kafka/ConsumerKafka.py) de la partie consumer.


