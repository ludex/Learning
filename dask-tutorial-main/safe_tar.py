"""Safe archive extraction helpers for the Dask tutorial downloader."""

from pathlib import Path
from tarfile import TarFile


class UnsafeArchiveError(ValueError):
    """Raised when a tar member could escape or alter the destination."""


def safe_extract(archive: TarFile, destination: str | Path) -> None:
    """Extract regular files/directories while rejecting traversal and links."""
    destination_path = Path(destination).resolve()
    destination_path.mkdir(parents=True, exist_ok=True)
    members = archive.getmembers()

    for member in members:
        if not (member.isfile() or member.isdir()):
            raise UnsafeArchiveError(
                f"Unsupported archive member type: {member.name!r}"
            )

        member_path = Path(member.name)
        if member_path.is_absolute():
            raise UnsafeArchiveError(f"Absolute archive path: {member.name!r}")

        resolved_target = (destination_path / member_path).resolve()
        if (
            resolved_target != destination_path
            and destination_path not in resolved_target.parents
        ):
            raise UnsafeArchiveError(f"Archive path traversal: {member.name!r}")

    archive.extractall(destination_path, members=members)
