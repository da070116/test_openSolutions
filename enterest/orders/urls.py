from django.urls import  path
from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view()),
    path('list/', views.OrderList.as_view()),
    path('detail/<int:pk>', views.OrderDetail.as_view()),
    path('manage/<int:pk>', views.OrderManage.as_view()),
]
