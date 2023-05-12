#!/usr/bin/python3
"""FileStorage autoinit module"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
