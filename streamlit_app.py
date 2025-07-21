import streamlit as st
from streamlit_option_menu import option_menu
import json

# Cargar productos
with open("data/productos.json", "r") as f:
    productos = json.load(f)

# Sesión para el carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Función para mostrar productos
def mostrar_productos():
    st.header("🛍️ Nuestros Productos")
    for producto in productos:
        with st.container():
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(producto["imagen"], width=150)
            with cols[1]:
                st.subheader(producto["nombre"])
                st.write(producto["descripcion"])
                st.write(f"**Precio:** ${producto['precio']:.2f}")
                if st.button("Agregar al carrito", key=f"btn_{producto['id']}"):
                    st.session_state.carrito.append(producto)
                    st.success("Producto agregado al carrito")

# Función para mostrar el carrito
def mostrar_carrito():
    st.header("🛒 Carrito de Compras")
    if not st.session_state.carrito:
        st.info("Tu carrito está vacío")
    else:
        total = 0
        for producto in st.session_state.carrito:
            st.write(f"- {producto['nombre']} - ${producto['precio']:.2f}")
            total += producto["precio"]
        st.write(f"**Total a pagar:** ${total:.2f}")

# Función para la página de contacto
def mostrar_contacto():
    st.header("📞 Contáctanos")
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    mensaje = st.text_area("Mensaje")
    if st.button("Enviar mensaje"):
        if nombre and email and mensaje:
            st.success("¡Gracias por tu mensaje!")
        else:
            st.warning("Por favor completa todos los campos")

# Navegación principal
st.set_page_config(page_title="Tienda Virtual", layout="centered")

with st.sidebar:
    selected = option_menu(
        menu_title="Menú",
        options=["Inicio", "Productos", "Carrito", "Contacto"],
        icons=["house", "shop", "cart", "envelope"],
        menu_icon="cast",
        default_index=0
    )

# Mostrar páginas
if selected == "Inicio":
    st.title("Bienvenido a nuestra Tienda Virtual 🛒")
    st.image("https://via.placeholder.com/800x300?text=Tienda+Virtual", use_column_width=True)
    st.write("Explora nuestros productos de calidad. Compra fácil, rápido y seguro.")

elif selected == "Productos":
    mostrar_productos()

elif selected == "Carrito":
    mostrar_carrito()

elif selected == "Contacto":
    mostrar_contacto()
