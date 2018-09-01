from tif.formatters.formatter import Formatter
from tif.formatters.csv import FormatterCSV

class FormatterFactory:
    
    formatters = {
            'csv': FormatterCSV,
            }
    
    @classmethod
    def format(cls, iocs, formatter):
        formatter = cls.formatters.get(formatter)(iocs)
        return formatter.format()
        
        
