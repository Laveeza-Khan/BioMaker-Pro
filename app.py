import streamlit as st
import wikipedia
import stmol
import py3Dmol

# 1. PDB Mapping Dictionary
pdb_dict = {
    "Polio": "1PIV",
    "Zika": "5IRE",
    "SARS-CoV-2": "6VXX",
    "Ebola": "4IDB",
    "Rabies": "6V5B",
    "Influenza": "1RVX",
    "Hepatitis B": "2I6Z",
    "Adenovirus": "6CGV",
    "Bacteriophage": "1X9B",
    "HIV": "1HVI"
}

st.title("🧬 BioMaker-Pro 2.0")
st.markdown("Developed by Laveeza Khan | Biotech Student @ KU")

# User Input
virus_name = st.text_input("Enter Virus Name (e.g. Polio, Ebola, Zika):", "Polio")

if virus_name:
    # 2. Information from Wikipedia
    try:
        summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        st.subheader(f"About {virus_name}")
        st.write(summary)
    except:
        st.warning("Could not fetch details from Wikipedia.")

    # 3. 3D Visualization Logic
    st.subheader("3D Molecular Structure")
    
    pdb_id = None
    for key in pdb_dict:
        if key.lower() in virus_name.lower():
            pdb_id = pdb_dict[key]
            break

    if pdb_id:
        st.info(f"Showing PDB Structure: {pdb_id}")
        view = py3Dmol.view(query=f'pdb:{pdb_id}')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        stmol.make_to_stmol(view, height=400)
    else:
        st.error(f"Sorry! 3D structure for '{virus_name}' is not in our database.")
        st.info("Try: Polio, Zika, or Ebola.")
