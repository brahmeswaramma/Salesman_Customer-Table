from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

def display_salesman(request):
    SQLO=Salesman.objects.all()
   # SQLO=Salesman.objects.order_by('name')
   # SQLO=Salesman.objects.order_by('-name')
   # SQLO=Salesman.objects.order_by(Length('name'))
   # SQLO=Salesman.objects.filter('name').order_by(Length('name').desc())
   # SQLO=Salesman.objects.exclude(city='London')
   # SQLO=Salesman.objects.filter(salesman_no__gt=5065).order_by('name')
   # SQLO=Salesman.objects.filter(name='Sindhu').order_by('name')
    
    d={'data1':SQLO}
    return render(request,'display_salesman.html',context=d)
    


def display_customer(request):
    CQLO=Customer.objects.all()
    #CQLO=Customer.objects.filter(salesman_no__gt=6000)
    #CQLO=Customer.objects.filter(salesman_no__gte=5005)
    #CQLO=Customer.objects.filter(salesman_no__lt=5746)
    #CQLO=Customer.objects.filter(salesman_no__lte=4350)
    #CQLO=Customer.objects.filter(salesman_no__month=12)
    #CQLO=Customer.objects.filter(cus_name__startswith='b')
    #CQLO=Customer.objects.filter(cus_name__endswith='o')
    #CQLO=Customer.objects.filter(cus_name__in=['B','P'])
    #CQLO=Customer.objects.filter(cus_name__contains='B')
    #CQLO=Customer.objects.order_by('cus_name')[2::2]
    #CQLO=Customer.objects.filter(cus_name__startswith='S',city__endswith='n')
    #CQLO=Customer.objects.filter((Q(cus_name__startswith='N'))&(Q(grade=100)))
    #CQLO=Customer.objects.filter(Q(customer_no__lt=4000)|Q(grade=100)).order_by('cus_name')[1:8:2]
    #CQLO=Customer.objects.filter(salesman_no__gt=5630)
    #///////CQLO=Customer.objects.filter(cus_name='Karuna').update(grade=500)===>> we can't store update method in CQLO

    d={'data2':CQLO}
    return render(request,'display_customer.html',context=d)


def insert_salesman(request):
    s_no=int(input('enter no'))
    n=input('enter name')
    c=input('enter city')
    comm=input('enter commission')
    SO=Salesman.objects.get_or_create(salesman_no=s_no,name=n,city=c,commission=comm)[0]
    SO.save()
    return HttpResponse('A salesman data is created')

def insert_customer(request):
    c_no=int(input('enter cus_num'))
    c_n=input('enter name')
    c=input('enter city')
    g=input('enter grade')
    sm_no=input('enter salesman_no')
    e=input('enter email')
    so=Salesman.objects.get(salesman_no=sm_no)
    so.save()
    CO=Customer.objects.get_or_create(customer_no=c_no,cus_name=c_n,city=c,grade=g,salesman_no=so,email=e)[0]
    CO.save()

    return HttpResponse('A customer data is created')



