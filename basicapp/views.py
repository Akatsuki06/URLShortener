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
            link.save()
            targetURL=link.targetURL
            linkid=link.pk
            print(link.pk)
            print('linkid--',linkid)
            shortenURL=al.encode(linkid)
            link.shortenURL=shortenURL
            print(targetURL,shortenURL)
            link.save()
    return render(request,'index.html',{'form':form,'shorturl':shortenURL})

def target(request,URLid):
    # target = models.Link.objects.filter(shortenURL=URLid)
    # print(target)
    target=get_object_or_404(models.Link,shortenURL=URLid)
    print(target)
    targetURL=target.targetURL
    print(targetURL)
    if(targetURL[:4]!='http'):
        targetURL='http://'+targetURL
    return HttpResponseRedirect(targetURL)
