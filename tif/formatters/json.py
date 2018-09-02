from tif.formatters.formatter import Formatter

from flask import make_response, jsonify


class FormatterJson(Formatter):
    def format(self):
        iocs = [str(ioc) for ioc in self.iocs]
        return jsonify(iocs)
