"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import math
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rectangle_area(request):
    
    try:
        height = int(request.GET.get('height'))
        width = int(request.GET.get('width'))
        area = height * width
        response = HttpResponse(f"<p>area is equal to {area}")
        return response
    except:
        response = HttpResponse()
        response.status_code = 400
        return response

def rectangle_perimeter(request, height, width):
    perimeter = (height*2) + (width*2)
    response = HttpResponse(f"<p>perimeter is equal to {perimeter}")
    return response

def circle_area(request, radius):
    area = round(math.pi * (radius ** 2))
    response = HttpResponse(f"<p>area is equal to {area}")
    return response

def circle_perimeter(request, radius):
    perimeter = round(2 * math.pi * radius)
    response = HttpResponse(f"<p>perimeter is equal to {perimeter}")
    return response

urlpatterns = [
    path('rectangle/area', rectangle_area),
    # path('rectangle/area/<int:height>/<int:width>', rectangle_area),
    path('rectangle/perimeter', rectangle_perimeter),
    path('rectangle/perimeter/<int:height>/<int:width>', rectangle_perimeter),
    path('circle/area', circle_area),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter', circle_perimeter),
    path('circle/perimeter/<int:radius>', circle_perimeter),
    path('admin/', admin.site.urls),
]
