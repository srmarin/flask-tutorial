import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from schemas import StoreSchema
from models import StoreModel

blp = Blueprint("Stores", "stores", description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(cls, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(cls, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        
        return {"message": "Store deleted."}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(cls):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(cls, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that alredy exists.")
        except SQLAlchemyError:
            abort(500, message="An error ocurred when trying to save the store.")

        return store