from shapely.geometry import LineString
import geopandas as gpd

def generate_route(template_geojson_path: str, network_geojson_path: str, start, target_km: float):
    # 데모용 더미: 템플릿 파일을 그대로 내보내기
    tpl = gpd.read_file(template_geojson_path).iloc[0].geometry
    gj = gpd.GeoDataFrame({"kind":["route"]}, geometry=[tpl], crs="EPSG:4326")
    return {"geojson": gj.__geo_interface__, "score": 0.5, "length_km": 1.0}
