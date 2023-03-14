from django.shortcuts import render
import datetime
# Create your views here.


def port(request):

    timenow = datetime.datetime.now()
    hour = int(timenow.strftime('%H'))
    message = 'hi'
    if hour<12:
        message+="good morning"
    else:
        message+='good evening' 
    name = 'Ansalr'
    date_dict = {'today_date' : timenow,'myname': name,'currnt_time': hour,'messagenow': message}
    return render(request,'app3_temp/dict.html',context = date_dict)