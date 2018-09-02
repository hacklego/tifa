from tif.formatters.formatter import Formatter
from tif.formatters.json import FormatterJson
from tif.formatters.csv import FormatterCSV
from tif.formatters.yara import FormatterYara

class FormatterFactory:
    
    formatters = {
            'csv': FormatterCSV,
            'yara': FormatterYara
            }
    
    @classmethod
    def format(cls, iocs, formatter):
        formatter = cls.formatters.get(formatter, FormatterJson)(iocs)
        return formatter.format()
        
        
