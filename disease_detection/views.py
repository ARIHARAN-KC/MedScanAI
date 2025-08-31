
# Create your views here.
from django.shortcuts import render
from django.conf import settings
import os, json, requests
import cv2
import numpy as np
from .models import ChestDiseaseModel, BrainTumorModel, SkinDiseaseModel, KidneyDiseaseModel
from keras.models import load_model
from .forms import ChestDiseaseForm,BrainTumorForm,SkinDiseaseForm,KidenyDiseaseForm
from io import BytesIO
from PIL import Image 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # store in .env for safety
# from js import FileReader
#loading all the models
chest_model=load_model(os.path.join(settings.BASE_DIR, 'disease_detection/models/chest_model.h5'))
brain_model=load_model(os.path.join(settings.BASE_DIR, 'disease_detection/models/brain_model.h5'))
skin_model=load_model(os.path.join(settings.BASE_DIR, 'disease_detection/models/skin_model.h5'))
kidney_model=load_model(os.path.join(settings.BASE_DIR, 'disease_detection/models/kidney_model.h5'))

# def process(path):
#   img=cv2.imread(path,cv2.IMREAD_COLOR)
# #   print(img)
#   img=cv2.resize(img,(32,32))
  
#   img=np.expand_dims(img,axis=0)
#   return img



def process(image_obj):
    # Read the image data from the uploaded image object
    img_data = image_obj.read()
    nparr = np.frombuffer(img_data, np.uint8)

    # Decode the image data using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Resize the image to the desired size
    img = cv2.resize(img, (32, 32))

    # Add an additional dimension to the image for batching (assuming you're using a CNN)
    img = np.expand_dims(img, axis=0)

    return img

def process_200(image_obj):
    # Read the image data from the uploaded image object
    img_data = image_obj.read()
    nparr = np.frombuffer(img_data, np.uint8)

    # Decode the image data using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Resize the image to the desired size
    img = cv2.resize(img, (200, 200))

    # Add an additional dimension to the image for batching (assuming you're using a CNN)
    img = np.expand_dims(img, axis=0)

    return img




def kideny_disease(pred_list):

  x=np.argmax(pred_list)
  if x==0:
    output="Disease: Cyst"
    
  elif x==1:
    output="Normal"
  elif x==2:
    output="Disease: Stone"
    
  elif x==3:
    output="Disease Tumor"
  return output
def kideny_disease_model_detection(img):
    pred=kidney_model.predict(img)
    output=kideny_disease(pred)
    return output

def chest_disease(pred_list):
  x=np.argmax(pred_list)
  if x==0:
    output='Covid'
  elif x==1:
    output='Pneumonia'
  elif x==2:
    output='Turberculosis'
  elif x==3:
    output='Normal'
  return output
def chest_disease_model_detection(img):
    pred=chest_model.predict(img)
    output=chest_disease(pred)
    return output

def brain_disease(pred_list):
  x=np.argmax(pred_list)
  if x==0:
    output='Tumor Detected'
  elif x==1:
    output='Tumor not detected'
  return output
def brain_disease_model_detection(img):
    pred=brain_model.predict(img)
    output=brain_disease(pred)
    return output

def skin_disease(pred_list):
  x=np.argmax(pred_list)
  if x==0:
    output='Acne'
  elif x==1:
    output='Eczema'
  elif x==2:
    output='Psoriasis'
  return output
def skin_disease_model_detection(img):
    pred=skin_model.predict(img)
    output=skin_disease(pred)
    return output


def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

# def info(request):
#     return render(request, 'info.html')
def info(request):
    # Query all disease models to get the data from the database
    chest_disease_data = ChestDiseaseModel.objects.all()
    brain_tumor_data = BrainTumorModel.objects.all()
    skin_disease_data = SkinDiseaseModel.objects.all()
    kidney_disease_data = KidneyDiseaseModel.objects.all()

    # Pass the query results to the template context
    return render(request, 'info.html', {
        'chest_disease_data': chest_disease_data,
        'brain_tumor_data': brain_tumor_data,
        'skin_disease_data': skin_disease_data,
        'kidney_disease_data': kidney_disease_data,
    })

def detection(request):
    return render(request, 'detection.html')

def chest_disease_detect(request):
    if request.method == 'POST':
        form = ChestDiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image
            image = form.cleaned_data['p_image']


            image=process(image)
            output=chest_disease_model_detection(image)
            # form.p_disease=output
            # form.save()
            instance = form.save(commit=False)  # Do not save to database yet
            instance.p_disease = output
            instance.save()
            

            return render(request, 'chest_disease_detect.html', {
              'form': form, 
              'result': output
              })

    else:
        form = ChestDiseaseForm()

    return render(request, 'chest_disease_detect.html', {'form': form})

# Implement similar views for brain_tumor_detect, skin_disease_detect, and kidney_disease_detect
def skin_disease_detect(request):
    if request.method == 'POST':
        form = SkinDiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image
            image = form.cleaned_data['p_image']
            image=process_200(image)
            output=skin_disease_model_detection(image)
            # form.p_disease=output
            # form.save()
            instance = form.save(commit=False)  # Do not save to database yet
            instance.p_disease = output
            instance.save()


            return render(request, 'skin_disease_detect.html', {'form': form, 'result': output})

    else:
        form = SkinDiseaseForm()

    return render(request, 'skin_disease_detect.html', {'form': form})

# Similar views for skin_disease_detect and kidney_disease_detect
# ...
def brain_tumor_detect(request):
    if request.method == 'POST':
        form = BrainTumorForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image
            image = form.cleaned_data['p_image']
            image=process_200(image)
            output=brain_disease_model_detection(image)
            # form.p_disease=output
            # form.save()
            instance = form.save(commit=False)  # Do not save to database yet
            instance.p_disease = output
            instance.save()


            return render(request, 'brain_tumor_detect.html', {'form': form, 'result': output})

    else:
        form = BrainTumorForm()

    return render(request, 'brain_tumor_detect.html', {'form': form})

def kidney_disease_detect(request):
    if request.method == 'POST':
        form = KidenyDiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded image
            image = form.cleaned_data['p_image']
            image=process(image)
            output=kideny_disease_model_detection(image)
            # form.p_disease=output
            # form.save()
            instance = form.save(commit=False)  # Do not save to database yet
            instance.p_disease = output
            instance.save()

            return render(request, 'kidney_disease_detect.html', {'form': form, 'result': output})

    else:
        form = KidenyDiseaseForm()
    

    return render(request, 'kidney_disease_detect.html', {'form': form})


def chatbot_page(request):
    return render(request, "chatbot.html") 

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "")

        # System prompt to restrict bot answers
        system_prompt = (
            "You are a knowledgeable and reliable medical assistant. "
            "Answer questions strictly about medical and healthcare topics, including diseases, symptoms, treatments, "
            "diagnosis, prevention, medications, anatomy, and healthcare advice. "
            "If a user asks something non-medical (e.g., politics, sports, entertainment, coding), reply: "
            "'I can only answer medical-related questions.'"
        )

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "meta-llama/llama-3.3-70b-instruct:free",  # model loaded from OpenRouter
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message},
                    ],
                },
                timeout=30,
            )

            if response.status_code == 200:
                data = response.json()
                bot_reply = data["choices"][0]["message"]["content"]
            else:
                bot_reply = "Sorry, I am unable to process your request at the moment."

        except Exception as e:
            bot_reply = f"Error: {str(e)}"

        return JsonResponse({"response": bot_reply})

    return JsonResponse({"error": "Invalid request"}, status=400)
