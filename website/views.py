from flask import Blueprint,request, jsonify, render_template,current_app,send_from_directory ,request,redirect,url_for ,abort,flash, jsonify,request,session ,send_file,Response














views = Blueprint('views', __name__)





@views.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@views.route('/', methods=['GET', 'POST'])
def infoPage():
    return render_template("indxcalculator.html" )

   


@views.route('/ndvi-calculator', methods=['get','post'])
def ndvi_calcul():
    return render_template('ndvi.html')


@views.route('/ndbi-calculator', methods=['get','post'])

def ndbi_calcul():
    return render_template('ndbi.html')


@views.route('/ndwi-calculator', methods=['get','post'])

def ndwi_calcul():
    return render_template('ndwi.html')