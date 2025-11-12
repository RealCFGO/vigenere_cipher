import streamlit as st
from datetime import datetime

def vigenere_cipher(text, key, decrypt=False):
    """Vigenère cipher encryption/decryption."""
    if not key:
        return text
    result, key_idx = [], 0
    key = key.upper()
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_idx % len(key)]) - ord('A')
            result.append(chr((ord(char) - start + (-shift if decrypt else shift)) % 26 + start))
            key_idx += 1
        else:
            result.append(char)
    return ''.join(result)


def main():
    st.set_page_config(page_title="Vigenère Chiffer", layout="centered")
    
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    st.title("Vigenère Chiffer")
    st.markdown("Krypter og dekrypter beskeder med Vigenère-chifferet.")
    
    mode = st.radio("Vælg tilstand:", ("Krypter", "Dekrypter"), horizontal=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        label = "Indtast tekst at kryptere:" if mode == "Krypter" else "Indtast tekst at dekryptere:"
        placeholder = "Skriv din besked her..." if mode == "Krypter" else "Skriv din krypterede besked her..."
        input_text = st.text_area(label, height=150, placeholder=placeholder)
    with col2:
        key = st.text_input("Nøgle:", help="Kun bogstaver")
    
    if st.button(mode, use_container_width=True):
        if not input_text:
            st.warning("Indtast venligst noget tekst.")
        elif not key:
            st.warning("Indtast venligst en nøgle.")
        elif not key.isalpha():
            st.error("Nøglen må kun indeholde bogstaver.")
        else:
            result = vigenere_cipher(input_text, key, decrypt=(mode == "Dekrypter"))
            timestamp = datetime.now().strftime('%H:%M:%S')
            st.session_state.history.insert(0, {
                'mode': mode,
                'key': key,
                'input': input_text[:50] + '...' if len(input_text) > 50 else input_text,
                'result': result,
                'time': timestamp
            })
            if len(st.session_state.history) > 10:
                st.session_state.history.pop()
            st.success(f"{mode}ing gennemført!")
            st.text_area("Resultat:", value=result, height=150)
            st.code(result, language=None)
    
    if st.session_state.history:
        st.divider()
        st.subheader("Historik")
        for i, entry in enumerate(st.session_state.history):
            with st.expander(f"{entry['time']} - {entry['mode']} (Nøgle: {entry['key']})"):
                st.text(f"Input: {entry['input']}")
                st.code(entry['result'], language=None)
                if st.button(f"Dekrypter med samme nøgle", key=f"decrypt_{i}"):
                    decrypted = vigenere_cipher(entry['result'], entry['key'], decrypt=True)
                    st.text_area("Dekrypteret:", value=decrypted, height=100, key=f"dec_result_{i}")
    
    with st.expander("Om Vigenère-chifferet"):
        st.markdown("""
        **Vigenère-chifferet** er en krypteringsmetode der bruger forskellige Caesar-cifre 
        baseret på bogstaverne i et nøgleord.
        
        **Sådan virker det:**
        - Hvert bogstav i nøglen bestemmer forskydningen for det tilsvarende bogstav i beskeden
        - Nøglen gentages for at matche beskedens længde
        - Ikke-alfabetiske tegn (mellemrum, tegnsætning) bevares
        
        **Eksempel:**
        - Besked: `HALLO VERDEN`
        - Nøgle: `NØGLE`
        - Krypteret: `UNZZC IHKRHG`
        """)


if __name__ == "__main__":
    main()
