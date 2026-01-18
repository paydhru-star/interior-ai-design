'''
import streamlit as st

def display_home_tab():
    st.header("🏠 Welcome to AI Interior Designer")
    st.write("Transform your space using the power of AI.")
    st.info("Start by navigating to the **Upload** tab to provide a photo of your room.")

def display_upload_tab(preprocessor):
    st.header("📸 Upload Your Room")
    uploaded_file = st.file_uploader("Choose a room photo...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.session_state.uploaded_image = uploaded_file
        st.image(uploaded_file, caption="Original Image", use_container_width=True)
        
        if st.button("Process Image"):
            with st.spinner("Analyzing room layout..."):
                # This calls the preprocessor module you imported in app.py
                result = preprocessor.process(uploaded_file)
                st.session_state.segmentation_done = True
                st.success("Room analysis complete!")

def display_design_tab():
    st.header("🎨 Choose Your Style")
    style = st.selectbox("Select a Style", ["Modern", "Minimalist", "Industrial", "Bohemian", "Scandinavian"])
    color_palette = st.color_picker("Pick a base color", "#ffffff")
    prompt = st.text_area("Additional instructions", placeholder="e.g. Add a velvet blue sofa and gold lamps")
    
    # Store these in session state to use in the Results tab
    st.session_state.design_style = style
    st.session_state.design_prompt = prompt

def display_results_tab(generator, postprocessor, llm_designer_agent):
    st.header("✨ Generated Design")
    
    if st.session_state.uploaded_image is None:
        st.warning("Please upload an image first!")
        return

    if st.button("Generate Final Design"):
        with st.spinner("Reimagining your space..."):
            # This uses the generator module to call the AI
            try:
                # 1.Enhance prompt with LLM agent
                enhanced_prompt = llm_designer_agent.enhance(st.session_state.design_style, st.session_state.design_prompt)
                
                # 2. Generate image
                generated_url = generator.generate(st.session_state.uploaded_image, enhanced_prompt)
                
                # 3. Post-process (e.g. upscaling)
                final_image = postprocessor.clean_up(generated_url)
                
                st.image(final_image, caption="Your New Room", use_container_width=True)
                st.session_state.generated_images.append(final_image)
            except Exception as e:
                st.error(f"Generation failed: {e}")

def display_about_tab():
    st.header("ℹ️ About this Project")
    st.write("Created with Streamlit and Stable Diffusion.")
    st.write("This tool uses ControlNet architecture to maintain the structure of your room while changing the furniture and decor.")
'''
import streamlit as st

def display_home_tab():
    st.header("🏠 Welcome to AI Interior Designer")
    st.write("Transform your space using the power of AI.")
    st.info("Start by navigating to the **Upload** tab to provide a photo of your room.")

def display_upload_tab(preprocessor):
    st.markdown('<h2 class="sub-header">Step 1: 📸 Upload Your Room</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        processed_img = preprocessor.process(uploaded_file)
        st.session_state.uploaded_image = processed_img
        st.image(processed_img, caption="Original Room", width="stretch")

def display_design_tab():
    st.markdown('<h2 class="sub-header"> Step 2: 🎨 Choose Your Style</h2>',  unsafe_allow_html=True)
    if st.session_state.uploaded_image is None:
        st.warning("Please upload a photo first.")
        return
    st.selectbox("Style", ["Modern", "Minimalist", "Industrial", "Bohemian", "Scandinavian"])
    

def display_results_tab(generator, postprocessor, llm_designer_agent):
    st.markdown('<h2 class="sub-header">Step 3: Results</h2>' , unsafe_allow_html=True)
    if st.button("Generate Design"):
        # This calls the updated agent
        advice = llm_designer_agent.analyze_room(st.session_state.uploaded_image, "Modern")
        st.write(advice)

def display_about_tab():
    st.header("ℹ️ About this Project")
    st.info("AI Interior Design v2026.1", width="stretch")
    st.write("Created with Streamlit and Stable Diffusion.")
