from django.db import models

# Create your models here.
class TermDeposit(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField() # 금융 회사명
    fin_prdt_nm = models.TextField() # 금융상품명
    etc_note = models.TextField() # 금융상품 설명
    join_deny = models.IntegerField() # 가입 제한 (1: 제한 없음 2: 서민 전용 3. 일부제한)
    join_member = models.TextField() # 가입대상
    join_way = models.TextField() # 가입 방법
    spcl_cnd = models.TextField() # 우대 조건
    dcls_strt_day = models.TextField() # 공시 시작일
    
class TermDepositOptions(models.Model):
    product = models.ForeignKey(TermDeposit, on_delete= models.CASCADE)
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    intr_rate = models.FloatField(null = True) # 저축금리
    intr_rate2 = models.FloatField(null =True) # 최고우대 금리
    save_trm = models.IntegerField() # 저축 기간 단위(개월)
    
    
class Savings(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField() # 금융 회사명
    fin_prdt_nm = models.TextField() # 금융상품명
    etc_note = models.TextField() # 금융상품 설명
    join_deny = models.IntegerField() # 가입 제한 (1: 제한 없음 2: 서민 전용 3. 일부제한)
    join_member = models.TextField() # 가입대상
    join_way = models.TextField() # 가입 방법
    spcl_cnd = models.TextField() # 우대 조건
    dcls_strt_day = models.TextField() # 공시 시작일
    
class SavingsOptions(models.Model):
    product = models.ForeignKey(Savings, on_delete= models.CASCADE)
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 저축금리 유형명
    intr_rate = models.FloatField(null = True) # 저축금리
    intr_rate2 = models.FloatField(null =True) # 최고우대 금리
    save_trm = models.IntegerField() # 저축 기간 단위(개월)    