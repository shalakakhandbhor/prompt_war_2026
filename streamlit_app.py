import streamlit as st
import time
from datetime import datetime

# Page Settings - Full Width Modern Web App
st.set_page_config(
    page_title="JalDrishti | जलदृष्टी - AI Precision Irrigation",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enterprise SaaS Custom CSS (Glassmorphism & Neon Glow)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0B0F19;
        color: #F8FAFC;
    }
    
    /* Top Navigation Header */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 25px;
        background: rgba(17, 24, 39, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .brand-title {
        font-size: 1.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #10B981 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
        margin: 0;
    }
    .nav-badge {
        background: rgba(16, 185, 129, 0.12);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-left: 8px;
    }
    
    /* Telemetry Metric Cards */
    .metric-box {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94A3B8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-val {
        font-size: 2rem;
        font-weight: 700;
        margin: 8px 0 4px 0;
    }
    
    /* Live Terminal Console */
    .agent-terminal {
        background: #030712;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 18px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.88rem;
        color: #38BDF8;
        height: 290px;
        overflow-y: auto;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);
    }
    
    /* Marathi WhatsApp Card */
    .farmer-card {
        background: #064E3B;
        border: 1px solid #059669;
        border-radius: 12px;
        padding: 16px;
        color: #ECFDF5;
        margin-top: 15px;
    }
    
    /* Custom button styling */
    .stButton>button {
        background: linear-gradient(90deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- TOP NAVBAR -----------------
st.markdown("""
<div class="top-nav">
    <div>
        <p class="brand-title">🌱 JalDrishti | जलदृष्टी</p>
        <span style="color:#94A3B8; font-size:0.85rem;">Autonomous Climate-Adaptive Precision Irrigation System</span>
    </div>
    <div>
        <span class="nav-badge">● Google Vertex AI</span>
        <span class="nav-badge">⚡ Cloud Run: asia-south1</span>
        <span class="nav-badge">IoT Edge Nodes: Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- ONE-CLICK SCENARIO BAR -----------------
st.markdown("#### ⚡ 1-Click Simulation Scenarios (For Live Demo)")
sc_col1, sc_col2, sc_col3, sc_col4 = st.columns(4)

if "moisture" not in st.session_state:
    st.session_state.moisture = 22
    st.session_state.rain = 5
    st.session_state.power = True

with sc_col1:
    if st.button("🚨 Scenario A: Severe Drought", use_container_width=True):
        st.session_state.moisture = 18
        st.session_state.rain = 0
        st.session_state.power = True
with sc_col2:
    if st.button("⚡ Scenario B: Rural Power Cut", use_container_width=True):
        st.session_state.moisture = 20
        st.session_state.rain = 10
        st.session_state.power = False
with sc_col3:
    if st.button("🌧️ Scenario C: Monsoon Incoming", use_container_width=True):
        st.session_state.moisture = 29
        st.session_state.rain = 85
        st.session_state.power = True
with sc_col4:
    if st.button("🔄 Reset to Default", use_container_width=True):
        st.session_state.moisture = 35
        st.session_state.rain = 15
        st.session_state.power = True

st.markdown("<hr style='border:none; border-top: 1px solid rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)

# ----------------- LIVE TELEMETRY CARDS -----------------
tcol1, tcol2, tcol3, tcol4 = st.columns(4)

with tcol1:
    m_color = "#EF4444" if st.session_state.moisture < 25 else "#10B981"
    st.markdown(f"""
    <div class="metric-box">
        <span class="metric-label">💧 Root Zone Moisture</span>
        <p class="metric-val" style="color:{m_color};">{st.session_state.moisture}%</p>
        <span style="color:#64748B; font-size:0.8rem;">Threshold: 35%</span>
    </div>
    """, unsafe_allow_html=True)

with tcol2:
    p_status = "ONLINE (3-PHASE)" if st.session_state.power else "OUTAGE (LOAD SHED)"
    p_color = "#10B981" if st.session_state.power else "#EF4444"
    st.markdown(f"""
    <div class="metric-box">
        <span class="metric-label">⚡ Rural Grid Status</span>
        <p class="metric-val" style="color:{p_color}; font-size:1.4rem; padding-top:10px;">{p_status}</p>
        <span style="color:#64748B; font-size:0.8rem;">Substation Feed</span>
    </div>
    """, unsafe_allow_html=True)

with tcol3:
    st.markdown(f"""
    <div class="metric-box">
        <span class="metric-label">🌧️ 24h Rain Radar</span>
        <p class="metric-val" style="color:#38BDF8;">{st.session_state.rain}%</p>
        <span style="color:#64748B; font-size:0.8rem;">Open-Meteo Satellite Sync</span>
    </div>
    """, unsafe_allow_html=True)

with tcol4:
    st.markdown("""
    <div class="metric-box">
        <span class="metric-label">🌡️ Field Temperature</span>
        <p class="metric-val" style="color:#F59E0B;">33.4°C</p>
        <span style="color:#64748B; font-size:0.8rem;">ET₀: 5.8 mm/day</span>
    </div>
    """, unsafe_allow_html=True)

# ----------------- AGENT EXECUTION SECTION -----------------
st.markdown("<br>", unsafe_allow_html=True)
left_col, right_col = st.columns([1.3, 1])

with left_col:
    st.subheader("🧠 Autonomous Agent Reasoning Stream")
    terminal_placeholder = st.empty()
    run_cycle = st.button("🚀 Trigger Autonomous Decision Cycle", use_container_width=True)

with right_col:
    st.subheader("⚙️ Hardware Actuator & Farmer Advisory")
    status_card_placeholder = st.empty()
    sms_placeholder = st.empty()

# ----------------- AGENTIC ENGINE -----------------
def run_jaldrishti_agent(moisture, rain, power):
    now = datetime.now().strftime("%H:%M:%S")
    logs = [
        f"[{now}] [INGEST] Ingested 4 IoT node metrics from Maharashtra Agro-Cluster.",
        f"[{now}] [TOOL: check_soil_deficit] Root zone moisture is {moisture}% (Target: 38%).",
        f"[{now}] [TOOL: verify_rain_radar] Rainfall probability in next 24h: {rain}%.",
        f"[{now}] [TOOL: inspect_power_grid] Rural 3-phase grid status: {'AVAILABLE' if power else 'UNAVAILABLE'}."
    ]
    
    if rain >= 60:
        logs.append(f"[{now}] [REASONING] Imminent heavy rainfall ({rain}%). Over-irrigation will trigger root rot.")
        logs.append(f"[{now}] [ACTION: SUPPRESS] All valves locked. Suppressed water usage.")
        action_title = "PUMP OFF / RAIN DELAY"
        action_desc = "Rain predicted within 24h. Postponing cycle to conserve groundwater."
        action_color = "#38BDF8"
        marathi = f"नमस्कार! पुढील २४ तासांत पाऊस पडण्याची शक्यता {rain}% आहे. त्यामुळे ठिबक सिंचन थांबवले आहे. अंदाजे १,२०० लिटर पाणी वाचवले."
    elif not power:
        logs.append(f"[{now}] [REASONING] Critical moisture deficit ({moisture}%) but 3-Phase pump cannot start (Power Outage).")
        logs.append(f"[{now}] [ACTION: FAILSAFE] Activating 12V DC Solar Farm-Pond Gravity Solenoid Valve.")
        action_title = "SOLAR GRAVITY VALVE: OPEN"
        action_desc = "3-Phase grid down. Switched automatically to DC Solar gravity backup line."
        action_color = "#F59E0B"
        marathi = f"सावधान! शेतात ३-फेज वीज उपलब्ध नाही. मातीत ओलावा ({moisture}%) कमी असल्याने सोलर बॅटरीवर चालणाऱ्या व्हॉल्व्हद्वारे पिकाला पाणी सुरू केले आहे."
    else:
        run_time = 25 if moisture < 22 else 15
        logs.append(f"[{now}] [REASONING] Soil dry ({moisture}%) & power active. Calculating FAO-56 Penman-Monteith pulse.")
        logs.append(f"[{now}] [ACTION: DISPATCH] Sending pulse command to 3-Phase Drip Motor for {run_time} mins.")
        action_title = f"MAIN PUMP: ON ({run_time} MINS)"
        action_desc = f"Optimal micro-pulse scheduled. Minimum evaporative loss at 33°C."
        action_color = "#10B981"
        marathi = f"नमस्कार! ३-फेज वीज उपलब्ध असताना टोमॅटो पिकासाठी {run_time} मिनिटे ठिबक सुरू केले आहे. पाणी बचत: ३८%."
        
    return logs, action_title, action_desc, action_color, marathi

if run_cycle:
    with st.spinner("JalDrishti Agent is reasoning over IoT telemetry..."):
        time.sleep(0.5)
        logs, title, desc, color, marathi = run_jaldrishti_agent(
            st.session_state.moisture,
            st.session_state.rain,
            st.session_state.power
        )
        
        terminal_placeholder.markdown(f"""
        <div class="agent-terminal">
            {'<br>'.join(logs)}
        </div>
        """, unsafe_allow_html=True)
        
        status_card_placeholder.markdown(f"""
        <div style="background:#111827; border-left:4px solid {color}; border-radius:10px; padding:15px;">
            <p style="margin:0; font-size:0.8rem; color:#94A3B8; font-weight:600;">DISPATCHED ACTION</p>
            <h3 style="margin:4px 0; color:#F8FAFC;">{title}</h3>
            <p style="margin:0; color:#94A3B8; font-size:0.9rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        
        sms_placeholder.markdown(f"""
        <div class="farmer-card">
            <span style="font-weight:700; font-size:0.85rem; text-transform:uppercase;">📱 Shetkari WhatsApp Alert (मराठी)</span>
            <p style="margin:8px 0 0 0; font-size:0.95rem; line-height:1.4;">💬 {marathi}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    terminal_placeholder.markdown("""
    <div class="agent-terminal">
        [SYS READY] JalDrishti v2.4 initialized.<br>
        [STANDBY] Telemetry streaming active. Press "Trigger Autonomous Decision Cycle" or select a scenario above...
    </div>
    """, unsafe_allow_html=True)
    # ----------------- LIVE AI CHATBOT (शेतकरी संवाद) -----------------
st.markdown("<hr style='border:none; border-top: 1px solid rgba(255,255,255,0.08); margin: 30px 0;'>", unsafe_allow_html=True)
st.subheader("💬 Ask JalDrishti AI (शेतकरी कृषी सहाय्यक)")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "नमस्कार! मी जलदृष्टी AI सहाय्यक आहे. तुमच्या शेतातील ओलावा, वीज आणि पिकांच्या सिंचनाबद्दल तुम्ही मला मराठी किंवा इंग्रजीत काहीही विचारू शकता."}
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input from user
user_input = st.chat_input("शेती किंवा सिंचनाबद्दल प्रश्न विचारा... (उदा. सध्या पाणी देऊ का?)")

if user_input:
    # Append user question
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Dynamic Smart AI Response using current Dashboard Telemetry
    m = st.session_state.moisture
    p = st.session_state.power
    r = st.session_state.rain

    q_lower = user_input.lower()

    if any(w in q_lower for w in ["पाणी", "water", "irrigation", "सिंचन", "मोटर", "motor"]):
        if r >= 60:
            ans = f"🌧️ **सध्या पाणी देण्याची गरज नाही.** पुढच्या २४ तासांत पावसाची शक्यता {r}% आहे. जर पाणी दिले तर मुळे सडण्याची शक्यता आहे."
        elif not p:
            ans = f"⚡ **शेतात ३-फेज वीज उपलब्ध नाही.** मातीतील ओलावा {m}% आहे. जास्त ताण पडू नये म्हणून सोलर व्हॉल्व्ह द्वारे पाणी सोडण्याची शिफारस आहे."
        elif m < 25:
            ans = f"🚨 **होय, त्वरित पाणी देणे आवश्यक आहे!** मातीतील ओलावा खूप कमी ({m}%) झाला आहे. ३-फेज वीज उपलब्ध असल्याने २५ मिनिटे ठिबक चालवा."
        else:
            ans = f"✅ **मातीमध्ये सध्या चांगला ओलावा ({m}%) आहे.** पिकाला आत्ता पाण्याचा ताण नाही, सायंकाळी पुन्हा तपासणी केली जाईल."

    elif any(w in q_lower for w in ["पाऊस", "rain", "weather", "हवामान"]):
        ans = f"🌦️ सध्याच्या रडार डेटानुसार पुढील २४ तासांत **{r}% पाऊस पडण्याची शक्यता** आहे. तापमान ३३.४°C नोंदवले गेले आहे."

    elif any(w in q_lower for w in ["वीज", "light", "power", "grid", "load"]):
        p_txt = "उपलब्ध आहे (3-Phase Online)" if p else "खंडित आहे (Load-Shedding Outage)"
        ans = f"⚡ फिडर स्टेटस: सध्या शेतातील ३-फेज वीज **{p_txt}**. वीज खंडित झाल्यास जलदृष्टी स्वयंचलितपणे सोलर बॅकअपवर स्विच होते."

    else:
        ans = f"🌱 तुमच्या शेताची सध्याची स्थिती: मातीचा ओलावा {m}%, पावसाचा अंदाज {r}%, आणि वीज स्थिती: {'सुरू' if p else 'बंद'}. पिकांचे नुकसान टाळण्यासाठी जलदृष्टी सातत्याने मॉनिटरिंग करत आहे."

    # Assistant reply
    with st.chat_message("assistant"):
        st.write(ans)
    st.session_state.messages.append({"role": "assistant", "content": ans})