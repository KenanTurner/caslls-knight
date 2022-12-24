# HOOK FILE FOR SPACY TRANSFORMERS
from PyInstaller.utils.hooks import collect_all

# ----------------------------- TRANSFORMERS -----------------------
print('=================== TRANSFORMERS =====================')
datas = []
binaries = []
hiddenimports = []

# There should be a way to get this list, perhaps from importlib_metadata
# Hint: 
# >>> from importlib_metadata import packages_distributions
# >>> import en_core_web_trf
# >>> nlp = en_core_web_trf.load()
# >>> modules = [k for k,v in packages_distributions().items()]
# modules = ['altgraph', 'blis', 'catalogue', 'certifi', 'charset_normalizer', 'click', 'colorama', 'confection', 'cymem', 'en_core_web_trf', 'filelock', 'future', 'libfuturize', 'libpasteurize', 'past', 'huggingface_hub', 'idna', 'importlib_metadata', 'jinja2', 'langcodes', 'markupsafe', 'murmurhash', 'numpy', 'packaging', 'pathy', 'ordlookup', 'pefile', 'peutils', 'pip', 'preshed', 'pydantic', 'PyInstaller', '_pyinstaller_hooks_contrib', 'win32ctypes', '_yaml', 'yaml', 'regex', 'requests', '_distutils_hack', 'pkg_resources', 'setuptools', 'six', 'smart_open', 'spacy', 'spacy_alignments', 'spacy_legacy', 'spacy_loggers', 'spacy_transformers', 'srsly', 'thinc', 'tokenizers', 'caffe2', 'functorch', 'torch', 'torchgen', 'tqdm', 'transformers', 'typer', 'typing_extensions', 'urllib3', 'wasabi', 'wheel', 'zipp']
modules = ['spacy_transformers', 'transformers', 'torch', 'srsly', 'spacy_alignments', 'filelock', 'numpy', 'packaging', 'regex', 'requests', 'tokenizers', 'tqdm', 'typing_extensions', 'catalogue', 'charset_normalizer', 'colorama']
for mod in modules:
    data = collect_all(mod)
    datas += data[0]
    binaries += data[1]
    hiddenimports += data[2]

# MXB: This is not the right way to write a hook file, but this gets transformers imports and it works.
# When transformers update, we will have to update the above list...

print('=================== TRANSFORMERS DONE =====================')