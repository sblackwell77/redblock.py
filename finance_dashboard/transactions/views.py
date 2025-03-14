from django.shortcuts import render
from .models import Transaction, Stock
import requests

# Existing add_transaction function
def add_transaction(request):
    if request.method == 'POST':
        Transaction.objects.create(
            category=request.POST['category'],
            description=request.POST['description'],
            amount=request.POST['amount'],
            date=request.POST['date']
        )
    return render(request, 'transactions/add_transaction.html')

# Existing transaction_list function (if already added)
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

# New stock_prices function
def stock_prices(request):
    stocks = []
    if request.method == 'POST':
        symbol = request.POST['symbol']
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            stocks.append(stock_data)
    return render(request, 'transactions/stock_prices.html', {'stocks': stocks})

# Helper function to fetch stock data from Alpha Vantage API
def fetch_stock_data(symbol):
    api_key = 'your_alpha_vantage_api_key'  # Replace with your API key
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url).json()
    if "Global Quote" in response:
        stock_info = response["Global Quote"]
        return {
            'symbol': stock_info['01. symbol'],
            'price': stock_info['05. price'],
        }
    return None
