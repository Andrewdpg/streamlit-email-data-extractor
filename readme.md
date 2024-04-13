# Email Parser

### Integrantes:

- [Silem Nabib Villa Contreras](https://github.com/SilemNabib) - A00395548
- [María Alejandra Mantilla Coral](https://github.com/alejandramantillac) - A00395792
- [Andrés David Parra García](https://github.com/Andrewdpg) - A00395676

**$Note_1$:** *In order to run the main program, run by command line: `streamlit run main.py` inside the src folder*

**$Note_2$:** *In order to run python tests, run by command line: `pytest` inside the src folder*

## Index:

**1. Documentation:**

   1. Class diagram [VPP](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/Email_Parser.vpp) - [PDF](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/Email_parser.pdf)
   2. Literature review [md](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/literature_review.md)
   3. Poster [PDF](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/Poster.pdf) - [JPG](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/Poster.jpg) - [MIRO]()
   4. Test documentation [md](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/docs/test_documentation.md)


**2. Code:**

   1. Automata module [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/model/automata_module) - [test](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/tests/test_automata.py)
   2. Grammar module [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/model/grammar_module) - [test](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/tests/test_structure_grammar.py)
   3. Regular Expressions module [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/model/regex_module) - [test](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/tests/test_regex_module.py)
   4. Transducer module [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/model/transducers_module) - [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/tests/test_transducers.py)
   5. User interface [src](https://github.com/Andrewdpg/streamlit-email-data-extractor/blob/main/src/main.py)

3. DEployed at: [streamlit](https://app-email-data-extractor-fmsd2eon28ygrf4wdbgucs.streamlit.app/)


## Introduction

In contemporary data analysis, the abundance of textual information presents a challenge in extracting meaningful insights efficiently. The **Email Parser** project aims to tackle this challenge by developing a robust software solution adept at parsing text documents, specifically email messages, and extracting specific types of information. Through the utilization of Python, integrating methodologies such as regular expressions, automata, transducers, and context-free grammars, the project endeavors to develop a pragmatic software solution providing users with a reliable tool for extracting structured and relevant data from various textual sources.

The exponential growth of digital communication, particularly in the form of email correspondence, has led to an overwhelming influx of unstructured textual data. This data, while rich in potential insights, often remains underutilized due to the complexity of manually processing vast amounts of information. The Email Parser project addresses this challenge by leveraging advanced computational techniques to automate the extraction of critical information from email messages.

By harnessing the power of regular expressions, the system can efficiently identify and extract well-structured data elements such as URLs, email addresses, and phone numbers. However, to handle more complex linguistic patterns and contextual information, the project employs sophisticated formal language theory techniques, including finite automata, transducers, and context-free grammars. These methodologies enable the system to recognize and analyze intricate patterns, facilitating the extraction of structured information such as tasks, events, and physical addresses.

## Objectives

The primary objectives of the Email Parser project are:

1. Develop a solution for extracting relevant information from unstructured textual data, with a focus on email messages.
2. Leverage computational techniques, including regular expressions, automata, transducers, and context-free grammars, to accurately identify and extract information from email content.
3. Provide users with a user-friendly interface to interact with the system and easily access extracted information.
4. Enhance the system's adaptability and scalability to handle diverse email communication styles and evolving data formats.

## Methods

The Email Parser project employs a modular approach, utilizing a combination of techniques to effectively process and extract information from email messages:

1. **Grammar for Structure Validation**: A context-free grammar is defined to model the syntactic structure of email messages. This grammar is used to validate the structure of an email and ensure that it conforms to the expected format, facilitating further processing and information extraction:

   1. The grammar is defined using the Lark parsing library, which provides a convenient way to specify and parse context-free grammars.
   2. The grammar rules are designed to capture the various components of an email message, such as headers, boundaries, and body sections (plain text and HTML).
   3. By parsing the email using this grammar, the system can identify and separate the different parts of the message, enabling more targeted analysis and extraction of relevant information.
2. **Automata for Classification**: Non-deterministic finite automata (NFA) are constructed to recognize specific patterns and classify email content into different categories, such as spam, invitations, security-related messages, or work tasks.

   1. This classification module provides valuable insights into the nature and purpose of the email, informing subsequent information extraction processes.
   2. The NFA models are designed to identify keywords, phrases, and patterns that are indicative of specific email categories.
   3. By analyzing the email content against these models, the system can assign a classification label to the email, allowing for more focused extraction and interpretation of the information.
3. **Transducer for Text Normalization**: Transducers are employed to normalize and standardize the extracted information from email messages. This module performs tasks such as replacing, correcting and properly formatting characters ensuring consistency.

   1. Transducers are finite automata that not only recognize patterns but also perform transformations on the input string.
   2. In the context of the Email Parser, transducers are used to handle common issues in email data, such as encoding issues, misspellings, and inconsistent formatting.
   3. By applying a series of transformation rules, the transducer module can clean and normalize the extracted data, facilitating more reliable and accurate information extraction.
4. **Regular Expressions for Information Extraction**: Regular expressions are utilized to identify and extract well-structured data elements from email content, such as dates, addresses, links, greetings, verification codes, and other relevant information. This module leverages the power of regular expressions to efficiently process textual data and extract valuable insights.

   1. Regular expressions are a concise and flexible way to describe patterns in text data, making them well-suited for identifying and extracting specific types of information from email messages.
   2. The system defines a set of regular expressions tailored to various data elements of interest, such as date formats, URL patterns, and address structures.
   3. By applying these regular expressions to the email content, the system can accurately extract and isolate the relevant information.

In addition to these core modules, the Email Parser project incorporates auxiliary components to enhance its functionality and usability:

- **Email Parsing**: A dedicated module is responsible for parsing email messages in the `.eml` format, handling various encoding schemes and ensuring proper decoding of the email content.
- **User Interface**: A user-friendly interface, built using the Streamlit library, allows users to interact with the system, upload email files, and view the extracted information in a structured and intuitive manner.
- **Data Visualization**: The extracted information is presented to users through various data visualization techniques, such as charts and graphs, providing a clear and concise representation of the system's output.

By combining these techniques and components, the Email Parser project aims to provide a comprehensive and robust solution for extracting structured and relevant information from email messages, enabling users to efficiently navigate and utilize the wealth of data contained within their digital communications.

## Results and Conclusions

The Email Parser project has demonstrated promising capabilities in extracting relevant information from email messages. By integrating regular expressions, automata, transducers, and context-free grammars, the system has achieved a satisfactory degree of accuracy in identifying and extracting various data types, including dates, addresses, links, tasks, events, and different codes.

However, the project has also encountered several challenges and limitations. One notable issue is the system's performance when processing large volumes of text or highly complex email content. The regular expression module and automata-based classification approach can become computationally intensive, leading to suboptimal performance in certain scenarios. For example, the automaton-based classification module may need to evaluate the text multiple times to classify the email content accurately, which can be inefficient for longer emails or emails with intricate linguistic patterns.

Additionally, the system's ability to extract information from highly contextual or domain-specific email content remains a challenge. While the current implementation can handle well-structured data and common patterns, it may struggle with emails that contain industry-specific jargon, specialized terminology, or complex semantic relationships.

Despite these challenges, the user-friendly interface and data visualization components have enhanced the system's usability and accessibility, enabling users to effortlessly interact with the extracted information and gain valuable insights from their email data.

Moving forward, several areas for improvement and further research have been identified. Incorporating advanced natural language processing techniques, such as deep learning models and semantic analysis, could enhance the system's ability to understand and extract information from more complex and contextual email content. Additionally, exploring optimization strategies and parallel processing techniques could improve the system's performance when dealing with large volumes of data or computationally intensive operations.

Overall, the Email Parser project represents a step forward in the field of information extraction from unstructured textual data. While challenges remain, the project has laid foundation for future research and development, paving the way for more sophisticated and robust solutions in the realm of email information extraction and beyond.
