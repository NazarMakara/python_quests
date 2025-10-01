from abc import ABC, abstractmethod

docs = ["report", "invoice", "contract", "letter"]

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Report(Document):
    def render(self) -> str:
        return "Report document"

class Invoice(Document):
    def render(self) -> str:
        return "Invoice document"

class Contract(Document):
    def render(self) -> str:
        return "Contract document"

class NullDocument(Document):
    def render(self) -> str:
        return "Unknown document type"

class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        if doc_type == "report":
            return Report()
        elif doc_type == "invoice":
            return Invoice()
        elif doc_type == "contract":
            return Contract()
        else:
            return NullDocument()

for i in docs:
    doc = DocumentFactory.create(i)
    print(doc.render())