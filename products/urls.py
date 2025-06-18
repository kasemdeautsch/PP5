
from django.urls import path
from . import views

urlpatterns = [

    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]

# import os

#os.environ.setdefault("SECRET_KEY", "lp0|>i)]*H<F6q-xnAji:Rb?S(J)Po=hNEmVh1Bn9}FpFKS[k)jUcXE(2tPj/O*")

#os.environ.setdefault('STRIPE_PUBLIC_KEY', 'pk_test_51RZUB0PSaDnciGD0sUTsZISSLTIr3pNb1G2ZtjKtPXSpa9Eoza#9Lspk2QtJrGcqOx3JGUuHR3326RJcOX63ScIBl00cpDtnMhw')
#os.environ.setdefault('STRIPE_SECRET_KEY', 'sk_test_51RZUB0PSaDnciGD0zP7nMYiaK7IhzqaXwkyXfwPN2XqBpEvdlwKuImqygnQePGoKhFfjfDQhAHqF0oRVsIfGMkaF00I2FiojD4')

