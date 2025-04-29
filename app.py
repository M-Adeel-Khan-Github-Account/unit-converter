import streamlit as st

def unit_converter():
    # ---------- CSS Styling ----------
    st.markdown("""
        <style>
        .main-title {
            font-size: 45px;
            text-align: center;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 0px 0px 12px #00ffe5, 0px 0px 20px #00bfff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .app-background {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
        }
        .glass-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px 30px;
            border-radius: 20px;
            backdrop-filter: blur(14px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
            max-width: 500px;
            margin: 50px auto;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .result {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            background-color: #1abc9c;
            color: white;
            padding: 12px;
            border-radius: 10px;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: #ccc;
            margin-top: 50px;
        }
        </style>
        <div class="app-background"></div>
    """, unsafe_allow_html=True)

    # ---------- Title ----------
    st.markdown("<h1 class='main-title'>🌐 VIP Unit Converter by Adeel</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)

    # ---------- Conversion Logic ----------
    conversion_factors = {
        "Weight": {
            "Gram": 1,
            "Kilogram": 0.001,
            "Pound": 0.00220462,
            "Ounce": 0.035274
        },
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        },
        "Currency": {
            "USD": 1,
            "PKR": 279.96,
            "EUR": 0.95,
            "GBP": 0.79,
            "INR": 87.19,
        }
    }

    category = st.selectbox("🔢 Select Category", list(conversion_factors.keys()))
    from_unit = st.selectbox("🔁 From Unit", list(conversion_factors[category].keys()))
    to_unit = st.selectbox("➡️ To Unit", list(conversion_factors[category].keys()))
    input_value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")

    if st.button("🎯 Convert"):
        if from_unit == to_unit:
            result = input_value
        else:
            result = input_value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
        st.markdown(f"<div class='result'>{input_value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Made with ❤️ by Adeel using Python & Streamlit</div>", unsafe_allow_html=True)

# ---------- Run App ----------
if __name__ == "__main__":
    unit_converter()
