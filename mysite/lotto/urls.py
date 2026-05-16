from django.urls import path
from . import views  # 현재 폴더의 views.py를 가져옵니다.

urlpatterns = [
    # 'http://127.0.0.1:8000/lotto/buy/' 주소로 들어왔을 때 views.buy_auto 함수를 실행합니다.
    path('', views.home, name='home'),
    path('buy/', views.buy_auto, name='buy_auto'),
    path('manual/', views.buy_manual, name='buy_manual'),
    path('check/', views.check_result, name='check_result'),
    
    path('admin-sales/', views.admin_sales, name='admin_sales'),
    path('admin-draw/', views.admin_draw, name='admin_draw'),
    path('admin-draw-results/', views.admin_draw_results, name='admin_draw_results'),
]