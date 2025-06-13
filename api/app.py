from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@db/assetdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Asset

@app.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([{
        'id': asset.id,
        'name': asset.name,
        'type': asset.type,
        'status': asset.status,
        'location': asset.location
    } for asset in assets])

@app.route('/assets', methods=['POST'])
def add_asset():
    data = request.get_json()
    asset = Asset(
        name=data['name'],
        type=data['type'],
        status=data['status'],
        location=data['location']
    )
    db.session.add(asset)
    db.session.commit()
    return jsonify({'message': 'Asset added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')