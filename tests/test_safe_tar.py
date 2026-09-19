import io
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

TUTORIAL_DIRECTORY = Path(__file__).resolve().parents[1] / "dask-tutorial-main"
sys.path.insert(0, str(TUTORIAL_DIRECTORY))

from safe_tar import UnsafeArchiveError, safe_extract


def _archive_with(member: tarfile.TarInfo, content: bytes = b"") -> io.BytesIO:
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode="w") as archive:
        archive.addfile(member, io.BytesIO(content) if member.isfile() else None)
    stream.seek(0)
    return stream


class SafeTarTests(unittest.TestCase):
    def test_regular_file_is_extracted(self):
        member = tarfile.TarInfo("dataset/data.csv")
        content = b"year,value\n2024,1\n"
        member.size = len(content)

        with tempfile.TemporaryDirectory() as temporary_directory:
            with tarfile.open(fileobj=_archive_with(member, content)) as archive:
                safe_extract(archive, temporary_directory)
            extracted = Path(temporary_directory) / member.name
            self.assertEqual(extracted.read_bytes(), content)

    def test_parent_traversal_is_rejected(self):
        member = tarfile.TarInfo("../outside.txt")
        content = b"unsafe"
        member.size = len(content)

        with tempfile.TemporaryDirectory() as temporary_directory:
            with tarfile.open(fileobj=_archive_with(member, content)) as archive:
                with self.assertRaises(UnsafeArchiveError):
                    safe_extract(archive, temporary_directory)

    def test_symbolic_link_is_rejected(self):
        member = tarfile.TarInfo("dataset/link")
        member.type = tarfile.SYMTYPE
        member.linkname = "../../outside.txt"

        with tempfile.TemporaryDirectory() as temporary_directory:
            with tarfile.open(fileobj=_archive_with(member)) as archive:
                with self.assertRaises(UnsafeArchiveError):
                    safe_extract(archive, temporary_directory)


if __name__ == "__main__":
    unittest.main()
