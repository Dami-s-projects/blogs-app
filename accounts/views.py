from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Function registers a new user"""
    #Get request type first

    if request.method != 'POST':
        #Not a Post request, a GET request or other types
        form=UserCreationForm()
    else:
        #Else, it is a POST request, then process data
        form=UserCreationForm(data=request.POST)

        #Then check form validity before saving
        if form.is_valid():
            #form valid, save user details
            new_user = form.save()
            #Then log the user in
            login(request, new_user)
            #Then redirect to homepage with the user logged in
            return redirect('blogs:index')
    
    #Runs after a GET request or when form is not valid
    context = {"form": form}
    return render(request,'registration/register.html',context)


