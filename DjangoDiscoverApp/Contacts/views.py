from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from discoverApp.models import Message, Abonnement
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/signin/")
def contact(request):
    user = request.user.username
    list_user = []
    requestAbonnement = Abonnement.objects.filter()

    for elem in requestAbonnement:
        if(str(elem.abonne) == str(user)):
            list_user.append(elem.abonnement.username)

    return render(request, 'contact.html', {'list_user': list_user})

@login_required(login_url="/login/signin/")
def getMessage(request):
    #if(request.method == "POST"):
    #   list_message = Message.objects.get(envoyeur=request.POST['envoyeur'], receveur=request.POST['receveur'])
    #list_message = ["test", "test2"]
    #return render(request, 'contact.html', {'list_message': list_message})
    data = {
        'message': 'Données reçues avec succès'
    }
    return JsonResponse(data)
