import importlib

libraries = set()
libraries_missing = set()
for library in ["igraph", "rustworkx", "networkx", "intbitset"]:
    try:
        importlib.import_module(library)
        libraries.add(library)
    except ImportError:
        libraries_missing.add(library)
        pass
