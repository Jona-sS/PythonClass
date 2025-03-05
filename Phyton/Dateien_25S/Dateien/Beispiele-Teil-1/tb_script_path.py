
# tb_script_path.py

import os

# Skriptpfad und -namen ausgeben
print(__file__)
print(os.path.basename(__file__))

# Gerätemanager aufrufen, wenn unter Windows
if os.name == "nt": os.system("devmgmt.msc")


