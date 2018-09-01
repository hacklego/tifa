from flask import Flask
from flask_restful import Resource, Api

from tif.rest.base_url import Rest, RestFormat
from tif.rest.key import Key, KeyFormat
from tif.rest.value import Value, ValueFormat
from tif.rest.last import Last, LastFormat

app = Flask(__name__)

api = Api(app)

FORMATTER = '/format/<string:formatter>'
BASE_URL = '/rest'

api.add_resource(Rest, BASE_URL)
api.add_resource(RestFormat, BASE_URL + FORMATTER)
api.add_resource(Key, BASE_URL + '/<string:ioc_key>')
api.add_resource(KeyFormat, BASE_URL + '/<string:ioc_key>' + FORMATTER)
api.add_resource(Value, BASE_URL + '/<string:ioc_key>/<string:ioc_value>')
api.add_resource(ValueFormat, BASE_URL + '/<string:ioc_key>/<string:ioc_value>' + FORMATTER)
api.add_resource(Last, BASE_URL + '/last/<int:days>')
api.add_resource(LastFormat, BASE_URL + '/last/<int:days>' + FORMATTER)


if __name__ == '__main__':
    app.run(debug=True)
