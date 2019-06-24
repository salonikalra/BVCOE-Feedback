from django.conf.urls import url
from django.urls import path

from . import views

app_name='feedbacks'

urlpatterns = [
    url(r"new/$", views.Createfeedback.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.Userfeedbacks.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.feedbackDetail.as_view(),name="single"),
    url(r"completed/$",views.FeedbackCompletedView.as_view(),name="completed"),

    path('ajax/load-teachers/', views.load_teachers, name='ajax_load_teachers'),  # <-- this one here


]
