from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages

def  inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
       form=CreerUtilisateur(request.POST)
       if form.is_valid():
           form.save()
           user=form.cleaned_data.get('username')
           messages.success(request,"Felicitation, Votre Compte a ete Cree avec Succes! ")
           return redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)


def accesPage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.info(request,"Le Nom d'Utilisateur ou le Mot de Passe est Incorrect.")
    return render(request,'compte/acces.html',context)


def logoutUser(request):
    logout(request)
    return redirect('acces')