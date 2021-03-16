from abc import ABCMeta, abstractmethod


class IContent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_content(self):
        pass


class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    def set_content(self):
        return f"<myML>{self.content}</myML>"


class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = MyContent.set_content(content)

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
