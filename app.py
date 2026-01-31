import io
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSV Test Writer", layout="centered")

st.title("CSV hochladen und 'Test' eintragen")

uploaded = st.file_uploader("CSV-Datei auswählen", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"CSV konnte nicht gelesen werden: {exc}")
    else:
        # Ensure a consistent change: add or overwrite a column named 'Test'
        df["Test"] = "Test"

        st.subheader("Vorschau")
        st.dataframe(df, use_container_width=True)

        buf = io.StringIO()
        df.to_csv(buf, index=False)
        st.download_button(
            "CSV herunterladen",
            data=buf.getvalue(),
            file_name="with_test.csv",
            mime="text/csv",
        )
else:
    st.caption("Bitte eine CSV-Datei hochladen.")
