import yaml
from jinja2 import Template

with open('data.yml') as data_file:
    config_data = yaml.safe_load(data_file)

with open('vhosts.j2') as template_file:
    template_html = template_file.read()

template = Template(template_html)
vhosts_conf = template.render(config_data)

with open('vhosts.conf', 'w') as vhosts_file:
    vhosts_file.write(vhosts_conf)
