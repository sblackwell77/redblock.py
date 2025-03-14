from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),  # List transactions
    path('add/', views.add_transaction, name='add_transaction'),  # Add transaction
    path('stocks/', views.stock_prices, name='stock_prices'),  # Stock prices
]

