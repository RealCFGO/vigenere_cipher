# Vigenère Chiffer App

Webapplikation til kryptering og dekryptering af beskeder med Vigenère-chifferet, bygget med Streamlit.

![Vigenère Chiffer Preview](123.gif)

## Funktioner

- Krypter beskeder med brugerdefineret nøgle
- Dekrypter beskeder med samme nøgle
- Historik på skærmen med de seneste 10 operationer
- Hurtig dekryptering direkte fra historik
- Bevarer mellemrum og tegnsætning
- Kompakt, optimeret kode

## Installation

```bash
pip install -r requirements.txt
```

## Brug

```bash
streamlit run app.py
```

## Funktionalitet

1. Vælg tilstand (Krypter/Dekrypter)
2. Indtast tekst og nøgle (kun bogstaver)
3. Klik på knappen for at behandle
4. Resultat vises og gemmes i historik

## Historik

Alle operationer gemmes i session:
- Viser de seneste 10 krypteringer/dekrypteringer
- Inkluderer tidspunkt, nøgle, og resultat
- Klik for at dekryptere direkte fra historik

## Eksempel

- Besked: `HALLO VERDEN`
- Nøgle: `NØGLE`
- Krypteret: `UNZZC IHKRHG`

## Krav

- Python 3.7+
- Streamlit 1.31.0+
