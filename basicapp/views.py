from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
from basicapp import models,forms
from basicapp.shortener_algo import algo
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone

from urllib.parse import urlparse
BASE_URL='http://su06.herokuapp.com/'

def check_and_create(targetURL):
    al=algo()
    shortenURL,created_date='',''
    targetURL=targetURL.lower()
    if urlparse(targetURL).scheme=='':
        targetURL='http://'+targetURL
    link = models.Link.objects.filter(targetURL = targetURL)

    if link.count() == 0:
        link = models.Link()
        urlid = models.Link.objects.count()
        shortenURL = BASE_URL+al.encode(urlid)
        created_date = timezone.now()
        link.targetURL = targetURL
        link.shortenURL = shortenURL
        link.created_date = created_date
        link.save()
    else:
         link=link[0]
    return link


def shorten(request):
    form=forms.LinkForm()
    al=algo()
    shortenURL=''
    if request.method=='POST':
        form=forms.LinkForm(request.POST)
        if form.is_valid():
            targetURL=form.cleaned_data['targetURL']
            link = check_and_create(targetURL)
            shortenURL=link.shortenURL

    return render(request,'index.html',{'form':form,'shortenurl':shortenURL})


def target(request,URLid):
    al=algo()
    urlid=al.decode(URLid)+1
    target = get_object_or_404(models.Link,pk=urlid)
    targetURL=target.targetURL
    print('targetURL:',targetURL)
    return HttpResponseRedirect(targetURL)


from basicapp import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication

class CreateAPI(APIView):
    serializer_class = serializers.LinkSerializer

    def post(self,request):
        serializer = serializers.LinkSerializer(data=request.data)
        if serializer.is_valid():
            targetURL = serializer.data.get('targetURL')
            link = check_and_create(targetURL)
            return Response({'created_date':link.created_date,'targetURL':link.targetURL,'shortenURL':link.shortenURL})
        else:
            return Response({'error':'error occured while making request'})
