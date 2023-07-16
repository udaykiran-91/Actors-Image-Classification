import cv2
import os 


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_to_crop = r"C:\Users\varun\Desktop\uk\Projects\Image Classification\model\Testing dataset\z_combined_images\count"





face_path = os.path.join(BASE_DIR,"opencv/haarcascades/haarcascade_frontalface_default.xml")
eyes_path = os.path.join(BASE_DIR,"./opencv/haarcascades/haarcascade_eye.xml")


face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eyes_path)

def get_cropped_image_if_2_eyes(image_path):
    list=[]
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes)>=2:
                list.append(roi_color)
        return list
    except:
        pass


import pywt
import numpy as np

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255;
    # compute coefficients 
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)  
    coeffs_H[0] *= 0;  

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)

    return imArray_H



def gray_to_rgb_convertor(gray_image):

# Assuming you have a single gray image called gray_image
# with shape (height, width)

# Create an empty array to store the RGB image
    height, width = gray_image.shape
    rgb_image = np.empty((height, width, 3), dtype=np.uint8)

# Assign the gray intensity values to all three color channels
    rgb_image[..., 0] = gray_image
    rgb_image[..., 1] = gray_image
    rgb_image[..., 2] = gray_image

    return rgb_image


def combined_image_function(image_cv):
    final_array = []
        
    count = 0
    for each_img in image_cv:
        img_har = w2d(each_img,'db1',5)
        scaled_raw_img = cv2.resize(each_img,(128,128))
        scaled_img_har = cv2.resize(img_har,(128,128))
        scaled_rgb_img_har = gray_to_rgb_convertor(scaled_img_har)
        combined_img = np.vstack((scaled_raw_img,scaled_rgb_img_har))
        combined_image_scaled = combined_img/255
        combined_image_scaled = np.array(combined_image_scaled)
        final_array.append(combined_image_scaled)

        # combined_image_scaled = combined_image_scaled.reshape(count,256,128,3)

        
        path_to_image = path_to_crop+str(count) + ".png"
        cv2.imwrite(path_to_image,combined_img)
        count +=1
    final_array = np.array(final_array)
    return final_array