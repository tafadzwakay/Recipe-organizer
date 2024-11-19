from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('add', views.add_recipe, name = "add_recipe"),
    path('view/<int:id>', views.view_recipe, name = "view_recipe"),
    path('delete/<int:id>', views.delete_recipe, name = "delete_recipe"),
    path('update/<int:id>', views.update_recipe, name = "update_recipe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    