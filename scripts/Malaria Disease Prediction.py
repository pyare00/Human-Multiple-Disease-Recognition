#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy.random import seed
seed(1)


# In[1]:


import numpy as np 
import pandas as pd
import os 
from pathlib import Path
import cv2
import matplotlib.pyplot as plt 
import os
from PIL import Image
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
from keras.utils import np_utils
from tensorflow.keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,GlobalAveragePooling2D,Activation,BatchNormalization,Dropout
from tensorflow.keras import Sequential,backend,optimizers


# In[4]:


parasitized_data = os.listdir('malaria/cell_images/Parasitized')
uninfected_data = os.listdir('malaria/cell_images/Uninfected/')
data = []
labels = []

for img in parasitized_data:
    try:
        img_read = plt.imread('malaria/cell_images/Parasitized/' + img)
        img_resize = cv2.resize(img_read, (125, 125))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(1)
    except:
        None
        
for img in uninfected_data:
    try:
        img_read = plt.imread('malaria/cell_images/Uninfected/' + img)
        img_resize = cv2.resize(img_read, (125, 125))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(0)
    except:
        None

image_data = np.array(data)
labels = np.array(labels)
print("image_data:",len(image_data))
print("labels:",len(labels))


# In[5]:


print("Parasitized Sample:\n")
plt.figure(figsize = (15,15))
for i in range(3):
    plt.subplot(4, 4, i+1)
    img = cv2.imread('malaria/cell_images/Parasitized/'+ parasitized_data[i])
    plt.imshow(img)
plt.show()

print("Uninfected Sample:\n")
plt.figure(figsize = (15,15))
for i in range(3):
    plt.subplot(4, 4, i+1)
    img = cv2.imread('malaria/cell_images/Uninfected/'+ uninfected_data[i])
    plt.imshow(img)
plt.show()


# In[6]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(image_data, labels, test_size = 0.25,random_state = 0)

print("X_train:",len(X_train))
print("X_test:",len(X_test))
print("y_train:",len(y_train))
print("y_test:",len(y_test))


# In[16]:


import tensorflow as tf
vgg = tf.keras.applications.vgg19.VGG19(include_top=False, weights='imagenet', 
                                        input_shape=(125,125,3))
# Freeze the layers
vgg.trainable = True

set_trainable = False
for layer in vgg.layers:
    if layer.name in ['block5_conv1', 'block4_conv1']:
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False
    
base_vgg = vgg
base_out = base_vgg.output
pool_out = tf.keras.layers.Flatten()(base_out)
hidden1 = tf.keras.layers.Dense(512, activation='relu')(pool_out)
drop1 = tf.keras.layers.Dropout(rate=0.3)(hidden1)
hidden2 = tf.keras.layers.Dense(512, activation='relu')(drop1)
drop2 = tf.keras.layers.Dropout(rate=0.3)(hidden2)

out = tf.keras.layers.Dense(1, activation='sigmoid')(drop2)

vgg_model = tf.keras.Model(inputs=base_vgg.input, outputs=out)
vgg_model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=1e-5),
                loss='binary_crossentropy',
                metrics=['accuracy'])

print("Total Layers:", len(vgg_model.layers))
print("Total trainable layers:", sum([1 for l in vgg_model.layers if l.trainable]))


# In[17]:


vgg_model.fit(X_train, y_train, epochs = 10, batch_size = 32)


# In[18]:


y_pred=vgg_model.predict(X_test)


# In[19]:


y_pred=y_pred.flatten().round()
y_pred


# In[20]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[22]:


vgg_model.save('malaria_vggModel.h5')

