from .views import RosesCreateView , RosesDeleteView ,RosesDetailView ,RosesListView ,RosesUpdateView
from django.urls import path 



urlpatterns=[
    path('' , RosesListView.as_view() , name='roses'),
    path('<int:pk>/detail/' , RosesDetailView.as_view() , name='detail'),
    path('create/' , RosesCreateView.as_view() , name='create'),
    path('<int:pk>/update/' , RosesUpdateView.as_view() , name='update'),
    path('<int:pk>/delete/' , RosesDeleteView.as_view() , name='delete'),
]