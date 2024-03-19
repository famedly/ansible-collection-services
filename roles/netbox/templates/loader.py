import yaml
import os

def __pfusch(path):
  for node in os.scandir(path):
    if node.is_dir():
      load_dir(node.path)
    else:
      for k,v in yaml.safe_load(open(node.path)).items():
        globals()[k] = v # we just add *all* the kv pairs to the scope netbox will use to access it's config

__pfusch(os.environ.get('NETBOX_YAML_CONFIG_DIR','/opt/netbox/config'))
