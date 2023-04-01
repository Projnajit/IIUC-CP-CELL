from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Video
from django import http
from login.models import coders
from django.shortcuts import render, redirect
from django.http import HttpResponse
from signup.forms import codersform, videoform


@login_required(login_url='login')
def func(request, coders_id):
    profile = coders.objects.get(id=coders_id)
    context = {'profile': profile}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def prof(request, coders_id):
    coder = coders.objects.get(id=coders_id)
    form = codersform(instance=coder)
    tm = str(coders_id) + "/#l2" 
    context = {'coder': coder, 'form': form,'cod':coders_id, 'tm':tm}
    if request.method == 'POST':
        nform =  codersform(request.POST, instance=coder)
        if nform.is_valid():
            nform.save()
            return redirect('home', coders_id)
        else:
            print(nform.errors.as_data())
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def vid(request,coders_id):
    form = videoform()
    context={'form':form,'cod':coders_id}
    if request.method=='POST':
        form = videoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home',coders_id)
    return render(request,'addvideo.html',context)

    
def lgout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def graph(request, coders_id):
    cat = str("Graph")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def mathematics(request, coders_id):
    cat = str("Mathematics")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def profile(request, coders_id):
    cat = str("Geometry")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def dynamic_programming(request, coders_id):
    cat = str("Dynamic Programming")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def implementation(request, coders_id):
    cat = str("Implementation")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def algorithm(request, coders_id):
    cat = str("Algorithm")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def data_structure(request, coders_id):
    cat = str("Data Structures")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def miscellaneous(request, coders_id):
    cat = str("Miscellaneous")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def string(request, coders_id):
    cat = str("String")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def geometry(request, coders_id):
    cat = str("Geometry")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def searching(request, coders_id):
    cat = str("Searching and Sortings")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)


@login_required(login_url='login')
def lcon(request, coders_id):
    cat = str("Live Contests")
    Videos = Video.objects.filter(category=cat, ps=1)
    context = {'Videos': Videos, 'cat': cat, 'cod': coders_id}
    return render(request, 'inside.html', context)
