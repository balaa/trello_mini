from django.conf.urls import url
from trelloboard import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^board_creation/$', views.TrelloList.as_view()),
    url(r'^board_details/(?P<pk>[0-9]+)/$', views.TrelloDetail.as_view()),
    url(r'^list_creation/$', views.TrelloList.as_view()),
    url(r'^list_details/(?P<pk>[0-9]+)/$', views.TrelloDetail.as_view()),
    url(r'^card_creation/$', views.TrelloList.as_view()),
    url(r'^card_details/(?P<pk>[0-9]+)/$', views.TrelloDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
