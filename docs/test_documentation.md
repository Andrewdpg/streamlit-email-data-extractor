# Tests documentation

## Grammar Module

### Scenarios

#### Table 1: Scenarios

| Name               | Class                  | Scenario                                      |
| ------------------ | ---------------------- | --------------------------------------------- |
| Validate Structure | test_structure_grammar | Verify if the structure of an email is valid. |
| Get Body           | test_structure_grammar | Retrieve the body of an email.                |
| Get Metadata       | test_structure_grammar | Obtain metadata from an email.                |
| Parse Email        | test_structure_grammar | Parse a single email.                         |
| Parse Emails       | test_structure_grammar | Parse multiple emails.                        |
| Parse Empty Emails | test_structure_grammar | Parse empty emails.                           |

### Use Cases

#### Table 2: Use Cases

| Class                  | Method                  | Scenario           | Input Values                                                                       | Expected Results                                                                                                                                                                                                                        |
| ---------------------- | ----------------------- | ------------------ | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| test_structure_grammar | test_validate_structure | Validate Structure | SAMPLE_EMAIL_1, True                                                               | Should return True if the structure is valid, False otherwise.                                                                                                                                                                          |
| test_structure_grammar | test_get_body           | Get Body           | SAMPLE_EMAIL_1, "text", "Este es el cuerpo en texto plano."                        | Should return the text body of the email: "Este es el cuerpo en texto plano."                                                                                                                                                           |
| test_structure_grammar | test_get_body           | Get Body           | SAMPLE_EMAIL_1, "html", "`<html><body>`Este es el cuerpo en HTML.`</body></html>`" | Should return the HTML body of the email: "`<html><body>`Este es el cuerpo en HTML.`</body></html>`"                                                                                                                                    |
| test_structure_grammar | test_get_body           | Get Body           | SAMPLE_EMAIL_1, "invalid", ValueError                                              | Should raise ValueError when attempting to retrieve an invalid body type.                                                                                                                                                               |
| test_structure_grammar | test_get_email_metadata | Get Metadata       | SAMPLE_FIELDS_1, EXPECTED_METADATA_1                                               | Should return the extracted metadata from the email in the format: {"FROM": "sender@example.com", "TO": "recipient@example.com", "SUBJECT": "Correo de Prueba", "DATE": "Mon, 12 Apr 2024 10:00:00 +0000", "ID": "<12345@example.com>"} |
| test_structure_grammar | test_parse_email        | Parse Email        | SAMPLE_EMAIL_1, True                                                               | Should return a dictionary with the parsed email information.                                                                                                                                                                           |
| test_structure_grammar | test_parse_email        | Parse Email        | "Invalid email content", False                                                     | Should return False if the email content is invalid.                                                                                                                                                                                    |
| test_structure_grammar | parse_emails            | Parse Emails       | [SAMPLE_EMAIL_1, SAMPLE_EMAIL_2], 2                                                | Should return a list of dictionaries with the parsed email information for each valid email in the input list.                                                                                                                          |
| test_structure_grammar | parse_emails            | Parse Emails       | [""], 0                                                                            | Should return an empty dictionary if there are no valid emails in the input list.                                                                                                                                                       |

## Transducers Module

### Scenarios

#### Table 1: Scenarios

| Name                                 | Class                        | Scenario                                                |
| ------------------------------------ | ---------------------------- | ------------------------------------------------------- |
| Translate Single Word                | test_transducers_translate_1 | Translate a single word with no special characters.     |
| Translate Multi-Word                 | test_transducers_translate_2 | Translate multiple words with no special characters.    |
| Translate Special Chars              | test_transducers_translate_3 | Translate text containing special characters.           |
| Translate Multi-Word & Special Chars | test_transducers_translate_4 | Translate multiple words containing special characters. |

### Use Cases

#### Table 2: Use Cases

| Class       | Method                       | Scenario                             | Input Values                                  | Expected Results                                           |
| ----------- | ---------------------------- | ------------------------------------ | --------------------------------------------- | ---------------------------------------------------------- |
| Transducers | test_transducers_translate_1 | Translate Single Word                | A single word without special characters.     | Should return the same word without any translation.       |
| Transducers | test_transducers_translate_2 | Translate Multi-Word                 | Multiple words without special characters.    | Should return the same text without any translation.       |
| Transducers | test_transducers_translate_3 | Translate Special Chars              | Text containing special characters.           | Should return the text with special characters translated. |
| Transducers | test_transducers_translate_4 | Translate Multi-Word & Special Chars | Multiple words containing special characters. | Should return the text with special characters translated. |

## Regex Module

### Scenarios

#### Table 1: Scenarios

| Name              | Class                     | Scenario                                                 |
| ----------------- | ------------------------- | -------------------------------------------------------- |
| Extract Events    | test_regex_info_extractor | Extract events from email content.                       |
| Extract Dates     | test_regex_info_extractor | Extract dates from email content.                        |
| Extract Addresses | test_regex_info_extractor | Extract physical addresses from email content.           |
| Extract Links     | test_regex_info_extractor | Extract links from email content.                        |
| Extract Tasks     | test_regex_info_extractor | Extract tasks from email content.                        |
| Extract Info      | test_regex_info_extractor | Extract various types of information from email content. |

### Use Cases

#### Table 2: Use Cases

| Class                     | Method                   | Scenario          | Input Values                                                         | Expected Results                                                       |
| ------------------------- | ------------------------ | ----------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| test_regex_info_extractor | test_extract_tasks_1     | Extract Tasks     | Text with a list of tasks.                                           | Should return a list of tasks extracted from the input text.           |
| test_regex_info_extractor | test_extract_tasks_2     | Extract Tasks     | Text with a single task.                                             | Should return a list with a single task extracted from the input text. |
| test_regex_info_extractor | test_extract_tasks_3     | Extract Tasks     | Text with no tasks.                                                  | Should return None as no tasks are present in the input text.          |
| test_regex_info_extractor | test_extract_tasks_4     | Extract Tasks     | Text with a list of tasks.                                           | Should return a list of tasks extracted from the input text.           |
| test_regex_info_extractor | test_extract_links_1     | Extract Links     | Text with a single link.                                             | Should return a list with a single link extracted from the input text. |
| test_regex_info_extractor | test_extract_links_2     | Extract Links     | Text with no links.                                                  | Should return None as no links are present in the input text.          |
| test_regex_info_extractor | test_extract_links_3     | Extract Links     | Text with list of links.                                             | Should return a list with of links extracted from the input text.      |
| test_regex_info_extractor | test_extract_events_1    | Extract Events    | Text announcing a meeting with date, time, and location.             | Should extract a single event with date, time, and location.           |
| test_regex_info_extractor | test_extract_events_2    | Extract Events    | Text mentioning a scheduled event and a specific date.               | Should extract a two events (event and date)                           |
| test_regex_info_extractor | test_extract_events_3    | Extract Events    | Text with a simple event mentioned                                   | Should a simple event                                                  |
| test_regex_info_extractor | test_extract_events_4    | Extract Events    | Text announcing an event with no specific details.                   | Should not extract any events.                                         |
| test_regex_info_extractor | test_extract_dates_1     | Extract Dates     | Text mentioning a deadline date (DD/MM/YYYY format).                 | Should extract a single deadline date.                                 |
| test_regex_info_extractor | test_extract_dates_2     | Extract Dates     | Text reminding of a meeting date (DD-MM-YYYY format).                | Should extract a single meeting date.                                  |
| test_regex_info_extractor | test_extract_dates_3     | Extract Dates     | Text mentioning a specific date (DD de Month YYYY format).           | Should extract a single specific date.                                 |
| test_regex_info_extractor | test_extract_dates_4     | Extract Dates     | Text with no dates mentioned.                                        | Should not extract any dates.                                          |
| test_regex_info_extractor | test_extract_addresses_1 | Extract Addresses | Text mentioning a physical address (Format: "Street Number, Floor"). | Should extract a single physical address.                              |
| test_regex_info_extractor | test_extract_addresses_2 | Extract Addresses | Text with no address mentioned.                                      | Should not extract any addresses.                                      |
| test_regex_info_extractor | test_extract_addresses_3 | Extract Addresses | Text mentioning a physical address (Format: "Street Name, Floor").   | Should extract a single physical address.                              |
| test_regex_info_extractor | test_extract_info_1      | Extract Info      | Text mentioning tasks, dates, links, and events.                     | Should extract various types of information from the email content.    |
| test_parse_email_address_1      | parse_email_address      | parse_email_address      | "=?UTF-8?Q?John_Doe?= <john@example.com>"                                                 | ("John_Doe", "john@example.com")                                       |
| test_parse_email_address_2      | parse_email_address      | parse_email_address      | "john@example.com"                                                                        | (None, "john@example.com")                                             |
| test_parse_email_address_3      | parse_email_address      | parse_email_address      | "=?UTF-8?Q?Jane_Doe?= <jane@example.com>"                                                 | ("Jane_Doe", "jane@example.com")                                       |
| test_parse_email_address_4      | parse_email_address      | parse_email_address      | "=?UTF-8?Q?Juan_P=C3=A9rez?= <juan@example.com>"                                          | ("Juan_Pérez", "juan@example.com")                                     |
| test_parse_email_address_list_1 | parse_email_address_list | parse_email_address_list | "=?UTF-8?Q?John_Doe?= <john@example.com>, =?UTF-8?Q?Jane_Doe?= <jane@example.com>"        | [("John_Doe", "john@example.com"), ("Jane_Doe", "jane@example.com")]   |
| test_parse_email_address_list_2 | parse_email_address_list | parse_email_address_list | "john@example.com, jane@example.com"                                                      | [(None, "john@example.com"), (None, "jane@example.com")]               |
| test_parse_email_address_list_3 | parse_email_address_list | parse_email_address_list | "=?UTF-8?Q?John_Doe?= <john@example.com>, =?UTF-8?Q?Juan_P=C3=A9rez?= <juan@example.com>" | [("John_Doe", "john@example.com"), ("Juan_Pérez", "juan@example.com")] |

## Automata Module

### Scenarios

#### Table 1: Scenarios

| Name                    | Class                               | Scenario                                   |
| ----------------------- | ----------------------------------- | ------------------------------------------ |
| Spam Classification     | test_ndfa_classification_spam_1     | Classify text containing spam keywords.    |
| Work Classification     | test_ndfa_classification_work_1     | Classify text related to work tasks.       |
| Security Classification | test_ndfa_classification_security_1 | Classify text related to security matters. |
| Text Classification     | test_ndfa_classification_text_1     | Classify a text with mixed content.        |

### Use Cases

#### Table 2: Use Cases

| Class               | Method                              | Scenario                | Input Values                      | Expected Results                                   |
| ------------------- | ----------------------------------- | ----------------------- | --------------------------------- | -------------------------------------------------- |
| NDFA Classification | test_ndfa_classification_spam_1     | Spam Classification     | Text containing spam keywords.    | Should classify the text as spam.                  |
| NDFA Classification | test_ndfa_classification_work_1     | Work Classification     | Text related to work tasks.       | Should classify the text as work-related.          |
| NDFA Classification | test_ndfa_classification_security_1 | Security Classification | Text related to security matters. | Should classify the text as security-related.      |
| NDFA Classification | test_ndfa_classification_text_1     | Text Classification     | Text with mixed content.          | Should classify the text with multiple categories. |
