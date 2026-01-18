'''
import torch
import numpy as np
from PIL import Image
from transformers import pipeline, Mask2FormerImageProcessor, Mask2FormerForUniversalSegmentation
from config import SEGMENTATION_MODEL_NAME, DEPTH_ESTIMATION_MODEL, LABELS, COLORS, ALPHA, DEFAULT_IMAGE_SIZE

def load_input(image):
    """Load image from Streamlit upload"""
    return Image.open(image).convert("RGB")

def preprocess_image(image, size=DEFAULT_IMAGE_SIZE):
    return image.resize(size)

def create_depth_map(image):
    """Create depth map from input image using MiDaS"""
    depth_estimator = pipeline("depth-estimation", model=DEPTH_ESTIMATION_MODEL)
    depth_result = depth_estimator(image)
    depth_map = depth_result["depth"]
    
    depth_array = np.array(depth_map)
    depth_array = (depth_array - depth_array.min()) / (depth_array.max() - depth_array.min()) * 255
    depth_array = depth_array.astype(np.uint8)
    
    depth_image = Image.fromarray(depth_array).convert("RGB")
    return depth_image

def setup_segmentation_model():
    """Setup segmentation model for room element detection"""
    processor = Mask2FormerImageProcessor.from_pretrained(SEGMENTATION_MODEL_NAME)
    model = Mask2FormerForUniversalSegmentation.from_pretrained(SEGMENTATION_MODEL_NAME)
    return processor, model

def run_segmentation_detection(image):
    """Run segmentation to detect walls, floor, ceiling etc."""
    processor, model = setup_segmentation_model()
    
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)

    seg = processor.post_process_semantic_segmentation(
            outputs, target_sizes=[image.size[::-1]]
         )[0]

    seg_map = seg.cpu().numpy()
    return seg_map

def visualize_segmentation_results(image, seg_map):
    """Visualize segmentation results with color overlays"""
    overlay = np.array(image).copy()

    for label_name, label_id in LABELS.items():
        mask = (seg_map == label_id)
        overlay[mask] = (
            overlay[mask] * (1 - ALPHA) + np.array(COLORS[label_name]) * ALPHA
        )

    overlay = overlay.astype(np.uint8)
    return Image.fromarray(overlay)


def analyze_room_structure(image):
    processed_image = preprocess_image(image)
    depth_map = create_depth_map(processed_image)
    seg_map = run_segmentation_detection(processed_image)
    seg_visualization = visualize_segmentation_results(processed_image, seg_map)
    
    return {
        'processed_image': processed_image,
        'depth_map': depth_map,
        'seg_map': seg_map,
        'seg_visualization': seg_visualization
    }
'''
from PIL import Image
from config import DEFAULT_IMAGE_SIZE

def process(uploaded_file):
    # This function is called by viewer.py
    image = Image.open(uploaded_file).convert("RGB")
    processed = image.resize(DEFAULT_IMAGE_SIZE)
    return processed

'''
import requests
from PIL import Image
from io import BytesIO

def clean_up(image_url):
    """
    Downloads the generated image from the URL so it can be 
    displayed and saved in the Streamlit app.
    """
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img
'''
