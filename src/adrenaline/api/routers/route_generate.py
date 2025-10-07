from flask import Blueprint, request, jsonify
from adrenaline.core.shape_match.matcher import generate_route
bp = Blueprint("route_generate", __name__)
@bp.post("/generate")
def generate():
    req = request.get_json() or {}
    out = generate_route(
        req.get("template_path","data/templates/heart_01.geojson"),
        req.get("network_path","data/network/pedestrian.geojson"),
        tuple(req.get("start",[126.972,37.562])),
        float(req.get("target_km",1.0))
    )
    return jsonify({"template_score": out["score"], "length_km": out["length_km"], "route_geojson": out["geojson"], "turns": []})
