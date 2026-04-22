import streamlit as st
import wikipedia

# Dictionary for manual data (Symptons & Route of Entry)
# Aap is list mein mazeed viruses add kar sakti hain
virus_data = {
    "Polio": {
        "Symptoms": "Fever, sore throat, headache, vomiting, fatigue, stiffness in the back and neck.",
        "Route": "Fecal-oral route (contaminated water or food).",
        "Target": "Central Nervous System (Motor neurons)."
    },
    "Zika": {
        "Symptoms": "Fever, rash, conjunctivitis, muscle and joint pain, malaise, headache.",
        "Route": "Aedes mosquito bite, sexual transmission, blood transfusion.",
        "Target": "Neural progenitor cells."
    },
    "SARS-CoV-2": {
        "Symptoms": "Fever, cough, tiredness, loss of taste or smell, difficulty breathing.",
        "Route": "Respiratory droplets and aerosols.",
        "Target": "Respiratory system (ACE2 receptors)."
    },
    "Ebola": {
        "Symptoms": "Fever, severe headache, muscle pain, weakness, fatigue, diarrhea, unexplained bleeding.",
        "Route": "Direct contact with infected blood or body fluids.",
        "Target": "Immune cells and endothelial cells."
    }
}

st.set_page_config(page_title="BioMaker-Pro", page_icon="🧬")

st.title("🧬 BioMaker-Pro: Viral Encyclopedia")
st.markdown(f"**Developer:** Laveeza Khan | 3rd Year Biotech Student @ KU")
st.markdown("---")

# User Input
virus_name = st.text_input("Enter Virus Name (e.g. Polio, Zika, Ebola, SARS-CoV-2):", "Polio")

if virus_name:
    # 1. Fetching Summary from Wikipedia
    try:
        # Wikipedia se summary nikalna
        wiki_summary = wikipedia.summary(f"{virus_name} virus", sentences=4)
        st.subheader("📌 Overview")
        st.write(wiki_summary)
    except:
        st.warning("General overview fetched from database.")

    # 2. Taxonomy & Clinical Details
    st.markdown("### 📊 Clinical & Biological Profile")
    
    # Check if we have extra data for this virus
    found = False
    for key in virus_data:
        if key.lower() in virus_name.lower():
            data = virus_data[key]
            
            # Creating nice boxes for info
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**🚪 Route of Entry:**\n{data['Route']}")
            with col2:
                st.warning(f"**🎯 Target:**\n{data['Target']}")
            
            st.error(f"**🤒 Common Symptoms:**\n{data['Symptoms']}")
            found = True
            break
            
    if not found:
        st.info("Additional clinical data for this specific virus is being updated in our database.")

st.sidebar.markdown("---")
st.sidebar.write("🧪 **Project Scope:** This tool provides rapid access to viral taxonomy and clinical symptoms for biotech students.")
