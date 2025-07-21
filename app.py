import streamlit as st
from swatchpalette import ASEWriter
import io

def generate_blue_rgb_shades(n=120):
    blues = []
    for i in range(n):
        blue = int(255 - (i * 255 / (n - 1)))
        red = int(blue * 0.3)
        green = int(blue * 0.5)
        blues.append((red, green, blue))
    return sorted(blues, key=lambda rgb: 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2], reverse=True)

def create_ase_file(rgb_list):
    swatches = []
    for i, (r, g, b) in enumerate(rgb_list, 1):
        name = f"Blue {i:03d}"
        swatches.append((name, [r/255, g/255, b/255], "RGB"))
    output = io.BytesIO()
    ASEWriter(swatches, output)
    output.seek(0)
    return output

st.title("🎨 Blue Swatch Generator (.ASE)")
st.write("Generate a 120-shade blue swatch file for Illustrator.")

if st.button("Generate ASE File"):
    blue_shades = generate_blue_rgb_shades()
    ase_file = create_ase_file(blue_shades)

    st.success("✅ Swatch file ready!")
    st.download_button(
        label="⬇️ Download ASE file",
        data=ase_file,
        file_name="blue_palette_120.ase",
        mime="application/octet-stream"
    )
