from django.shortcuts import render, redirect,get_object_or_404
from .forms import ExpenseForm
from .models import Expense

def request(request):
    form = ExpenseForm()
    all_expenses = Expense.objects.all()
    
    if request.method == 'POST':
        amount = request.POST.get('amt', None)
        date = request.POST.get('dat', None)
        category = request.POST.get('cat', None)

        if amount and date and category:
            Expense.objects.create(
                amount=amount,
                date=date,
                category=category
            )  
    
    return render(request, 'home.html', {'form': form, 'all': all_expenses})

def delete_exp(request, expense_id):
    expense= get_object_or_404(Expense,id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('request')
    return render(request, 'delete.html', {'expense': expense})