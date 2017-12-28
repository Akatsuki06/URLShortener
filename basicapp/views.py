from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
import hashlib
import urllib
from basicapp import models,forms

# class index(TemplateView):
#     template_name='index.html'


from django.contrib.auth.hashers import make_password
def shorten(request):
    form=forms.LinkForm()
    shortenURL=''
    if request.method=='POST':
        form=forms.LinkForm(request.POST)
        if form.is_valid():
            link=form.save(commit=False)
            targetURL=link.targetURL
            # shortenURL=hashlib.md5(targetURL)
            shortenURL=len(targetURL)
            link.shortenURL=shortenURL
            # print(user.password,clearpwd,hashpwd)
            print(targetURL,shortenURL)
            # form.shortenURL = hashlib.md5(form.targetURL).hexdigest()[:8]
            # print('targeturl',form.targetURL)
            # print('short url',form.shortenURL)
            link.save()

    return render(request,'index.html',{'form':form,'shorturl':shortenURL})

def target(request,URLid):
    target = models.Link.objects.filter(shortenURL=URLid)
    # target=get_object_or_404(models.Link,shortenURL=URLid)
    targetURL=target.targetURL
    if(targetURL[:4]!='http'):
        targetURL='http://'+targetURL
    return redirect(targetURL)
