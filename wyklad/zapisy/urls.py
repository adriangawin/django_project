from django.conf.urls import url
import views
urlpatterns = [
    url(r'^search_form/$', views.search_form),
    url(r'^contact/$', views.contact),
    url(r'^search/$', views.search),
    url(r'^search_student/$', views.search_student),
    url(r'^search_student_result/$', views.search_student_result),
    url(r'^search_teacher/$', views.search_teacher),
    url(r'^search_teacher_result/$', views.search_teacher_result),
    url(r'^search_subjects/$', views.search_subjects),
    url(r'^search_subjects_result/$', views.search_subjects_result),
    url(r'^zapisz/$', views.zapisz),
    url(r'^zapisz_result/$', views.zapisz_result),
]
