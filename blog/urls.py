from django.conf.urls import include, url

from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^info/$', views.InfoView, name='info'),
    url(r'^contact/$',views.ContactView, name='contact'),
    url(r'^contact/thanks/$',views.ContactThanksView, name='contactthanks'),
    url(r'^projects/$',views.ProjectsView, name='projects'),
    url(r'^projects/(?P<slug>[-\w]+)/$',views.OneProjectView.as_view(), name='oneproject'),
    url(r'^knowledge/(?P<slug>[-\w]+)/$',views.KnowledgePostView.as_view(), name = 'knowledgepost'),
    url(r'(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post'),
]
