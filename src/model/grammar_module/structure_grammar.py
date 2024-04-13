import re

from lark import Lark

useful_camps_grammar = """
        start: FROM | TO | SUBJECT | DATE | ID
        
        FROM:  /(\\n|^)From: / FROM_VALUE
        TO:  /(\\n|^)To: / EMAIL_ADDRESS_LIST 
        SUBJECT:  /(\\n|^)Subject:/ CAMP_VALUE 
        DATE:  /(\\n|^)Date: / DATE_VALUE 
        ID: /(\\n|^)Message-ID:/ CAMP_VALUE
        
        FROM_VALUE: EMAIL_ADDRESS | /((?!<).)*/ "<" EMAIL_ADDRESS ">"
        EMAIL_ADDRESS_LIST: FROM_VALUE (", " FROM_VALUE)*
        DATE_VALUE: /\\w*, \\d{1,2} [a-zA-Z]{3} \\d{4} \\d{2}:\\d{2}:\\d{2} (\\+|-)\\d+/
        
        CAMP_VALUE: /(\\s.*)?((\\n(?!--)(\\s|\\t)(?!--).+)*)?/
        EMAIL_ADDRESS: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}/
        """

structure_grammar = """
        start: CAMP+ BOUNDARY BODY_TEXT BODY_HTML
        
        CAMP: /(?!--)//(\\n|^)/CAMP_KEY ":" CAMP_VALUE
        BOUNDARY: /--\\w*/
        BODY_TEXT: /(\\n|^)?Content-Type: text\\/plain.*\\n.*/ TEXT_BODY /--\\w*/
        BODY_HTML: /(\\n|^)?Content-Type: text\\/html.*\\n.*/ TEXT_BODY /--\\w*--/
        
        CAMP_KEY: /(\\w-?)*/
        CAMP_VALUE: /(\\s.*)?((\\n(?!--)(\\s|\\t)(?!--).+)*)?/
        TEXT_BODY: /((?!Content-Type: text).*\\n)*/
        
        %import common.WS
        %ignore WS
        """

structure_parser = Lark(structure_grammar, parser="lalr")
useful_camps_parser = Lark(useful_camps_grammar, parser="lalr")


def validate_structure(email):
    """
    Validates the structure of an email using the `structure_parser` parser.
    Args:
        email (str): The email to be validated.
    Returns:
        The parsed email if the structure is valid, otherwise None.
    """
    try:
        return structure_parser.parse(email)
    except Exception as e:
        return None

def get_body(text, type):
    """
    Extracts the body content from the given text based on the specified type.
    Args:
        text (str): The input text containing the body content.
        type (str): The type of content to extract. Must be either 'text' or 'html'.
    Returns:
        str: The extracted body content.
    Raises:
        ValueError: If the specified type is invalid.
    """
    if type == "text":
        exp = re.compile(
            r"^Content-Transfer-Encoding:.*\n((.*\n)*)--\w*$", re.MULTILINE
        )
    elif type == "html":
        exp = re.compile(
            r"^Content-Transfer-Encoding:.*\n((.*\n)*)--\w*--$", re.MULTILINE
        )
    else:
        raise ValueError("Invalid type. Must be 'text' or 'html'.")
    body = exp.search(text).group(1)
    return body

def get_email_metadata(camps:list):
    """
    Extracts metadata from a list of email camps.

    Args:
        camps (list): A list of email camps.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """
    metadata = {}
    for camp in camps:
        try:
            token = useful_camps_parser.parse(camp).children[0];
            metadata[token.type] = re.search(r"\n?((\w|-)*): (.*)", token.value).group(3)
        except Exception as e:
            continue
    return metadata

def parse_email(email):
    """
    Parses the given email and returns a dictionary with the parsed information.
    Args:
        email (str): The email to be parsed.
    Returns:
        dict: A dictionary containing the parsed information. The dictionary has the following keys:
            - "CAMPS": A list of camp objects extracted from the email.
            - "BOUNDARY": The boundary object extracted from the email.
            - "BODY_TEXT": The text body extracted from the email.
            - "BODY_HTML": The HTML body extracted from the email.
    """
    tree = validate_structure(email)
    if tree:
        camps = [camp for camp in tree.children if camp.type == "CAMP"]
        return {
            "CAMPS": camps,
            "BOUNDARY": tree.children[-3],
            "BODY_TEXT": get_body(tree.children[-2], "text"),
            "BODY_HTML": get_body(tree.children[-1], "html"),
            "META": get_email_metadata(camps)
        }
    else:
        return None

def parse_emails(emails:list):
    """
    Parses a list of emails and returns a list of dictionaries with the parsed information.
    Args:
        emails (list): A list of emails to be parsed.
    Returns:
        list: A list of dictionaries containing the parsed information for each email.
    """
    return {parse_email(email)["META"]["ID"]:parse_email(email) for email in emails if email and parse_email(email) and "ID" in parse_email(email)["META"].keys()}
