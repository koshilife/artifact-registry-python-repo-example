from flask import jsonify

def main(request):
    return jsonify(dict(result='ok'))
