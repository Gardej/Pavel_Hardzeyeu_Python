import sys
import platform
import json
import pip
import pkg_resources
import yaml
from distutils.sysconfig import get_python_lib

# 1. version
a1 = platform.python_version()
# 2. virtual environment (name)
a2 = sys.base_prefix
# 3. python executable location
a3 = sys.executable
# 4. pip location (each python version has its own version of pip)
a4 = pip.__path__[0]
# 5. PYTHONPATH
a5 = sys.path[0]
# 6. installed packages: name, version
inst_pack = {}
for d in pkg_resources.working_set:
    inst_pack[d.project_name] = d.version
# 7. site-packages location
a6 = get_python_lib()

my_lib = {'Metrics ': []}
my_lib['Metrics '].append([{
    'Version number': str(a1),
    'Virtual environment': str(a2),
    'Python executable location': str(a3),
    'Pip location': str(a4),
    'PYTHONPATH': str(a5),
    'Installed packages': inst_pack,
    'Site-packages location': str(a6)
}])
with open('metrics.json', 'w') as outfile:
    json.dump(my_lib, outfile, indent=3)

with open('metrics.yaml', 'w') as file:
    yaml.dump(my_lib, file)
