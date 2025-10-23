import yaml 




if __name__ == "__main__":
  with open("etl_factory_pattern_demo/config.yaml") as f:
    config = yaml.safe_load(f)

  print(config)
