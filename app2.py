import streamlit as st
import random

def create_animations():
    hearts = []
    stars = []
    for _ in range(5):
        hearts.append({'left': f"{random.uniform(0, 100)}vw", 'top': f"{random.uniform(0, 100)}vh"})
        stars.append({'left': f"{random.uniform(0, 100)}vw", 'top': f"{random.uniform(0, 100)}vh"})
    return hearts, stars

def main():
    st.set_page_config(page_title="Carta Especial", page_icon=":envelope:", layout="wide")
    st.title("Una invitación especial")
    
    # Display the invitation card with styling
    st.markdown("""
        <style>
            .envelope {{
                width: 300px;
                height: 200px;
                background-color: #f5d9d5;
                position: relative;
                cursor: pointer;
                transition: transform 0.3s ease;
                display: inline-block;
            }}
            .envelope:hover {{
                transform: scale(1.05);
            }}
            .envelope-text {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 18px;
                font-weight: bold;
                color: #8e4c4c;
            }}
            .card {{
                background-color: white;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 300px;
                margin: auto;
                transition: transform 0.3s ease;
                display: none;
            }}
            .card.open {{
                display: block;
                transform: scale(1);
                animation: cardOpen 1s ease;
            }}
            @keyframes cardOpen {{
                0% {{ transform: scale(0) rotate(0deg); }}
                50% {{ transform: scale(1.2) rotate(5deg); }}
                100% {{ transform: scale(1) rotate(0deg); }}
            }}
            h1 {{
                color: #ff69b4;
                animation: colorChange 5s infinite;
            }}
            @keyframes colorChange {{
                0% {{ color: #ff69b4; }}
                25% {{ color: #ff1493; }}
                50% {{ color: #ff4500; }}
                75% {{ color: #ff6347; }}
                100% {{ color: #ff69b4; }}
            }}
            button {{
                background-color: #ff69b4;
                color: white;
                border: none;
                padding: 10px 20px;
                margin: 10px;
                border-radius: 5px;
                cursor: pointer;
                transition: all 0.3s;
            }}
            button:hover {{
                background-color: #ff1493;
                transform: scale(1.1);
            }}
            .heart {{
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: red;
                transform: rotate(45deg);
                animation: heartBeat 1s infinite;
            }}
            .heart::before,
            .heart::after {{
                content: '';
                width: 20px;
                height: 20px;
                background-color: red;
                border-radius: 50%;
                position: absolute;
            }}
            .heart::before {{
                top: -10px;
                left: 0;
            }}
            .heart::after {{
                top: 0;
                left: -10px;
            }}
            @keyframes heartBeat {{
                0% {{ transform: rotate(45deg) scale(1); }}
                25% {{ transform: rotate(45deg) scale(1.1); }}
                50% {{ transform: rotate(45deg) scale(1); }}
                75% {{ transform: rotate(45deg) scale(1.1); }}
                100% {{ transform: rotate(45deg) scale(1); }}
            }}
            .star {{
                position: absolute;
                width: 0;
                height: 0;
                border-left: 10px solid transparent;
                border-right: 10px solid transparent;
                border-bottom: 20px solid gold;
                animation: starTwinkle 2s infinite;
            }}
            .star::after {{
                content: '';
                position: absolute;
                top: 15px;
                left: -10px;
                border-left: 10px solid transparent;
                border-right: 10px solid transparent;
                border-top: 20px solid gold;
            }}
            @keyframes starTwinkle {{
                0% {{ opacity: 1; }}
                50% {{ opacity: 0.3; }}
                100% {{ opacity: 1; }}
            }}
        </style>
    """, unsafe_allow_html=True)
    
    envelope_clicked = st.button('Abrir sobre')
    
    if envelope_clicked:
        hearts, stars = create_animations()
        st.markdown('<div class="card open">', unsafe_allow_html=True)
        st.write("Hanna y Sharon, me encantaría saber si alguna de ustedes quisiera tener una cita conmigo.")
        choice = st.radio("", ["Sí", "No"])
        if st.button('Enviar'):
            if choice == "Sí":
                st.write('¡Gracias por tu respuesta!')
            else:
                st.write('¡Esperamos verte pronto!')
        st.markdown('</div>', unsafe_allow_html=True)

        # Display hearts and stars
        for heart in hearts:
            st.markdown(f'<div class="heart" style="left: {heart["left"]}; top: {heart["top"]};"></div>', unsafe_allow_html=True)
        for star in stars:
            st.markdown(f'<div class="star" style="left: {star["left"]}; top: {star["top"]};"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
