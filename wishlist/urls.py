"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from wishlistapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

    path('home/',views.home,name='home'),
    path('wish/list/',views.list,name='list'),
    path('wish/create',views.wish_create,name='wish_create'),
    path('user/list/',views.user_list,name='user-list'),
    path('user/discover/',views.discover,name='user-discover'),

    #path('wish/<int:wish_id>/delete/',views.wish_delete ,name='wish-delete'),


#    path('user/create_list',views.create_list,name='create-list'),



]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
