from django.contrib.auth import logout
from django.urls import path
from . import views


urlpatterns=[
    path('<str:coders_id>/',views.func,name="home"),
    path('profile/<str:coders_id>/',views.prof,name="profile"),
    path('logut',views.lgout,name="logout"),

    path('graph/<str:coders_id>/',views.graph,name='graph'),
    path('mathematics/<str:coders_id>/',views.mathematics,name='mathematics'),
    path('dynamic_programming/<str:coders_id>/',views.dynamic_programming,name='dynamic_programming'),
    path('implementation/<str:coders_id>/',views.implementation,name='implementation'),
    path('algorithm/<str:coders_id>/',views.algorithm,name='algorithm'),
    path('data_structure/<str:coders_id>/',views.data_structure,name='data_structure'),
    path('miscellaneous/<str:coders_id>/',views.miscellaneous,name='miscellaneous'),
    path('string/<str:coders_id>/',views.string,name='string'),
    path('geometry/<str:coders_id>/',views.geometry,name='geometry'),
    path('searching/<str:coders_id>/',views.searching,name='searching'),
    path('profile/<str:coders_id>/',views.profile,name='profile'),
    path('addvideo/<str:coders_id>/',views.vid,name='addvideo'),
    path('livecontest/<str:coders_id>/',views.lcon,name='live'),
]