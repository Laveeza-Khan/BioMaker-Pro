import streamlit as st
import wikipedia
import random

# --- Professional Theme & CSS ---
st.set_page_config(page_title="BioMaker-Pro", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title and Header ---
st.title("BioMaker-Pro: Automated Viral Encyclopedia")
st.markdown("Developer: Laveeza Khan")
st.markdown("---")

# --- User Input ---
virus_name = st.text_input("Search Virus (e.g. Rabies, Dengue, Ebola, Hepatitis):", "Rabies")

if virus_name:
    try:
        # Search for the page
        page = wikipedia.page(f"{virus_name} virus")
        url = page.url
        summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        
        # Overview Section
        st.subheader("Overview")
        st.write(summary)
        st.caption(f"Source: [Wikipedia]({url})")

        st.markdown("---")
        
        # Automated Data Extraction Section
        st.subheader("Automated Clinical and Biological Profile")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("Biological Classification")
            # Yahan hum Taxonomy nikalne ki koshish karte hain
            content = page.content.lower()
            
            # Simple Logic to find Family
            if "family" in content:
                try:
                    family = content.split("family")[1].split(".")[0].split("\n")[0]
                    st.write(f"**Family:** {family.capitalize()}")
                except:
                    st.write("**Family:** Information available on full page.")
            
            # Setting BSL based on virus danger (Logic)
            danger_words = ["high mortality", "fatal", "ebola", "sars", "mers", "smallpox", "marburg"]
            if any(word in content for word in danger_words):
                bsl_level = "3 or 4"
            else:
                bsl_level = "2"
            st.error(f"Estimated Biosafety Level (BSL): {bsl_level}")

        with col2:
            st.warning("Clinical Characteristics")
            # Extracting potential symptoms
            if "symptoms" in content:
                symptoms_text = content.split("symptoms")[1].split(".")[0:2]
                st.write(f"**Potential Symptoms:** {'. '.join(symptoms_text).capitalize()}.")
            else:
                st.write("**Symptoms:** Please refer to the clinical summary above.")
            
            if "transmission" in content:
                trans = content.split("transmission")[1].split(".")[0]
                st.write(f"**Route of Entry:** {trans.capitalize()}.")

    except Exception as e:
        st.error("Could not find specific automated data for this virus. Please try a more specific name.")

# --- Sidebar Facts ---
st.sidebar.subheader("Viral Knowledge Base")
facts = [
    "Viruses are the most abundant biological entities on Earth.",
    "The human genome contains nearly 100,000 pieces of DNA from ancient viruses.",
    "Some viruses, like Phages, are used to treat bacterial infections.",
    "The first virus ever discovered was the Tobacco Mosaic Virus in 1892.",
    "Viruses come in various shapes: Helical, Icosahedral, Prolate, and Complex."
]
st.sidebar.info(random_fact := random.choice(facts))
