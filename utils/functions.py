import cv2   
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 
 
class Functions:
    def conf_plot(self, matrix):
        sns.heatmap(matrix, annot=True, cmap="Blues", square=True,
                xticklabels=np.arange(10), yticklabels=np.arange(10), linewidths=0.5, linecolor='black')
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.title('Confusion Matrix')

    def conv_binary(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY) 
        out_image = cv2.bitwise_not(binary_image) 
        return cv2.resize(out_image, (28, 28))      
    
    def loss_plot(self, history):
        plt.plot(history['loss'], color='red', label='Train')  
        plt.plot(history['val_loss'], color='blue', label='Validation') 
        plt.title('Loss vs iterarion') 
        plt.xlabel('iter.') 
        plt.legend()

    def split_digits(self, image, bordersize):
        _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])
        digit_images = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            digit_region = image[y:y+h, x:x+w]  
            border_size = bordersize
            digit_region = 255 * np.ones((h + 2 * border_size, w + 2 * border_size), dtype=np.uint8)
            digit_region[border_size:border_size + h, border_size:border_size + w] = image[y:y+h, x:x+w]
            _, digit_region = cv2.threshold(digit_region, 100, 255, cv2.THRESH_BINARY)
            digit_region = cv2.bitwise_not(digit_region)
            digit_region_resized = cv2.resize(digit_region, (28, 28))
            digit_images.append(digit_region_resized) 
        return digit_images    


