import streamlit as st
import json
import os

# Configuración de la página
st.set_page_config(page_title="Mi Tienda", layout="wide")

# Cargar productos
def cargar_productos():
    ruta = os.path.join("data", "productos.json")
    with open(ruta, "r") as archivo:
        return json.load(archivo)

productos = cargar_productos()

# Inicializar carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Menú de navegación
menu = st.sidebar.radio("Ir a:", ["Inicio", "Productos", "Carrito", "Contacto"])

# Página: Inicio
if menu == "Inicio":
    st.title("🛒 Bienvenido a Mi Tienda")
    st.image("https://via.placeholder.com/800x250?text=Bienvenido+a+Mi+Tienda", use_container_width=True)
    st.write("Explora nuestros productos y disfruta de tus compras en línea.")

# Página: Productos
elif menu == "Productos":
    st.title("📦 Productos disponibles")
    for producto in productos:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(producto["imagen"], width=150)
        with col2:
            st.subheader(producto["nombre"])
            st.write(producto["descripcion"])
            st.write(f"**Precio:** ${producto['precio']:.2f}")
            if st.button(f"Agregar '{producto['nombre']}' al carrito"):
                st.session_state.carrito.append(producto)
                st.success(f"'{producto['nombre']}' agregado al carrito")

# Página: Carrito
elif menu == "Carrito":
    st.title("🛒 Carrito de compras")
    if not st.session_state.carrito:
        st.info("Tu carrito está vacío.")
    else:
        total = 0
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']} (${item['precio']:.2f})")
            total += item["precio"]
        st.write(f"**Total: ${total:.2f}**")
        if st.button("Vaciar carrito"):
            st.session_state.carrito = []
            st.success("Carrito vaciado.")

# Página: Contacto
elif menu == "Contacto":
    st.title("📬 Contáctanos")
    nombre = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")
    mensaje = st.text_area("Mensaje")
    if st.button("Enviar mensaje"):
        if nombre and email and mensaje:
            st.success("¡Gracias por tu mensaje!")
        else:
            st.warning("Por favor, completa todos los campos.")