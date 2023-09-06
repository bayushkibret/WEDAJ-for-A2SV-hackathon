from django.shortcuts import render
from .main import *
from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import get_client_ip
from .models import advice_history
import datetime
from .ai import ai
# Create your views here.
def home(request):
    user = request.user
    history = advice_history.objects.filter(user__exact = user)
    return render(request, 'index.html', {'histories':history})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def give_me_advice(request):
    if request.method == 'POST':
        total_income = request.POST['total_income']
        total_income = int(total_income)
        total_expenditures = request.POST['total_expenditures']
        total_expenditures = int(total_expenditures)
        simple_interest_earned = request.POST['simple_interest_earned']
        simple_interest_earned = int(simple_interest_earned)
        result = calculate_financial_data(total_income, total_expenditures, simple_interest_earned)
        postive_cash_flow = result['postive_cash_flow']
        total_savings = result['total_savings']
        total_return = result['total_return']
        user = request.user
        ip_address = get_client_ip(request)
        geoip = GeoIP2('GeoLite2-Country.mmdb')
        country = geoip.country(ip_address)
        country = geoip.country_name(country)
        created_date = datetime.datetime.now()

        advice = ai(postive_cash_flow=postive_cash_flow, total_return=total_return, total_savings=total_savings, user=user, country=country)
        advice = str(advice)
        commit = advice_history(user = user, 
                            postive_cash_flow = postive_cash_flow,
                            total_savings = total_savings,
                            total_return = total_return,
                            total_income = total_income,
                            total_expenditure = total_expenditures,
                            simple_interest_earned = simple_interest_earned,
                            advice = advice,
                            created_date = created_date)
            
        commit.save()
        searched = True
        history = advice_history.objects.filter(user__exact = user)

        return render(request, 'index.html', 
                        {'postive_cash_flow':postive_cash_flow,
                            'total_savings':total_savings,
                            'total_return':total_return, 
                            'searched':searched,
                            'main_advice':advice,
                            'histories': history 
                            })
    else:
        return render(request, 'index.html', {'histories':history})