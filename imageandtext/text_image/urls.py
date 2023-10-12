# urls.py in your app
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('upload/', views.hadiths, name='haidth'),
    path('mishkat/', views.Mishkat, name='Mishkat'),
    path('tatorial/', views.tatorial_video, name='tatorial'),

    # Define URL for the success page
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

