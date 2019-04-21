from django.conf.urls import url
from gym import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',
        login_required(views.index),
        name='index'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^machines/$',
        login_required(views.machines),
        name='machines'),

    url(r'^users/$',
        login_required(views.UserListView.as_view()),
        name='users_list'),

    url(r'^machine/(?P<pk>\d+)$',
        login_required(views.MachineDetailView.as_view()),
        name='machine-detail'),

    url(r'^exercise-weight/$',
        login_required(views.new_weight),
        name='new_weight'),

    url(r'^exercise-weight/(?P<pk>\d+)$',
        login_required(views.new_weight),
        name='new_weight2'),

    url(r'^exercise-edit/(?P<pk>\d+)/(?P<id>\d+)$',
        login_required(views.ExerciseUpdate.as_view()),
        name='exercise_edit'),

    url(r'^exercise-delete/(?P<pk>\d+)/(?P<id>\d+)/$',
        login_required(views.ExerciseDelete.as_view()),
        name='exercise-delete'),

    url(r'^user-data/$',
        login_required(views.user_data),
        name='user_data'),

    url(r'^user-edit/$',
        login_required(views.edit_userprofile),
        name='user_edit'),

    url(r'^users-report-pdf/$',
        login_required(views.UsersReportPDF.as_view()),
        name='users_report_pdf'),

    url(r'^plot/(?P<pk>\d+)$',
        login_required(views.plot),
        name='view-plot'),

    url(r'^progress/$',
        login_required(views.progress),
        name='progress'),

    url(r'^upload/$',
        login_required(views.upload_image),
        name='upload_image'),

    url(r'^images/$',
        login_required(views.images_view),
        name='images'),

    url(r'^image-edit/(?P<pk>\d+)$',
        login_required(views.UserImagesUpdate.as_view()),
        name='image_edit'),

    url(r'^image-delete/(?P<pk>\d+)/$',
        login_required(views.ImageDelete.as_view()),
        name='image-delete'),

    url(r'^images/(?P<pk>\d+)$',
        login_required(views.images_view),
        name='images'),

    url(r'^social/$',
        login_required(views.social),
        name='social'),

    url(r'^users-search/$',
        login_required(views.users_search),
        name='users_search'),

    url(r'^friends-search/$',
        login_required(views.view_friends),
        name='view_friends'),

    url(r'^delete_relationship/(?P<pk>\d+)/(?P<delete_friend>\d+)/$',
        login_required(views.delete_relationship),
        name='delete'),

    url(r'^delete_relationship_confirm/(?P<pk>\d+)/(?P<delete_friend>\d+)/$',
        login_required(views.delete_relationship_confirm),
        name='delete-confirm'),

    url(r'^add_friend/(?P<pk>\d+)/(?P<add_friend>\d+)/$',
        login_required(views.add_relationship),
        name='add_friend'),

    url(r'^requests/$',
        login_required(views.view_requests),
        name='requests'),
]
