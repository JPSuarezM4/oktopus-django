from django.urls import path
from . import views
from . import viewsEDA
from . import viewsLinea

urlpatterns = [
    path('cards/', views.cards, name="cards"),
    path('', views.index, name='index'),
    path('graficoseda/', viewsEDA.graficos_eda, name='graficoseda'),
    path("graficosenlinea/", viewsLinea.graficos_linea, name="graficosenlinea"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
