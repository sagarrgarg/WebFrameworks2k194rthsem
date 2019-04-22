from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^create-users/$', UserRetrieveUpdate.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserRetrieveUpdate.as_view()),

    url(r'^genres/$', GenreListCreate.as_view()),
    url(r'^genres/(?P<pk>\d+)/$', GenreRetrieveUpdate.as_view()),

    url(r'^books/$', BookListCreate.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookRetrieveUpdate.as_view()),
    url(r'^books/(?P<pk>\d+)/del$', BookDestroy.as_view()),

    url(r'^comments/$', CommentListCreate.as_view()),
    url(r'^comments/(?P<pk>\d+)/$', CommentRetrieveUpdate.as_view())
]