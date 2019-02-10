class Config:
    def __init__(self, file_scheme: str, action: str, from_path: str, to_path: str, ids: []):
        self.file_scheme = file_scheme
        self.action = action
        self.from_path = from_path
        self.to_path = to_path
        self.ids = ids