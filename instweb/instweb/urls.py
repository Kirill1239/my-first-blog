from django.contrib import admin
from django.urls import path, re_path, include
from instant import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('success', views.success, name = 'success'),
    re_path(r'^image_upload/$', views.image_view, name='image_upload'),
    #path('hotel_images', display_hotel_images, name = 'hotel_images'),
    re_path(r'^images/$', views.display_images, name='images'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
