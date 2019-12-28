from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ml import views

router = routers.DefaultRouter()
router.register(r'results', views.ResultView, 'result')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('results/', views.foobar),
]
