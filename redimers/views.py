from django.http import Http404
from django.http import HttpResponse
from .models import Reminder
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from .forms import Redimerform

def index(request):

    if request.method == "POST":
        reminder =Reminder()
        reminder.content= request.POST.get("content")
        reminder.important= request.POST.get("important") =="on"
        reminder.save()
        return redirect("index")


    reminders = Reminder.objects.order_by("-id")
    context = {"reminders": reminders, "form":Redimerform()}
    return render(request, "reminders/index.html", context)
    ##return HttpResponse(", ".join([f"{Reminder.id}-{Reminder.content} - {Reminder.createdAt} - Completado: {Reminder.important}" for Reminder in Reminder.objects.all()]))
    ##reminder = Reminder.objects.order_by("-id")
    ##template = loader.get_template("redimers/index.html")
    ##context = {"reminders": reminder}
    ##return HttpResponse(template.render(context, request))



def editar(request,id):
    
    reminder=get_object_or_404(Reminder, pk=id)

    if request.method == "POST":
        reminder.content= request.POST.get("content")
        reminder.important= request.POST.get("important") =="on"
        reminder.save()
        return redirect("index")


    return render(request,"reminders/editar.html", {"reminders": reminder})


    ##try:
    ##    reminder =Reminder.objects.get(pk=id)
    ##    return render(request,"reminders/editar.html", {"reminders": reminder})
    ##except Reminder.DoesNotExist:
    ##    raise Http404("Recordatorio no existe")

