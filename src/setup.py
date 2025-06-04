from pathlib import Path
from typing import List

from config import Config


def setup_directories(config: Config):
    directories: List[Path] = [
        config.data_dir,
        config.input_dir,
        config.output_dir,
    ]

    for animal_id in range(1, config.number_of_animals + 1):
        animal = f"animal_{animal_id}"
        for state in ["rem", "nrem"]:
            for folder in ["original", "chunked"]:
                path = Path(config.output_dir) / animal / state / folder
                directories.append(path)

    for d in directories:
        Path(d).mkdir(parents=True, exist_ok=True)
