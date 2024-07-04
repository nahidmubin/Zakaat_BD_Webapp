from django.shortcuts import render
from .forms import Zakaatform
import requests
from bs4 import  BeautifulSoup


def home(request, snippet='no'):
    try:
        buying_price, selling_price = get_gold_silver_price()
    except:
        buying_price, selling_price = fetch_false_data()
        
    threshold_price = calc_threshold_price(selling_price)
    if 'snippet' in request.GET and request.GET['snippet'] == 'yes':
        snippet = request.GET['snippet']
        template = 'home_snippet'
    else:
        template = 'home'
    
    return render(request, f'zakaat_calculator/{template}.html', {'buying_price': buying_price, 'selling_price': selling_price, 'threshold_price': threshold_price, 'snippet':snippet})


def get_gold_silver_price():
    # Extracting Gold and Silver prices from Bangladesh Juwellers's Association (BAJUS)
    BAJUS_URL = "https://www.bajus.org/gold-price"
    r = requests.get(BAJUS_URL)
    soup = BeautifulSoup(r.content, features='html.parser')
    gold_silver_type = ['24K_G', '22K_G', '21K_G', '18K_G', 'Traditional_G', '24K_S', '22K_S', '21K_S', '18K_S', 'Traditional_S']
    
    gold_silver_rawprice = soup.find_all('span', attrs={'class':'price'})
    gold_silver_price = []
    for row in gold_silver_rawprice:
        price, _ = row.text.split(' ')
        if ',' in price:
            price = price.replace(',', '')
        gold_silver_price.append(float(price))

    gold24k = gold_silver_price[0] * (24/22)
    silver24k = gold_silver_price[4] * (24/22)
    
    gold_silver_price.insert(0, gold24k)
    gold_silver_price.insert(5, silver24k)
    
    buying_price = {gold_silver_type[i] : gold_silver_price[i] for i in range(len(gold_silver_type))}

    # Extrapolated Price of 24 Karat Gold and Silver
    buying_price['24K_G'] = buying_price['22K_G'] * (24/22)
    buying_price['24K_S'] = buying_price['22K_S'] * (24/22)

    # Selling Price is 20% less than the buying price
    selling_price = {price : round(buying_price[price] * 0.8) for price in buying_price}
    
    return buying_price, selling_price

def fetch_false_data():
    gold_silver_type = ['24K_G', '22K_G', '21K_G', '18K_G', 'Traditional_G', '24K_S', '22K_S', '21K_S', '18K_S', 'Traditional_S']
    buying_price = {gold_silver_type[i] : 0 for i in range(len(gold_silver_type))}
    selling_price = {gold_silver_type[i] : 0 for i in range(len(gold_silver_type))}
    
    return buying_price, selling_price


def calc_threshold_price(gold_silver_price):
    GOLD_THRESHOLD_GM = 85
    SILVER_THERSHOLD_GM = 595

    gold_threshold_price = GOLD_THRESHOLD_GM * gold_silver_price['24K_G']
    silver_threshold_price = SILVER_THERSHOLD_GM * gold_silver_price['24K_S']

    return round(min(gold_threshold_price, silver_threshold_price))

def calc_net_asset(zakaat_data, selling_price):
    total_gold_silver = (((zakaat_data['gold_22k_gram'] + 11.664 * zakaat_data['gold_22k_vori']) * selling_price['22K_G'])
                            + ((zakaat_data['gold_21k_gram'] + 11.664 * zakaat_data['gold_21k_vori']) * selling_price['21K_G'])
                            + ((zakaat_data['gold_18k_gram'] + 11.664 * zakaat_data['gold_18k_vori']) * selling_price['18K_G'])
                            + ((zakaat_data['gold_trad_gram'] + 11.664 * zakaat_data['gold_trad_vori']) * selling_price['Traditional_G'])
                            + ((zakaat_data['silver_22k_gram'] + 11.664 * zakaat_data['silver_22k_vori']) * selling_price['22K_S'])
                            + ((zakaat_data['silver_21k_gram'] + 11.664 * zakaat_data['silver_21k_vori']) * selling_price['21K_S'])
                            + ((zakaat_data['silver_18k_gram'] + 11.664 * zakaat_data['silver_18k_vori']) * selling_price['18K_S'])
                            + ((zakaat_data['silver_trad_gram'] + 11.664 * zakaat_data['silver_trad_vori']) * selling_price['Traditional_S']))
    
    total_liquid_money = zakaat_data['cash'] + zakaat_data['bank_balance'] + zakaat_data['liquid_money']
    total_business_asset = zakaat_data['business_asset'] + zakaat_data['stock']
    total_debt = zakaat_data['debt']
                
    net_asset = total_gold_silver + total_liquid_money + total_business_asset - total_debt
    
    return net_asset


def calculate_zakaat(request):
    if request.method == 'POST':
        form = Zakaatform(request.POST)
        if form.is_valid():
            zakaat_data = form.cleaned_data
            try:
                _ , selling_price = get_gold_silver_price()
                            
            except:
                _ , selling_price = fetch_false_data()
                
            net_asset = calc_net_asset(zakaat_data, selling_price)
            threshold_price = calc_threshold_price(selling_price)  

            
            return render(request, 'zakaat_calculator/zakaat_result.html', {'net_asset':net_asset, 'threshold_price':threshold_price})
            
        return render(request, 'zakaat_calculator/zakaat_form.html', {'form':form, 'invalid': True})
    form = Zakaatform()
    return render(request, 'zakaat_calculator/zakaat_form.html', {'form':form})

def about(request):
    return render(request, 'zakaat_calculator/about.html')