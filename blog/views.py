from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os


def home(request):
	return render(request, "blog/home.html")

def about(request):
	return render(request, "blog/about.html")

def submit_data_view(request):
    if request.method == 'POST':
        my_data = request.POST.get('my_data')

        # The input text is input_field.
        # we can send output through context to fronted. 
        print('Hello, world!')

        # image_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'blog', 'static', 'images')
        # image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith('.jpg')]
        # Do something with the list of image paths



        image_dir = os.path.join(settings.BASE_DIR, 'blog', 'static', 'images')
        image_paths = [os.path.join('/static/images', f) for f in os.listdir(image_dir) if f.endswith('.jpg')]
        
        context = {'image_paths': image_paths}

        context = {
        'image_paths': image_paths
        }



        image_path = '/static/images/image6.jpg'
   
        # context = {
        # 'message': image_paths
        # }

   



        return render(request, 'blog/home.html', context)
    else:
        return render(request, 'blog/about.html')