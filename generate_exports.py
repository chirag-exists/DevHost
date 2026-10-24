import os
import sys
from playwright.sync_api import sync_playwright
from PIL import Image

OUTPUT_DIRS = {
    "crisis": "exports/crisis",
    "ai_input": "exports/ai_input",
    "solution": "exports/solution",
    "branding_base": "exports/branding_base",
    "svg": "exports/svg"
}

def ensure_dirs():
    for d in OUTPUT_DIRS.values():
        os.makedirs(d, exist_ok=True)

def trim_transparent(image_path, padding=24):
    """Trims excess empty transparent pixels while maintaining padding for soft drop shadows."""
    with Image.open(image_path) as im:
        if im.mode != "RGBA":
            return
        bbox = im.getbbox()
        if not bbox:
            return
        left = max(0, bbox[0] - padding)
        top = max(0, bbox[1] - padding)
        right = min(im.width, bbox[2] + padding)
        bottom = min(im.height, bbox[3] + padding)
        
        cropped = im.crop((left, top, right, bottom))
        cropped.save(image_path, "PNG", optimize=True)
        print(f"  -> Trimmed {os.path.basename(image_path)} to {cropped.size} (RGBA)")

def capture_elements():
    print("========================================")
    print("Capturing ResQTravel UI Components (3x Ultra-Res)")
    print("========================================")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            headless=True
        )
        
        # 1. Capture Components from export_stage.html
        context = browser.new_context(
            viewport={"width": 1920, "height": 1400},
            device_scale_factor=3  # 3x Ultra-High Resolution for 4K / 3D compositing
        )
        page = context.new_page()
        stage_url = "file:///" + os.path.abspath("export_stage.html").replace("\\", "/")
        print(f"Loading stage: {stage_url}")
        page.goto(stage_url, wait_until="networkidle")
        page.wait_for_function("() => document.fonts.status === 'loaded'")
        page.wait_for_timeout(1000)

        targets = [
            # Branding
            ("stage-logo", OUTPUT_DIRS["branding_base"] + "/branding_resqtravel_logo.png", 20),
            ("stage-brand-icon", OUTPUT_DIRS["branding_base"] + "/branding_resqtravel_icon.png", 16),
            
            # Crisis Elements
            ("stage-crisis-banner", OUTPUT_DIRS["crisis"] + "/crisis_disruption_banner.png", 32),
            ("stage-crisis-badge", OUTPUT_DIRS["crisis"] + "/crisis_badge_live_disruption.png", 16),
            ("stage-leg1-card", OUTPUT_DIRS["crisis"] + "/crisis_leg1_flight_card.png", 24),
            ("stage-leg1-with-connector", OUTPUT_DIRS["crisis"] + "/crisis_leg1_flight_with_connector.png", 24),
            ("stage-leg2-card", OUTPUT_DIRS["crisis"] + "/crisis_leg2_train_card.png", 24),
            ("stage-leg2-with-connector", OUTPUT_DIRS["crisis"] + "/crisis_leg2_train_with_connector.png", 24),
            
            # AI & Input
            ("stage-ticket-ingestion", OUTPUT_DIRS["ai_input"] + "/ai_ticket_ingestion_card.png", 24),
            ("stage-constraint-pills-group", OUTPUT_DIRS["ai_input"] + "/ai_constraint_pills_group.png", 20),
            ("stage-pill-senior", OUTPUT_DIRS["ai_input"] + "/ai_constraint_pill_senior_citizen.png", 16),
            ("stage-pill-budget", OUTPUT_DIRS["ai_input"] + "/ai_constraint_pill_budget.png", 16),
            ("stage-pill-arrive", OUTPUT_DIRS["ai_input"] + "/ai_constraint_pill_arrive_time.png", 16),
            ("stage-agent-active-pill", OUTPUT_DIRS["ai_input"] + "/ai_agent_active_pill.png", 16),
            
            # Solution Elements
            ("stage-akasa-card", OUTPUT_DIRS["solution"] + "/solution_akasa_recommendation_card.png", 32),
            ("stage-hotel-dispatch", OUTPUT_DIRS["solution"] + "/solution_hotel_hold_card.png", 28),
            ("stage-rebook-btn", OUTPUT_DIRS["solution"] + "/solution_1click_rebook_btn.png", 18),
            ("stage-whatsapp-btn", OUTPUT_DIRS["solution"] + "/solution_whatsapp_api_btn.png", 18),
        ]

        for elem_id, out_path, pad in targets:
            loc = page.locator(f"#{elem_id}")
            if loc.count() > 0:
                loc.screenshot(path=out_path, omit_background=True)
                trim_transparent(out_path, padding=pad)
            else:
                print(f"Warning: Element #{elem_id} not found!")

        # 2. Capture Clean Base App Interface in 1080p and 4K
        print("\nCapturing Clean Base App Interface (Full HD 1080p and 4K UHD)...")
        base_url = "file:///" + os.path.abspath("clean_base_stage.html").replace("\\", "/")
        
        # 1080p with Guide Slots
        p_1080 = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        p_1080.goto(base_url, wait_until="networkidle")
        p_1080.wait_for_timeout(800)
        p_1080.screenshot(path=OUTPUT_DIRS["branding_base"] + "/clean_base_app_interface_guides_1080p.png", full_page=True)
        print("  -> Saved clean_base_app_interface_guides_1080p.png (1920x1080)")

        # 1080p Pure Blank Canvas
        p_1080.evaluate("() => document.getElementById('baseBody').classList.add('pure-blank')")
        p_1080.wait_for_timeout(300)
        p_1080.screenshot(path=OUTPUT_DIRS["branding_base"] + "/clean_base_app_interface_pure_1080p.png", full_page=True)
        print("  -> Saved clean_base_app_interface_pure_1080p.png (1920x1080)")
        p_1080.close()

        # 4K UHD with Guide Slots
        p_4k = browser.new_page(viewport={"width": 3840, "height": 2160}, device_scale_factor=1)
        p_4k.goto(base_url, wait_until="networkidle")
        p_4k.wait_for_timeout(800)
        p_4k.screenshot(path=OUTPUT_DIRS["branding_base"] + "/clean_base_app_interface_guides_4k.png", full_page=True)
        print("  -> Saved clean_base_app_interface_guides_4k.png (3840x2160)")

        # 4K UHD Pure Blank Canvas
        p_4k.evaluate("() => document.getElementById('baseBody').classList.add('pure-blank')")
        p_4k.wait_for_timeout(300)
        p_4k.screenshot(path=OUTPUT_DIRS["branding_base"] + "/clean_base_app_interface_pure_4k.png", full_page=True)
        print("  -> Saved clean_base_app_interface_pure_4k.png (3840x2160)")
        p_4k.close()

        browser.close()
        print("\nAll high-resolution raster PNGs successfully exported!")

if __name__ == "__main__":
    ensure_dirs()
    capture_elements()
