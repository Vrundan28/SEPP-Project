from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Feedback


# Create your views here.
def feedback(request):
    if request.method == "POST":
        username = request.session['uname']

        feedback1 = request.POST.get('feedback')
        f = Feedback(Uname=username,Feedback = feedback1)
        f.save()
        return HttpResponseRedirect("/Menu/viewMenu/")
    else:
        return render(request,'feedback.html')