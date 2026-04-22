import streamlit as st
import wikipedia

# Extended Dictionary: Yahan humne mazeed viruses add kar diye hain
virus_data = {
    "Polio": {
        "Symptoms": "Fever, sore throat, vomiting, fatigue, stiffness in back/neck.",
        "Route": "Fecal-oral route (contaminated water/food).",
        "Target": "Motor neurons in the Central Nervous System.",
        "BSL": "2",
        "BSL_Info": "Standard lab safety with protective gear."
    },
    "Zika": {
        "Symptoms": "Fever, rash, joint pain, red eyes.",
        "Route": "Aedes mosquito bite, sexual transmission.",
        "Target": "Neural progenitor cells.",
        "BSL": "2",
        "BSL_Info": "Standard containment; special care for pregnant staff."
    },
    "SARS-CoV-2": {
        "Symptoms": "Fever, cough, loss of taste/smell, breathing issues.",
        "Route": "Respiratory droplets (coughing/sneezing).",
        "Target": "Respiratory system (Lungs).",
        "BSL": "3",
        "BSL_Info": "High-level containment with specialized ventilation (Negative pressure)."
    },
    "Ebola": {
        "Symptoms": "Internal/external bleeding, fever, severe headache.",
        "Route": "Direct contact with infected body fluids.",
        "Target": "Immune cells and blood vessel linings.",
        "BSL": "4",
        "BSL_Info": "Maximum containment! Positive pressure 'Space Suits' required."
    },
    "Bacteriophage": {
        "Symptoms": "None (They only infect bacteria, not humans!).",
        "Route": "Direct contact with host bacteria.",
        "Target": "Specific Bacterial cells (e.g., E. coli).",
        "BSL": "1",
        "BSL_Info": "Generally safe; handled in basic microbiology labs."
    },
    "Lambda": {
        "Symptoms": "Infects bacteria (non-pathogenic to humans).",
        "Route": "Infection of E. coli through the LamB receptor.",
        "Target": "E. coli bacteria (Lysogenic/Lytic cycles).",
        "BSL": "1",
        "BSL_Info": "Basic lab safety; widely used in genetic research."
    },
    "Dengue": {
        "Symptoms": "High fever, severe joint/muscle pain ('Breakbone fever'), rash.",
        "Route": "Aedes aegypti mosquito bite.",
        "Target": "Monocytes and macrophages.",
        "BSL": "2",
        "BSL_Info": "Standard BSL-2 practices; avoid needle sticks."
    },
    "Smallpox": {
        "Symptoms": "High fever, fatigue, and characteristic skin rashes (pustules).",
        "Route": "Face-to-face contact, infected droplets.",
        "Target": "Skin cells and lymph nodes.",
        "BSL": "4",
        "BSL_Info": "Only handled in extremely secure WHO-authorized labs (CDC/Russia)."
    },
    "HIV": {
        "Symptoms": "Flu-like symptoms initially, weight loss, weak immune system.",
        "Route": "Blood or sexual contact.",
        "Target": "CD4+ T cells.",
        "BSL": "2/3",
        "BSL_Info": "BSL-2 for tests; BSL-3 for research/culture."
    },
    "MERS": {
        "Symptoms": "Severe respiratory illness, fever, cough, shortness of breath.",
        "Route": "Zoonotic (from camels) and respiratory droplets.",
        "Target": "Lower respiratory tract.",
        "BSL": "3",
        "BSL_Info": "Requires BSL-3 containment and specialized PPE."
    }
}

st.set_page_config(page_title="BioMaker-Pro", page_icon="🧬")

st.title("🧬 BioMaker-Pro: Viral Encyclopedia")
st.markdown(f"**Developer:** Laveeza Khan | 3rd Year Biotech Student @ KU")
st.markdown("---")

virus_name = st.text_input("Search Virus (e.g. Lambda, Ebola, Dengue, Polio):", "Polio")

if virus_name:
    try:
        wiki_summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        st.subheader("📌 Overview")
        st.write(wiki_summary)
    except:
        st.info("Fetching overview...")

    st.markdown("### 📊 Clinical & Biosafety Profile")
    
    found = False
    search_query = virus_name.lower()
    for key in virus_data:
        if key.lower() in search_query:
            data = virus_data[key]
            
            st.error(f"⚠️ **Biosafety Level (BSL): {data['BSL']}**")
            st.caption(f"Security: {data['BSL_Info']}")

            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**🚪 Route of Entry:**\n{data['Route']}")
            with col2:
                st.warning(f"**🎯 Target:**\n{data['Target']}")
            
            st.success(f"**🤒 Symptoms:**\n{data['Symptoms']}")
            found = True
            break
            
    if not found:
        st.warning("Clinical details for this virus are not in the local database, but you can read the Wikipedia overview above!")

st.sidebar.info("💡 **Fun Fact:** Bacteriophages are being researched as 'Phage Therapy' to kill antibiotic-resistant bacteria!")
