from app.views import home,about,videos,connexion,index,login_in, update, forgot, admin, table
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='a_propos'),
    path('', home, name='home'),
    path('videos/', videos, name='videos'),
    path('connexion/', connexion, name='connexion'),
    path('index/', index, name='index'),
    path('login_in/', login_in, name='login_in'),
    path('update/', update, name='update'),
    path('forgot/', forgot, name='forgot'),
    path('table/', table, name='table')

]
