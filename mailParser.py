import email

class mailParser(object):
    def __init__(self, rawMime):
        self._mime = email.message_from_string(rawMime)
        self._messageContent = ''
        self._sender = email.utils.parseaddr(self._mime['from'])[1]
        self._recipient = email.utils.parseaddr(self._mime['to'])[1]
        self._subject = self._mime['subject']

    def getSender(self):
        return self._sender

    def getRecipient(self):
        return self._recipient

    def getSubject(self):
        return self._subject

    def getBody(self):
        if self._mime.is_multipart():
            for part in self._mime.get_payload():
                if part.get_filename() != '':
                    self._messageContent += part.get_payload(decode=True)
                elif part.get_content_type() == 'text/plain':
                    self._messageContent += str(part.get_payload(decode=True))
        else:
            if self._mime.get_filename() != '':
                self._messageContent += self._mime.get_payload(decode=True)
            else:
                self._messageContent += str(self._mime.get_payload())
        self._messageContent = self._messageContent\
                .replace('\n', '')\
                .replace('\r', '')\
                .replace('=', '')
        return self._messageContent
    

