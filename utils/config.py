
import streamlit as st

from st_pages import get_pages, get_script_run_ctx 
from streamlit_theme import st_theme

PAGES = {
    "app": {
        "page": "app.py",
        "label": "Home",
        "icon": "🏠",
        "hidden": False,
    },
    "prototipo": {
        "page": "./pages/prototipo.py",
        "label": "Prototipo",
        "icon": "⚛️",
        "hidden": False,
    },
    "review": {
        "page": "./pages/review.py",
        "label": "Evaluanos",
        "icon": "⭐",
        "hidden": True,
    },
    "about": {
        "page": "./pages/about.py",
        "label": "Sobre Nosotros",
        "icon": "👥",
        "hidden": False,
    },
}

def set_config(
        page_title: str | None = None,
        page_icon: str | None = None,
        layout: str | None = "centered"
    ):

    # st.session_state['momento'] = MOMENTO

    """
    Base Layout se encarga de configurar la pagina actual además de configurar el menu por defeato

    Args:
        page_title (str | None): Titlo de la pagina (el que se vera en el tab del navegador)
        page_icon (str | None, optional): Icono de la pagina (el que se vera en el tab del navegador). Defaults to None.
        layout (str | None, optional): Tipo de layout ('centered' o 'wide'). Defaults to "centered".
    """

    ctx = get_script_run_ctx()
    current_page_name = get_pages("")[ctx.page_script_hash]["page_name"]

    if layout not in [ "centered", "wide"]: 
        print(f"layouts.base_layout: 'layout must be 'centered' or 'wide', got {layout}. Default to 'centered")
        layout = "centered"

    st.set_page_config(
        layout=layout,
        page_title= PAGES[current_page_name]["label"] if page_title == None else page_title,
        page_icon=PAGES[current_page_name]["icon"] if page_icon == None else page_icon
    )  
    
    with st.sidebar:
        theme = st_theme()

        if theme != None and theme["base"] == 'dark':
            st.image("assets/img/uninorte-logo.png", use_column_width=True) 
        else: 
            st.image("assets/img/uninorte-logo-light.png", use_column_width=True)  

        st.divider()

        for page_link in PAGES.values():
            if not page_link["hidden"]: 
                st.page_link(
                    page_link["page"],
                    label = page_link["label"],
                    icon = page_link["icon"]
                )