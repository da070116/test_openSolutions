from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.VisitorCreate.as_view(), name="register"),
    path('list/', views.VisitorListView.as_view(), name="list"),
    path('auth/', include('rest_auth.urls'))
]
