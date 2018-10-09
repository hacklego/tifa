from tif.formatters.formatter import Formatter

from flask import make_response


class FormatterYara(Formatter):
    def format(self):
        meta_values = ["id", "feed", "date", "name", "type", "info", "threat"]
        output = list()
        for ioc in self.iocs:
            yara_rule = 'rule {}'.format(str(ioc.id) + ' {\n')
            metas = list()
            strings = list()
            conditions= list()
            for k, v in ioc.__dict__.items():
                if k in meta_values and v:
                    metas.append('\t\t{} = "{}"'.format(k, v))
                elif v:
                    strings.append('\t\t${} = "{}" wide'.format(k, v))
                    conditions.append('${}'.format(k))
            yara_rule += '\tmeta:\n'
            yara_rule += '\n'.join(metas)
            yara_rule += '\n\tstrings:\n'
            yara_rule += '\n'.join(strings)
            yara_rule += '\n\tcondition:\n\t\t'
            yara_rule += ' or '.join(conditions)
            yara_rule += '\n}'
            output.append(yara_rule)

        output = make_response('\n'.join(output))
        output.headers["Content-type"] = "text/*"
        return output
