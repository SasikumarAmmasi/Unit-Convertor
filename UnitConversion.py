import streamlit as st
import math

# ====================================================================
# 1. UNIT CONVERTER CLASS - This contains the necessary conversion logic.
# ====================================================================
class UnitConverter:
    # --- PRESSURE Conversion Logic ---
    def convert_pressure(self, value, from_unit, to_unit):
        # 1. Convert to a base unit (e.g., kPa absolute)
        # Note: 'barg' conversion assumes standard atmospheric pressure for gauge to absolute
        if from_unit == 'barg':
            base_value = value * 100 + 101.325 # approx to kPa absolute
        elif from_unit == 'kg/cm2':
            base_value = value * 98.0665        # to kPa
        elif from_unit == 'pasig':
            base_value = value * 0.00689476      # to kPa (assuming a gauge pressure)
        elif from_unit == 'kPa':
            base_value = value
        elif from_unit == 'pascal':
            base_value = value / 1000            # to kPa
        elif from_unit == 'mmH2O':
            base_value = value * 0.00980638      # to kPa
        else:
            raise ValueError(f"Unknown pressure unit: {from_unit}")

        # 2. Convert from the base unit (kPa) to the target unit
        if to_unit == 'barg':
            return (base_value - 101.325) / 100
        elif to_unit == 'kg/cm2':
            return base_value / 98.0665
        elif to_unit == 'pasig':
            return base_value / 0.00689476
        elif to_unit == 'kPa':
            return base_value
        elif to_unit == 'pascal':
            return base_value * 1000
        elif to_unit == 'mmH2O':
            return base_value / 0.00980638
        else:
            raise ValueError(f"Unknown pressure unit: {to_unit}")

    # --- TEMPERATURE Conversion Logic ---
    def convert_temperature(self, value, from_unit, to_unit):
        # 1. Convert to a base unit (Kelvin)
        if from_unit == 'C':
            base_value = value + 273.15
        elif from_unit == 'F':
            base_value = (value - 32) * (5/9) + 273.15
        elif from_unit == 'K':
            base_value = value
        elif from_unit == 'R':
            base_value = value * (5/9)
        else:
            raise ValueError(f"Unknown temperature unit: {from_unit}")

        # 2. Convert from the base unit (Kelvin) to the target unit
        if to_unit == 'C':
            return base_value - 273.15
        elif to_unit == 'F':
            return (base_value - 273.15) * (9/5) + 32
        elif to_unit == 'K':
            return base_value
        elif to_unit == 'R':
            return base_value * (9/5)
        else:
            raise ValueError(f"Unknown temperature unit: {to_unit}")

    # --- DENSITY Conversion Logic ---
    def convert_density(self, value, from_unit, to_unit):
        # Only two units, simple ratio conversion
        if from_unit == 'kg/m3' and to_unit == 'lb/ft3':
            return value * 0.06242796
        elif from_unit == 'lb/ft3' and to_unit == 'kg/m3':
            return value * 16.01846
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported density conversion pair.")
# ====================================================================

converter = UnitConverter() # Instantiate the converter class


def unit_converter_app():
    """Main Streamlit application logic for the unit converter."""
    st.title("Unit Converter App 📏")

    # --- Pressure Conversion ---
    st.header("Pressure Conversion 🌡️")
    pressure_units = ['barg', 'kg/cm2', 'pasig', 'kPa', 'pascal', 'mmH2O']

    col1, col2, col3 = st.columns(3)
    with col1:
        pressure_value = st.number_input("Pressure Value:", value=10.0, format="%f", key="p_value")
    with col2:
        # Set a default value that is in the options list
        pressure_from_unit = st.selectbox("From Unit:", options=pressure_units, index=3, key="p_from")
    with col3:
        pressure_to_unit = st.selectbox("To Unit:", options=pressure_units, index=0, key="p_to")

    if st.button('Convert Pressure', key="p_convert_btn"):
        try:
            result = converter.convert_pressure(
                pressure_value,
                pressure_from_unit,
                pressure_to_unit
            )
            st.success(f"**Result:** {pressure_value} {pressure_from_unit} is **{result:.3f}** {pressure_to_unit}")
        except Exception as e:
            st.error(f"Error during pressure conversion: {e}")

    st.markdown("---")

    # --- Temperature Conversion ---
    st.header("Temperature Conversion 🔥")
    temp_units = ['C', 'F', 'K', 'R']

    col4, col5, col6 = st.columns(3)
    with col4:
        temperature_value = st.number_input("Temperature Value:", value=25.0, format="%f", key="t_value")
    with col5:
        temperature_from_unit = st.selectbox("From Unit:", options=temp_units, index=0, key="t_from")
    with col6:
        temperature_to_unit = st.selectbox("To Unit:", options=temp_units, index=1, key="t_to")

    if st.button('Convert Temperature', key="t_convert_btn"):
        try:
            result = converter.convert_temperature(
                temperature_value,
                temperature_from_unit,
                temperature_to_unit
            )
            st.success(f"**Result:** {temperature_value}°{temperature_from_unit} is **{result:.2f}**°{temperature_to_unit}")
        except Exception as e:
            st.error(f"Error during temperature conversion: {e}")

    st.markdown("---")

    # --- Density Conversion ---
    st.header("Density Conversion ⚖️")
    density_units = ['kg/m3', 'lb/ft3']

    col7, col8, col9 = st.columns(3)
    with col7:
        density_value = st.number_input("Density Value:", value=1000.0, format="%f", key="d_value")
    with col8:
        density_from_unit = st.selectbox("From Unit:", options=density_units, index=0, key="d_from")
    with col9:
        density_to_unit = st.selectbox("To Unit:", options=density_units, index=1, key="d_to")

    if st.button('Convert Density', key="d_convert_btn"):
        try:
            result = converter.convert_density(
                density_value,
                density_from_unit,
                density_to_unit
            )
            st.success(f"**Result:** {density_value} {density_from_unit} is **{result:.3f}** {density_to_unit}")
        except Exception as e:
            st.error(f"Error during density conversion: {e}")


if __name__ == "__main__":
    unit_converter_app()
