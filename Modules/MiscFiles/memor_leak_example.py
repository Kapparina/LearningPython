class ClientConnection(...):
    def __del__(self):
        if self.socket is not None:
            self.socket.close()
            self.socket = None