from django.shortcuts import render
from .main import *
from .models import advice_history
import datetime
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
        
        advice = ""

        if postive_cash_flow > 0:
            if total_savings > 0:
                advice = "You are doing a good job saving money. You can consider investing the money."
                searched = True
            else:
                advice = "You are doing a good job generating positive cash flow. You should start saving money."
                searched = True
        else:
            if total_savings > 0:
                advice = "You should start investing your savings."
                searched = True
            else:
                advice = "You need to find ways to increase your income or reduce your expenses."
                searched = True

        if total_return > 0:
            advice += " You have made a profit. You can consider reinvesting the money."
            searched = True
        else:
            advice += " You have made a loss. You should reconsider your investment strategy."
            searched = True
        
        user = request.user
        created_date = datetime.datetime.now()
    
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