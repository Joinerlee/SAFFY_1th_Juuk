from django.urls import path, include
from . import views


urlpatterns = [
    # 정기 예금 가져오기
    path('term_deposit/update/', views.term_deposit_update, name='term_deposit_update'),
    # 정기 예금 전체 조회( 정기 예금 상품의 기간 별 금리 포함)
    path('term_deposit/', views.term_deposit, name='term_deposit'),
    # 상세 정기 예금 상품 조회
    path('term_deposit/detail/<fin_prdt_cd>/', views.term_deposit_detail, name='term_deposit_detail'), 
    # 적금 가져오기
    path('savings/update/', views.savings_update, name='savings_update'),
    # 적금 전체 조회( 정기 예금 상품의 기간 별 금리 포함)
    path('savings/', views.savings, name='savings'),
    # 상세 적금 상품 조회
    path('savings/detail/<fin_prdt_cd>/', views.savings_detail, name='savings_detail'),
    # 주택담보 대출 가져오기
    path('mortgageloan/update/', views.mortgageloan_update, name='mortgageloan_update'),
    # 
    path('mortgageloan/', views.mortgageloan, name='mortgageloan'),

]
