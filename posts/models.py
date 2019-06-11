from django.db import models

# Create your models here.
class Village(models.Model):
    # 시도명
    SIDO_NM = models.CharField(max_length=15, blank=True)
    # 시군명
    SIGUN_NM = models.CharField(max_length=10, blank=True)
    # 상세주소
    ADDR = models.CharField(max_length=100, blank=True)
    # 대지면적
    LOT_AREA = models.CharField(max_length=100, blank=True)
    # 건물면적
    BUILDING_AREA = models.CharField(max_length=100, blank=True)
    # 소유주명
    OWNER_NM = models.CharField(max_length=10, blank=True)
    # 소유주 연락처
    OWNER_CONTACT = models.CharField(max_length=100, blank=True)
    # 참고사항
    BIGO = models.CharField(max_length=100, blank=True)
    
    # 이미지 url 1
    FILE_PATH1 = models.CharField(max_length=100, blank=True)
    # 이미지 url 2
    FILE_PATH2 = models.CharField(max_length=100, blank=True)
    # 이미지 url 3
    FILE_PATH3 = models.CharField(max_length=100, blank=True)
    
    # 등록일
    REG_DT = models.CharField(max_length=20, blank=True)
    # 거래종류
    DEAL_TYPE = models.CharField(max_length=50, blank=True)
    # 귀농인 가구수
    RETURN_PEOPLE = models.IntegerField(default='0')
    
    
class three_four(models.Model):
    sido_nm = models.CharField(max_length=15, blank=True)
    sigun_nm = models.CharField(max_length=10, blank=True)
    gagu_count = models.IntegerField(blank=True)