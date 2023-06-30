from fastapi import APIRouter
import json

router = APIRouter()

# Opening JSON file
f = open('data/provinces_with_districts_and_municipalities_in_devanagari.json',encoding="utf8")
# returns JSON object as
# a dictionary
data = json.load(f)

@router.get("/np/province")
async def get_all_province():
    province  = []
    for i in data:
        province.append(i)
    return ({"result": province})

@router.get("/np/district")
async def get_all_districts():
    district = []
    for i in data:
        for j in data[i]:
            district.append(j)
    return ({"result": district})

@router.get("/np/district/{province_name}")
async def get_district_by_province(province_name: str):
    """
    province_name: Name of province found in ```/np/province```  API
    """
    p_district = []
    for i in data[province_name]:
        p_district.append(i)
    return ({"result": p_district})

@router.get("/np/municilapity/{district_name}")
async def get_munipality_by_district(district_name : str):
    """
    district_name: Name of district found in ```/np/district```  API
    """
    for i in data:
        for j in data[i]:
            if j == district_name:
                province = i
    d_municipality = data[province][district_name]
    return ({"result":d_municipality})