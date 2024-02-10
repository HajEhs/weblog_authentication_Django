from django.urls import path

from . import views

urlpatterns = [
    path("postList/", views.PostListView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("postCreate/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/postUpdate/", views.PostUpdateView.as_view(), name='post_update'),
    path("<int:pk>/postDelete/", views.PostDeleteView.as_view(), name="post_delete")

]
