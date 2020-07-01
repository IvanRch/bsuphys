from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    # path('file/<pk>/', views.download, name='download'),
    # path("<uploads>")
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),

]