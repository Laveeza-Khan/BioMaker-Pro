import streamlit as st
import wikipedia
import random

# --- Professional Styling (Your Palette) ---
st.set_page_config(page_title="BioMaker-Pro", layout="wide")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #D5D3CC; }}
    h1, h2, h3 {{ color: #19350C; font-family: 'Serif'; }}
    .stTextInput > div > div > input {{ border: 2px solid #406768; border-radius: 8px; }}
    .stInfo {{ background-color: #6FA9BB; color: #19350C; border: none; padding: 20px; border-radius: 10px; }}
    .stWarning {{ background-color: #687D31; color: #ffffff; padding: 10px; border-radius: 5px; }}
    .stSuccess {{ background-color: #406768; color: #ffffff; padding: 10px; border-radius: 5px; }}
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("BioMaker-Pro: Advanced Viral Taxonomy")
st.markdown("**Developer:** Laveeza Khan")
st.markdown("---")

# User Input
virus_name = st.text_input("Search Virus (e.g. Rabies, Ebola, Polio, Lambda):", "Polio")

if virus_name:
    try:
        # Wikipedia Search
        search_results = wikipedia.search(f"{virus_name} virus")
        if not search_results:
            st.error("No specific virus found. Try checking the spelling.")
        else:
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = wikipedia.summary(page_title, sentences=3)
            content_lower = page.content.lower()
            
            # Overview
            st.subheader("General Overview")
            st.info(summary)
            
            st.markdown("---")
            
            # Taxonomy & Clinical Profile
            st.subheader("Taxonomy and Biological Profile")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### Classification")
                family = "Not specified"
                genus = "Not specified"
                
                # Logic to extract Family and Genus
                lines = content_lower.split('\n')
                for line in lines[:60]:
                    if "family:" in line: family = line.split("family:")[1].strip()
                    if "genus:" in line: genus = line.split("genus:")[1].strip()
                
                st.write(f"**Family:** {family.capitalize()}")
                st.write(f"**Genus:** {genus.capitalize()}")
                st.write(f"**Species:** {page_title}")

            with col2:
                st.markdown("### Clinical Safety")
                # BSL Logic
                danger_score = any(word in content_lower[:3000] for word in ["fatal", "mortality", "ebola", "sars", "mers", "outbreak"])
                bsl = "3 or 4" if danger_score else "2"
                st.error(f"Biosafety Level (BSL): {bsl}")
                
                # --- FIXED ZOONOTIC LOGIC ---
                # 1. Known Human-only viruses (Blacklist for Zoonotic)
                human_only = ["polio", "smallpox", "measles", "rubella", "hiv"]
                
                # 2. Indicators for Zoonosis
                zoonotic_indicators = ["zoonosis", "zoonotic", "animal-to-human", "spillover", "natural reservoir"]
                
                is_zoonotic = any(word in content_lower[:4000] for word in zoonotic_indicators)
                is_human_only = any(h in page_title.lower() for h in human_only)

                if is_zoonotic and not is_human_only:
                    st.warning("Type: Zoonotic Virus")
                    st.caption("This virus can transmit from animals to humans.")
                else:
                    st.success("Type: Human-Specific / Non-Zoonotic")
                    st.caption("This virus primarily infects humans or specific hosts.")

            with col3:
                st.markdown("### Transmission")
                # Clinical Details extraction
                symp_text = "Refer to overview"
                if "symptoms" in content_lower:
                    symp_text = content_lower.split("symptoms")[1].split(".")[0]
                st.write(f"**Symptoms:** {symp_text.capitalize()}")
                
                trans_text = "Direct contact / Droplets"
                if "transmission" in content_lower:
                    trans_text = content_lower.split("transmission")[1].split(".")[0]
                st.write(f"**Route:** {trans_text.capitalize()}")
            
            st.markdown("---")
            st.markdown(f"🔗 **Research Source:** [Wikipedia Article]({page.url})")

    except Exception:
        st.warning("Automated extraction limit reached. Please check the source link.")
        st.markdown(f"🔗 [Search for {virus_name} Source](https://en.wikipedia.org/wiki/{virus_name.replace(' ', '_')}_virus)")

# Sidebar
st.sidebar.title("💡 Viral Facts")
facts = [
    "Zoonotic viruses like Rabies jump from animals to humans.",
    "Bacteriophages are viruses that eat bacteria—very useful in biotech!",
    "The 1918 Flu pandemic changed the way we study virology.",
    "Viruses are genetic material wrapped in a protein coat (capsid)."
]
st.sidebar.info(random.choice(facts))
