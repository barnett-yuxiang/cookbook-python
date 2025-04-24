import os
import toml

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'test-toml-config.toml')

config = toml.load(config_path)
print(config)

print(config['huggingface']['api_base'])
