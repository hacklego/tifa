from tif.formatters.formatter import Formatter

from flask import make_response

import csv
import io

class FormatterCSV(Formatter):
    def format(self):
        output = list()
        for ioc in self.iocs:
            csv_line = list()
            exclussions = ['id']
            try:
                ioc.date = ioc.date.strftime("%Y-%B-%d")
            except:
                pass
            for k, v in ioc.__dict__.items():
                if k not in exclussions and v:
                    csv_line.append(v)
                    
            output.append(csv_line)

        si = io.StringIO()
        cw = csv.writer(si)
        cw.writerows(output)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"
        return output
