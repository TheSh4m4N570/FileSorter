# File Sorter

from pathlib import Path

# Define the possible extensions

list_extensions = {

    "music": ('.mp3', '.wav', '.flac'),
    "videos": ('.avi', '.mp4', '.gifs'),
    "images": ('.jpg', '.jpeg', '.bmp', '.png'),
    "documents": ('.txt', '.pptx', '.csv', '.xls', '.opd'),
    "Divers": 'autres'
}


default_path = Path.home() / "Downloads"
files = [f for f in default_path.iterdir() if f.is_file()]

for f in files:
    if f.suffix in list_extensions['music']:
        output_dir = default_path / 'music'
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir/f.name)

    elif f.suffix in list_extensions['videos']:
        output_dir = default_path / 'videos'
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir / f.name)

    elif f.suffix in list_extensions['images']:
        output_dir = default_path / 'images'
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir / f.name)

    elif f.suffix in list_extensions['documents']:
        output_dir = default_path / 'documents'
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir / f.name)

    else:
        output_dir = default_path / 'autres'
        output_dir.mkdir(exist_ok=True)
        f.rename(output_dir / f.name)



