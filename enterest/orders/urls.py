from django.urls import  path
from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view()),
    path('display/', views.OrderShowList.as_view()),
    path('display/<int:pk>', views.OrderShowDetailed.as_view()),
    path('manage/<int:pk>', views.OrderManage.as_view()),
]
