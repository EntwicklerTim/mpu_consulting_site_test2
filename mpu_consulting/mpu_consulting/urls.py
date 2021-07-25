"""mpu_consulting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('Thank.html', views.thank, name="Thank"),
    path('Preise', views.preise, name="preise"),
    path('Der_Berater', views.berater, name="Der_Berater"),
    path('Die_Beratung', views.bertung, name="Die_Beratung"),
    path('Impressum', views.Impressum, name="Impressum"),
    path('Datenschutz', views.Datenschutz, name="Datenschutz"),
    path('AGB', views.AGB, name="AGB"),
    path('Widerrufsbelehrung', views.Widerrufsbelehrung, name="Widerrufsbelehrung"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  #statische hintendran hängen sonst problem

