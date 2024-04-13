import streamlit as st
import pandas as pd

import model.grammar_module.structure_grammar as sg
import model.regex_module.data_parser as dp
import model.regex_module.info_extractor as ie
import model.transducers_module.transducers as tr
from model.automata_module.ndfa_classification import Classification

selected_email = None
cl = Classification()
st.set_page_config(layout="wide")


def normalize_email(email):
    if email["META"]["FROM"]:
        email["META"]["FROM"] = tr.translate(
            dp.parse_email_address(email["META"]["FROM"])[0]
            + " "
            + dp.parse_email_address(email["META"]["FROM"])[1]
        )
    if email["META"]["TO"]:
        email["META"]["TO"] = [
            tr.translate(value)
            for value in dp.parse_email_address_list(email["META"]["TO"])
        ]
    if email["META"]["SUBJECT"]:
        email["META"]["SUBJECT"] = dp.parse_utf_text(email["META"]["SUBJECT"])
    if email["BODY_TEXT"]:
        email["BODY_TEXT"] = tr.translate(email["BODY_TEXT"])
        email["INFO"] = ie.extract_info(email["BODY_TEXT"])
        email["CLASSIFICATION"] = cl.execute(email["BODY_TEXT"])+cl.execute(email["META"]["SUBJECT"])
        email["CLASSIFICATION_CATEGORY"] = email["CLASSIFICATION"].idxmax(axis=1).values[0]
        email["CLASSIFICATION"].drop(columns=["OTRO"], inplace=True)
    return email


def parse_emails(emails):
    return {id: normalize_email(email) for id, email in sg.parse_emails(emails).items()}


st.title("Email parser")

uploaded = st.file_uploader("Selecciona los archivos eml", type="eml", accept_multiple_files=True)
if uploaded is not None:
    emails = parse_emails([file.read().decode().replace("\r", "") for file in uploaded])

email_list = st.expander("Lista de emails").container(height=300)
for id, email in emails.items():
    if email_list.button(f"{email['META']['SUBJECT']} - {email['META']['FROM']}"):
        selected_email = email

container = st.expander("Datos extraidos").container(height=400)
columns = container.columns(len(ie.info))
data = {ie.info[i]: columns[i] for i in range(len(ie.info))}
for key, column in data.items():
    column.write(key)

for id, email in emails.items():
    for key, value in email["INFO"].items():
        if value and key in ie.info:
            for item in value:
                try:
                    if data[key].button(f"{item}", key=f"{email['META']['ID']}{item}"):
                        selected_email = email
                except:
                    pass

st.divider()
st.divider()


if selected_email:

    to = ""
    for address in list(map(lambda x: "".join(x[1]), selected_email["META"]["TO"])):
        to += address + ", "
    to = to[:-2]
    st.header(f"Seleccionado: {selected_email['META']['SUBJECT']}")
    st.write(f"De: {selected_email['META']['FROM']}")
    st.write(f"Para: {to}")
    st.write(f"Fecha: {selected_email['META']['DATE']}")
    st.write(f"Asunto: {selected_email['META']['SUBJECT']}")

    st.text_area("Contenido del email", selected_email["BODY_TEXT"], height=400)

    st.header("Información extraida del email")

    email_columns = st.container(height=550).columns(len(ie.info))
    email_data = {ie.info[i]: email_columns[i] for i in range(len(ie.info))}
    for key, column in email_data.items():
        column.write(key)

    for key, value in selected_email["INFO"].items():
        if value and key in ie.info:
            for item in value:
                try:
                    if email_data[key].button(f"{item}", key=f'selected{email["META"]["ID"]}{item}'):
                        selected_email=selected_email
                except:
                    pass
    st.header(f"Clasificación: {selected_email['CLASSIFICATION_CATEGORY']}")
    st.bar_chart(selected_email["CLASSIFICATION"])
