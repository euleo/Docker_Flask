# Docker_Flask
app.py: carica la rete addestrata a fare crowd counting e crea il web service Flask. Quando arriva una richiesta HTTP POST usa la rete per fare la predizione e restituisce il conteggio.

Dockerfile: definisce cosa va nel container (creato a partire dalla Docker image tensorflow/tensorflow:latest-gpu-py3).

requirements.txt: usato dal Dockerfile per installare i requisiti necessari (Flask).

test_model.json: keras crowd counting network (https://github.com/euleo/Crowd_Counting)

test_model.h5: pesi della keras crowd counting network

Per creare l'immagine Docker clonare la repository e dalla cartella Docker_Flask eseguire il comando "docker build -t nome_immagine ."
