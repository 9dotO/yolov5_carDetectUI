from django.shortcuts import render
import io
from PIL import Image as im
import torch
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ImageModel
from .forms import ImageUploadForm
from django.conf import settings
import os
import numpy as np

class UploadImage(CreateView):
    model = ImageModel
    template_name = 'car/car_detect.html'
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()

            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))

            # yolov5모델로드
           
            model = torch.hub.load("yolov5", "best", source='local')

            # 객체 감지
            results = model(img, size=640)
            results.render()
            
            detected_classes = [results.names[int(pred[5])] for pred in results.pred[0]]
            confidences = [pred[4] * 100 for pred in results.pred[0]]

            # detected_classes에서 클래스 별로 카운트를 수행
            class_counts = {}
            for detected_class in detected_classes:
                if detected_class in class_counts:
                    class_counts[detected_class] += 1
                else:
                    class_counts[detected_class] = 1

            # 클래스와 해당 클래스의 카운트 출력
            for class_name, count in class_counts.items():
                print(f"Class: {class_name}, Count: {count}")

            # 결과이미지 저장 #########3db연동, 수정해야됨
            result_img = im.fromarray(np.uint8(results.render()[0]))
            result_img.save(os.path.join("static", 'img', 'image0.jpg'), format="JPEG")

            inference_img = "/static/img/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img,
              #  "detected_class": detected_classes,    
              #  "confidences" :  confidences,
                "class_counts": class_counts
            }
            return render(request, 'car/car_detect.html', context)

        else:      
            form = ImageUploadForm()
            context = {
                "form": form
            }
            return render(request, 'car/car_detect.html', context)
