'''import torch
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from config import CONTROLNET_MODEL, STABLE_DIFFUSION_MODEL, DEFAULT_NUM_INFERENCE_STEPS, DEFAULT_GUIDANCE_SCALE

def setup_pipeline():
    """Setup ControlNet pipeline with depth control"""
    controlnet = ControlNetModel.from_pretrained(
        CONTROLNET_MODEL,
        torch_dtype=torch.float32
    )

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        STABLE_DIFFUSION_MODEL, 
        controlnet=controlnet,
        torch_dtype=torch.float32,
        safety_checker=None
    ).to("cpu")
    
    pipe.enable_attention_slicing()
    return pipe

def generate_design_with_controlnet(prompt, input_image, depth_image, negative_prompt="", 
                                  strength=0.8, guidance_scale=DEFAULT_GUIDANCE_SCALE, 
                                  controlnet_conditioning_scale=0.8, seed=None):
    """Generate design using ControlNet for better structure preservation"""
    pipe = setup_pipeline()
    
    generator = torch.Generator(device="cpu")
    if seed is not None:
        generator.manual_seed(seed)
    
    result = pipe(
        prompt=prompt,
        image=depth_image,
        num_inference_steps=DEFAULT_NUM_INFERENCE_STEPS,
        guidance_scale=guidance_scale,
        generator=generator,
        negative_prompt=negative_prompt,
        controlnet_conditioning_scale=controlnet_conditioning_scale,
        strength=strength
    ).images[0]
    
    return result
'''

'''
import replicate
import streamlit as st
import os

def generate(uploaded_image, prompt):
    """
    Sends the room photo and prompt to the Replicate API 
    to generate the new interior design.
    """
    # Ensure the API token is set from Streamlit Secrets
    if "REPLICATE_API_TOKEN" in st.secrets:
        os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
    else:
        raise ValueError("Missing REPLICATE_API_TOKEN in Streamlit Secrets")

    # We use a specialized Interior Design ControlNet model
    # Model: adirik/interior-design
    output = replicate.run(
        "adirik/interior-design:76604a15c357e8446d93e60ef2e69ffed8ef3d3d5f3074091e600869a0397576",
        input={
            "image": uploaded_image,
            "prompt": prompt,
            "guidance_scale": 7.5,
            "num_inference_steps": 50
        }
    )
    
    # Replicate returns a list of URLs; the second one is usually the final result
    return output[1] if len(output) > 1 else output[0]
    '''

import replicate
import streamlit as st

def generate(image, prompt):
    # Uses Replicate API to generate the design
    output = replicate.run(
        "adirik/interior-design:76604a15c357e8446d93e60ef2e69ffed8ef3d3d5f3074091e600869a0397576",
        input={"image": image, "prompt": prompt}
    )
    return output[1] if len(output) > 1 else output[0]
