import re
from datetime import datetime

# Regular expression to find the task list
task_list_pattern = re.compile(r"((t|T)areas pendientes|(t|T)areas por hacer|(t|T)areas).*:\s*([\s\S]+?)(?:\n\n|\n$|$)")

# Regular expression to extract tasks
task_pattern_explicit = re.compile(r"([a-zA-Z0-9áéíóú]+\.?,?:?\s+|[ivxlcdm]+\.?\s*)\s*(.{5,})", re.MULTILINE)

# Regular expression to extract actions from an email
action_pattern = re.compile(r"(?:está\s+encargad[oa]?|debe|tendrá[s]?\s+que)\s+(?:de(?:l)?\s+)?([^.,]+)[.,]")

# Regular expression to extract a single action or task from an email
single_action_pattern = re.compile(r"(Tu\s+tarea\s+es|Necesito\s+que\s+hagas)\s+(((?!\.).)*)\.")

# Regular expression to find a task list without a header ("Tasks: ...")
task_list_pattern_no_header = re.compile(r"(\d+\.\s*\[^\n\]+\n+)+")

# Regular expression to extract dates
date_pattern= r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|(\d{1,2} (de )?[A-Za-z]{4,10}( de[l]?)? \d{2,4})"

# Function to extract tasks from an email
def extract_tasks(email):
    """
    Extracts tasks from the given email.

    Args:
        email (str): The email from which to extract tasks.

    Returns:
        list: A list of extracted tasks. If no tasks are found, returns None.
    """
    tasks = []
    task_list_match = task_list_pattern.search(email)
    if action_pattern.search(email):
        task_matches = action_pattern.findall(email)
        tasks.append(task_matches[0].strip())
    elif single_action_pattern.search(email):
        task_matches = single_action_pattern.findall(email)
        for __, task, _ in task_matches:
            clean_task = task.strip()
            tasks.append(clean_task)
    elif task_list_pattern_no_header.search(email):
        task_list_text = task_list_pattern_no_header.search(email).group()
        task_matches = task_pattern_explicit.findall(task_list_text)
        for match in task_matches:
            tasks.append(match)
    elif task_list_match:
        task_list_text = task_list_match.group(5)
        task_matches = task_pattern_explicit.findall(task_list_text)
        for num, match in task_matches:
            tasks.append(match)
    else: 
        tasks = None
    return tasks

# Function to extract links from an email
def extract_links(email):
    """
    Extracts links from the given email.

    Args:
        email (str): The email from which to extract links.

    Returns:
        list: A list of extracted links. If no links are found, returns None.
    """
    links = []
    link_matches = re.findall(r"(?:(?:https?|ftp):\/\/)?(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:\/[\w#!:.?+=&%@!\-\/]+)?", email)
    for link in link_matches:
        links.append(link)
    if len(links) == 0:
        links = None
    return links

def extract_events(email):
    """
    Extracts events from an email.

    Args:
        email (str): The email content.

    Returns:
        list: A list of dictionaries containing information about the extracted events. Each dictionary has the following keys:
            - 'type': The type of the event (e.g., 'reunión', 'evento', 'cita').
            - 'date': The date of the event in the format 'dd/mm/yyyy'.
            - 'time': The time of the event in the format 'hh:mm'.
            - 'location': The location of the event.
            - 'datetime': The datetime object representing the date and time of the event.

    """
    events = []
    event_pattern = re.compile(r"(\breuni[oó]n|\bevento|\bcita):?\s*((\bel|\bpara\s+\bel)?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{4}))?\s*((a\s*la[s]?)?\s*(\d{1,2}:\d{2}))?\s*(en\s*((\s*\w+)+)(\.|$))?",re.IGNORECASE,)
    matches = event_pattern.findall(email)

    if not matches:
        return None

    for match in matches:
        event_info = match[0].strip().lower()
        event_info += " " + match[1].strip() if match[2] else ""
        event_info += " " + match[4].strip() if match[4] else ""
        event_info += " " + match[7].strip() if match[7] else ""
        
        events.append(f"{event_info.capitalize()}")

    return events


def extract_code(email):
    """
    Extracts a verification code from the given email.

    Args:
        email (str): The email from which to extract the verification code.

    Returns:
        str: The verification code, if found. Otherwise, returns None.
    """
    code_pattern = re.compile(r"(Código de verificación:\s*\d+)|(código de \w*:?\s*\"\w*\")", re.IGNORECASE)
    match = code_pattern.search(email)

    if match:
        return [match.group(2) if match.group(2) else match.group(1)]
    else:
        return None

def extract_greetings(email):
    """
    Extracts greetings from the given email.

    Args:
        email (str): The email from which to extract greetings.

    Returns:
        list: A list of greetings found in the email.
    """
    greetings = []
    greeting_pattern = re.compile(r"(Hola|Saludos|Estimado|Querido)\s*[a-zA-Z]+,?")
    matches = greeting_pattern.findall(email)

    for match in matches:
        greetings.append(match)

    if not matches:
        greetings = None
        
    return greetings

def extract_dates(email):
    """
    Extracts dates from the given email.
    Args:
        email (str): The email from which to extract dates.
    Returns:
        list: A list of extracted dates. If no dates are found, returns None.
    """
    dates = []
    date_regex = re.compile(date_pattern)
    matches = date_regex.findall(email)
    for match in matches:
        try:
            date = None
            if "/" in match[0]:
                date = datetime.strptime(match[0], "%d/%m/%Y").date()
            elif "-" in match[0]:
                date = datetime.strptime(match[0], "%d-%m-%Y").date()
            else:
                date = match[1]
            dates.append(date)
        except ValueError:
            continue
    if len(dates) == 0:
        dates = None
    return dates

def extract_physical_addresses(email):
    """
    Extracts physical addresses from the given email.
    Args:
        email (str): The email from which to extract physical addresses.
    Returns:
        list: A list of extracted physical addresses. If no addresses are found, returns None.
    """
    addresses = []

    address_pattern = re.compile(r"\b(?:Calle|Cra|Avenida|Carrera)\s+\d+[A-Za-z]*\s*(?:#?\d+[A-Za-z\-]*)*,?\s*(?:\s*piso\s*\d+)?(?:\s*apto\s*\d+)?(?:\s*local\s*\w+)?\b", re.IGNORECASE)

    matches = address_pattern.findall(email)

    for match in matches:
        addresses.append(match)

    if len(addresses) == 0:
        addresses = None

    return addresses

# Extract important information from the email
def extract_info(email):
    """
    Extracts important information from the given email.

    Args:
        email (str): The email from which to extract information.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    info = {}
    info["tasks"] = extract_tasks(email)
    info["links"] = extract_links(email)
    info["events"] = extract_events(email)
    info["code"] = extract_code(email)
    info["greetings"] = extract_greetings(email)
    info["dates"] = extract_dates(email)
    info["physical_addresses"] = extract_physical_addresses(email)

    return info

info = ["tasks", "links", "events", "dates", "code", "greetings", "physical_addresses"] # List od data to be shown in the interface

