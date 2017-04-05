from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import json as simplejson
from .models import Person
from .models import Products
from .models import Supermarket
# Create your views here.


def returnAllPeople(self):
    json = simplejson.dumps([{'pk': person.pk, 'name': person.name,'password': person.password, 'type':person.type, 'gmail':person.gmail}
                             for person in Person.objects.all()])
    return HttpResponse(json, content_type='application/json')

def returnType(self,type):
    if(int(type) != 2):
        json = simplejson.dumps([{'pk': person.pk, 'name': person.name, 'password': person.password, 'type':person.type, 'gmail':person.gmail}
                                 for person in Person.objects.filter(type=type)])
    else:
        json = simplejson.dumps([{'pk': person.pk, 'name': person.name, 'password': person.password, 'type':person.type, 'gmail':person.gmail,
                                  'supermarketName':person.supermarket_set.all()[0].name,'supermarketID':person.supermarket_set.all()[0].pk}
                                 for person in Person.objects.filter(type=type)])

    return HttpResponse(json, content_type='application/json')

def returnAllProducts(self):
    json = simplejson.dumps([{'pk': product.pk, 'name': product.name, 'supermarketName': product.supermarket.name,'supermarketID':product.supermarket.pk} for product in Products.objects.all()])
    return HttpResponse(json, content_type='application/json')


def addCusomerOrOwner(self,username,password,gmail,type,prefix,supermarketName = "-"):
    person = Person.objects.create(name=username,password=password,gmail=gmail+"@"+prefix+".com",type=int(type))
    Supermarket.objects.create(name=supermarketName,owner=person)
    return returnAllPeople(self)


def addProduct(self,productName,supermarketID):
    supermarket = Supermarket.objects.get(pk=int(supermarketID))
    Products.objects.create(name=productName,supermarket=supermarket)
    return returnAllProducts(self)



def searchAboutPerson(self,data):
    json = simplejson.dumps([{'pk': person.pk, 'name': person.name, 'password': person.password, 'type':person.type, 'gmail':person.gmail}
             for person in Person.objects.filter(name__contains=data)])
    return HttpResponse(json, content_type='application/json')

def searchAboutProduct(self,data):
    json = simplejson.dumps([{'pk': product.pk, 'name': product.name}
             for product in Products.objects.filter(name__contains=data)])
    return HttpResponse(json, content_type='application/json')


def deletePerson(self,data):
    Person.objects.filter(name=data).delete()
    return returnAllPeople(self)


def simple_upload(self,request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.POST['name']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return returnAllProducts(self)
    return returnAllPeople(self)


def returnPersonByID(self,id):
    person = Person.objects.get(id=id)
    if(person.type != 2):
        json = simplejson.dumps([{'pk': person.pk, 'name': person.name,'password': person.password, 'type':person.type, 'gmail':person.gmail}])
    else:
        json = simplejson.dumps([{'pk': person.pk, 'name': person.name, 'password': person.password, 'type':person.type, 'gmail':person.gmail,
                                  'supermarketName':person.supermarket_set.all()[0].name,'supermarketID':person.supermarket_set.all()[0].pk}])
    return HttpResponse(json, content_type='application/json')

