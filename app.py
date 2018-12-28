from flask import Flask
    
import tensorflow as tf
import PIL
import numpy as np
import os

from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.vgg16 import preprocess_input
from tensorflow.python.keras.models import model_from_json

from flask import Flask, request
app = Flask(__name__)

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

global graph
graph = tf.get_default_graph()

# load json and create model
json_file = open('test_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load weights into new model
model.load_weights("test_model.h5")

@app.route('/',methods = ['POST'])
def count():
   if not 'image' in request.files:
       return 'no file'

   img_file = request.files.get('image')
   return str(prediction(img_file))


def prediction(im):     
    img = image.load_img(im)
    img = img.resize((224,224),PIL.Image.BILINEAR)
    x = image.img_to_array(img)
    x = preprocess_input(x)
    x = np.expand_dims(x, axis=0)
    
    with graph.as_default():
        features = model.predict(x)

    return features

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
