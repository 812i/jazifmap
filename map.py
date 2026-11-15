
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="JAZIF MAP",
    page_icon="🌿",
    layout="wide"
)

# COLORS
DARK = "#263D32"
GREEN = "#496653"
LIGHT = "#E7EDE5"
BG = "#F7F7F2"
MUTED = "#66766A"

# STYLE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F7F7F2;
    color: #263D32;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

.hero {
    background: #263D32;
    color: #F7F7F2;
    padding: 38px 30px;
    border-radius: 22px;
    margin-bottom: 25px;
}

.eyebrow {
    color: #C5D3C6;
    font-size: 11px;
    letter-spacing: 3px;
}

.hero h1 {
    font-size: clamp(42px, 8vw, 68px);
    font-weight: 800;
    margin: 12px 0;
    letter-spacing: -2px;
}

.hero p {
    color: #E2E8DF;
    font-size: 14px;
    line-height: 1.8;
    max-width: 520px;
}

.section {
    font-size: 23px;
    font-weight: 800;
    margin: 28px 0 12px;
}

.place {
    background: white;
    border: 1px solid #E2E8DF;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
}

.category {
    color: #66766A;
    font-size: 11px;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.place h3 {
    color: #263D32;
    margin: 8px 0;
    font-size: 18px;
}

.place p {
    color: #66766A;
    font-size: 13px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #66766A;
    font-size: 11px;
    padding: 35px 0 15px;
}
</style>
""", unsafe_allow_html=True)

# PLACES
places = [
    {
        "name": "Visitor Pavilion",
        "category": "Visitor Experience",
        "description": "A starting point to discover the park and its destinations.",
        "lat": 24.7143,
        "lon": 46.71166
    },
    {
        "name": "Royal Arts Complex",
        "category": "Arts & Culture",
        "description": "A destination for art, creativity and cultural experiences.",
        "lat": 24.7160,
        "lon": 46.7100
    },
    {
        "name": "Museum of World Cultures",
        "category": "Museum",
        "description": "Discover cultures, stories and heritage from around the world.",
        "lat": 24.7170,
        "lon": 46.7130
    },
    {
        "name": "Outdoor Cinema",
        "category": "Entertainment",
        "description": "An outdoor space for screenings and shared experiences.",
        "lat": 24.7125,
        "lon": 46.7150
    },
    {
        "name": "Amphitheater",
        "category": "Entertainment",
        "description": "A venue for performances, gatherings and events.",
        "lat": 24.7105,
        "lon": 46.7105
    },
    {
        "name": "Art Park",
        "category": "Nature & Art",
        "description": "An open space combining nature and artistic experiences.",
        "lat": 24.7180,
        "lon": 46.7080
    },
    {
        "name": "Walking Trails",
        "category": "Outdoor",
        "description": "Explore the park through outdoor walking paths.",
        "lat": 24.7130,
        "lon": 46.7060
    }
]

# HEADER
st.markdown("""
<div class="hero">
    <div class="eyebrow">DISCOVER • EXPLORE • CONNECT</div>
    <h1>JAZIF MAP.</h1>
    <p>
        Your guide to discovering the destinations,
        spaces and experiences of King Salman Park.
    </p>
    <div style="color:#C5D3C6;font-size:11px;margin-top:22px;">
        RIYADH, SAUDI ARABIA / EXPLORE THE PARK
    </div>
</div>
""", unsafe_allow_html=True)

# FILTER
st.markdown('<div class="section">Explore the park</div>',
            unsafe_allow_html=True)

categories = ["All"] + sorted(set(p["category"] for p in places))

category = st.selectbox("Filter by category", categories)

filtered = [
    p for p in places
    if category == "All" or p["category"] == category
]

# MAP
st.markdown('<div class="section">Interactive map</div>',
            unsafe_allow_html=True)

st.caption("Select a destination below to explore its details.")

map_data = pd.DataFrame(filtered)

st.map(
    map_data,
    latitude="lat",
    longitude="lon",
    color="#496653",
    size=20,
    zoom=13,
    use_container_width=True
)

# DESTINATION DETAILS
st.markdown('<div class="section">Discover destinations</div>',
            unsafe_allow_html=True)

selected_name = st.selectbox(
    "Choose a destination",
    [p["name"] for p in filtered]
)

selected = next(
    p for p in filtered
    if p["name"] == selected_name
)

st.markdown(f"""
<div class="place">
    <div class="category">{selected['category']}</div>
    <h3>{selected['name']}</h3>
    <p>{selected['description']}</p>
    <p>📍 {selected['lat']}, {selected['lon']}</p>
</div>
""", unsafe_allow_html=True)

# ALL PLACES
st.markdown('<div class="section">All destinations</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

for i, place in enumerate(filtered):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="place">
            <div class="category">{place['category']}</div>
            <h3>{place['name']}</h3>
            <p>{place['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    JAZIF MAP © 2026<br>
    EXPLORE KING SALMAN PARK
</div>
""", unsafe_allow_html=True)
