from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login 

urlpatterns = [
     # path('', views.index, name='index'),
     path('',views.index, name='index')
     # url(r'^login/$',login,{'template_name':accounts/login.html})
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)