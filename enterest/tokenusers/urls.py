from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.VisitorCreate.as_view(), name="register"),
    path('display/', views.VisitorShowList.as_view(), name="list"),
    path('authorize/', include('rest_auth.urls'))
]
