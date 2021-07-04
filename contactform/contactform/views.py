from django.shortcuts import render
from contactform.forms import contactformemail
from django.core.mail import send_mail

def contactsendmail(request):
    if request.method=="GET":
        form=contactformemail()
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            contact=form.cleaned_data['contact']
            fromemail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,fromemail,['xyz@gmail.com',fromemail])
    return render(request,'Contact.html',{'forms':form})
    
        