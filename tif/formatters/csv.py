from tif.formatters.formatter import Formatter

from flask import make_response


class FormatterCSV(Formatter):
    def format(self):
        output = list()
        for ioc in self.iocs:
            csv_line = ''
            exclussions = ['id']
            try:
                ioc.date = ioc.date.strftime("%Y-%B-%d")
            except:
                pass
            for k, v in ioc.__dict__.items():
                if k not in exclussions and v:
                    csv_line += v + ','

            output.append(csv_line[:-1])

        output = make_response('\n'.join(output))
        output.headers["Content-type"] = "text/csv"
        return output
