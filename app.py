import streamlit as st
import wikipedia
import random

# --- Professional Dark Theme Styling ---
st.set_page_config(page_title="BioMaker-Pro", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #233939; color: #D5D3CC; }}
    h1, h2, h3 {{ color: #687D31; font-family: 'Serif'; }}
    .stTextInput > div > div > input {{ background-color: #D5D3CC; color: #19350C; border: 2px solid #687D31; border-radius: 8px; }}
    .stInfo {{ background-color: #6FA9BB; color: #19350C; border-radius: 10px; border: none; }}
    .stWarning {{ background-color: #19350C; color: #D5D3CC; border: 1px solid #687D31; }}
    .stSuccess {{ background-color: #406768; color: #ffffff; }}
    .stError {{ background-color: #932a2a; color: #ffffff; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

st.title("BioMaker-Pro: Advanced Viral Taxonomy")
st.markdown("**Developer:** Laveeza Khan")
st.markdown("---")

virus_name = st.text_input("Search Virus (e.g. Rabies, Ebola, Polio, Bacteriophage):", "Rabies")

if virus_name:
    try:
        search_results = wikipedia.search(f"{virus_name} virus")
        if not search_results:
            st.error("Virus not found in database. Check spelling.")
        else:
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = wikipedia.summary(page_title, sentences=3)
            content_lower = page.content.lower()
            
            # 1. Overview
            st.subheader("General Overview")
            st.info(summary)
            st.markdown("---")
            
            # 2. Taxonomy & Biosafety Profile
            st.subheader("Biological Classification & Clinical Profile")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### Taxonomy")
                # Improved Taxonomy Logic
                family, genus = "Information in Article", "Information in Article"
                
                if "rabies" in page_title.lower():
                    family, genus = "Rhabdoviridae", "Lyssavirus"
                else:
                    for line in content_lower.split('\n')[:100]:
                        if "family" in line and ":" in line:
                            family = line.split(":")[1].strip().split(" ")[0].replace(".", "").replace(",", "")
                        if "genus" in line and ":" in line:
                            genus = line.split(":")[1].strip().split(" ")[0].replace(".", "").replace(",", "")
                
                st.write(f"**Family:** {family.capitalize()}")
                st.write(f"**Genus:** {genus.capitalize()}")
                st.write(f"**Species:** {page_title}")

            with col2:
                st.markdown("### Clinical Safety")
                bsl_4_list = ["ebola", "marburg", "lassa", "smallpox", "crimean-congo"]
                bsl_3_list = ["sars", "mers", "covid", "hiv", "rabies", "hantavirus"]
                
                name_low = page_title.lower()
                if any(v in name_low for v in bsl_4_list): bsl = "4"
                elif any(v in name_low for v in bsl_3_list): bsl = "3"
                else: bsl = "2"
                
                st.error(f"Biosafety Level (BSL): {bsl}")
                
                # Zoonotic Logic
                human_only = ["polio", "smallpox", "measles", "hiv", "rubella"]
                zoonotic_indicators = ["zoonosis", "zoonotic", "animal-to-human", "spillover", "natural reservoir"]
                
                is_zoonotic = any(word in content_lower[:4000] for word in zoonotic_indicators)
                is_human_specific = any(h in name_low for h in human_only)

                if is_zoonotic and not is_human_specific:
                    st.warning("Type: Zoonotic Virus")
                else:
                    st.success("Type: Human-Specific")

            with col3:
                st.markdown("### Pathogenesis")
                symp = "Check Overview"
                if "symptoms" in content_lower:
                    try:
                        # CLEANING LOGIC: '==' aur 'the first' ko skip karne ke liye
                        raw_data = content_lower.split("symptoms")[1].split(". ")
                        # Pehla valid sentence dhoondna
                        for sentence in raw_data:
                            clean = sentence.replace("==", "").replace("=", "").strip()
                            if len(clean) > 15 and not clean.startswith("the first"):
                                symp = clean
                                break
                    except: pass
                st.write(f"**Symptoms:** {symp.capitalize()}")
                
                trans = "Contact/Droplets"
                if "transmission" in content_lower:
                    try:
                        raw_trans = content_lower.split("transmission")[1].split(". ")[0]
                        trans = raw_trans.replace("==", "").replace("=", "").strip()
                    except: pass
                st.write(f"**Route:** {trans.capitalize()}")
            
            st.markdown("---")
            st.markdown(f"🔗 **Detailed Research:** [Wikipedia Source]({page.url})")

    except Exception:
        st.warning("Automated summary generated. Check the link for full taxonomy.")
        st.markdown(f"🔗 [Manual Source](https://en.wikipedia.org/wiki/{virus_name.replace(' ', '_')}_virus)")

# Sidebar
st.sidebar.title("💡 Viral Facts")
facts = [
    "Viruses are classified into families based on genome type and structure.",
    "BSL-4 labs are used for viruses with no known vaccine or treatment.",
    "Zoonotic spillover is a major cause of emerging infectious diseases.",
    "Taxonomy helps in understanding viral evolution and host range."
]
st.sidebar.info(random.choice(facts))
