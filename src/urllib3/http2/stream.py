class HTTP2Stream:
    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id
        self._headers: list[tuple[bytes, bytes]] = []
    
    def add_header(self, name, value):
        self._headers.append(name, value)
