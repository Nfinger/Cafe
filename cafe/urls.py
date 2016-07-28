from django.conf.urls import include,url
from .views import Home,Menu,About,Contact


urlpatterns = [
	url(r'^contact$',Contact.as_view(),name='contact'),
	url(r'^about$',About.as_view(),name='about'),
	url(r'^menu$',Menu.as_view(),name='menu'),
    url(r'^$',Home.as_view(),name='home')
]
