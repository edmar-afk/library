from django.shortcuts import render, redirect
from .models import Respondents
from django.contrib import messages
import requests
# Create your views here.


def homepage(request):
    bsit1 = Respondents.objects.filter(course='BSIT', year_level='1st Year').count()
    bsit2 = Respondents.objects.filter(course='BSIT', year_level='2nd Year').count()
    bsit3 = Respondents.objects.filter(course='BSIT', year_level='3rd Year').count()
    bsit4 = Respondents.objects.filter(course='BSIT', year_level='4th Year').count()
    
    bsce1 = Respondents.objects.filter(course='BSCE', year_level='1st Year').count()
    bsce2 = Respondents.objects.filter(course='BSCE', year_level='2nd Year').count()
    bsce3 = Respondents.objects.filter(course='BSCE', year_level='3rd Year').count()
    bsce4 = Respondents.objects.filter(course='BSCE', year_level='4th Year').count()
    
    bapols1 = Respondents.objects.filter(course='BaPOLS', year_level='1st Year').count()
    bapols2 = Respondents.objects.filter(course='BaPOLS', year_level='2nd Year').count()
    bapols3 = Respondents.objects.filter(course='BaPOLS', year_level='3rd Year').count()
    bapols4 = Respondents.objects.filter(course='BaPOLS', year_level='4th Year').count()
    
    beed1 = Respondents.objects.filter(course='BEED', year_level='1st Year').count()
    beed2 = Respondents.objects.filter(course='BEED', year_level='2nd Year').count()
    beed3 = Respondents.objects.filter(course='BEED', year_level='3rd Year').count()
    beed4 = Respondents.objects.filter(course='BEED', year_level='4th Year').count()
    
    bsed1 = Respondents.objects.filter(course='BSED', year_level='1st Year').count()
    bsed2 = Respondents.objects.filter(course='BSED', year_level='2nd Year').count()
    bsed3 = Respondents.objects.filter(course='BSED', year_level='3rd Year').count()
    bsed4 = Respondents.objects.filter(course='BSED', year_level='4th Year').count()
    
    abpolsci1 = Respondents.objects.filter(course='AB Polsci', year_level='1st Year').count()
    abpolsci2 = Respondents.objects.filter(course='AB Polsci', year_level='2nd Year').count()
    abpolsci3 = Respondents.objects.filter(course='AB Polsci', year_level='3rd Year').count()
    abpolsci4 = Respondents.objects.filter(course='AB Polsci', year_level='4th Year').count()
    
    
    bsmath1 = Respondents.objects.filter(course='BS MATH', year_level='1st Year').count()
    bsmath2 = Respondents.objects.filter(course='BS MATH', year_level='2nd Year').count()
    bsmath3 = Respondents.objects.filter(course='BS MATH', year_level='3rd Year').count()
    bsmath4 = Respondents.objects.filter(course='BS MATH', year_level='4th Year').count()
    
    socialwork1 = Respondents.objects.filter(course='Social Work', year_level='1st Year').count()
    socialwork2 = Respondents.objects.filter(course='Social Work', year_level='2nd Year').count()
    socialwork3 = Respondents.objects.filter(course='Social Work', year_level='3rd Year').count()
    socialwork4 = Respondents.objects.filter(course='Social Work', year_level='4th Year').count()
    
    bsit = Respondents.objects.filter(course='BSIT').count()
    bsed = Respondents.objects.filter(course='BSED').count()
    bsce = Respondents.objects.filter(course='BSCE').count()
    beed = Respondents.objects.filter(course='BEED').count()
    bsmath = Respondents.objects.filter(course='BS MATH').count()
    socialwork = Respondents.objects.filter(course='Social Work').count()
    polsci = Respondents.objects.filter(course='AB Polsci').count()
    bapols = Respondents.objects.filter(course='BaPOLS').count()
    
    if request.method == 'POST':
        course = request.POST['course']
        year = request.POST['year']
        sex = request.POST['sex']
        dept = request.POST['department']
        
        add_respondent = Respondents(course=course, year_level=year, sex=sex, dept=dept)
        add_respondent.save()
        messages.success(request, "Successfully Added!")
        return redirect("home")
      
    context = {
        'bsit1' : bsit1,
        'bsit2' : bsit2,
        'bsit3' : bsit3,
        'bsit4' : bsit4,
        
        'bsce1' : bsce1,
        'bsce2' : bsce2,
        'bsce3' : bsce3,
        'bsce4' : bsce4,
        
        'bapols1' : bapols1,
        'bapols2' : bapols2,
        'bapols3' : bapols3,
        'bapols4' : bapols4,
        
        'beed1' : beed1,
        'beed2' : beed2,
        'beed3' : beed3,
        'beed4' : beed4,
        
        'bsed1' : bsed1,
        'bsed2' : bsed2,
        'bsed3' : bsed3,
        'bsed4' : bsed4,
        
        'abpolsci1' : abpolsci1,
        'abpolsci2' : abpolsci2,
        'abpolsci3' : abpolsci3,
        'abpolsci4' : abpolsci4,
        
        'bsmath1' : bsmath1,
        'bsmath2' : bsmath2,
        'bsmath3' : bsmath3,
        'bsmath4': bsmath4,
        
        'socialwork1': socialwork1,
        'socialwork2': socialwork2,
        'socialwork3': socialwork3,
        'socialwork4': socialwork4,
        
        'bsit' : bsit,
        'bsed' : bsed,
        'bsce' : bsce,
        'beed' : beed,
        'bsmath' : bsmath,
        'socialwork' : socialwork,
        'polsci' : polsci,
        'bapols' : bapols,
    }
    
    return render(request, 'index.html', context)






def form(request):
    if request.method == 'POST':
        course = request.POST['course']
        year = request.POST['year']
        sex = request.POST['sex']
       
        
        add_respondent = Respondents(course=course, year_level=year, sex=sex)
        add_respondent.save()
        messages.success(request, "Successfully Logged in!")
        return redirect("form")
    return render(request, 'form.html')











def sidebar(request):
    return render(request, 'includes/sidebar.html')

def bsit(request):
    bsit = Respondents.objects.filter(course='BSIT').count()
    bsed = Respondents.objects.filter(course='BSED').count()
    bsce = Respondents.objects.filter(course='BSCE').count()
    beed = Respondents.objects.filter(course='BEED').count()
    bsmath = Respondents.objects.filter(course='BS MATH').count()
    socialwork = Respondents.objects.filter(course='Social Work').count()
    polsci = Respondents.objects.filter(course='AB Polsci').count()
    bapols = Respondents.objects.filter(course='BaPOLS').count()
    
    if request.method == 'POST':
        course = request.POST['course']
        year = request.POST['year']
        sex = request.POST['sex']
        dept = request.POST['department']
        
        add_respondent = Respondents(course=course, year_level=year, sex=sex, dept=dept)
        add_respondent.save()
        messages.success(request, "Successfully Added!")
        return redirect("bsit")
    
    
    bsit1 = Respondents.objects.filter(course='BSIT', year_level='1st Year').count()
    bsit2 = Respondents.objects.filter(course='BSIT', year_level='2nd Year').count()
    bsit3 = Respondents.objects.filter(course='BSIT', year_level='3rd Year').count()
    bsit4 = Respondents.objects.filter(course='BSIT', year_level='4th Year').count()
    
    
    context = {
        'bsit' : bsit,
        'bsed' : bsed,
        'bsce' : bsce,
        'beed' : beed,
        'bsmath' : bsmath,
        'socialwork' : socialwork,
        'polsci' : polsci,
        'bapols' : bapols,
        
        'bsit1' : bsit1,
        'bsit2' : bsit2,
        'bsit3' : bsit3,
        'bsit4' : bsit4,
    }
    return render(request, 'includes/bsit.html', context)



def bsce(request):
    bsit = Respondents.objects.filter(course='BSIT').count()
    bsed = Respondents.objects.filter(course='BSED').count()
    bsce = Respondents.objects.filter(course='BSCE').count()
    beed = Respondents.objects.filter(course='BEED').count()
    bsmath = Respondents.objects.filter(course='BS MATH').count()
    socialwork = Respondents.objects.filter(course='Social Work').count()
    polsci = Respondents.objects.filter(course='AB Polsci').count()
    bapols = Respondents.objects.filter(course='BaPOLS').count()
    
    if request.method == 'POST':
        course = request.POST['course']
        year = request.POST['year']
        sex = request.POST['sex']
        dept = request.POST['department']
        
        add_respondent = Respondents(course=course, year_level=year, sex=sex, dept=dept)
        add_respondent.save()
        messages.success(request, "Successfully Added!")
        return redirect("bsit")
    
    
    bsce1 = Respondents.objects.filter(course='BSCE', year_level='1st Year').count()
    bsce2 = Respondents.objects.filter(course='BSCE', year_level='2nd Year').count()
    bsce3 = Respondents.objects.filter(course='BSCE', year_level='3rd Year').count()
    bsce4 = Respondents.objects.filter(course='BSCE', year_level='4th Year').count()
    
    
    context = {
        'bsit' : bsit,
        'bsed' : bsed,
        'bsce' : bsce,
        'beed' : beed,
        'bsmath' : bsmath,
        'socialwork' : socialwork,
        'polsci' : polsci,
        'bapols' : bapols,
        
        'bsce1' : bsce1,
        'bsce2' : bsce2,
        'bsce3' : bsce3,
        'bsce4' : bsce4,
    }
    return render(request, 'includes/bsce.html', context)