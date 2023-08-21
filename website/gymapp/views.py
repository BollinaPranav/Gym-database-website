from django.shortcuts import render
from gymapp.models import Trainers, Client
from gymapp.forms import TrainersForm, ClientForm
from django.http import HttpResponseRedirect
import pyodbc



def searchclients(request):
    if request.method == "POST":
        searched = request.POST['searched']
        clients = Client.objects.filter(name__contains=searched)
        return render(request, 'searchclients.html', {'searched':searched, 'clients':clients})
    else:
        return render(request, 'searchclients.html', {})


def saverecords(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/saverecords?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'index.html', {'form': form, 'submitted': submitted})


    # conn= pyodbc.connect('DRIVER={Sql Server};'
    #                      'Server=LAPTOP-A134KU3E\MSSQLSERVER01;'
    #                      'Database=mydb;'
    #                      'Trusted_Connection=yes')
    # cursor2 = conn.cursor()
    # cursor2.execute("select * from trainers")
    # result = cursor2.fetchall()
    # if request.method=="POST":
    #     if request.POST.get('name') and request.POST.get('dateofjoining') and request.POST.get('phonenumber') and  request.POST.get('amountdue') and  request.POST.get('trainer') and request.POST.get('clientimage'):
    #         insertclvalues = Client()
    #         insertclvalues.name= request.POST.get('name')
    #         insertclvalues.phonenumber = request.POST.get('phonenumber')
    #         insertclvalues.date = request.POST.get('dateofjoining')
    #         insertclvalues.amount = request.POST.get('amountdue')
    #         insertclvalues.trainer = request.POST.get('trainer')
    #         insertclvalues.clientimage = request.POST.get('clientimage')
    #         cursor=conn.cursor()
    #         cursor.execute("insert into client values('"+insertclvalues.name+"','"+insertclvalues.date+"','"+insertclvalues.phonenumber+"','"+insertclvalues.amount+"','"+insertclvalues.trainer+"')")
    #         cursor.commit()
    #
    #         return render(request,'index.html',{'Trainer':result})
    # else:
    #     return render(request,'index.html',{'Trainer':result})

def home(request):
	return render(request, 'home.html', {})

def connsql(request):
    result = Client.objects.all()
    return render(request, 'clientview.html', {'Client': result})
    # conn = pyodbc.connect('Driver={Sql Server};'
    #                       'Server=LAPTOP-A134KU3E\MSSQLSERVER01;'
    #                       'Database=mydb;'
    #                       'Trusted_Connection=yes'
    #                       )
    #
    # cursor=conn.cursor()
    #
    # cursor.execute("select * from client")
    # result=cursor.fetchall()


def addtrainer(request):
    submitted = False
    if request.method == "POST":
        form = TrainersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addtrainer?submitted=True')
    else:
        form = TrainersForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'trainerindex.html',{'form':form, 'submitted':submitted})
    # conn = pyodbc.connect('DRIVER={Sql Server};'
    #                       'Server=LAPTOP-A134KU3E\MSSQLSERVER01;'
    #                       'Database=mydb;'
    #                       'Trusted_Connection=yes')
    #
    #
    # if request.method == "POST":
    #     if request.POST.get('name') and request.POST.get('address') and request.POST.get('phonenumber') and request.POST.get('email'):
    #         insertclvalues = Trainers()
    #         insertclvalues.name = request.POST.get('name')
    #         insertclvalues.address = request.POST.get('address')
    #         insertclvalues.phonenumber = request.POST.get('phonenumber')
    #         insertclvalues.email = request.POST.get('email')
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             "insert into trainers values('" + insertclvalues.name + "','" + insertclvalues.address + "','" + insertclvalues.phonenumber + "','" + insertclvalues.email + "')")
    #         cursor.commit()
    #         return render(request, 'trainerindex.html')
    #
    # else:
    #     return render(request, 'trainerindex.html')
        # if request.POST.get('name') and request.POST.get('address') and request.POST.get(
        #         'phonenumber') and request.POST.get('email'):


        # form = TrainersForm
        # return render(request, 'trainerindex.html',{'form':form})



def trainerview(request):
    result = Trainers.objects.all()
    return render(request, 'trainerview.html', {'Trainer': result})
    # conn = pyodbc.connect('Driver={Sql Server};'
    #                       'Server=LAPTOP-A134KU3E\MSSQLSERVER01;'
    #                       'Database=mydb;'
    #                       'Trusted_Connection=yes'
    #                       )
    # cursor=conn.cursor()
    # cursor.execute("select * from trainers")
    # result=cursor.fetchall()


def showclient(request, clientid):
    client = Client.objects.get(pk=clientid)
    return render(request, 'clients.html', {'client':client})
