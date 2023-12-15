from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Loan, Item
from django.shortcuts import redirect
from datetime import datetime

u = ""
def login(request, s):
    u = s
    item = get_object_or_404(Item, pk=s) 
    print(item)
    context = {
        "itemstate": item.item_state,
        "S":s,
        
    }
    print("hufhdhifosdjfijsijfijsijgisjgisjigj")
    print(item.item_state)

   
    
    if 'btn' in request.POST:
        item_id = request.POST["los-1"]  # Replace 'item_id' with the actual field name from your form
        student_id = "user"  # Assuming the logged-in user is the student
        date_of_loan = datetime.now()
        loan_due_date = request.POST[datetime.now]  # Replace 'loan_due_date' with the actual field name from your form
        loan_is_finished = False

        # Create a new Loan object
        loan = Loan.objects.create(
            item_id=Item.objects.get(pk=item_id),
            student_id=student_id,
            date_of_loan=date_of_loan,
            loan_due_date=loan_due_date,
            loan_is_finished=loan_is_finished,
        )
        return render(request, "rent/approved.html")


    if (item.item_state == 0):
        return render(request, 'rent/loan.html', context)
    else:
        return render(request, 'rent/decline.html', context)

    


    