from django.urls import path,include
from .views import  CompanyView

urlpatterns = [
    #path('UserView/', UserView),
    path('CompanyView', CompanyView.as_view({'get': 'list'}), name='CompanyView')
]
