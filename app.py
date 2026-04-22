import streamlit as st
import wikipedia

# Dictionary for manual data: Symptoms, Route, Target, and BSL Levels
virus_data = {
    "Polio": {
        "Symptoms": "Fever, sore throat, headache, vomiting, fatigue, stiffness in the back and neck.",
        "Route": "Fecal-oral route (contaminated water or food).",
        "Target": "Central Nervous System (Motor neurons).",
        "BSL": "2",
        "BSL_Info": "Handle with standard microbiological practices and protective clothing."
    },
    "Zika": {
        "Symptoms": "Fever, rash, conjunctivitis, muscle and joint pain, malaise, headache.",
        "Route": "Aedes mosquito bite, sexual transmission, blood transfusion.",
        "Target": "Neural progenitor cells.",
        "BSL": "2",
        "BSL_Info": "Requires Biosafety Level 2 facilities and containment."
    },
    "SARS-CoV-2": {
        "Symptoms": "Fever, cough, tiredness, loss of taste or smell, difficulty breathing.",
        "Route": "Respiratory droplets and aerosols.",
        "Target": "Respiratory system (ACE2 receptors).",
        "BSL": "3",
        "BSL_Info": "Requires specialized ventilation systems and strictly controlled access."
    },
    "Ebola": {
        "Symptoms": "Fever, severe headache, muscle pain, weakness, fatigue, diarrhea, unexplained bleeding.",
        "Route": "Direct contact with infected blood or body fluids.",
        "Target": "Immune cells and endothelial cells.",
        "BSL": "4",
        "BSL_Info": "Maximum containment! Requires positive pressure suits and dedicated air supply."
    },
    "HIV": {
        "Symptoms": "Flu-like symptoms, fever, sore throat, and fatigue.",
        "Route": "Blood-to-blood contact, sexual contact.",
        "Target": "CD4+ T cells (Immune system).",
        "BSL": "2/3",
        "BSL_Info": "BSL-2 for clinical work; BSL-3 for large-scale production or research."
    },
    "Rabies": {
        "Symptoms": "Fever, headache, excess salivation, muscle spasms, paralysis, and mental confusion.",
        "Route": "Saliva of infected animals (usually through a bite).",
        "Target": "Central Nervous System.",
        "BSL": "2",
        "BSL_Info": "Requires BSL-2 practices; vaccination is highly recommended for lab workers."
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
        wiki_summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        st.subheader("📌 Overview")
        st.write(wiki_summary)
    except:
        st.warning("Fetching data...")

    # 2. Clinical & Biosafety Details
    st.markdown("### 📊 Clinical & Biosafety Profile")
    
    found = False
    for key in virus_data:
        if key.lower() in virus_name.lower():
            data = virus_data[key]
            
            # BSL Level Highlight (Aik baray box mein)
            st.error(f"⚠️ **Biosafety Level (BSL): {data['BSL']}**")
            st.caption(f"Security Requirement: {data['BSL_Info']}")

            # Creating nice boxes for clinical info
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**🚪 Route of Entry:**\n{data['Route']}")
            with col2:
                st.warning(f"**🎯 Target Organ:**\n{data['Target']}")
            
            st.success(f"**🤒 Common Symptoms:**\n{data['Symptoms']}")
            found = True
            break
            
    if not found:
        st.info("Additional clinical and BSL data for this specific virus is being updated.")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Learning Tip:** BSL-4 is for the most dangerous pathogens with no vaccines, like Ebola.")
