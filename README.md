# Docker_Flask
Files per creare una Docker image con tensorflow-gpu (che include Python 3.5) e Flask

1) Installare Docker

2) Per creare la Docker image clonare la repository e dalla cartella Docker_Flask eseguire il comando "docker build -t nome_immagine ."

3) Per eseguire l'immagine eseguire il comando "docker run -p 4000:80 nome_immagine"

4) Esempio di richiesta: curl -X POST -F image=@image_name.jpg http://127.0.0.1:4000

app.py: carica la rete addestrata a fare crowd counting e crea il web service Flask. Quando arriva una richiesta HTTP POST usa la rete per fare la predizione e restituisce il conteggio.

Dockerfile: definisce cosa va nel container (creato a partire dalla Docker image tensorflow/tensorflow:latest-gpu-py3).

requirements.txt: usato dal Dockerfile per installare i requisiti necessari (Flask).

test_model.json: keras crowd counting network (https://github.com/euleo/Crowd_Counting)

test_model.h5: pesi della keras crowd counting network
