from django.shortcuts import render
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
import urllib
import json
from pprint import pprint
from .models import Village, three_four

# Create your views here.

def index(request):
    api_key = "b002eee32ff9696286c39f5a98ee26af0db17f9a3f1aeaa9ef1c32b2cf8cc15a"
    api_url = "Grid_20150914000000000230_1"
    url =  f"http://211.237.50.150:7080/openapi/{api_key}/json/{api_url}/1/100"
    
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        dicts = json.loads(response_body.decode('utf-8'))

    # 리셋
    Village.objects.all().delete()

    #저장
    for i in range(100):
        img_url = dicts[f'{api_url}']['row'][i]['FILE_PATH1']
        img_url1 = "http://" + img_url[5:]
        SIGUN_NM = dicts[f'{api_url}']['row'][i]['SIGUN_NM']
        # api시군코드가 db에 저장되어있는 시군코드에 있으면 
        return_farm_cnt = three_four.objects.get(sigun_nm=SIGUN_NM)

        vil = Village.objects.create(
            SIDO_NM = dicts[f'{api_url}']['row'][i]['SIDO_NM'],
            SIGUN_NM = dicts[f'{api_url}']['row'][i]['SIGUN_NM'],
            ADDR = dicts[f'{api_url}']['row'][i]['ADDR'],
            LOT_AREA = dicts[f'{api_url}']['row'][i]['LOT_AREA'],
            BUILDING_AREA = dicts[f'{api_url}']['row'][i]['BUILDING_AREA'],
            OWNER_NM = dicts[f'{api_url}']['row'][i]['OWNER_NM'],
            OWNER_CONTACT = dicts[f'{api_url}']['row'][i]['OWNER_CONTACT'],
            BIGO = dicts[f'{api_url}']['row'][i]['BIGO'],
            FILE_PATH1 = img_url1,
            FILE_PATH2 = dicts[f'{api_url}']['row'][i]['FILE_PATH2'],
            FILE_PATH3 = dicts[f'{api_url}']['row'][i]['FILE_PATH3'],
            REG_DT = dicts[f'{api_url}']['row'][i]['REG_DT'],
            DEAL_TYPE = dicts[f'{api_url}']['row'][i]['DEAL_TYPE'],
            RETURN_PEOPLE = return_farm_cnt.gagu_count
        )
        
        vil.save()
    return render(request, 'posts/list.html')
    
def list(request):
    emptyhouses = Village.objects.all()
    paginator = Paginator(emptyhouses, 9)
    page = request.GET.get('page',1)
    contacts = paginator.get_page(page)
    
    try:
        emptyhouse = paginator.page(page)
    except PageNotAnInteger:
        emptyhouse = paginator.page(1)
    except EmptyPage:
        emptyhouse = paginator.page(paginator.num_pages)
        
        
    return render(request, 'posts/list.html',{"emptyhouses":emptyhouses, "emptyhouse":emptyhouse})
    
def map(request):
    return render(request, 'posts/map.html')
    
def detail(request,id) :
    emptyhouse = Village.objects.get(id=id)
    return render(request, 'posts/detail.html',{'emptyhouse':emptyhouse})