from django.urls import path

from shops import apps
from shops import views


app_name = apps.ShopsConfig.name

urlpatterns = [
    path('', views.MapTemplateView.as_view(), name='map'),
    path('points/', views.PointListView.as_view(), name='points'),
    path('new-shop/', views.NewShopFormView.as_view(), name='new-shop'),
]
