import streamlit as st
import folium
from streamlit_folium import st_folium

# =====================================================
# JAZIF MAP | KING SALMAN PARK
# Independent mobile-first Streamlit project
# =====================================================

st.set_page_config(
    page_title="JAZIF MAP",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- COLORS -------------------------

DARK = "#263D32"
GREEN = "#496653"
SOFT = "#E7EDE5"
BG = "#F7F7F2"
WHITE = "#FFFFFF"
MUTED = "#66766A"
BORDER = "#E2E8DF"

# -------------------- VERIFIED LOCATION DATA ---------

# Coordinates published for King Salman Park Visitor Pavilion.
# Other attractions are listed but deliberately have no invented coordinates.

PLACES = [
    {
        "id": "visitor",
        "name": "جناح الزوار",
        "english": "Visitor Pavilion",
        "category": "مرافق وخدمات",
        "icon": "🏛️",
        "description": "جناح الزوار، ويضم مرافق استقبال ومعارض ومساحات للفعاليات.",
        "lat": 24.7143,
        "lon": 46.71166,
        "verified": True,
        "source": "OpenStreetMap data via Mapcarta",
    },
    {
        "id": "royal",
        "name": "المجمع الملكي للفنون",
        "english": "Royal Arts Complex",
        "category": "ثقافة وفنون",
        "icon": "🎨",
        "description": "وجهة ثقافية وفنية تضم مجموعة من المرافق الفنية والثقافية.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "King Salman Park Foundation",
    },
    {
        "id": "museum",
        "name": "متحف الثقافات العالمية",
        "english": "Museum of World Cultures",
        "category": "ثقافة وفنون",
        "icon": "🏺",
        "description": "متحف ضمن المجمع الملكي للفنون، مخصص للتعرف على ثقافات العالم.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "Saudi Vision 2030",
    },
    {
        "id": "cinema",
        "name": "السينما الخارجية",
        "english": "Outdoor Cinema",
        "category": "ترفيه",
        "icon": "🎬",
        "description": "مساحة سينمائية خارجية ضمن وجهات الحديقة.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "King Salman Park Foundation",
    },
    {
        "id": "amphi",
        "name": "المسرح المكشوف",
        "english": "Amphitheater",
        "category": "ترفيه",
        "icon": "🎭",
        "description": "مسرح خارجي للعروض والفعاليات.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "King Salman Park Foundation",
    },
    {
        "id": "artpark",
        "name": "حديقة الفنون",
        "english": "Art Park",
        "category": "طبيعة وحدائق",
        "icon": "🌳",
        "description": "مساحة تجمع الفن والطبيعة والتجارب الخارجية.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "King Salman Park Foundation",
    },
    {
        "id": "loop",
        "name": "مسار المشاة",
        "english": "Walking Trails",
        "category": "رياضة ومشي",
        "icon": "🚶",
        "description": "مسارات للمشي والحركة والاستمتاع بالمساحات الخضراء.",
        "lat": None,
        "lon": None,
        "verified": False,
        "source": "King Salman Park Foundation",
    },
]

CATEGORIES = [
    "الكل",
    "ثقافة وفنون",
    "طبيعة وحدائق",
    "ترفيه",
    "رياضة ومشي",
    "مرافق وخدمات",
]

# -------------------- CSS -----------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');

    html, body, [class*="css"], button, input {
        font-family: 'IBM Plex Sans Arabic', sans-serif !important;
    }

    .stApp {
        background: #F7F7F2;
        color: #263D32;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1150px;
        padding: 1.2rem 1rem 3rem !important;
    }

    .map-header {
        background: #263D32;
        color: white;
        border-radius: 22px;
        padding: 24px 22px;
        margin-bottom: 20px;
    }

    .map-header h1 {
        color: white !important;
        font-size: 30px;
        margin: 8px 0;
    }

    .map-header p {
        color: #E7EDE5 !important;
        font-size: 14px;
        margin-bottom: 0;
    }

    .eyebrow {
        color: #DCE8D9;
        font-size: 11px;
        letter-spacing: 2px;
        font-weight: 600;
    }

    .section-heading {
        color: #263D32;
        font-size: 21px;
        font-weight: 700;
        margin: 22px 0 10px;
    }

    .place-card {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 10px;
    }

    .place-icon {
        font-size: 25px;
    }

    .place-name {
        color: #263D32;
        font-size: 16px;
        font-weight: 700;
    }

    .place-en {
        color: #66766A;
        font-size: 12px;
    }

    .place-desc {
        color: #66766A;
        font-size: 13px;
        line-height: 1.8;
        margin-top: 7px;
    }

    .status {
        display: inline-block;
        padding: 5px 9px;
        border-radius: 20px;
        background: #E7EDE5;
        color: #263D32;
        font-size: 11px;
        margin-top: 8px;
    }

    .status-pending {
        background: #F2EFE4;
        color: #786B42;
    }

    .detail-box {
        background: white;
        border: 1px solid #E2E8DF;
        border-radius: 18px;
        padding: 20px;
        margin-top: 12px;
    }

    .detail-box h3 {
        color: #263D32 !important;
    }

    .stButton button {
        background: #263D32 !important;
        color: white !important;
        border: 1px solid #263D32 !important;
        border-radius: 12px !important;
        min-height: 42px;
        font-weight: 600;
    }

    .stButton button p {
        color: white !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: white;
        border-radius: 12px;
        border-color: #E2E8DF;
    }

    .map-note {
        background: #E7EDE5;
        border-radius: 13px;
        padding: 12px 14px;
        color: #263D32;
        font-size: 12px;
        line-height: 1.8;
        margin: 12px 0;
    }

    .footer {
        color: #66766A;
        text-align: center;
        font-size: 12px;
        padding: 28px 5px;
    }

    @media(max-width: 600px) {
        .block-container {
            padding: 0.7rem 0.7rem 2rem !important;
        }

        .map-header {
            padding: 21px 17px;
            border-radius: 18px;
        }

        .map-header h1 {
            font-size: 25px;
        }

        .section-heading {
            font-size: 19px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- SESSION STATE ------------------

if "selected_place" not in st.session_state:
    st.session_state.selected_place = "visitor"

if "saved_places" not in st.session_state:
    st.session_state.saved_places = []

# -------------------- HEADER --------------------------

st.markdown(
    """
    <div class="map-header">
        <div class="eyebrow">JAZIF PRESENTS</div>
        <h1>JAZIF MAP 🌿</h1>
        <p>اكتشف حديقة الملك سلمان، مكاناً بعد مكان.</p>
        <p>Explore · Discover · Connect</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- FILTERS -------------------------

st.markdown(
    '<div class="section-heading">استكشف الخريطة</div>',
    unsafe_allow_html=True,
)

filter_col, info_col = st.columns([2, 1])

with filter_col:
    selected_category = st.selectbox(
        "اختر نوع المكان",
        CATEGORIES,
        index=0,
    )

with info_col:
    st.selectbox(
        "طريقة العرض",
        ["الخريطة", "قائمة الأماكن"],
        key="display_mode",
    )

filtered_places = [
    place for place in PLACES
    if selected_category == "الكل"
    or place["category"] == selected_category
]

# -------------------- MAP -----------------------------

# The map is centered on the published Visitor Pavilion coordinates.
# It is NOT a verified park boundary or a complete masterplan overlay.

visitor = next(p for p in PLACES if p["id"] == "visitor")

park_map = folium.Map(
    location=[visitor["lat"], visitor["lon"]],
    zoom_start=15,
    tiles="OpenStreetMap",
    control_scale=True,
)

for place in filtered_places:
    if place["lat"] is None or place["lon"] is None:
        continue

    popup_html = f"""
    <div style="font-family:Arial;min-width:150px;">
        <b>{place['icon']} {place['name']}</b><br>
        <span>{place['english']}</span><br>
        <small>{place['category']}</small>
    </div>
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=place["name"],
        popup=folium.Popup(popup_html, max_width=230),
        icon=folium.Icon(
            color="green",
            icon="info-sign",
        ),
    ).add_to(park_map)

# Show a map only with verified pins.
if st.session_state.display_mode == "الخريطة":
    st_folium(
        park_map,
        use_container_width=True,
        height=440,
        returned_objects=["last_object_clicked", "last_object_clicked_tooltip"],
        key="jazif_interactive_map",
    )

    st.markdown(
        """
        <div class="map-note">
            📍 المواقع الظاهرة على الخريطة هي المواقع التي توفرت لها
            إحداثيات منشورة. بقية المعالم موجودة في قائمة الاستكشاف
            بانتظار التحقق من مواقعها الدقيقة.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- PLACE LIST ---------------------

st.markdown(
    '<div class="section-heading">وجهات الحديقة</div>',
    unsafe_allow_html=True,
)

for place in filtered_places:
    with st.container(border=True):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(
                f"""
                <div class="place-icon">{place['icon']}</div>
                <div class="place-name">{place['name']}</div>
                <div class="place-en">{place['english']}</div>
                <div class="place-desc">{place['description']}</div>
                """,
                unsafe_allow_html=True,
            )

            if place["verified"]:
                st.markdown(
                    '<span class="status">📍 موقع منشور</span>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<span class="status status-pending">الموقع الدقيق قيد التحقق</span>',
                    unsafe_allow_html=True,
                )

        with col2:
            if st.button(
                "التفاصيل",
                key=f"details_{place['id']}",
                use_container_width=True,
            ):
                st.session_state.selected_place = place["id"]
                st.rerun()

# -------------------- SELECTED PLACE -----------------

selected = next(
    (p for p in PLACES if p["id"] == st.session_state.selected_place),
    visitor,
)

st.markdown(
    '<div class="section-heading">تفاصيل المكان</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown(f"## {selected['icon']} {selected['name']}")
    st.caption(selected["english"])
    st.write(selected["description"])
    st.caption(f"التصنيف: {selected['category']}")

    if selected["verified"]:
        st.success("تم العثور على إحداثيات منشورة لهذا الموقع.")

        st.code(
            f"{selected['lat']}, {selected['lon']}",
            language="text",
        )

        maps_url = (
            f"https://www.google.com/maps?q="
            f"{selected['lat']},{selected['lon']}"
        )

        st.link_button(
            "افتح الموقع في Google Maps ↗",
            maps_url,
            use_container_width=True,
        )
    else:
        st.warning(
            "لم نتحقق بعد من الإحداثيات الدقيقة لهذا المعلم. "
            "لن نضع له Pin حتى نتأكد من موقعه."
        )

    save_label = (
        "✓ تمت إضافته للمحفوظات"
        if selected["id"] in st.session_state.saved_places
        else "♡ احفظ هذا المكان"
    )

    if st.button(save_label, use_container_width=True):
        if selected["id"] in st.session_state.saved_places:
            st.session_state.saved_places.remove(selected["id"])
        else:
            st.session_state.saved_places.append(selected["id"])
        st.rerun()

# -------------------- SAVED PLACES --------------------

st.markdown(
    '<div class="section-heading">أماكنك المحفوظة ♡</div>',
    unsafe_allow_html=True,
)

if st.session_state.saved_places:
    for place_id in st.session_state.saved_places:
        place = next(p for p in PLACES if p["id"] == place_id)
        st.write(f"{place['icon']} {place['name']}")
else:
    st.caption("الأماكن التي تحفظها ستظهر هنا.")

# -------------------- FOOTER --------------------------

st.markdown(
    """
    <div class="footer">
        <b>JAZIF MAP 🌿</b><br>
        Discover your next destination.
    </div>
    """,
    unsafe_allow_html=True,
)