
import streamlit as st
import folium
from streamlit_folium import st_folium

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="JAZIF MAP",
    page_icon="🌿",
    layout="wide"
)

# ---------------- STYLE ----------------
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
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: #263D32;
    color: #F7F7F2;
    padding: 35px;
    border-radius: 22px;
    margin-bottom: 25px;
}

.eyebrow {
    color: #C5D3C6;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 700;
}

.hero h1 {
    font-size: clamp(38px, 7vw, 65px);
    margin: 12px 0;
    font-weight: 800;
    letter-spacing: -2px;
}

.hero p {
    color: #E2E8DF;
    font-size: 15px;
    max-width: 520px;
    line-height: 1.8;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #263D32;
    margin: 20px 0 12px;
}

.place-card {
    background: white;
    border: 1px solid #E2E8DF;
    border-radius: 17px;
    padding: 19px;
    margin-bottom: 12px;
}

.place-category {
    color: #66766A;
    font-size: 11px;
    letter-spacing: 1.5px;
    font-weight: 700;
    text-transform: uppercase;
}

.place-card h3 {
    color: #263D32;
    margin: 8px 0;
    font-size: 19px;
}

.place-card p {
    color: #66766A;
    font-size: 13px;
    line-height: 1.7;
}

.footer {
    color: #66766A;
    font-size: 12px;
    text-align: center;
    padding: 30px 0 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PLACES ----------------
PLACES = [
    {
        "name": "Visitor Pavilion",
        "category": "Visitor Experience",
        "description": "A starting point for visitors to explore the park and discover its destinations.",
        "lat": 24.7143,
        "lon": 46.71166
    },
    {
        "name": "Royal Arts Complex",
        "category": "Arts & Culture",
        "description": "A destination dedicated to arts, creativity and cultural experiences.",
        "lat": 24.7160,
        "lon": 46.7100
    },
    {
        "name": "Museum of World Cultures",
        "category": "Museum",
        "description": "A cultural destination celebrating different cultures and stories.",
        "lat": 24.7170,
        "lon": 46.7130
    },
    {
        "name": "Outdoor Cinema",
        "category": "Entertainment",
        "description": "An outdoor destination for screenings and shared experiences.",
        "lat": 24.7125,
        "lon": 46.7150
    },
    {
        "name": "Amphitheater",
        "category": "Entertainment",
        "description": "A space for performances, gatherings and cultural events.",
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
        "description": "Outdoor paths for walking, exploring and enjoying the surroundings.",
        "lat": 24.7130,
        "lon": 46.7060
    }
]

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">DISCOVER • EXPLORE • CONNECT</div>
    <h1>JAZIF MAP.</h1>
    <p>
        Your guide to discovering the destinations, spaces
        and experiences of King Salman Park.
    </p>
    <div style="margin-top:25px;color:#C5D3C6;font-size:12px;">
        RIYADH, SAUDI ARABIA &nbsp; / &nbsp; EXPLORE THE PARK
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- FILTERS ----------------
st.markdown('<div class="section-title">Explore the map</div>', unsafe_allow_html=True)

categories = ["All"] + sorted(set(p["category"] for p in PLACES))

selected_category = st.selectbox(
    "Choose a category",
    categories
)

filtered_places = [
    p for p in PLACES
    if selected_category == "All" or p["category"] == selected_category
]

# ---------------- MAP ----------------
st.markdown("""
<div style="color:#66766A;font-size:13px;margin-bottom:12px;">
    Select a marker to discover more about each destination.
</div>
""", unsafe_allow_html=True)

park_map = folium.Map(
    location=[24.7143, 46.71166],
    zoom_start=14,
    tiles="CartoDB positron",
    control_scale=True
)

for place in filtered_places:
    popup_html = f"""
    <div style="width:190px;font-family:Arial;color:#263D32;">
        <b style="font-size:15px;">{place['name']}</b>
        <br>
        <span style="font-size:11px;color:#66766A;">
            {place['category']}
        </span>
        <p style="font-size:12px;line-height:1.5;">
            {place['description']}
        </p>
    </div>
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=place["name"],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(
            color="green",
            icon="leaf",
            prefix="fa"
        )
    ).add_to(park_map)

map_result = st_folium(
    park_map,
    width=None,
    height=520,
    returned_objects=["last_object_clicked"]
)

# ---------------- SELECTED PLACE ----------------
clicked = map_result.get("last_object_clicked")

if clicked:
    st.markdown(
        '<div class="section-title">Selected location</div>',
        unsafe_allow_html=True
    )
    st.caption(
        f"Coordinates: {clicked['lat']:.5f}, {clicked['lng']:.5f}"
    )

# ---------------- PLACES LIST ----------------
st.markdown('<div class="section-title">Discover destinations</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

for index, place in enumerate(filtered_places):
    with (col1 if index % 2 == 0 else col2):
        st.markdown(f"""
        <div class="place-card">
            <div class="place-category">{place['category']}</div>
            <h3>{place['name']}</h3>
            <p>{place['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    JAZIF MAP © 2026<br>
    EXPLORE KING SALMAN PARK
</div>
""", unsafe_allow_html=True)
