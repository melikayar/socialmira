from flask import Blueprint, jsonify, render_template

influencer_bp = Blueprint("influencer", __name__)

# Influencer verileri
influencers = [
    {
        "id": 1,
        "username": "katykargozar",
        "name": "Fatemeh Kargozar",
        "followers": "397K",
        "nation": "Iran",
        "language": "Persian",
        "lived_in": "London",
        "category": "Beauty, Fashion, Luxury Travel",
        "instagram_link": "https://www.instagram.com/katykargozar/"
    },
    {
        "id": 2,
        "username": "mozhdeh_blogjourney",
        "name": "Mozhdeh Ahmadi",
        "followers": "190K",
        "nation": "Iran",
        "language": "Persian",
        "lived_in": "USA",
        "category": "Lifestyle, Family, Humor",
        "instagram_link": "https://www.instagram.com/mozhdeh_blogjourney/"
    },
    {
        "id": 3,
        "username": "sanam_samipoor",
        "name": "Sanam Samipoor",
        "followers": "2.9M",
        "nation": "Iran",
        "language": "Persian",
        "lived_in": "Dubai",
        "category": "Lifestyle, Humor",
        "instagram_link": "https://www.instagram.com/sanam_samipoor/"
    },
    {
        "id": 4,
        "username": "zhatiis",
        "name": "Zhatiis",
        "followers": "1.1M",
        "nation": "Iran",
        "language": "Persian",
        "lived_in": "Turkey",
        "category": "Lifestyle, Fashion",
        "instagram_link": "https://www.instagram.com/zhatiis/"
    }
]

# Influencer listesini dönen route
@influencer_bp.route("/list", methods=["GET"])
def list_influencers():
    return jsonify({"influencers": influencers})

# Influencer detay sayfası
@influencer_bp.route("/detail/<username>", methods=["GET"])
def influencer_detail(username):
    influencer = next((i for i in influencers if i["username"] == username), None)
    if influencer:
        return render_template("influencer_detail.html", influencer=influencer)
    else:
        return "Influencer not found", 404
