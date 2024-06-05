import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
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
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))

        user_logged=request.user
        user = User.objects.get(username=data['abonnement'].replace('`', ''))
        list_message_User = Message.objects.filter(envoyeur=user, receveur=user_logged)
        list_message_User_Logged = Message.objects.filter(envoyeur=user_logged, receveur=user)
        print(list_message_User)
        print(list_message_User_Logged)

        minIdUserLogged = None
        for elem in list_message_User_Logged:
            if(minIdUserLogged == None):
                minIdUserLogged = elem.id
            elif(minIdUserLogged > elem.id):
                minIdUserLogged = elem.id

        minIdUser = None
        for elem in list_message_User:
            if(minIdUser == None):
                minIdUser = elem.id
            elif(minIdUser > elem.id):
                minIdUser = elem.id
        
        #Last comparaison
        if(minIdUser < minIdUserLogged):
            firstUser = list_message_User
            secondUser = list_message_User_Logged
        elif(minIdUser > minIdUserLogged):
            firstUser = list_message_User_Logged
            secondUser = list_message_User


    """
    for elem in firstUser:
        print(elem.date)

    #Change data format

    n = 0
    v = 0
    listMessage = []
    for elem in firstUser:
        if(n == 0):
            listMessage.append([elem.id, elem])
            n += 1
        elif(listMessage[-1][0]) < int(elem.id):
            listMessage.append([elem.id, elem])
        else:
            for i in range(v, len(secondUser)):
                if(v == 0):
                    listMessage.append([secondUser[i].id, secondUser[i]])
                    v += 1
                elif(int(listMessage[-1][0]) + 1 == int(secondUser[i].id)):
                    listMessage.append([secondUser[i].id, secondUser[i]])
                    v += 1
                else:
                    print("entree")
                    break
        
        print('continue')
        
    print(listMessage)

    """

    l1 = []
    for elem in firstUser:
        l1.append(elem)

    l2 = []
    for elem in secondUser:
        l2.append(elem)

    data = {
        'firstUser': l1,
        'secondUser': l2
    }

    return JsonResponse(data)
