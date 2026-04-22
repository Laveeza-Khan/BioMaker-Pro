import streamlit as st
import wikipedia
import random

# Extended Dictionary: Viruses data without emojis
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
        "BSL_Info": "Maximum containment! Positive pressure suits required."
    },
    "Bacteriophage": {
        "Symptoms": "None (Infects bacteria only).",
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
        "Symptoms": "High fever, severe joint/muscle pain, rash.",
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
        "BSL_Info": "Only handled in extremely secure WHO-authorized labs."
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

st.set_page_config(page_title="BioMaker-Pro")

st.title("BioMaker-Pro: Viral Encyclopedia")
st.markdown("Developer: Laveeza Khan")
st.markdown("---")

virus_name = st.text_input("Search Virus (e.g. Lambda, Ebola, Dengue, Polio):", "Polio")

if virus_name:
    try:
        wiki_summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        st.subheader("Overview")
        st.write(wiki_summary)
    except:
        st.info("Fetching overview from database...")

    st.markdown("### Clinical and Biosafety Profile")
    
    found = False
    search_query = virus_name.lower()
    for key in virus_data:
        if key.lower() in search_query:
            data = virus_data[key]
            
            st.error(f"Biosafety Level (BSL): {data['BSL']}")
            st.caption(f"Security Requirement: {data['BSL_Info']}")

            col1, col2 = st.columns(2)
            with col1:
                st.info(f"Route of Entry:\n{data['Route']}")
            with col2:
                st.warning(f"Target:\n{data['Target']}")
            
            st.success(f"Symptoms:\n{data['Symptoms']}")
            found = True
            break
            
    if not found:
        st.info("Additional clinical details for this virus are not in the local database.")

# Sidebar Facts without emojis
st.sidebar.markdown("---")
st.sidebar.subheader("Did You Know?")

facts = [
    "Bacteriophages are being researched as Phage Therapy to kill antibiotic-resistant bacteria.",
    "Viruses are not technically alive because they cannot reproduce without a host cell.",
    "The MimiVirus is so large that it was originally mistaken for a bacterium.",
    "About 8 percent of human DNA actually comes from ancient viruses.",
    "Some viruses can survive being frozen for thousands of years in permafrost.",
    "The word virus comes from a Latin word meaning poison or slimy liquid."
]

random_fact = random.choice(facts)
st.sidebar.info(random_fact)
