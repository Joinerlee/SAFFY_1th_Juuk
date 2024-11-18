from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import TermDeposit, TermDepositOptions, Savings, SavingsOptions
from .serializers import TermDepositSerializer, TermDepositOptionSerializer, TermDepositAllSerializer, SavingsSerializer, SavingsOptionSerializer, SavingsAllSerializer


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi'
API_KEY = '815324d1a571acce6fbe7341cfa853f1'
# Create your views here.

# 정기예금 가져오기
@api_view(['GET'])
def term_deposit_update(request):
    URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'  # 슬래시 수정
    print(URL)
    topFinGrpNos = [ '020000', '030300' ]# 은행, 저축은행
    
    for topFinGrpNo in topFinGrpNos:
        params = {
            'auth': API_KEY,  # 변수명 오타 수정 및 일관성 유지
            'topFinGrpNo': topFinGrpNo,
            'pageNo': 1
        }
        response = requests.get(URL, params=params).json()
        products = response.get('result').get('baseList')
        ## 예금 정보 저장
        for product in products:
            fin_prdt_cd = product.get('fin_prdt_cd',)
            kor_co_nm = product.get('kor_co_nm')
            fin_prdt_nm = product.get('fin_prdt_nm')
            etc_note = product.get('etc_note' )
            join_deny = product.get('join_deny')
            join_member =product.get('join_member')
            join_way = product.get('join_way')
            spcl_cnd = product.get('spcl_cnd')
            dcls_strt_day = product.get('dcls_strt_day')
            save_data ={
                'fin_prdt_cd' : fin_prdt_cd,
                'kor_co_nm' : kor_co_nm,
                'fin_prdt_nm' : fin_prdt_nm,
                'etc_note': etc_note,
                'join_deny' : join_deny,
                'join_member': join_member,
                'join_way' : join_way,
                'spcl_cnd' : spcl_cnd,
                'dcls_strt_day':dcls_strt_day,
            }
            if TermDeposit.objects.filter(
                fin_prdt_cd = fin_prdt_cd, 
                ).exists():
                continue
            serializer = TermDepositSerializer(data =save_data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()  
                
        #option 저장
        products_options = response.get('result').get('optionList') 
        for option in products_options:
            fin_prdt_cd = option.get('fin_prdt_cd',)
            intr_rate_type_nm = option.get('intr_rate_type_nm')
            intr_rate = option.get('intr_rate', -1)
            intr_rate2 = option.get('intr_rate2',-1 )
            save_trm = option.get('save_trm')
            save_option_data ={
                'fin_prdt_cd' : fin_prdt_cd,
                'intr_rate_type_nm' : intr_rate_type_nm,
                'intr_rate' : intr_rate,
                'intr_rate2': intr_rate2,
                'save_trm' : save_trm,
            }      
            if TermDepositOptions.objects.filter(
                fin_prdt_cd = fin_prdt_cd, intr_rate_type_nm = intr_rate_type_nm, intr_rate = intr_rate,
                intr_rate2 = intr_rate2, save_trm = save_trm
                ).exists():
                continue
            serializer = TermDepositOptionSerializer(data =save_option_data)
            
            product = TermDeposit.objects.get(fin_prdt_cd=fin_prdt_cd)
            if serializer.is_valid(raise_exception = True):
                serializer.save(product = product)   
        
        
    return Response({'message' : '검색 완료'})

# 정기 예금 전체 조회
@api_view(["GET"])
def term_deposit(request):
    deposits = TermDeposit.objects.all()
    serializers = TermDepositAllSerializer(deposits, many=True)
    return Response(serializers.data)


# 정기 예금 상세 조회
@api_view(["GET"])
def term_deposit_detail(request,fin_prdt_cd):
    deposit = TermDeposit.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = TermDepositSerializer(deposit)
    return Response(serializer.data)


#######################
###################################
###적금

# 적금 가져오기
@api_view(['GET'])
def savings_update(request):
    URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'  # 슬래시 수정
    print(URL)
    topFinGrpNos = [ '020000', '030300' ]# 은행, 저축은행
    
    for topFinGrpNo in topFinGrpNos:
        params = {
            'auth': API_KEY,  # 변수명 오타 수정 및 일관성 유지
            'topFinGrpNo': topFinGrpNo,
            'pageNo': 1
        }
        response = requests.get(URL, params=params).json()
        products = response.get('result').get('baseList')
        ## 적금 정보 저장
        for product in products:
            fin_prdt_cd = product.get('fin_prdt_cd',)
            kor_co_nm = product.get('kor_co_nm')
            fin_prdt_nm = product.get('fin_prdt_nm')
            etc_note = product.get('etc_note' )
            join_deny = product.get('join_deny')
            join_member =product.get('join_member')
            join_way = product.get('join_way')
            spcl_cnd = product.get('spcl_cnd')
            dcls_strt_day = product.get('dcls_strt_day')
            save_data ={
                'fin_prdt_cd' : fin_prdt_cd,
                'kor_co_nm' : kor_co_nm,
                'fin_prdt_nm' : fin_prdt_nm,
                'etc_note': etc_note,
                'join_deny' : join_deny,
                'join_member': join_member,
                'join_way' : join_way,
                'spcl_cnd' : spcl_cnd,
                'dcls_strt_day':dcls_strt_day,
            }
            if Savings.objects.filter(
                fin_prdt_cd = fin_prdt_cd, 
                ).exists():
                continue
            serializer = SavingsSerializer(data =save_data)
            if serializer.is_valid(raise_exception= True):
                serializer.save()  
                
        #option 저장
        products_options = response.get('result').get('optionList') 
        for option in products_options:
            fin_prdt_cd = option.get('fin_prdt_cd',)
            intr_rate_type_nm = option.get('intr_rate_type_nm')
            intr_rate = option.get('intr_rate', -1)
            intr_rate2 = option.get('intr_rate2',-1 )
            save_trm = option.get('save_trm')
            save_option_data ={
                'fin_prdt_cd' : fin_prdt_cd,
                'intr_rate_type_nm' : intr_rate_type_nm,
                'intr_rate' : intr_rate,
                'intr_rate2': intr_rate2,
                'save_trm' : save_trm,
            }      
            if SavingsOptions.objects.filter(
                fin_prdt_cd = fin_prdt_cd, intr_rate_type_nm = intr_rate_type_nm, intr_rate = intr_rate,
                intr_rate2 = intr_rate2, save_trm = save_trm
                ).exists():
                continue
            serializer = SavingsOptionSerializer(data =save_option_data)
            
            product = Savings.objects.get(fin_prdt_cd=fin_prdt_cd)
            if serializer.is_valid(raise_exception = True):
                serializer.save(product = product)   
    return Response({'message' : '검색 완료'})

# 정기 예금 전체 조회
@api_view(["GET"])
def savings(request):
    deposits = Savings.objects.all()
    serializers = SavingsAllSerializer(deposits, many=True)
    return Response(serializers.data)


# 정기 예금 상세 조회asdf
@api_view(["GET"])
def savings_detail(request,fin_prdt_cd):
    deposit = Savings.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingsSerializer(deposit)
    return Response(serializer.data)

