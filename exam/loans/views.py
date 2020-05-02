from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from loans.models import Lender,Borrow
from django.template import RequestContext
from django.utils import timezone
from loans.forms import RegisterLender, RegisterBorrow
from django.views.generic import TemplateView
from django.db import connection

# Create your views here.

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

class RegisterView(TemplateView):
    template_name = 'loans/RegisterCreate.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'aform': RegisterLender(prefix='aform_pre'), 'bform': RegisterBorrow(prefix='bform_pre')})

    def post(self, request, *args, **kwargs):
        aform = _get_form(request, RegisterLender, 'aform_pre')
        bform = _get_form(request, RegisterBorrow, 'bform_pre')
        if aform.is_bound and aform.is_valid():
            # Process aform and render response
            lender = Lender(First_Name=aform.cleaned_data['First_Name'],
                                Last_Name=aform.cleaned_data['Last_Name'],
                                Email=aform.cleaned_data['Email'],
                                Password=aform.cleaned_data['Password'],
                                Money=aform.cleaned_data['Money'],
                            )
            lender.save()
        elif bform.is_bound and bform.is_valid():
            # Process bform and render response
            borrow = Borrow(First_Name=bform.cleaned_data['First_Name'],
                                Last_Name=bform.cleaned_data['Last_Name'],
                                Email=bform.cleaned_data['Email'],
                                Password=bform.cleaned_data['Password'],
                                Money_Need=bform.cleaned_data['Money_Need'],
                                Subject=bform.cleaned_data['Subject'],
                                Description=bform.cleaned_data['Description'],
                            )
            borrow.save()
        return HttpResponseRedirect('/register/')
   




def Lender_Details(request,id):
    try:
        lender = Lender.objects.get(pk=id)
    except Lender.DoesNotExist:
        raise Http404
    borrows = Borrow.objects.all()
    return render_to_response('loans/lender_detail.html', {'lender':lender , 'borrows':borrows})

def Borrower_Details(request,id):
    try:
        borrow = Borrow.objects.get(pk=id)
    except Borrow.DoesNotExist:
        raise Http404

    cursor  = connection.cursor()
    loans= cursor.execute('select  p.First_Name,p.Email,t.Loans_Money,t.loans_borrow_id from loans_loans as t, loans_lender as p where t.loans_borrow_id =%s and t.loans_lender_id = p.id',[id]).fetchall()
    cursor.close()

    cursor  = connection.cursor()
    total = cursor.execute('select  b.First_Name,sum(l.Loans_Money) from loans_loans as l, loans_borrow as b where b.id = %s and b.id = l.Loans_Lender_id group by b.id, l.Loans_Lender_id',[id]).fetchall()

      
    return render_to_response('loans/borrower_detail.html', {'borrow':borrow , 'loans':loans, 'total':total})