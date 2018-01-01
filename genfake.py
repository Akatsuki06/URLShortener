import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','URLShortener.settings')
import django
django.setup()
from faker import Faker
from basicapp.models import Link
from django.utils import timezone
from basicapp.shortener_algo import algo
BASE_URL='http://su06.herokuapp.com/'
def populate(N):
    fake=Faker()
    al=algo()
    urls=set()
    while len(urls)<N:
        url=fake.url()
        urls.add(url)

    for url in urls:
        try:
            check=Link.objects.get(targetURL=url)# retrieve the object
        except:
            check = None
        if check is None:
            urlid=Link.objects.count()
            shortenURL=BASE_URL+al.encode(urlid)
            created_date=timezone.now()
            link=Link.objects.get_or_create(created_date=created_date,shortenURL=shortenURL,targetURL=url)[0]
            link.save()

    print(len(urls))

populate(1000)
