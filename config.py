from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    data_dir: Path
    raw_data_dir: Path
    input_dir: Path
    output_dir: Path
    number_of_animals: int
    verbose: bool
    time_chunks: int

    @staticmethod
    def from_yaml(yaml_path: str) -> "Config":
        import yaml

        with open(yaml_path, "r") as file:
            data = yaml.safe_load(file)
        return Config(**data)


config = Config.from_yaml("config.yaml")
