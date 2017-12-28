from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
import hashlib
import urllib
from basicapp import models,forms

from basicapp.shortener_algo import algo
from django.http import HttpResponseRedirect
# from django.contrib.auth.hashers import make_password
def shorten(request):
    form=forms.LinkForm()
    al=algo()
    shortenURL=''
    if request.method=='POST':
        form=forms.LinkForm(request.POST)
        if form.is_valid():
            link=form.save(commit=False)
            targetURL=form.cleaned_data['targetURL']
            #check if this url is already exists
            try:
                check=models.Link.objects.get(targetURL=targetURL)# retrieve the object
            except:
                check = None
            # check=get_object_or_404(models.Link,targetURL=targetURL)
            print('check',check)
            if check is not None:
                shortenURL=check.shortenURL
                print('check not none shortenURL',shortenURL)
            else:
                linkid=models.Link.objects.count()
                shortenURL=al.encode(linkid)
                link.targetURL=targetURL
                link.shortenURL=shortenURL
                link.save()
                print('linkcount',linkid)
            print('targetURL,shortenURL',targetURL,shortenURL)

    return render(request,'index.html',{'form':form,'shorturl':shortenURL})

def target(request,URLid):
    al=algo()
    linkid=al.decode(URLid)+1
    target = get_object_or_404(models.Link,pk=linkid)
    targetURL=target.targetURL
    print('targetURL:',targetURL)
    return HttpResponseRedirect(targetURL)
