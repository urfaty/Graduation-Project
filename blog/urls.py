from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "blog-home"),
    path("about/", views.about, name = "blog-about"),
    path('submit_data/', views.submit_data_view, name='submit_data'),
]
