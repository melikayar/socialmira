from flask import Blueprint, request, jsonify

brand_bp = Blueprint("brand", __name__)

# Geçici olarak RAM'de tutulacak marka verileri
# Temporary in-memory brand list (RAM'de tutulur)
brands = []

@brand_bp.route("/register", methods=["POST"])
def register_brand():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    # Aynı email'le kayıt varsa ekleme
    for brand in brands:
        if brand["email"] == email:
            return jsonify({"error": "Brand already registered"}), 409

    brands.append({"name": name, "email": email})
    return jsonify({"message": f"Brand '{name}' registered successfully!"}), 201


# ✅ BURASI yeni eklenen GET endpoint
@brand_bp.route("/list", methods=["GET"])
def list_brands():
    return jsonify({"brands": brands})
