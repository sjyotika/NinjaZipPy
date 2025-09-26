import py7zr
from pathlib import Path

def zip_to_7z(source, dest):
    """Compress file/folder into .7z archive."""
    source_path = Path(source)
    dest_path = Path(dest)

    with py7zr.SevenZipFile(dest_path, 'w') as archive:
        if source_path.is_dir():
            archive.writeall(source_path, arcname=source_path.name)
        else:
            archive.write(source_path, arcname=source_path.name)


def unzip_from_7z(archive_file, dest_folder):
    """Extract .7z archive into a folder."""
    archive_path = Path(archive_file)
    dest_path = Path(dest_folder)
    dest_path.mkdir(parents=True, exist_ok=True)

    with py7zr.SevenZipFile(archive_path, 'r') as archive:
        archive.extractall(path=dest_path)
