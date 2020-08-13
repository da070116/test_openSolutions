from django.urls import include, path

urlpatterns = [

    path('', include('tokenusers.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
