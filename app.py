from flask import Flask
from flask_restful import Resource, Api

from tif.rest.base_url import Rest
from tif.rest.key import Key
from tif.rest.value import Value
from tif.rest.last import Last

app = Flask(__name__)

api = Api(app)

api.add_resource(Rest, '/rest')
api.add_resource(Key, '/rest/<string:ioc_key>')
api.add_resource(Value, '/rest/<string:ioc_key>/<string:ioc_value>')
api.add_resource(Last, '/rest/last/<int:days>')


if __name__ == '__main__':
    app.run(debug=True)
