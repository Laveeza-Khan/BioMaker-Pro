import streamlit as st
import wikipedia
import random

# --- Professional Styling using Your Palette ---
st.set_page_config(page_title="BioMaker-Pro", layout="wide")

st.markdown(f"""
    <style>
    /* Main Background: Light Gray from palette */
    .stApp {{
        background-color: #D5D3CC; 
    }}
    /* Main Title and Headers: Phthalo Green */
    h1, h2, h3 {{
        color: #19350C;
        font-family: 'Serif';
    }}
    /* Search Bar and Boxes: Deep Space Sparkle & Moonstone Blue */
    .stTextInput > div > div > input {{
        border: 2px solid #406768;
        border-radius: 8px;
    }}
    /* Custom Info Boxes */
    .stInfo {{
        background-color: #6FA9BB; /* Moonstone Blue */
        color: #19350C;
        border: none;
    }}
    .stWarning {{
        background-color: #687D31; /* Mustard Green */
        color: #ffffff;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("BioMaker-Pro: Advanced Viral Taxonomy")
st.markdown("**Developer:** Laveeza Khan")
st.markdown("---")

# --- Search Section ---
virus_name = st.text_input("Search Virus (e.g. Rabies, Ebola, MERS, T4 Phage):", "Rabies")

if virus_name:
    try:
        # Wikipedia Search Logic
        search_results = wikipedia.search(f"{virus_name} virus")
        if not search_results:
            st.error("No specific virus found. Try checking the spelling.")
        else:
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = wikipedia.summary(page_title, sentences=3)
            content_lower = page.content.lower()
            
            # 1. Overview Section
            st.subheader("General Overview")
            st.info(summary)
            
            st.markdown("---")
            
            # 2. Advanced Classification & Profile
            st.subheader("Taxonomy and Biological Profile")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### Classification")
                # Extracting Family, Genus, Species
                family = "Not found"
                genus = "Not found"
                for line in content_lower.split("\n"):
                    if "family:" in line or "family " in line: family = line
                    if "genus:" in line or "genus " in line: genus = line
                
                st.write(f"**Family:** {family.replace('family', '').strip().capitalize()}")
                st.write(f"**Genus:** {genus.replace('genus', '').strip().capitalize()}")
                st.write(f"**Species:** {page_title}")

            with col2:
                st.markdown("### Clinical Safety")
                # BSL Estimation
                danger_score = any(word in content_lower for word in ["fatal", "mortality", "high risk", "outbreak", "pandemic"])
                bsl = "3 or 4" if danger_score else "2"
                st.error(f"Biosafety Level (BSL): {bsl}")
                
                # Zoonotic Status Logic
                zoonotic_words = ["animal", "bird", "bat", "camel", "pig", "monkey", "zoonotic", "bite"]
                is_zoonotic = any(word in content_lower for word in zoonotic_words)
                if is_zoonotic:
                    st.warning("Type: Zoonotic Virus (Transmitted from animals)")
                else:
                    st.success("Type: Human-specific or Non-zoonotic")

            with col3:
                st.markdown("### Transmission")
                # Symptoms and Entry
                if "symptoms" in content_lower:
                    symp = content_lower.split("symptoms")[1].split(".")[0]
                    st.write(f"**Symptoms:** {symp.capitalize()}.")
                
                if "transmission" in content_lower:
                    trans = content_lower.split("transmission")[1].split(".")[0]
                    st.write(f"**Route:** {trans.capitalize()}.")
            
            st.markdown("---")
            st.markdown(f"🔗 **Deep Research Link:** [Read more about {page_title} on Wikipedia]({page.url})")

    except Exception:
        st.warning("Direct data extraction failed. Please use the link below for full research.")
        st.markdown(f"🔗 [Search for {virus_name} Source](https://en.wikipedia.org/wiki/{virus_name.replace(' ', '_')}_virus)")

# --- Sidebar Fun Facts ---
st.sidebar.title("💡 Viral Facts")
facts = [
    "Viruses are not technically 'alive' but carry genetic blueprints.",
    "Bacteriophages look like tiny lunar landers and only kill bacteria.",
    "The world's smallest virus is the Porcine Circovirus.",
    "The 1918 Flu pandemic was one of the deadliest in human history.",
    "Zoonotic viruses jump from animals to humans through close contact."
]
st.sidebar.info(random.choice(facts))
