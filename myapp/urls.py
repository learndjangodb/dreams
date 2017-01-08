from django.conf.urls import url
from .views import (viewArticle, viewArticles, disdate, hello, StaticView, DreamRealList, login, UserTest, formView, 
    contact, AboutUsView, ContactView, create, tagTest, display_meta, search)
from .Auth_view import SavedProfile, home
from django.views.generic import TemplateView
from django.contrib.auth import views
from .forms import LoginForm

urlpatterns = [
    url(r'^article/(\d+)/$', viewArticle, name='article'),
    url(r'^articles2/(?P<month>\d{2})/(?P<year>\d{4})$', viewArticles, name="viewArticles"),
    url(r'^articles/date/$', disdate, name="disdate"),
    url(r'^hello/$', hello, name="hello"),
    url(r'^stview/$', StaticView.as_view(), name="stview"),
    url(r'drlist/$', DreamRealList.as_view(), name="drlist"),
    url(r'^login/', UserTest.as_view(), name="login"),
    url(r'^success/$', login, name="success"),
    url(r'^profile/', TemplateView.as_view(template_name='myapp/profile.html')),
    url(r'^saved/$', SavedProfile, name='saved'),
    url(r'^connection/', formView, name='loginform'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about_us/$', AboutUsView.as_view(), name="aboutus"),
    url(r'^contact2/$', ContactView.as_view(), name="contact2"),
    url(r'^create/$', create, name="adddata"),
    url(r'^tagtst/(?P<value>\w+)/$', tagTest, name="tagtest"),
    url(r'^$', home, name="home"),
    url(r'^login/$', views.login, {'template_name': 'myapp/Auth/login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^meta/$', display_meta, name="metainfo"),
    url(r'^searchform/$', TemplateView.as_view(template_name="myapp/search-form.html")),
    url('^search/$', search, name="search"),
]
