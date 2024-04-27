from django import urls


from . import views

urlpatterns = [
    urls.path("", views.index, name="site_hosting_finder"),
]
