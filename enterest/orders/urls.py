from django.urls import  path
from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name="orders_create"),
    path('display/', views.OrderShowList.as_view(), name="orders_display_all"),
    path('display/<int:pk>', views.OrderShowDetailed.as_view(), name="orders_display_detail"),
    path('manage/<int:pk>', views.OrderManage.as_view(), name="orders_manage"),
]
