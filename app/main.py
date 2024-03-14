from __future__ import annotations
import traceback
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: traceback
    ) -> None:
        try:
            with open(self.filename, "r") as f:
                f.read()
            os.remove(self.filename)
        except FileNotFoundError:
            pass
