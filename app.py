import streamlit as st
import wikipedia
import stmol
import py3Dmol

# 1. PDB Mapping
pdb_dict = {
    "Polio": "1PIV",
    "Zika": "5IRE",
    "SARS-CoV-2": "6VXX",
    "Ebola": "4IDB",
    "Rabies": "6V5B",
    "Influenza": "1RVX",
    "Hepatitis": "2I6Z",
    "Adenovirus": "6CGV",
    "HIV": "1HVI"
}

st.title("🧬 BioMaker-Pro 2.0")
st.markdown("Developed by Laveeza Khan | Biotech @ KU")

virus_name = st.text_input("Enter Virus Name:", "Polio")

if virus_name:
    # Wikipedia Info
    try:
        summary = wikipedia.summary(f"{virus_name} virus", sentences=3)
        st.subheader(f"About {virus_name}")
        st.write(summary)
    except:
        st.write("Information fetching...")

    # 3D Structure
    st.subheader("3D Molecular Structure")
    
    pdb_id = None
    for key in pdb_dict:
        if key.lower() in virus_name.lower():
            pdb_id = pdb_dict[key]
            break

    if pdb_id:
        st.info(f"PDB ID: {pdb_id}")
        view = py3Dmol.view(query=f'pdb:{pdb_id}')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        # Sab se stable function use kar rahe hain
        stmol.show2stmol(view, height=400)
    else:
        st.warning("Structure not in list, try Polio or Zika.")
