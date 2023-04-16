from .item import Item


class Email(Item):
    def __connect(self, smpt_server):
        pass

    def __email_body(self):
        return f"""
        Hello Recipient,
        We have {self.quantity} of the following item: {self.name}.
        Regards, ItemWarehouse.
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("server")
        self.__email_body()
        self.__send()