from django.shortcuts import render
from client.models import Client
from commande.models import Commande
from django.contrib.auth.decorators import login_required



@login_required(login_url='acces')

def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/accueil.html',context)

