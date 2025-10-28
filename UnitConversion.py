import streamlit as st
import math

# --- UnitConverter Class (Example/Template) ---
class UnitConverter:
    # --- PRESSURE Conversion Logic ---
    def convert_pressure(self, value, from_unit, to_unit):
        # 1. Convert everything to a base unit (e.g., kPa)
        if from_unit == 'barg':
            base_value = value * 100 + 101.325 # approx to kPa absolute
        elif from_unit == 'kg/cm2':
            base_value = value * 98.0665 # to kPa
        elif from_unit == 'pasig':
            base_value = value * 0.00689476 # to kPa
        elif from_unit == 'kPa':
            base_value = value
        elif from_unit == 'pascal':
            base_value = value / 1000 # to kPa
        elif from_unit == 'mmH2O':
            base_value = value * 0.00980638 # to kPa
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
        # 1. Convert everything to a base unit (e.g., Kelvin)
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
        # The two density units are kg/m3 and lb/ft3
        if from_unit == 'kg/m3' and to_unit == 'lb/ft3':
            # 1 kg/m3 = 0.06242796 lb/ft3
            return value * 0.06242796
        elif from_unit == 'lb/ft3' and to_unit == 'kg/m3':
            # 1 lb/ft3 = 16.01846 kg/m3
            return value * 16.01846
        elif from_unit == to_unit:
            return value
        else:
            # Handle mixed unit inputs not covered by the pairs above
            raise ValueError("Unsupported density conversion pair.")

# --- End of UnitConverter Class ---
