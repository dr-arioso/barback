# core/errors.py
class PipelineError(Exception):
    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code


class FileError(Exception):
    def __init__(self, message: str, code: int = 2):
        super().__init__(message)
        self.code = code


class BackendError(Exception):
    def __init__(self, message: str, code: int = 3):
        super().__init__(message)
        self.code = code


class BrandError(Exception):
    def __init__(self, message: str, code: int = 4):
        super().__init__(message)
        self.code = code
