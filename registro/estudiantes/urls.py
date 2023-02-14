
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="estudiante"),
    path('<letter>',views.index,name="estudiante"),
   path('view/<int:id>',views.view,name="view"),
   path('create/',views.create,name="create"),
   path('delete/<int:id>',views.delete,name="delete"),
   path('edit/<int:id>',views.edit,name="edit"),
]
