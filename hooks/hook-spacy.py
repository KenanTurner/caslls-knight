# HOOK FILE FOR SPACY
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_all

# ----------------------------- SPACY -----------------------------
print('=================== SPACY =====================')
datas = collect_data_files("spacy")
hiddenimports = collect_submodules("spacy")

# ----------------------------- spacy models -----------------------------
# data = collect_all('en_core_web_sm')
# datas += data[0]
# binaries = data[1]
# hiddenimports += data[2]

data = collect_all('en_core_web_md')
datas += data[0]
binaries = data[1]
hiddenimports += data[2]

# data = collect_all('en_core_web_trf')
# datas += data[0]
# binaries = data[1]
# hiddenimports += data[2]

# alternatively, on PyInstaller command line you may just add:
# --collect-all=en_core_web_lg
# --collect-all=en_core_web_trf

print('=================== SPACY DONE =====================')
