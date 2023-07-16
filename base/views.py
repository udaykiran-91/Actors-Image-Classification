from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.

from . utils import get_cropped_image_if_2_eyes,combined_image_function

import cv2
import os
import numpy as np
import joblib
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pkldir=os.path.join(BASE_DIR, 'model/saved_model.pkl')
jsondir = os.path.join(BASE_DIR, 'model/class_dictionary.json')

def home(request):
    return render(request,"base/home.html")

def uploadedPic(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        imgpath = os.path.join(BASE_DIR,'static/uploaded_images',name)
        

        image_cv = get_cropped_image_if_2_eyes(imgpath)
        
        combined_image = combined_image_function(image_cv)

        if len(combined_image)<1:
            messages.info(request,"Sorry,No Face has been detected. Please choose an Image with Two clear eyes.")
            return redirect('home')
        
        if len(combined_image)>=2:
            messages.info(request,"More than One Image has been detected. Classifies into one of the actors below who are more similar to them.")

        

        predicted_percentages = classify_image(combined_image)
        

        #finding max from percentages and names
        names_list = []
        for i in predicted_percentages :
            final_output = np.argmax(i)
            names_of_numbers = load_saved_artifacts(final_output)
            names_list.append(names_of_numbers)
        
        #rounding off the percentages
        final_percentage_array = []
        predicted_percentages = np.array(predicted_percentages)
        for percentages_list in predicted_percentages:
            percentages_list = np.around(percentages_list*100,2)
            final_percentage_array.append(percentages_list)
       
        
        winner = names_list
        
      
        perc = '%'

        zipped_data = zip(winner, final_percentage_array)

    return render(request,"base/home.html",{'zipped_data':zipped_data,'name':name,'perc':perc,'y_predicted':names_list})





def load_saved_artifacts(i):
    with open(jsondir,"r") as f:
        __class_name_in_number = json.load(f)
        for name, number in __class_name_in_number.items():
            if number == i:
                return name
            
def classify_image(combined_image):
    __model = None
    if __model is None:
        with open(pkldir, 'rb') as f:
            __model = joblib.load(f)

    predicted_percentages = __model.predict(combined_image)
    print(predicted_percentages)
    return predicted_percentages

    

    