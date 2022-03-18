from django.urls import path
from . import views

app_name = 'rec'

urlpatterns = [
    path('', views.rec, name='rec'),
    path('rec/', views.rec_movie, name='submit_rec'),
    path('results/', views.view_results, name='results'),

]