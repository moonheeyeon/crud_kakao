from django.urls import path
from . import views

app_name = "products" 
urlpatterns = [
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),
    path('edit/<int:id>/', views.edit, name="edit"),
    #path('show/<int:id>/', views.show, name="show"), 이렇게 주소를 간력화 할 수 있음
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]

#앱을 여러개 만들면 create라는 html을 여러개 만들게 될텐데. app_name을 설정하면 products:create라고 써야해서 create.html여러개 만들어도 구분할 수 있음
#id라는 이름으로, integer라는 타입으로 주소를 전달한다
#int 타입인 id를 views에서 받을 수 있어야 함
