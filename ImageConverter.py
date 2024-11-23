import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageTk


class ImageConverter:

    def is_numpy_array(obj):
        return isinstance(obj, np.ndarray)

    def is_pil_image(obj):
        return isinstance(obj, Image.Image)
    
    @staticmethod
    def toPIL(img):
        if ImageConverter.is_numpy_array(img):
            return Image.fromarray(img)
        else:
            return img

    @staticmethod
    def toNumpy(img):
        if ImageConverter.is_numpy_array(img) == False:
            return np.array(img)
        else:
            return img
    
    @staticmethod
    def toPhotoImage(img):
        img = ImageConverter.toPIL(img)
        return ImageTk.PhotoImage(image=img)
        

    
