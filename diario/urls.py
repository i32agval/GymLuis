from django.conf.urls import url
from diario import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^entry-list/$',
        login_required(views.entry_list), name='entry_list'),
    url(r'^post-entry/$',
        login_required(views.post_entry), name='post_entry'),
    url(r'^entry-delete/(?P<pk>\d+)/$',
        login_required(views.EntryDelete.as_view()), name='entry_delete'),
    url(r'^entry-edit/(?P<pk>\d+)$',
        login_required(views.EntryUpdateView.as_view()), name='entry_edit'),
]
