from django.shortcuts import render,redirect
from  .models import Expence,ExpenceForm
# Create your views here.
from django.contrib.auth.models import User
def expence_view(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        # f=ExpenceForm(request.POST)
        expence=request.POST.get('expence')
        expence_type=request.POST.get('expence_type')
        expence_date=request.POST.get('expence_date')
        description=request.POST.get('description')
        exp=Expence()
        exp.expence=expence
        exp.expence_type=expence_type
        exp.expence_date=expence_date
        exp.description=description
        exp.user=User.objects.get(id=uid)
        exp.save()

        return redirect('/')
    else:
        f=ExpenceForm
        context={'form':f}        
        return render(request,'add_expence.html',context)
    
def exp_list(request):
    # uid=request.session.get('uid')
    # # expl=Expence.objects.all()
    # expl=Expence.objects.filter(user=uid)
    # context={'expl':expl}
    # return render(request,'expencelist.html',context)

    uid=request.session.get('uid')
    # expl=Expence.objects.all()
    expl=Expence.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expence_type)
    context={'expl':expl,'expt':expt}
    return render(request,'expencelist.html',context)

def delete_exp(request,expid):
    exp1=Expence.objects.get(id=expid)
    exp1.delete()
    return redirect('/')

def edit_exp(request,expid):
    exp=Expence.objects.get(id=expid)
    if request.method=='POST':
        f=ExpenceForm(request.POST,instance=exp)
        f.save()
        return redirect('/')
    else:
        f=ExpenceForm(instance=exp)
        context={'form':f}        
        return render(request,'add_expence.html',context)
    
def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    expl=Expence.objects.filter(user=uid,description__contains=srch)
    context={'expl':expl}
    return render(request,'expencelist.html',context)

def sort_by_expence_type(request,ext2):
    uid=request.session.get('uid')
    # expl=Expence.objects.all()
    expl=Expence.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expence_type)
        expl=Expence.objects.filter(user=uid,expence_type=ext2)
    context={'expl':expl,'expt':expt}
    return render(request,'expencelist.html',context)