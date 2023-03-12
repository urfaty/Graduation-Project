from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "blog/home.html")

def about(request):
	return render(request, "blog/about.html")

def submit_data_view(request):
    if request.method == 'POST':
        my_data = request.POST.get('my_data')

        # The input text is input_field.
        # we can send output through context to fronted. 

        context = {
        'message': my_data
        }

        return render(request, 'blog/home.html', context)
    else:
        return render(request, 'blog/about.html')