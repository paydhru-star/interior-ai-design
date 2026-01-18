# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. Main Background - Using your requested 80ED99 */
    .stApp {
        background-color: #80ED99 !important;
        background-image: linear-gradient(180deg, #80ED99 0%, #57CC99 100%) !important;
        background-attachment: fixed;
    }

    /* 2. Global Text - Forced to the darkest color in your palette for readability */
    html, body, [class*="st-"], p, span, label, .stMarkdown {
        color: #225A5E !important; /* Deepened version of 38A3A5 for legibility */
        font-weight: 500;
    }

    /* 3. Main Header - Gradient using the full Emerald palette */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #38A3A5, #48B89F, #57CC99, #225A5E);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 4. Sharp Square Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #38A3A5 !important; /* Darkest Mint for the bar */
        padding: 0px;
        border-radius: 0px; 
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #ffffff !important;
        border-radius: 0px !important; 
        padding: 12px 30px;
        color: #38A3A5 !important;
        font-weight: 700;
        border: 1px solid #38A3A5 !important;
    }

    /* Active Tab - Emerald Green with White Text */
    .stTabs [aria-selected="true"] {
        background: #57CC99 !important;
        color: #FFFFFF !important;
        border-bottom: 4px solid #38A3A5 !important;
    }

    /* 5. Square Content Cards - White background to make text pop */
    .feature-card, .info-box, .stAlert {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 3px solid #38A3A5 !important;
        color: #225A5E !important;
        border-radius: 0px !important;
        box-shadow: 8px 8px 0px #48B89F !important; /* Square offset shadow */
        padding: 20px;
        margin: 10px 0px;
    }

    /* 6. Inputs & Buttons - Sharp Squares */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: #ffffff !important;
        color: #225A5E !important;
        border-radius: 0px !important;
        border: 2px solid #38A3A5 !important;
    }

    .stButton button {
        background: #38A3A5 !important;
        color: #ffffff !important;
        border-radius: 0px !important;
        border: none !important;
        font-weight: 700;
        padding: 15px 40px;
        box-shadow: 4px 4px 0px #225A5E !important;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background: #48B89F !important;
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #225A5E !important;
    }

    /* 7. Sub-headers with Palette Accent */
    .sub-header {
        color: #225A5E;
        border-left: 10px solid #38A3A5;
        padding-left: 15px;
        background: rgba(255, 255, 255, 0.3);
        font-weight: 700;
    }
</style>
"""
