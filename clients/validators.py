import re
from validate_docbr import CPF


def name_is_valid(name):
    """Check if the Name is Valid"""
    return name.isalpha()


def document_is_valid(document):
    """Check if the Document is Valid"""
    cpf = CPF()
    return cpf.validate(document)


def phone_is_valid(phone):
    """Check if the Phone is Valid"""
    model = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(model, phone)

    return response
