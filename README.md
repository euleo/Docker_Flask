# Docker_Flask
app.py: carica la rete addestrata a fare crowd counting e crea il web service Flask. Quando gli arriva una richiesta HTTP POST usa la rete per fare la predizione e restituisce il conteggio.

Dockerfile: definisce cosa va nel container (creato a partire dalla Docker image tensorflow/tensorflow:latest-gpu-py3)

requirements.txt: usato dal Dockerfile per installare i requisiti necessari (Flask)
