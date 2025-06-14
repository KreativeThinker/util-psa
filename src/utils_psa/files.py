import shutil
from pathlib import Path
from typing import List

from src.utils_psa.config import config


def get_all_animals(raw_dir: Path) -> List[Path]:
    """List all animal folders inside raw data dir"""
    return [d for d in raw_dir.iterdir() if d.is_dir()]


def get_all_sessions(animal_dir: Path) -> List[Path]:
    """List all sessions (BL, test) inside an animal dir"""
    return [s for s in animal_dir.iterdir() if s.is_dir()]


def find_cfft_file(session_dir: Path) -> Path:
    """Find the cFFT file inside a session folder"""
    for file in session_dir.glob("*_cFFT.csv"):
        return file
    raise FileNotFoundError(f"No cFFT file found in {session_dir}")


def copy_cfft_to_input(animal_name: str, session_name: str, source_file: Path):
    """Copy cleaned cFFT file to input folder structure"""
    dest_dir = Path(config.input_dir) / animal_name / session_name
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "Traces_cFFT.csv"
    shutil.copy(source_file, dest)
    if config.verbose:
        print(f"Copied {source_file} to {dest}")


def clean_cfft_file(path: Path):
    """Drops first 20 lines of metadata from cFFT file"""
    lines = path.read_text().splitlines()[20:]
    path.write_text("\n".join(lines))
    if config.verbose:
        print(f"Cleaned metadata from {path}")


def process_all_cfft_files():
    raw_dir = Path(config.raw_data_dir)

    for animal_dir in get_all_animals(raw_dir):
        animal_name = animal_dir.name
        for session_dir in get_all_sessions(animal_dir):
            session_name = session_dir.name
            try:
                cfft = find_cfft_file(session_dir)
                clean_cfft_file(cfft)
                copy_cfft_to_input(animal_name, session_name, cfft)
            except FileNotFoundError as e:
                if config.verbose:
                    print(e)
