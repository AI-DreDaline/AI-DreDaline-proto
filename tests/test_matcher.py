from adrenaline.core.shape_match.matcher import generate_route
def test_smoke():
    out = generate_route("data/templates/heart_01.geojson","data/network/pedestrian.geojson",(0,0),1.0)
    assert "geojson" in out and out["length_km"] > 0
