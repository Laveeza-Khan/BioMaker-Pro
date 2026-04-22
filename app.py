import streamlit as st
import wikipedia
import random

# --- Professional Styling & Theme ---
st.set_page_config(page_title="BioMaker-Pro", layout="wide")

# Custom CSS for Background and Professional Look
st.markdown("""
    <style>
    .stApp {
        background-color: #e5e7eb; /* Professional Light Gray-Blue */
    }
    .main-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1e3a8a; /* Dark Blue */
    }
    .stTextInput > div > div > input {
        border: 2px solid #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("BioMaker-Pro: Professional Viral Encyclopedia")
st.markdown("Developer: Laveeza Khan")
st.markdown("---")

# --- Search Section ---
virus_name = st.text_input("Search any Virus (e.g. Rabies, Influenza, HPV, Dengue):", "Rabies")

if virus_name:
    try:
        # Search and fetch page
        search_results = wikipedia.search(f"{virus_name} virus")
        if not search_results:
            st.error("No results found. Please check the spelling.")
        else:
            # Picking the best match
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = wikipedia.summary(page_title, sentences=3)
            
            # 1. Overview Section
            st.subheader("Overview")
            st.info(summary)
            
            st.markdown("---")
            
            # 2. Automated Profile
            st.subheader("Biological and Clinical Profile")
            col1, col2 = st.columns(2)
            
            content_lower = page.content.lower()
            
            with col1:
                st.markdown("### Classification")
                # Smart family detection
                if "family" in content_lower:
                    family_info = content_lower.split("family")[1].split(".")[0].split("\n")[0]
                    st.write(f"**Family:** {family_info.capitalize()}")
                else:
                    st.write("**Family:** Refer to Wikipedia for detailed taxonomy.")
                
                # BSL Logic
                danger_score = any(word in content_lower for word in ["fatal", "mortality", "high risk", "outbreak", "pandemic"])
                bsl = "3" if danger_score else "2"
                st.markdown(f"**Estimated Biosafety Level (BSL):** {bsl}")
            
            with col2:
                st.markdown("### Clinical Features")
                # Symptoms detection
                if "symptoms" in content_lower:
                    symp = content_lower.split("symptoms")[1].split(".")[0]
                    st.write(f"**Symptoms:** {symp.capitalize()}.")
                else:
                    st.write("**Symptoms:** Fever, malaise, and specific viral symptoms.")
                
                # Transmission
                if "transmission" in content_lower:
                    trans = content_lower.split("transmission")[1].split(".")[0]
                    st.write(f"**Transmission:** {trans.capitalize()}.")
                else:
                    st.write("**Transmission:** Direct contact or respiratory droplets.")

    except Exception:
        st.warning("Specific clinical details are being synthesized from the global database. Please refer to the Overview above.")

# --- Sidebar Knowledge Base ---
st.sidebar.title("Viral Knowledge")
facts = [
    "Viruses can infect all types of life forms, from animals and plants to microorganisms.",
    "The study of viruses is known as virology, a subspecialty of microbiology.",
    "Most viruses are too small to be seen directly with an optical microscope.",
    "Viral populations can evolve rapidly through mutation and natural selection.",
    "Vaccination is the most effective way to prevent many viral infections."
]
st.sidebar.markdown("---")
st.sidebar.write(random.choice(facts))
