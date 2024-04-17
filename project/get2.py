import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.utils import img_to_array

def predict(path):

    img = plt.imread(path)
    img_resize = cv2.resize(img, (125, 125))
    input_img = img_to_array(img_resize)
    input_img = input_img.reshape((1,) + input_img.shape)
    
    model = load_model('malaria_vggModel.h5')
    prediction = model.predict(input_img)
    prediction = prediction.round()[0]

    return int(prediction)
        

    
    
