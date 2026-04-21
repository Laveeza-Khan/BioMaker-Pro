import streamlit as st
import wikipedia
import stmol
import py3Dmol

st.set_page_config(page_title="BioMaker Pro", layout="wide")

st.title("BioMaker 2.0: Disease Intelligence 🧬")

# Search Input
virus_query = st.text_input("Search for a Virus (e.g., Polio, Zika, SARS-CoV-2):", "")

if virus_query:
    try:
        with st.spinner('Fetching Bio-Data...'):
            # Wikipedia summary
            result = wikipedia.summary(f"{virus_query} virus", sentences=3)
            
            tab1, tab2 = st.tabs(["Classification & Overview", "3D Structure"])
            
            with tab1:
                st.subheader(f"About {virus_query}")
                st.info(result)
            
            with tab2:
                st.subheader("3D Molecular Visualization")
                # Default PDB IDs for common viruses
                pdb_map = {"Polio": "1PIV", "Zika": "5IRE", "SARS-CoV-2": "6VXX"}
                
                # Check if we have a specific PDB, else use a generic protein
                pdb_id = "1AIE" # Default example
                for key in pdb_map:
                    if key.lower() in virus_query.lower():
                        pdb_id = pdb_map[key]
                
                st.write(f"Viewing PDB Structure: **{pdb_id}**")
                view = py3Dmol.view(query=f'pdb:{pdb_id}')
                view.setStyle({'cartoon': {'color': 'spectrum'}})
                stmol.showmol(view, height=500, width=800)

    except Exception as e:
        st.error(f"Error: {e}")

st.write("---")
st.caption("Developed by Laveeza Khan | University of Karachi")