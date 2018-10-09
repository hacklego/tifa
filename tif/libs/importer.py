import os
import types
import importlib
import importlib.machinery


class ImporterException(Exception):
    pass


class Importer:

    @staticmethod
    def import_subclasses_from_path(path, parent_class):
        if not os.path.isdir(path):
            raise ImporterException("%s is not directory" % path)

        subclasses = []
        for filepath in Importer._module_files_in_directory(path):
                file_subclasses = Importer._try_import_subclasses_from_file(filepath, parent_class)
                subclasses.extend(file_subclasses)
        return subclasses

    @staticmethod
    def _module_files_in_directory(path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                yield os.path.join(root, filename)

    @staticmethod
    def _try_import_subclasses_from_file(filepath, parent_class):
        try:
            return Importer.import_subclasses_from_file(filepath, parent_class)
        except ImporterException:
            return []

    @staticmethod
    def import_subclasses_from_file(filepath, parent_class):
        try:
            module = Importer.import_source_module(filepath)
            subclasses = Importer._extract_subclasses_in_module(module, parent_class)
        except ValueError as ex:
            raise ImporterException("Error importing %s: %s" % (filepath, str(ex)))
        except SyntaxError as ex:
            raise ImporterException("Syntax error in %s: %s" % (filepath, str(ex)))

        return subclasses

    @staticmethod
    def import_source_module(filepath):
        if not os.path.isfile(filepath):
            raise ImporterException("%s is not file" % filepath)

        loader = importlib.machinery.SourceFileLoader(filepath, filepath)
        mod = types.ModuleType(loader.name)
        loader.exec_module(mod)
        return mod

    @staticmethod
    def _extract_subclasses_in_module(module, parent_class):
        return [subclass for subclass in module.__dict__.values() if Importer._is_subclass(subclass, parent_class) if subclass != parent_class]

    @staticmethod
    def _is_subclass(subclass, parent_class):
        try:
            return issubclass(subclass, parent_class)
        except TypeError:
            return False
