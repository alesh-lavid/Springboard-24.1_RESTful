"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "1312378"

connect_db(app)

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/api/cupcakes")
def all_cupcakes():
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake():
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes", methods=["POST"])
def make_cupcake():
    req = request.json
    new_cupcake = Cupcake(flavor=req['flavor'], rating=req['rating'], size=req['size'], image=req['image'] or None)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake():
    
    req = request.json
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = req['flavor']
    cupcake.rating = req['rating']
    cupcake.size = req['size']
    cupcake.image = req['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")