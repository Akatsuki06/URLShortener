from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
from basicapp import models,forms
from basicapp.shortener_algo import algo
from django.http import HttpResponseRedirect
from django.utils import timezone

def shorten(request):
    BASE_URL='http://su06.herokuapp.com/'
    form=forms.LinkForm()
    al=algo()
    shortenURL=''
    if request.method=='POST':
        form=forms.LinkForm(request.POST)
        if form.is_valid():
            link=form.save(commit=False)
            targetURL=form.cleaned_data['targetURL']
            #check if this url already exists
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
                urlid=models.Link.objects.count()
                shortenURL=BASE_URL+al.encode(urlid)
                link.targetURL=targetURL
                link.shortenURL=shortenURL
                link.created_date= timezone.now()
                link.save()
                print('linkcount',urlid)
            print('targetURL,shortenURL',targetURL,shortenURL)

    return render(request,'index.html',{'form':form,'shortenurl':shortenURL})

def target(request,URLid):
    al=algo()
    urlid=al.decode(URLid)+1
    target = get_object_or_404(models.Link,pk=urlid)
    targetURL=target.targetURL
    print('targetURL:',targetURL)
    return HttpResponseRedirect(targetURL)
