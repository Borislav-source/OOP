class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f'{document.__repr__()}\n'
        return result

    @staticmethod
    def find_category(id, categories):
        for category in categories:
            if category.id == id:
                return category

    @staticmethod
    def find_topic(id, topics):
        for topic in topics:
            if topic.id == id:
                return topic

    @staticmethod
    def find_document(id, documents):
        for document in documents:
            if document.id == id:
                return document

    def add_category(self, category: object):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: object):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: object):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_category(category_id, self.categories)
        category.name = new_name

    def delete_category(self, category_id: int):
        category = self.find_category(category_id, self.categories)
        self.categories.remove(category)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_category(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def delete_topic(self, topic_id: int):
        topic = self.find_topic(topic_id, self.topics)
        self.topics.remove(topic)

    def edit_document(self, document_id: int,  new_file_name: str):
        document = self.find_document(document_id, self.documents)
        document.file_name = new_file_name

    def delete_document(self, document_id: int):
        document = self.find_document(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        document = self.find_document(document_id, self.documents)
        return document
