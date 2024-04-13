import re

from model.transducers_module.transducers import *


def parse_email_address(address):
    """
    Parses an email address and returns a tuple with the name and the email.

    Args:
        address (str): The email address to be parsed.

    Returns:
        tuple: A tuple containing the name and the email.
    """
    match = re.search(r"(=\?UTF-8\?Q\?(.*)\?=|(.*)) <(.*)>", address)
    if match:
        groups = match.groups()
        if groups[1]:
            return (translate(groups[1]), groups[3])
        elif groups[2]:
            return (groups[2], groups[3])
        else:
            return None
    else:
        return (None, address)


def parse_email_address_list(list):
    """
    Parses a list of email addresses and returns a list of tuples with the names and the emails.

    Args:
        list (str): The list of email addresses to be parsed.

    Returns:
        list: A list of tuples containing the names and the emails.
    """
    return [parse_email_address(address) for address in list.split(", ")]

def parse_utf_text(text):
    match = re.search(r"=\?UTF-8\?Q\?(.*)\?=|(.*)", text)

    if match:
        groups = match.groups()
        if groups[0]:
            return translate(groups[0])
        elif groups[1]:
            return groups[1]
        else:
            return None
