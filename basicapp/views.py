from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
# Create your views here.
import hashlib
import urllib
from basicapp import models,forms

# class index(TemplateView):
#     template_name='index.html'


def shorten(request):
    url=forms.LinkForm()
    if request.method=='POST':
        url=forms.LinkForm(data=request.POST)
        url.shortenURL = hashlib.md5(url.targetURL).hexdigest()[:8]
        url.save()
    return render(request,'index.html')

# 	try:
# 		check = URLs.objects.get(shrinkedURL = shrinkedURL)
# 	except URLs.DoesNotExist:
# 		entry = URLs(shrinkedURL = shrinkedURL, targetURL=url)
# 		entry.save()
# 	return render(request, 'shrink/index.html',{
# 			'shrinkedURL':shrinkedURL
# })
def target(request,URLid):
    target=get_object_or_404(models.Link,shortenURL=URLid)
    targetURL=target.targetURL
    if(targetURL[:4]!='http'):
        targetURL='http://'+targetURL
    return redirect(targetURL)
