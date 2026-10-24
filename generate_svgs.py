import os

SVG_DIR = "exports/svg"
os.makedirs(SVG_DIR, exist_ok=True)

# 1. Primary ResqTravel Logo SVG
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 64" width="320" height="64" fill="none">
  <defs>
    <linearGradient id="brandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1D4ED8" />
      <stop offset="100%" stop-color="#0D9488" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.12" />
    </filter>
  </defs>
  <style>
    .brand-text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; font-size: 32px; font-weight: 800; letter-spacing: -0.02em; }
  </style>
  <g transform="translate(4, 10)" filter="url(#shadow)">
    <rect width="44" height="44" rx="12" fill="url(#brandGrad)" />
    <!-- Lucide shield-check icon -->
    <g transform="translate(10, 10)" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
      <path d="m9 12 2 2 4-4" />
    </g>
  </g>
  <text x="60" y="42" class="brand-text" fill="#0F172A">Resq<tspan fill="#1D4ED8">Travel</tspan></text>
</svg>"""

with open(f"{SVG_DIR}/branding_resqtravel_logo.svg", "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. ResqTravel Shield Icon Alone SVG
icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
  <defs>
    <linearGradient id="iconGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1D4ED8" />
      <stop offset="100%" stop-color="#0D9488" />
    </linearGradient>
    <filter id="iconShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#1E3A8A" flood-opacity="0.25" />
    </filter>
  </defs>
  <rect x="4" y="4" width="56" height="56" rx="16" fill="url(#iconGrad)" filter="url(#iconShadow)" />
  <g transform="translate(16, 16)" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M16 29.33s10.67-5.33 10.67-13.33V6.67L16 2.67 5.33 6.67v9.33c0 8 10.67 13.33 10.67 13.33z" />
    <path d="m12 16 2.67 2.67 5.33-5.34" />
  </g>
</svg>"""

with open(f"{SVG_DIR}/branding_resqtravel_icon.svg", "w", encoding="utf-8") as f:
    f.write(icon_svg)

# 3. Green "AI Agent Active" Pill SVG
agent_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 40" width="260" height="40" fill="none">
  <defs>
    <filter id="pillShadow" x="-5%" y="-10%" width="110%" height="130%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#15803D" flood-opacity="0.1" />
    </filter>
    <filter id="dotGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#22C55E" flood-opacity="0.8" />
    </filter>
  </defs>
  <style>
    .text-main { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600; fill: #15803D; }
    .text-sub  { font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 400; fill: #64748B; }
  </style>
  <rect x="2" y="2" width="254" height="34" rx="17" fill="#F0FDF4" stroke="#DCFCE7" stroke-width="1.2" filter="url(#pillShadow)" />
  <!-- Glowing green dot -->
  <circle cx="20" cy="19" r="4.5" fill="#22C55E" filter="url(#dotGlow)" />
  <circle cx="20" cy="19" r="2.5" fill="#FFFFFF" opacity="0.6" />
  <text x="34" y="24" class="text-main">AI Agent Active <tspan class="text-sub">(Gemini 2.5 Flash)</tspan></text>
</svg>"""

with open(f"{SVG_DIR}/ai_agent_active_pill.svg", "w", encoding="utf-8") as f:
    f.write(agent_svg)

# 4. Red "Live Disruption Detected" Badge Pill SVG
badge_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 40" width="240" height="40" fill="none">
  <defs>
    <filter id="badgeShadow" x="-10%" y="-15%" width="120%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#DC2626" flood-opacity="0.3" />
    </filter>
  </defs>
  <style>
    .badge-text { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 700; fill: #FFFFFF; letter-spacing: 0.01em; }
  </style>
  <rect x="3" y="3" width="232" height="32" rx="16" fill="#DC2626" filter="url(#badgeShadow)" />
  <!-- Zap icon -->
  <g transform="translate(18, 9)" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <polygon points="11 1 2 12 9 12 8 19 17 8 10 8 11 1" />
  </g>
  <text x="44" y="24" class="badge-text">Live Disruption Detected</text>
</svg>"""

with open(f"{SVG_DIR}/crisis_badge_live_disruption.svg", "w", encoding="utf-8") as f:
    f.write(badge_svg)

# 5. Blue "1-Click Rebook" Button SVG
rebook_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 48" width="200" height="48" fill="none">
  <defs>
    <linearGradient id="rebookGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <filter id="btnShadow" x="-10%" y="-15%" width="120%" height="145%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#1D4ED8" flood-opacity="0.35" />
    </filter>
  </defs>
  <style>
    .btn-text { font-family: 'Inter', sans-serif; font-size: 14.5px; font-weight: 700; fill: #FFFFFF; }
  </style>
  <rect x="4" y="4" width="190" height="40" rx="20" fill="url(#rebookGrad)" filter="url(#btnShadow)" />
  <rect x="4.5" y="4.5" width="189" height="39" rx="19.5" stroke="rgba(255,255,255,0.25)" stroke-width="1" />
  <!-- Zap icon -->
  <g transform="translate(24, 14)" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <polygon points="12 1 3 12 10 12 9 20 18 9 11 9 12 1" />
  </g>
  <text x="52" y="29" class="btn-text">1-Click Rebook</text>
</svg>"""

with open(f"{SVG_DIR}/solution_1click_rebook_btn.svg", "w", encoding="utf-8") as f:
    f.write(rebook_svg)

# 6. Green "Send via WhatsApp API" Button SVG
whatsapp_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 46" width="230" height="46" fill="none">
  <defs>
    <filter id="waShadow" x="-10%" y="-15%" width="120%" height="145%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#25D366" flood-opacity="0.35" />
    </filter>
  </defs>
  <style>
    .wa-text { font-family: 'Inter', sans-serif; font-size: 13.5px; font-weight: 600; fill: #FFFFFF; }
  </style>
  <rect x="4" y="4" width="220" height="36" rx="18" fill="#25D366" filter="url(#waShadow)" />
  <rect x="4.5" y="4.5" width="219" height="35" rx="17.5" stroke="rgba(255,255,255,0.2)" stroke-width="1" />
  <!-- Message Circle icon -->
  <g transform="translate(18, 12)" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z" />
  </g>
  <text x="46" y="27" class="wa-text">Send via WhatsApp API</text>
</svg>"""

with open(f"{SVG_DIR}/solution_whatsapp_api_btn.svg", "w", encoding="utf-8") as f:
    f.write(whatsapp_svg)

# 7. Constraint Pills Group SVG
pills_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 50" width="650" height="50" fill="none">
  <style>
    .chip-text { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500; fill: #1E40AF; }
  </style>
  <!-- Pill 1: Senior citizen -->
  <g transform="translate(0, 5)">
    <rect x="2" y="2" width="180" height="36" rx="18" fill="#EFF6FF" stroke="#DBEAFE" stroke-width="1.2" />
    <g transform="translate(14, 10)" stroke="#1D4ED8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
    </g>
    <text x="42" y="25" class="chip-text">Senior citizen</text>
    <g transform="translate(150, 12)" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"><line x1="14" y1="4" x2="4" y2="14" /><line x1="4" y1="4" x2="14" y2="14" /></g>
  </g>
  <!-- Pill 2: Budget < ₹3,000 -->
  <g transform="translate(195, 5)">
    <rect x="2" y="2" width="165" height="36" rx="18" fill="#EFF6FF" stroke="#DBEAFE" stroke-width="1.2" />
    <g transform="translate(14, 10)" stroke="#1D4ED8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="M6 3h12M6 8h12M6 13l8.5 8M6 13h3a4.5 4.5 0 0 0 0-9" />
    </g>
    <text x="42" y="25" class="chip-text">Budget &lt; ₹3,000</text>
    <g transform="translate(135, 12)" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"><line x1="14" y1="4" x2="4" y2="14" /><line x1="4" y1="4" x2="14" y2="14" /></g>
  </g>
  <!-- Pill 3: Arrive before 9:00 PM -->
  <g transform="translate(375, 5)">
    <rect x="2" y="2" width="205" height="36" rx="18" fill="#EFF6FF" stroke="#DBEAFE" stroke-width="1.2" />
    <g transform="translate(14, 10)" stroke="#1D4ED8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <circle cx="10" cy="10" r="9" />
      <polyline points="10 5 10 10 14 10" />
    </g>
    <text x="42" y="25" class="chip-text">Arrive before 9:00 PM</text>
    <g transform="translate(175, 12)" stroke="#94A3B8" stroke-width="1.8" stroke-linecap="round"><line x1="14" y1="4" x2="4" y2="14" /><line x1="4" y1="4" x2="14" y2="14" /></g>
  </g>
</svg>"""

with open(f"{SVG_DIR}/ai_constraint_pills.svg", "w", encoding="utf-8") as f:
    f.write(pills_svg)

print("Generated clean standalone vector SVGs in exports/svg!")
