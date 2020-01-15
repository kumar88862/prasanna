from django.shortcuts import render
from projectapp.models import Student_Info
from projectapp.forms import StudentForm,Delete
# Create your views here.
def index_view(request):
    return render(request,'html/index.html')

def Student_Form(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        f=404
        if form.is_valid():
            t=form.cleaned_data['telugu']
            h=form.cleaned_data['hindi']
            e=form.cleaned_data['english']
            ma=form.cleaned_data['maths']
            sc=form.cleaned_data['science']
            so=form.cleaned_data['social']
            name=form.cleaned_data['name']
            roll=form.cleaned_data['rollno']
            total=t+h+e+ma+sc+so
            list=[t,h,e,ma,sc,so]
            per=format(total*100/600,'.2f')
            g=format(gpa(list),'.2f')
            m=Student_Info(name=name,rollno=roll,telugu=t,hindi=h,english=e,maths=ma,science=sc,social=so,total=total,gpa=g,per=per)
            m.save()
            f={'name':name,'roll':roll,'telugu':t,'hindi':h,'english':e,'maths':ma,'science':sc,'social':so,'total':total,'gpa':g,'per':per}
            if f==404:
                pass
            else:
                return preview(request,f)
    return render(request,'html/input.html',{'form':form})

def Student_display(request):
    list=Student_Info.objects.all()
    return render(request,'html/display.html',{'list':list})

def delete(request):
    form=Delete()
    if request.method=='POST':
        form=Delete(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            a=Student_Info.objects.filter(name=name).delete()
            if a[1]['projectapp.Student_Info'] ==0:
                return render(request,'html/error1.html',{'name':name})
            else:
                return render(request,'html/error.html',{'name':name})
    return render(request,'html/delete.html',{'form':form})

def preview(request,form):
    return render(request,'html/preview.html',{'form':form})

def rank(request):
    list=Student_Info.objects.order_by('per').reverse()
    return render(request,'html/rank.html',{'list':list})


def gpa(l):
    sum=0
    for i in l:
        sum=sum+gpacal(i)
    return sum/6

def gpacal(num):
    if num<=100 and num >90:
        return 10
    elif num<=90 and num >80:
        return 9
    elif num<=80 and num >70:
        return 8
    elif num<=70 and num >60:
        return 7
    elif num<=60 and num >50:
        return 6
    elif num<=50 and num>40:
        return 5
    elif num<=40 and num>30:
        return 4
