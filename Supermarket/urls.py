
from django.conf.urls import url
from django.contrib import admin
from supermarketProject import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls), # http://127.0.0.1:8000/admin/
    url(r'^person/$', views.returnAllPeople), # http://127.0.0.1:8000/person/
    url(r'^person/(?P<type>[1-3])/$', views.returnType),  # http://127.0.0.1:8000/person/3/
    url(r'^product/$', views.returnAllProducts),  # http://127.0.0.1:8000/product/
    url(r'^person/register/(?P<username>\w+)-(?P<password>\w+)-(?P<gmail>\w+)@(?P<prefix>\w+)\.com-(?P<type>\w+)-(?P<supermarketName>\w+)/$', views.addCusomerOrOwner),  #
    url(r'^person/search/(?P<data>\w+)/$', views.searchAboutPerson),  # http://127.0.0.1:8000/person/3/
    url(r'^product/search/(?P<data>\w+)/$', views.searchAboutProduct),  # http://127.0.0.1:8000/person/3/و
    url(r'^person/delete/(?P<data>\w+)/$', views.deletePerson),  # http://127.0.0.1:8000/person/3/
    url(r'^$', views.simple_upload),  # http://127.0.0.1:8000/person/3/
    url(r'^supermarket/addProduct/(?P<productName>\w+)/(?P<supermarketID>\w+)/$', views.addProduct),  # http://127.0.0.1:8000/person/3/
    url(r'^returnPersonByID/(?P<id>\w+)/$', views.returnPersonByID),  # http://127.0.0.1:8000/person/3/


]
urlpatterns = format_suffix_patterns(urlpatterns)


