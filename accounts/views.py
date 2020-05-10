from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db.models import Sum
from .models import Account, AccountBalance
from django.db.models import Max
from transfers.models import Transfer
from transactions.models import Transaction
from django.shortcuts import render
from .forms import GetDateForm, AccountForm
from datetime import date
import numpy as np
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy

def index(request):
    total_cash = 0
    template = loader.get_template ('accounts/index.html')
    account_list = AccountBalance.objects.values_list('account__account_name', flat=True).distinct()
    latest_account = []

    for account in account_list:
        latest_account.append(AccountBalance.objects.filter(account__account_name=account).values ('account__account_name', 'balance', 'balance_date').latest('balance_date'))
    print (latest_account)

    for account in latest_account:
        total_cash= account['balance'] + total_cash
    
    print (total_cash)
    context = {
          'latest_account': latest_account,
          'total_cash': total_cash,
       }
    return HttpResponse(template.render(context, request))





class CreateAccount(CreateView):
     template_name = 'accounts/accounts_form.html'
     form_class = AccountForm
     success_url = reverse_lazy('accounts-index') 
     model = Account

     def form_valid(self, form):
        account_name = form.cleaned_data['account_name']
        initial_balance = form.cleaned_data['initial_balance']
        date = form.cleaned_data ['date']
        account_type = form.cleaned_data['account_type']
        balance_description = 'initial'
        self.object = form.save()    
        account_record = Account.objects.filter(account_name=account_name)
        new_record = AccountBalance(account=account_record[0], balance_description = balance_description, balance=initial_balance, balance_date=date)        
        new_record.save() 
        return super().form_valid(form)

class UpdateAccount(UpdateView):
     template_name = 'accounts/accounts_form.html'
     form_class = AccountForm
     success_url = reverse_lazy('accounts-index') 
     model = Account

class DeleteAccount(DeleteView):
     template_name = 'accounts/accounts_delete.html'
     form_class = AccountForm
     success_url = reverse_lazy('account-index') 
     model = Account