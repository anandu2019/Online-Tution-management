from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin



urlpatterns=[
path('',views.home,name="home"),
#path('register',views.register,name="register"),
path('accounts/login/',views.loginview,name="login"),
path('accounts/signup/',views.sign_up,name="sign_up"),
path('logout',views.logoutview,name="logout"),
path('firstpage',views.firstpage,name="firstpage"),
path('adduser',views.adduser,name="adduser"),
path('display',views.display),
path('displaymarks',views.displaymarks,name="displaymarks"),
path('aboutus',views.aboutus,name="aboutus"),
path('fileview',views.fileview,name="fileview"),
path('matplot',views.matplot,name="matplot"),
url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
]
if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)