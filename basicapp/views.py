from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
import hashlib
import urllib
from basicapp import models,forms

from basicapp.shortener_algo import algo

# from django.contrib.auth.hashers import make_password
def shorten(request):
    form=forms.LinkForm()
    al=algo()
    if request.method=='POST':
        form=forms.LinkForm(request.POST)
        if form.is_valid():
            link=form.save(commit=False)
            targetURL=link.targetURL
            linkid=link.linkid
            shortenURL=al.encode(linkid)
            link.shortenURL=shortenURL
            print(targetURL,shortenURL)
            link.save()
    return render(request,'index.html',{'form':form,'shorturl':shortenURL})

def target(request,URLid):
    target = models.Link.objects.filter(shortenURL=URLid)
    # target=get_object_or_404(models.Link,shortenURL=URLid)
    targetURL=target.targetURL
    if(targetURL[:4]!='http'):
        targetURL='http://'+targetURL
    return redirect(targetURL)
