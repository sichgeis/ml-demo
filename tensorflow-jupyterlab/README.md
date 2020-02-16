# Jupyter with Docker Compose

This repository contains a simple docker-compose definition for launching the popular JupyterLab with a Tensorflow backend, Keras and TensorBoard server.

## Setting the password
The default password is 'banana'.

You can define a password with the script ```generate_token.py -p S-E-C-R-E-T``` and generate SSL certificates as described below.
```
import IPython as IPython

hash = IPython.lib.passwd("S-E-C-R-E-T")
print(hash)
```

## Control the container:
* ```docker-compose up``` mounts the directory and starts the container
* ```docker-compose build``` builds the container
* ```docker-compose down``` destroys the container

## Code formatting in JupyterLab using Black
Using the [black python code formatter](https://github.com/psf/black) and the jupyterlab_code_formatter plugin code can be formated within the notebooks using the shortcut ctrl + M, L or the 'Format notebook' button in the notbook toolbar.

## Using TensorBoard
TensorBoard expects the training log in the directory '/home/jovyan/logs/'. So a suitable configuration with the notebook could look like:
```
import keras
from keras.callbacks import TensorBoard
from time import time

tensorboard_callback = TensorBoard(log_dir='/home/jovyan/logs/{}'.format(time()), histogram_freq=1)
```

## Loggin into JupyterLab and TensorBoard
After starting the docker-compose stack, you can access the JupyterLab at http://localhost:8888 and TensorBoard at http://localhost:6006.
