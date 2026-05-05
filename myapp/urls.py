from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Event detail page
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),

    # Meetings pages
    path('meetings/', views.meetings, name='meetings'),
    path('meeting-details/', views.meeting_details, name='meeting_details'),
    path('scholarship/', views.scholarship, name='scholarship'),
    # Chatbot API
    path('chatbot/', views.chatbot_api, name='chatbot'),
]