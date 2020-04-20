from django.urls import path
#similar to router in express.
from . import views
from products.views import View
#empty path means all urls
#views.functions are defined in views.py
#and views are like controllers in python
urlpatterns = [
    path('' , views.home , name='home'),
    path('getAllProds',views.getAllProducts),
    path('addProduct',views.addProduct),
    path('getProduct',views.getProduct)

]
