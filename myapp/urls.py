from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name="home"),
	path('/add', views.AddCompView.as_view(), name="add"),
	path('edit/<int:pk>', views.UpdatePostView.as_view(), name="edit"),
	path('/<int:pk>/remove', views.DeletePostView.as_view(), name="delete"),
]