import functools

from flask import (Blueprint, request,jsonify)
from werkzeug.security import generate_password_hash
from .db import get_db

bp = Blueprint('allies', __name__, url_prefix='/allies')


@bp.route('/')
def index():
    return "Support engineer technical challenge API"

@bp.route('/<allyId>/credentials',methods=['GET','POST'])
def credentials(allyId):
    if request.method == 'GET':
        db = get_db()
        with db:
            with db.cursor() as curs:
                curs.execute("SELECT * FROM public.stores WHERE id = %s",(allyId,))
                result = curs.fetchone()
                if result == None:
                    return jsonify(message='Ally not found',status=404),404   
                elif(result[1]['credentials'] != None):
                    return jsonify(message="Ally has credentials set!"),200
                else:
                    return jsonify(message="Ally does not have credentials set!"),400
    elif request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        db = get_db()
        allyName = None

        if not username:
            return jsonify(message="Username and password are required."),400
        elif not password:
            return jsonify(message="Password is required."),400
        else:
            with db:
                with db.cursor() as curs:
                    curs.execute("SELECT * FROM public.stores WHERE id = %s",(allyId,))
                    result = curs.fetchone()
                    if result == None:
                        return jsonify(message="Ally not found"),404   
                    else:
                        hashed_creds = '"%s"'%generate_password_hash(password)
                        allyName=result[1]['name']
                        curs.execute("UPDATE public.stores s SET ""data""=jsonb_set(to_jsonb(s.""data""),'"+"{"+"credentials"+"}"+"',%s,false) WHERE id=%s;",(hashed_creds,allyId))
                db.commit()
                return jsonify(message="Credentials added",
                    AllyId=allyId,
                    AllyName=allyName),200
    else:
        return jsonify(message= "It was not possible to process your request, check the available methods"), 400


@bp.errorhandler(400)
def not_found(error):
    return jsonify(message=str(error), status=400), 400

@bp.errorhandler(404)
def url_not_found(error):
    return jsonify(message=str(error), status=404), 404

@bp.errorhandler(500)
def not_found(error):
    return jsonify(message=str(error), status=500), 500