"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url


from climate.views import HomePage,user1,zone,types
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage.as_view()),
    url(r'^topic',user1.as_view()),
    url(r'^time',zone.as_view()),
    url(r'^plot',types.as_view())
]

