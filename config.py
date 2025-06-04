from dataclasses import dataclass


@dataclass
class Config:
    input_folder: str
    output_folder: str
    number_of_animals: int
    verbose: bool
    time_chunks: int


config = Config(
    input_folder="data/input",
    output_folder="data/output",
    number_of_animals=7,
    verbose=True,
    time_chunks=3600,  # 1 Hour chunks
)
