'''
import streamlit as st

# 1. MUST be the first Streamlit command - No exceptions!
st.set_page_config(
    page_title="AI Interior Design Generator", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Local Imports (Ensure these files are in your GitHub root folder)
try:
    from theme_config_css import CSS_STYLES
    from viewer import (
        display_home_tab, 
        display_upload_tab, 
        display_design_tab, 
        display_results_tab, 
        display_about_tab
    )
    import preprocessor
    import generator
    import postprocessor
    import llm_designer_agent
except ImportError as e:
    st.error(f"Missing File Error: {e}")
    st.stop()

# 3. Apply CSS styles (Now that page config is set, we can apply CSS)
st.markdown(CSS_STYLES, unsafe_allow_html=True)

# 4. Initialize session state
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'segmentation_done' not in st.session_state:
    st.session_state.segmentation_done = False
if 'depth_map' not in st.session_state:
    st.session_state.depth_map = None
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'seg_visualization' not in st.session_state:
    st.session_state.seg_visualization = None
if 'generated_images' not in st.session_state:
    st.session_state.generated_images = []

# 5. Tab structure
tab_home, tab1, tab2, tab3, tab_about = st.tabs(["Home", "Upload", "Design", "Results", "About"])

with tab_home:
    display_home_tab()

with tab1:
    display_upload_tab(preprocessor)

with tab2:
    display_design_tab()

with tab3:
    display_results_tab(generator, postprocessor, llm_designer_agent)

with tab_about:
    display_about_tab()
'''

import streamlit as st

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 1. MUST be the first Streamlit command - No exceptions!
st.set_page_config(
    page_title="AI Interior Design Generator", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Local Imports (Ensure these files are in your GitHub root folder)
try:
    from theme_config_css import CSS_STYLES
    from viewer import (
        display_home_tab, 
        display_upload_tab, 
        display_design_tab, 
        display_results_tab, 
        display_about_tab
    )
    import preprocessor
    import generator
    import postprocessor
    import llm_designer_agent
except ImportError as e:
    st.error(f"Missing File Error: {e}")
    st.stop()

# 3. Apply CSS styles
st.markdown(CSS_STYLES, unsafe_allow_html=True)

# --- NEW HEADER SECTION ---
# This adds the left-aligned title and slogan using your requested palette
st.markdown('''

<div style="text-align: left; padding: 10px 0px 20px 0px; margin-bottom: 20px; border-bottom: 3px solid #38A3A5;">
        <h1 style="color: #000000; font-size: 3rem; margin-bottom: 0px; font-weight: 800;">
            SmartSpace AI
        </h1>
        <p style="color: #225A5E; font-size: 1.2rem; font-weight: 600; margin-top: 5px;">
            Smarter design for modern living.
        </p>
</div>
''', unsafe_allow_html=True)
# ---------------------------

# 4. Initialize session state
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'segmentation_done' not in st.session_state:
    st.session_state.segmentation_done = False
if 'depth_map' not in st.session_state:
    st.session_state.depth_map = None
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'seg_visualization' not in st.session_state:
    st.session_state.seg_visualization = None
if 'generated_images' not in st.session_state:
    st.session_state.generated_images = []

# 5. Tab structure
tab_home, tab1, tab2, tab3, tab_about = st.tabs(["Home", "Upload", "Design", "Results", "About"])

with tab_home:
    display_home_tab()

with tab1:
    display_upload_tab(preprocessor)

with tab2:
    display_design_tab()

with tab3:
    display_results_tab(generator, postprocessor, llm_designer_agent)

with tab_about:
    display_about_tab()
