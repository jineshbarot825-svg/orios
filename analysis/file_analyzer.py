import hashlib
from pathlib import Path


def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    """Return SHA-256 for an authorized local file."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def analyze_file(path: str) -> dict:
    """Return metadata and hash for a local file."""
    target = Path(path)
    stat = target.stat()
    return {
        "path": str(target.resolve()),
        "name": target.name,
        "size_bytes": stat.st_size,
        "suffix": target.suffix,
        "sha256": sha256_file(str(target)),
    }
