import streamlit as st
from streamlit_option_menu import option_menu
import time

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Puli Architha | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & Base ── */
* { margin: 0; padding: 0; box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #030712 !important;
    color: #e2e8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at 20% 0%, #0f172a 0%, #030712 60%) !important;
}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.block-container { padding: 0 2rem 3rem 2rem !important; max-width: 1200px !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0f1e 0%, #060b18 100%) !important;
    border-right: 1px solid rgba(56, 189, 248, 0.15) !important;
}
[data-testid="stSidebar"] * { font-family: 'Rajdhani', sans-serif !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #030712; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #38bdf8, #818cf8); border-radius: 2px; }

/* ── Section heading ── */
.section-title {
    font-family: 'Orbitron', monospace !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #38bdf8, #818cf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.section-divider {
    height: 2px;
    background: linear-gradient(90deg, #38bdf8, #818cf8, transparent);
    border: none;
    border-radius: 1px;
    margin-bottom: 2.5rem;
}

/* ── Glasscard ── */
.glass-card {
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(56, 189, 248, 0.18);
    border-radius: 16px;
    padding: 1.8rem;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
}
.glass-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(56,189,248,0.05) 0%, transparent 60%);
    pointer-events: none;
}
.glass-card:hover {
    border-color: rgba(56, 189, 248, 0.45);
    box-shadow: 0 0 28px rgba(56, 189, 248, 0.15), 0 0 60px rgba(129, 140, 248, 0.08);
    transform: translateY(-3px);
}

/* ── Hero ── */
.hero-wrapper {
    min-height: 88vh;
    display: flex;
    align-items: center;
    padding: 3rem 0 2rem;
    position: relative;
}
.hero-name {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.4rem, 5vw, 4.2rem);
    font-weight: 900;
    letter-spacing: 4px;
    background: linear-gradient(135deg, #ffffff 0%, #38bdf8 40%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 1rem;
}
.hero-role {
    font-family: 'Space Mono', monospace;
    font-size: 0.9rem;
    color: #38bdf8;
    letter-spacing: 2px;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}
.hero-intro {
    font-size: 1.15rem;
    color: #94a3b8;
    line-height: 1.8;
    max-width: 540px;
    margin-bottom: 2.5rem;
}
.hero-badge {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    background: rgba(56,189,248,0.1);
    border: 1px solid rgba(56,189,248,0.3);
    border-radius: 99px;
    color: #38bdf8;
    font-size: 0.75rem;
    font-family: 'Space Mono', monospace;
    letter-spacing: 1px;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}

/* ── Avatar ── */
.avatar-ring {
    width: 240px;
    height: 240px;
    border-radius: 50%;
    background: linear-gradient(135deg, #38bdf8, #818cf8, #f472b6);
    padding: 3px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
    animation: spin-ring 8s linear infinite;
    box-shadow: 0 0 40px rgba(56,189,248,0.3), 0 0 80px rgba(129,140,248,0.15);
}
@keyframes spin-ring {
    0%   { box-shadow: 0 0 40px rgba(56,189,248,0.3), 0 0 80px rgba(129,140,248,0.15); }
    50%  { box-shadow: 0 0 60px rgba(244,114,182,0.4), 0 0 100px rgba(56,189,248,0.2); }
    100% { box-shadow: 0 0 40px rgba(56,189,248,0.3), 0 0 80px rgba(129,140,248,0.15); }
}
.avatar-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 5.5rem;
}

/* ── Buttons ── */
.btn-primary {
    display: inline-block;
    padding: 0.75rem 2rem;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    color: #030712 !important;
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 8px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(56,189,248,0.3);
    margin-right: 1rem;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(56,189,248,0.5);
    filter: brightness(1.1);
}
.btn-outline {
    display: inline-block;
    padding: 0.75rem 2rem;
    background: transparent;
    color: #38bdf8 !important;
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    border-radius: 8px;
    text-decoration: none;
    border: 1.5px solid #38bdf8;
    cursor: pointer;
    transition: all 0.3s ease;
}
.btn-outline:hover {
    background: rgba(56,189,248,0.1);
    transform: translateY(-2px);
    box-shadow: 0 4px 20px rgba(56,189,248,0.2);
}

/* ── Social icons ── */
.social-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 42px; height: 42px;
    border-radius: 50%;
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.25);
    color: #38bdf8 !important;
    font-size: 1.1rem;
    text-decoration: none;
    margin-right: 0.6rem;
    transition: all 0.3s ease;
}
.social-icon:hover {
    background: rgba(56,189,248,0.2);
    border-color: #38bdf8;
    transform: scale(1.15);
    box-shadow: 0 0 16px rgba(56,189,248,0.35);
}

/* ── Skill bar ── */
.skill-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: #cbd5e1;
    letter-spacing: 1px;
    margin-bottom: 4px;
}
.skill-track {
    height: 6px;
    background: rgba(255,255,255,0.07);
    border-radius: 3px;
    overflow: hidden;
    margin-bottom: 14px;
}
.skill-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    animation: grow 1.2s ease-out forwards;
    transform-origin: left;
}
@keyframes grow {
    from { width: 0%; }
}

/* ── Soft skill pill ── */
.soft-pill {
    display: inline-block;
    padding: 0.45rem 1.1rem;
    background: rgba(129,140,248,0.1);
    border: 1px solid rgba(129,140,248,0.3);
    border-radius: 99px;
    color: #a5b4fc;
    font-size: 0.85rem;
    font-family: 'Space Mono', monospace;
    letter-spacing: 0.5px;
    margin: 0.3rem;
    transition: all 0.25s ease;
}
.soft-pill:hover {
    background: rgba(129,140,248,0.2);
    border-color: #818cf8;
    transform: scale(1.05);
}

/* ── Timeline ── */
.timeline-item {
    position: relative;
    padding-left: 2rem;
    margin-bottom: 1.8rem;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: 0; top: 6px;
    width: 12px; height: 12px;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(56,189,248,0.6);
}
.timeline-item::after {
    content: '';
    position: absolute;
    left: 5px; top: 22px;
    width: 2px;
    height: calc(100% + 4px);
    background: linear-gradient(180deg, rgba(56,189,248,0.4), transparent);
}
.timeline-item:last-child::after { display: none; }
.timeline-degree {
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: 1px;
}
.timeline-school {
    font-size: 0.9rem;
    color: #38bdf8;
    margin: 0.2rem 0;
}
.timeline-score {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    background: rgba(56,189,248,0.1);
    border: 1px solid rgba(56,189,248,0.3);
    border-radius: 99px;
    color: #7dd3fc;
    font-size: 0.78rem;
    font-family: 'Space Mono', monospace;
    margin-top: 0.3rem;
}

/* ── Project card ── */
.project-card {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 16px;
    padding: 1.6rem;
    height: 100%;
    transition: all 0.35s ease;
    position: relative;
    overflow: hidden;
}
.project-card::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle at center, rgba(56,189,248,0.04) 0%, transparent 60%);
    pointer-events: none;
}
.project-card:hover {
    border-color: rgba(56,189,248,0.5);
    transform: translateY(-6px);
    box-shadow: 0 12px 40px rgba(56,189,248,0.18);
}
.project-title {
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: 1.5px;
    margin-bottom: 0.7rem;
    text-transform: uppercase;
}
.project-desc {
    font-size: 0.9rem;
    color: #94a3b8;
    line-height: 1.7;
    margin-bottom: 1.2rem;
}
.project-tag {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    background: rgba(244,114,182,0.1);
    border: 1px solid rgba(244,114,182,0.25);
    border-radius: 4px;
    color: #f9a8d4;
    font-size: 0.7rem;
    font-family: 'Space Mono', monospace;
    margin: 0.2rem;
}

/* ── Cert card ── */
.cert-card {
    background: rgba(15,23,42,0.7);
    border: 1px solid rgba(129,140,248,0.2);
    border-radius: 12px;
    padding: 1.4rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    transition: all 0.3s ease;
}
.cert-card:hover {
    border-color: rgba(129,140,248,0.5);
    transform: translateX(4px);
    box-shadow: 4px 0 20px rgba(129,140,248,0.15);
}
.cert-icon {
    font-size: 2rem;
    flex-shrink: 0;
}
.cert-name {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    color: #e2e8f0;
    margin-bottom: 0.2rem;
}
.cert-issuer {
    font-size: 0.82rem;
    color: #818cf8;
    font-family: 'Space Mono', monospace;
}

/* ── Contact ── */
.contact-info-row {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.9rem 1.2rem;
    background: rgba(15,23,42,0.6);
    border: 1px solid rgba(56,189,248,0.12);
    border-radius: 10px;
    margin-bottom: 0.8rem;
    transition: all 0.25s ease;
}
.contact-info-row:hover {
    border-color: rgba(56,189,248,0.35);
    background: rgba(56,189,248,0.05);
}
.contact-icon { font-size: 1.4rem; }
.contact-label { font-size: 0.72rem; color: #64748b; font-family: 'Space Mono', monospace; letter-spacing: 1px; }
.contact-value { font-size: 0.95rem; color: #e2e8f0; font-weight: 500; }

/* ── Streamlit widget overrides ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(56,189,248,0.2) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(56,189,248,0.6) !important;
    box-shadow: 0 0 12px rgba(56,189,248,0.15) !important;
}
.stTextInput label, .stTextArea label {
    color: #94a3b8 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
    letter-spacing: 1px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #38bdf8, #818cf8) !important;
    color: #030712 !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 2rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 20px rgba(56,189,248,0.3) !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(56,189,248,0.5) !important;
    filter: brightness(1.1) !important;
}

/* ── Option menu sidebar overrides ── */
.nav-link { border-radius: 8px !important; margin-bottom: 4px !important; }
.nav-link-selected {
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(129,140,248,0.2)) !important;
    border: 1px solid rgba(56,189,248,0.35) !important;
}

/* ── Floating particles (CSS only) ── */
.particle {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    animation: float-particle linear infinite;
    opacity: 0;
    z-index: 0;
}
@keyframes float-particle {
    0%   { transform: translateY(100vh) scale(0); opacity: 0; }
    10%  { opacity: 0.6; }
    90%  { opacity: 0.3; }
    100% { transform: translateY(-10vh) scale(1); opacity: 0; }
}

/* ── Sidebar avatar ── */
.sidebar-avatar {
    width: 90px; height: 90px;
    border-radius: 50%;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    padding: 2px;
    margin: 0 auto 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
}
.sidebar-avatar-inner {
    width: 100%; height: 100%;
    border-radius: 50%;
    background: #0a0f1e;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.2rem;
}
.sidebar-name {
    font-family: 'Orbitron', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    color: #e2e8f0;
    text-align: center;
    letter-spacing: 1px;
}
.sidebar-role {
    font-size: 0.72rem;
    color: #38bdf8;
    text-align: center;
    font-family: 'Space Mono', monospace;
    margin-top: 0.3rem;
}

/* ── Experience card ── */
.exp-header {
    display: flex;
    align-items: flex-start;
    gap: 1.2rem;
    margin-bottom: 1rem;
}
.exp-logo {
    width: 52px; height: 52px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(129,140,248,0.15));
    border: 1px solid rgba(56,189,248,0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    flex-shrink: 0;
}
.exp-title {
    font-family: 'Orbitron', monospace;
    font-size: 1.05rem;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: 1px;
}
.exp-company {
    color: #38bdf8;
    font-size: 0.9rem;
    margin: 0.2rem 0;
}
.exp-date {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    background: rgba(244,114,182,0.1);
    border: 1px solid rgba(244,114,182,0.25);
    border-radius: 99px;
    color: #f9a8d4;
    font-size: 0.72rem;
    font-family: 'Space Mono', monospace;
}
.exp-bullet {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.35rem 0;
    color: #94a3b8;
    font-size: 0.9rem;
}
.exp-bullet::before {
    content: '▸';
    color: #38bdf8;
    font-size: 0.75rem;
    flex-shrink: 0;
}

/* ── Stat counter ── */
.stat-box {
    text-align: center;
    padding: 1.2rem;
    background: rgba(15,23,42,0.6);
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 12px;
}
.stat-number {
    font-family: 'Orbitron', monospace;
    font-size: 2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label {
    font-size: 0.78rem;
    color: #64748b;
    font-family: 'Space Mono', monospace;
    letter-spacing: 1px;
    margin-top: 0.3rem;
}

/* ── Section spacing ── */
.section-wrap { padding: 3.5rem 0 2rem; }

/* ── Glow line ── */
.glow-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, #38bdf8, transparent);
    margin: 3rem 0;
    border: none;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 1.5rem 0.5rem 1rem; text-align:center;'>
        <div class='sidebar-avatar'>
            <div class='sidebar-avatar-inner'>👩‍💻</div>
        </div>
        <div class='sidebar-name'>PULI ARCHITHA</div>
        <div class='sidebar-role'>CSE Student</div>
        <div style='margin-top:0.8rem;'>
            <span class='hero-badge' style='font-size:0.65rem;'>Python</span>
            <span class='hero-badge' style='font-size:0.65rem;'>AI</span>
        </div>
    </div>
    <hr class='glow-line' style='margin:1rem 0;'/>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Skills", "Education", "Experience", "Projects", "Certifications", "Contact"],
        icons=["house-fill", "person-fill", "code-slash", "mortarboard-fill", "briefcase-fill",
               "grid-fill", "patch-check-fill", "envelope-fill"],
        default_index=0,
        styles={
            "container": {"padding": "0", "background-color": "transparent"},
            "icon": {"color": "#38bdf8", "font-size": "1rem"},
            "nav-link": {
                "font-family": "'Rajdhani', sans-serif",
                "font-size": "0.95rem",
                "font-weight": "500",
                "color": "#94a3b8",
                "letter-spacing": "0.5px",
                "padding": "0.6rem 1rem",
                "--hover-color": "rgba(56,189,248,0.1)",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, rgba(56,189,248,0.15), rgba(129,140,248,0.15))",
                "color": "#e2e8f0",
                "font-weight": "600",
                "border-left": "3px solid #38bdf8",
            },
        },
    )

    st.markdown("""
    <hr class='glow-line' style='margin:1rem 0;'/>
    <div style='text-align:center; padding:0 0.5rem;'>
        <a href='mailto:archithapuli@gmail.com' class='social-icon' style='color:#38bdf8'>📧</a>
        <a href='https://linkedin.com' target='_blank' class='social-icon' style='color:#38bdf8'>💼</a>
        <a href='https://github.com' target='_blank' class='social-icon' style='color:#38bdf8'>🐙</a>
        <a href='https://instagram.com' target='_blank' class='social-icon' style='color:#38bdf8'>📸</a>
    </div>
    <div style='text-align:center; margin-top:1.5rem; color:#334155; font-size:0.7rem; font-family:"Space Mono",monospace;'>
        ⚡ BUILT WITH PYTHON
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: HOME / HERO
# ═════════════════════════════════════════════
if selected == "Home":
    left, right = st.columns([1.4, 1], gap="large")

    with left:
        st.markdown("""
        <div class='hero-wrapper'>
        <div>
            <div style='margin-bottom:1rem;'>
                <span class='hero-badge'>⚡ OPEN TO OPPORTUNITIES</span>
                <span class='hero-badge' style='border-color:rgba(244,114,182,0.3);color:#f472b6;background:rgba(244,114,182,0.08);'>🎓 B.TECH CSE</span>
            </div>
            <div class='hero-name'>PULI<br>ARCHITHA</div>
            <div class='hero-role'>// Computer Science Engineering Student<br>// Python Developer · AI Enthusiast</div>
            <div class='hero-intro'>
                Passionate about building intelligent AI-powered solutions and modern software applications.
                Turning ideas into impactful digital experiences, one line of code at a time.
            </div>
            <div style='margin-bottom:2rem;'>
                <a href='mailto:archithapuli@gmail.com' class='btn-primary'>📬 Contact Me</a>
                <a href='#' class='btn-outline'>📄 Download CV</a>
            </div>
            <div>
                <a href='https://linkedin.com' target='_blank' class='social-icon'>💼</a>
                <a href='https://github.com' target='_blank' class='social-icon'>🐙</a>
                <a href='mailto:archithapuli@gmail.com' class='social-icon'>📧</a>
                <a href='https://instagram.com' target='_blank' class='social-icon'>📸</a>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;height:88vh;gap:2rem;'>
            <div class='avatar-ring'>
                <div class='avatar-inner'>👩‍💻</div>
            </div>
            <div style='display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;width:100%;max-width:280px;'>
                <div class='stat-box'>
                    <div class='stat-number'>9.2</div>
                    <div class='stat-label'>CGPA</div>
                </div>
                <div class='stat-box'>
                    <div class='stat-number'>3+</div>
                    <div class='stat-label'>PROJECTS</div>
                </div>
                <div class='stat-box'>
                    <div class='stat-number'>1</div>
                    <div class='stat-label'>INTERNSHIP</div>
                </div>
                <div class='stat-box'>
                    <div class='stat-number'>3+</div>
                    <div class='stat-label'>CERTS</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='glow-line'>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; margin-bottom:2.5rem;'>
        <div style='color:#475569; font-family:"Space Mono",monospace; font-size:0.72rem; letter-spacing:3px; margin-bottom:1.2rem;'>TECH STACK</div>
        <div style='display:flex; flex-wrap:wrap; justify-content:center; gap:0.8rem;'>
            <span class='hero-badge'>🐍 Python</span>
            <span class='hero-badge'>☕ Java</span>
            <span class='hero-badge'>🗄️ SQL</span>
            <span class='hero-badge'>🌐 HTML/CSS</span>
            <span class='hero-badge'>🤖 AI/ML</span>
            <span class='hero-badge'>📊 Data Structures</span>
            <span class='hero-badge'>🔐 OOP</span>
            <span class='hero-badge'>🗃️ DBMS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: ABOUT
# ═════════════════════════════════════════════
elif selected == "About":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4], gap="large")

    with col1:
        st.markdown("""
        <div class='glass-card' style='text-align:center;'>
            <div class='avatar-ring' style='width:180px;height:180px;margin:0 auto 1.5rem;'>
                <div class='avatar-inner' style='font-size:4rem;'>👩‍💻</div>
            </div>
            <div style='font-family:"Orbitron",monospace; font-size:1.1rem; font-weight:700; color:#e2e8f0; letter-spacing:2px;'>PULI ARCHITHA</div>
            <div style='color:#38bdf8; font-family:"Space Mono",monospace; font-size:0.78rem; margin:0.5rem 0 1rem;'>B.Tech CSE Student</div>
            <div style='color:#64748b; font-size:0.82rem; font-family:"Space Mono",monospace;'>📍 Hyderabad, Telangana</div>
            <hr style='border:none; border-top:1px solid rgba(56,189,248,0.15); margin:1.2rem 0;'>
            <div style='display:flex; justify-content:space-around;'>
                <div>
                    <div style='font-family:"Orbitron",monospace; font-size:1.4rem; font-weight:900; color:#38bdf8;'>9.2</div>
                    <div style='color:#64748b; font-size:0.7rem; font-family:"Space Mono",monospace;'>CGPA</div>
                </div>
                <div>
                    <div style='font-family:"Orbitron",monospace; font-size:1.4rem; font-weight:900; color:#818cf8;'>3+</div>
                    <div style='color:#64748b; font-size:0.7rem; font-family:"Space Mono",monospace;'>PROJECTS</div>
                </div>
                <div>
                    <div style='font-family:"Orbitron",monospace; font-size:1.4rem; font-weight:900; color:#f472b6;'>1</div>
                    <div style='color:#64748b; font-size:0.7rem; font-family:"Space Mono",monospace;'>INTERN</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#38bdf8; letter-spacing:2px; margin-bottom:1rem;'>// WHO AM I</div>
            <p style='color:#cbd5e1; font-size:1rem; line-height:1.9; margin-bottom:1.2rem;'>
                I'm <strong style='color:#e2e8f0;'>Puli Architha</strong>, a passionate B.Tech Computer Science Engineering student
                at <strong style='color:#38bdf8;'>Malla Reddy Engineering College for Women</strong>, Hyderabad.
            </p>
            <p style='color:#94a3b8; font-size:0.95rem; line-height:1.8; margin-bottom:1.2rem;'>
                My journey in tech is driven by a deep fascination with <strong style='color:#818cf8;'>Artificial Intelligence</strong>,
                <strong style='color:#818cf8;'>Python development</strong>, and building software that creates real-world impact.
                I believe technology is the most powerful tool for solving human problems.
            </p>
            <p style='color:#94a3b8; font-size:0.95rem; line-height:1.8; margin-bottom:1.8rem;'>
                A quick learner with a strong problem-solving mindset, I thrive on challenges and am always
                looking for opportunities to apply my skills to projects that matter — especially in women's safety,
                education, and social good.
            </p>
            <div style='display:grid; grid-template-columns:1fr 1fr; gap:0.8rem;'>
                <div style='background:rgba(56,189,248,0.06); border:1px solid rgba(56,189,248,0.15); border-radius:8px; padding:0.8rem;'>
                    <div style='font-size:1.3rem; margin-bottom:0.3rem;'>🧠</div>
                    <div style='font-size:0.82rem; color:#e2e8f0; font-weight:600;'>AI & ML</div>
                    <div style='font-size:0.75rem; color:#64748b;'>Deep interest in intelligent systems</div>
                </div>
                <div style='background:rgba(129,140,248,0.06); border:1px solid rgba(129,140,248,0.15); border-radius:8px; padding:0.8rem;'>
                    <div style='font-size:1.3rem; margin-bottom:0.3rem;'>🐍</div>
                    <div style='font-size:0.82rem; color:#e2e8f0; font-weight:600;'>Python Dev</div>
                    <div style='font-size:0.75rem; color:#64748b;'>Building real solutions</div>
                </div>
                <div style='background:rgba(244,114,182,0.06); border:1px solid rgba(244,114,182,0.15); border-radius:8px; padding:0.8rem;'>
                    <div style='font-size:1.3rem; margin-bottom:0.3rem;'>🔍</div>
                    <div style='font-size:0.82rem; color:#e2e8f0; font-weight:600;'>Problem Solving</div>
                    <div style='font-size:0.75rem; color:#64748b;'>Analytical approach</div>
                </div>
                <div style='background:rgba(52,211,153,0.06); border:1px solid rgba(52,211,153,0.15); border-radius:8px; padding:0.8rem;'>
                    <div style='font-size:1.3rem; margin-bottom:0.3rem;'>🚀</div>
                    <div style='font-size:0.82rem; color:#e2e8f0; font-weight:600;'>Quick Learner</div>
                    <div style='font-size:0.75rem; color:#64748b;'>Always growing</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: SKILLS
# ═════════════════════════════════════════════
elif selected == "Skills":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    tech_skills = [
        ("Python", 90),
        ("Java", 75),
        ("Data Structures", 82),
        ("Algorithms", 78),
        ("OOP", 85),
        ("SQL", 80),
        ("DBMS", 75),
        ("HTML", 82),
        ("CSS", 76),
    ]

    with col1:
        st.markdown("""
        <div class='glass-card'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#38bdf8; letter-spacing:2px; margin-bottom:1.4rem;'>// TECHNICAL SKILLS</div>
        """, unsafe_allow_html=True)
        for skill, pct in tech_skills:
            st.markdown(f"""
            <div class='skill-label'>{skill} <span style='float:right;color:#38bdf8;'>{pct}%</span></div>
            <div class='skill-track'><div class='skill-fill' style='width:{pct}%;'></div></div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    soft_skills = ["Communication", "Team Collaboration", "Time Management", "Logical Thinking", "Self Motivation"]

    with col2:
        st.markdown("""
        <div class='glass-card' style='margin-bottom:1.2rem;'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#818cf8; letter-spacing:2px; margin-bottom:1.2rem;'>// SOFT SKILLS</div>
            <div>
        """, unsafe_allow_html=True)
        for s in soft_skills:
            st.markdown(f"<span class='soft-pill'>✦ {s}</span>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='glass-card'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#f472b6; letter-spacing:2px; margin-bottom:1.2rem;'>// TOOLS & TECH</div>
            <div style='display:grid; grid-template-columns: repeat(3,1fr); gap:0.7rem;'>
        """, unsafe_allow_html=True)
        tools = [("🐍","Python"),("☕","Java"),("🗄️","SQL"),("🤖","AI/ML"),("📊","DSA"),("🌐","HTML/CSS"),("🔐","OOP"),("🗃️","DBMS"),("💡","Algorithms")]
        for icon, name in tools:
            st.markdown(f"""
            <div style='background:rgba(15,23,42,0.8);border:1px solid rgba(56,189,248,0.12);border-radius:8px;
                        padding:0.7rem;text-align:center;transition:all 0.25s ease;'>
                <div style='font-size:1.4rem;margin-bottom:0.3rem;'>{icon}</div>
                <div style='font-size:0.72rem;color:#94a3b8;font-family:"Space Mono",monospace;'>{name}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: EDUCATION
# ═════════════════════════════════════════════
elif selected == "Education":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    education = [
        {
            "icon": "🎓",
            "degree": "B.Tech — Computer Science Engineering",
            "school": "Malla Reddy Engineering College for Women",
            "score": "CGPA: 9.2",
            "year": "2022 – 2026",
            "desc": "Focused on AI, Python, Data Structures, DBMS, and Software Development. Active participant in coding competitions and technical seminars.",
            "color": "#38bdf8",
        },
        {
            "icon": "📚",
            "degree": "Intermediate (Class XII)",
            "school": "Telangana Board",
            "score": "97%",
            "year": "2020 – 2022",
            "desc": "Strong foundation in Mathematics, Physics, and Chemistry. Achieved outstanding academic results.",
            "color": "#818cf8",
        },
        {
            "icon": "🏫",
            "degree": "SSC (Class X)",
            "school": "National Open School",
            "score": "93%",
            "year": "2019 – 2020",
            "desc": "Completed secondary education with distinction. Built strong fundamentals in core subjects.",
            "color": "#f472b6",
        },
    ]

    for edu in education:
        st.markdown(f"""
        <div class='glass-card' style='margin-bottom:1.2rem; border-left:3px solid {edu["color"]};'>
            <div style='display:flex; align-items:flex-start; gap:1.2rem;'>
                <div style='font-size:2.5rem; flex-shrink:0; margin-top:0.2rem;'>{edu["icon"]}</div>
                <div style='flex:1;'>
                    <div style='display:flex; flex-wrap:wrap; align-items:center; gap:0.8rem; margin-bottom:0.5rem;'>
                        <div style='font-family:"Orbitron",monospace; font-size:1rem; font-weight:700; color:#e2e8f0; letter-spacing:1px;'>{edu["degree"]}</div>
                        <span style='padding:0.2rem 0.7rem; background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.2); border-radius:99px; color:#64748b; font-size:0.7rem; font-family:"Space Mono",monospace;'>{edu["year"]}</span>
                    </div>
                    <div style='color:{edu["color"]}; font-size:0.9rem; margin-bottom:0.5rem;'>🏛️ {edu["school"]}</div>
                    <div style='color:#94a3b8; font-size:0.88rem; line-height:1.7; margin-bottom:0.7rem;'>{edu["desc"]}</div>
                    <span style='padding:0.25rem 0.8rem; background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.25); border-radius:99px; color:#7dd3fc; font-size:0.78rem; font-family:"Space Mono",monospace;'>⭐ {edu["score"]}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: EXPERIENCE
# ═════════════════════════════════════════════
elif selected == "Experience":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Experience</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='glass-card' style='max-width:760px;'>
        <div class='exp-header'>
            <div class='exp-logo'>🐍</div>
            <div>
                <div class='exp-title'>Python Intern</div>
                <div class='exp-company'>Axcentra Technologies</div>
                <div style='margin-top:0.4rem;'>
                    <span class='exp-date'>📅 Feb 2026 – Mar 2026</span>
                    <span class='exp-date' style='margin-left:0.5rem;'>📍 Hyderabad</span>
                </div>
            </div>
        </div>
        <hr style='border:none; border-top:1px solid rgba(56,189,248,0.1); margin:1rem 0;'>
        <div style='font-family:"Space Mono",monospace; font-size:0.72rem; color:#38bdf8; letter-spacing:2px; margin-bottom:0.8rem;'>// RESPONSIBILITIES</div>
        <div class='exp-bullet'>Python programming and scripting for automation tasks</div>
        <div class='exp-bullet'>Problem solving through algorithmic design and implementation</div>
        <div class='exp-bullet'>Debugging and optimizing existing codebases</div>
        <div class='exp-bullet'>Data handling, parsing, and processing pipelines</div>
        <div class='exp-bullet'>Software development lifecycle and version control best practices</div>
        <div class='exp-bullet'>Team collaboration in an agile development environment</div>
        <div style='margin-top:1.4rem; padding:1rem; background:rgba(56,189,248,0.05); border:1px solid rgba(56,189,248,0.12); border-radius:8px;'>
            <div style='font-size:0.78rem; color:#64748b; font-family:"Space Mono",monospace; letter-spacing:1px; margin-bottom:0.5rem;'>SKILLS GAINED</div>
            <span class='hero-badge'>Python</span>
            <span class='hero-badge'>Debugging</span>
            <span class='hero-badge'>Data Handling</span>
            <span class='hero-badge'>Team Work</span>
            <span class='hero-badge'>Algorithms</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: PROJECTS
# ═════════════════════════════════════════════
elif selected == "Projects":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    projects = [
        {
            "icon": "🛡️",
            "title": "SAFEZONE AI",
            "subtitle": "Danger Zone Prediction for Women",
            "desc": "AI-powered women safety system using GPS tracking, crime data analysis, and real-time alerts. Leverages machine learning to predict high-risk zones and notify users proactively.",
            "tags": ["Python", "AI/ML", "GPS", "Real-time", "Safety Tech"],
            "accent": "#f472b6",
            "featured": True,
        },
        {
            "icon": "📊",
            "title": "Student Result Management",
            "subtitle": "Academic Performance System",
            "desc": "A comprehensive system to manage, analyze, and visualize student academic results. Features automated report generation, grade calculation, and performance analytics.",
            "tags": ["Python", "SQL", "DBMS", "Analytics"],
            "accent": "#38bdf8",
            "featured": False,
        },
        {
            "icon": "🌐",
            "title": "Personal Portfolio Website",
            "subtitle": "Interactive Developer Showcase",
            "desc": "A modern, animated personal portfolio built with Streamlit featuring glassmorphism UI, futuristic design, smooth animations, and a fully responsive layout.",
            "tags": ["Python", "Streamlit", "CSS", "UI/UX"],
            "accent": "#818cf8",
            "featured": False,
        },
    ]

    col1, col2, col3 = st.columns(3, gap="medium")
    cols = [col1, col2, col3]

    for i, proj in enumerate(projects):
        with cols[i]:
            featured_badge = "<span style='float:right; padding:0.2rem 0.6rem; background:rgba(244,114,182,0.15); border:1px solid rgba(244,114,182,0.3); border-radius:99px; color:#f9a8d4; font-size:0.65rem; font-family:\"Space Mono\",monospace;'>⭐ FEATURED</span>" if proj["featured"] else ""
            tags_html = "".join([f"<span class='project-tag'>{t}</span>" for t in proj["tags"]])
            st.markdown(f"""
            <div class='project-card' style='border-left:3px solid {proj["accent"]};'>
                <div style='font-size:2.2rem; margin-bottom:0.8rem;'>{proj["icon"]}</div>
                <div class='project-title'>{featured_badge}{proj["title"]}</div>
                <div style='color:{proj["accent"]}; font-size:0.8rem; font-family:"Space Mono",monospace; margin-bottom:0.8rem;'>{proj["subtitle"]}</div>
                <div class='project-desc'>{proj["desc"]}</div>
                <div style='margin-bottom:1.2rem;'>{tags_html}</div>
                <div style='display:flex; gap:0.6rem;'>
                    <a href='https://github.com' target='_blank' style='flex:1; padding:0.5rem; background:rgba(15,23,42,0.8); border:1px solid rgba(56,189,248,0.2); border-radius:6px; color:#38bdf8; text-align:center; font-size:0.75rem; font-family:"Space Mono",monospace; text-decoration:none; transition:all 0.25s ease;'>🐙 GitHub</a>
                    <a href='#' style='flex:1; padding:0.5rem; background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.3); border-radius:6px; color:#38bdf8; text-align:center; font-size:0.75rem; font-family:"Space Mono",monospace; text-decoration:none; transition:all 0.25s ease;'>🚀 Live Demo</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: CERTIFICATIONS
# ═════════════════════════════════════════════
elif selected == "Certifications":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Certifications</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    certs = [
        {
            "icon": "🐍",
            "name": "Python Basics Workshop",
            "issuer": "Technical Training Program",
            "desc": "Comprehensive hands-on workshop covering Python fundamentals, data structures, OOP concepts, and real-world application development.",
            "color": "#38bdf8",
            "year": "2024",
        },
        {
            "icon": "🌐",
            "name": "Introduction to Web Development",
            "issuer": "Web Technologies Certification",
            "desc": "Covered HTML5, CSS3, responsive design principles, and modern web development best practices and standards.",
            "color": "#818cf8",
            "year": "2024",
        },
        {
            "icon": "💡",
            "name": "Technical Seminars & Coding Sessions",
            "issuer": "College Technical Events",
            "desc": "Participated in multiple technical seminars, hackathons, and coding competitions. Earned recognition for problem-solving excellence.",
            "color": "#f472b6",
            "year": "2023–2025",
        },
    ]

    for cert in certs:
        st.markdown(f"""
        <div class='glass-card' style='border-left:3px solid {cert["color"]}; margin-bottom:1.2rem;'>
            <div style='display:flex; align-items:flex-start; gap:1.2rem;'>
                <div style='font-size:2.5rem; flex-shrink:0;'>{cert["icon"]}</div>
                <div style='flex:1;'>
                    <div style='display:flex; align-items:center; flex-wrap:wrap; gap:0.8rem; margin-bottom:0.4rem;'>
                        <div style='font-family:"Orbitron",monospace; font-size:0.95rem; font-weight:700; color:#e2e8f0; letter-spacing:1px;'>{cert["name"]}</div>
                        <span style='padding:0.2rem 0.6rem; background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.2); border-radius:99px; color:#64748b; font-size:0.68rem; font-family:"Space Mono",monospace;'>{cert["year"]}</span>
                    </div>
                    <div style='color:{cert["color"]}; font-size:0.82rem; font-family:"Space Mono",monospace; margin-bottom:0.6rem;'>{cert["issuer"]}</div>
                    <div style='color:#94a3b8; font-size:0.9rem; line-height:1.7;'>{cert["desc"]}</div>
                </div>
                <div style='font-size:2rem; flex-shrink:0;'>🏅</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═════════════════════════════════════════════
# SECTION: CONTACT
# ═════════════════════════════════════════════
elif selected == "Contact":
    st.markdown("<div class='section-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("""
        <div class='glass-card'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#38bdf8; letter-spacing:2px; margin-bottom:1.4rem;'>// GET IN TOUCH</div>
            <p style='color:#94a3b8; font-size:0.95rem; line-height:1.8; margin-bottom:1.6rem;'>
                I'm open to internship opportunities, collaborative projects, and interesting conversations about AI and tech.
                Let's build something amazing together! 🚀
            </p>
            <div class='contact-info-row'>
                <div class='contact-icon'>📧</div>
                <div>
                    <div class='contact-label'>EMAIL</div>
                    <div class='contact-value'>archithapuli@gmail.com</div>
                </div>
            </div>
            <div class='contact-info-row'>
                <div class='contact-icon'>📱</div>
                <div>
                    <div class='contact-label'>PHONE</div>
                    <div class='contact-value'>+91 7702997487</div>
                </div>
            </div>
            <div class='contact-info-row'>
                <div class='contact-icon'>📍</div>
                <div>
                    <div class='contact-label'>LOCATION</div>
                    <div class='contact-value'>Hyderabad, Telangana</div>
                </div>
            </div>
            <hr style='border:none; border-top:1px solid rgba(56,189,248,0.12); margin:1.4rem 0;'>
            <div style='font-family:"Orbitron",monospace; font-size:0.72rem; color:#64748b; letter-spacing:2px; margin-bottom:0.8rem;'>FIND ME ON</div>
            <div>
                <a href='https://www.linkedin.com/in/architha-puli?utm_source=share_via&utm_content=profile&utm_medium=member_android' target='_blank' class='social-icon'>💼</a>
                <a href='https://github.com/Archithapuli' target='_blank' class='social-icon'>🐙</a>
                <a href='mailto:archithapuli@gmail.com' class='social-icon'>📧</a>
                <a href='https://www.instagram.com/archithagoud_?igsh=MTMyazA4ZXc4MHN1dg==' target='_blank' class='social-icon'>📸</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <div style='font-family:"Orbitron",monospace; font-size:0.75rem; color:#818cf8; letter-spacing:2px; margin-bottom:1.4rem;'>// SEND A MESSAGE</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("YOUR NAME", placeholder="e.g. John Doe")
            email = st.text_input("YOUR EMAIL", placeholder="e.g. hello@example.com")
            subject = st.text_input("SUBJECT", placeholder="e.g. Internship Opportunity")
            message = st.text_area("MESSAGE", placeholder="Write your message here...", height=140)
            submitted = st.form_submit_button("⚡ SEND MESSAGE")

            if submitted:
                if name and email and message:
                    st.markdown("""
                    <div style='padding:1rem; background:rgba(52,211,153,0.1); border:1px solid rgba(52,211,153,0.3);
                                border-radius:8px; color:#6ee7b7; font-family:"Space Mono",monospace; font-size:0.82rem; margin-top:0.8rem;'>
                        ✅ Message sent successfully! I'll get back to you soon.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style='padding:1rem; background:rgba(244,114,182,0.1); border:1px solid rgba(244,114,182,0.3);
                                border-radius:8px; color:#f9a8d4; font-family:"Space Mono",monospace; font-size:0.82rem; margin-top:0.8rem;'>
                        ⚠️ Please fill in all required fields.
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<hr class='glow-line' style='margin-top:3rem;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; padding:1.5rem 0 1rem;'>
        <div style='font-family:"Orbitron",monospace; font-size:0.7rem; color:#334155; letter-spacing:3px;'>
            DESIGNED & BUILT BY PULI ARCHITHA · 2026 · BUILT WITH PYTHON & STREAMLIT ⚡
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
