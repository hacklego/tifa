from tif.formatters.formatter import Formatter

class FormatterCSV(Formatter):
    def format(self):
        output = list()
        for ioc in self.iocs:
            csv_line = ''
            for k, v in ioc.__dict__.items():
                if v:
                    try:
                        csv_line += v + ','
                    except:
                        csv_line += v.strftime("%Y-%B-%d")

            output.append(csv_line[:-1])

        return '\n'.join(output)
