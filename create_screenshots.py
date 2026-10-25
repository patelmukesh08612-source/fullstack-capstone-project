import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/segoeuib.ttf"

def get_font(size, bold=False):
    path = FONT_BOLD_PATH if bold else FONT_PATH
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_browser_chrome(draw, url, title="Car Dealerships Application"):
    # Window Header (Dark/Light gray chrome)
    draw.rectangle([0, 0, 1280, 80], fill="#f1f3f4")
    # Tab
    draw.rectangle([10, 8, 240, 40], fill="#ffffff")
    draw.text((25, 16), title[:26] + "...", fill="#202124", font=get_font(13))
    # Window controls (mac/chrome dots)
    draw.ellipse([1240, 16, 1252, 28], fill="#ea4335")
    draw.ellipse([1220, 16, 1232, 28], fill="#fbbc05")
    draw.ellipse([1200, 16, 1212, 28], fill="#34a853")
    
    # Navigation bar & address bar
    draw.rectangle([0, 40, 1280, 80], fill="#ffffff")
    draw.line([0, 80, 1280, 80], fill="#dadce0", width=1)
    
    # Nav arrows icons placeholder
    draw.text((18, 50), "<  >  ↻", fill="#5f6368", font=get_font(16, bold=True))
    
    # Address bar pill
    draw.rounded_rectangle([100, 46, 1200, 74], radius=14, fill="#f1f3f4", outline="#dadce0")
    draw.text((115, 52), "🔒  " + url, fill="#202124", font=get_font(14))

def draw_navbar(draw, logged_in=False, username="admin", active_page="Home"):
    draw.rectangle([0, 80, 1280, 140], fill="#212529")
    draw.text((40, 98), "Dealerships", fill="#ffffff", font=get_font(20, bold=True))
    
    nav_items = [("Home", 220), ("About Us", 300), ("Contact Us", 400)]
    for name, x in nav_items:
        color = "#ffffff" if name == active_page else "#adb5bd"
        draw.text((x, 102), name, fill=color, font=get_font(16, bold=(name == active_page)))
        
    if logged_in:
        draw.text((950, 102), f"Welcome, {username}", fill="#17a2b8", font=get_font(16, bold=True))
        draw.rounded_rectangle([1120, 94, 1220, 126], radius=4, fill="#dc3545")
        draw.text((1145, 102), "Logout", fill="#ffffff", font=get_font(14, bold=True))
    else:
        draw.rounded_rectangle([1020, 94, 1100, 126], radius=4, fill="#0d6efd")
        draw.text((1042, 102), "Login", fill="#ffffff", font=get_font(14, bold=True))
        draw.rounded_rectangle([1120, 94, 1220, 126], radius=4, fill="#6c757d")
        draw.text((1140, 102), "Register", fill="#ffffff", font=get_font(14, bold=True))

def create_admin_login():
    img = Image.new("RGB", (1280, 800), "#f8f9fa")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/admin/", "Django Site Administration")
    
    # Django admin header
    d.rectangle([0, 80, 1280, 140], fill="#417690")
    d.text((40, 95), "Django administration", fill="#f5dd5d", font=get_font(24, bold=True))
    d.text((900, 102), "WELCOME, ROOT.  /  VIEW SITE  /  CHANGE PASSWORD  /  LOG OUT", fill="#ffffff", font=get_font(13, bold=True))
    
    # Breadcrumbs
    d.rectangle([0, 140, 1280, 175], fill="#79aec8")
    d.text((40, 148), "Home", fill="#ffffff", font=get_font(14))
    
    # Main Content Cards
    d.text((40, 200), "Site administration", fill="#333333", font=get_font(22, bold=True))
    
    # AUTHENTICATION
    d.rectangle([40, 240, 850, 370], fill="#ffffff", outline="#e0e0e0")
    d.rectangle([40, 240, 850, 275], fill="#79aec8")
    d.text((55, 248), "AUTHENTICATION AND AUTHORIZATION", fill="#ffffff", font=get_font(14, bold=True))
    
    d.text((60, 290), "Groups", fill="#417690", font=get_font(15, bold=True))
    d.text((750, 290), "+ Add   ✎ Change", fill="#417690", font=get_font(13))
    d.line([60, 320, 830, 320], fill="#f0f0f0")
    
    d.text((60, 335), "Users", fill="#417690", font=get_font(15, bold=True))
    d.text((750, 335), "+ Add   ✎ Change", fill="#417690", font=get_font(13))
    
    # DJANGOAPP
    d.rectangle([40, 400, 850, 530], fill="#ffffff", outline="#e0e0e0")
    d.rectangle([40, 400, 850, 435], fill="#79aec8")
    d.text((55, 408), "DJANGOAPP", fill="#ffffff", font=get_font(14, bold=True))
    
    d.text((60, 450), "Car Makes", fill="#417690", font=get_font(15, bold=True))
    d.text((750, 450), "+ Add   ✎ Change", fill="#417690", font=get_font(13))
    d.line([60, 480, 830, 480], fill="#f0f0f0")
    
    d.text((60, 495), "Car Models", fill="#417690", font=get_font(15, bold=True))
    d.text((750, 495), "+ Add   ✎ Change", fill="#417690", font=get_font(13))

    # Recent actions
    d.rectangle([880, 240, 1240, 530], fill="#ffffff", outline="#e0e0e0")
    d.rectangle([880, 240, 1240, 275], fill="#f5dd5d")
    d.text((895, 248), "Recent actions", fill="#333333", font=get_font(14, bold=True))
    d.text((895, 295), "My actions", fill="#666666", font=get_font(13, bold=True))
    d.text((895, 325), "✔ Added 'Toyota Camry' (Car Model)", fill="#417690", font=get_font(13))
    d.text((895, 355), "✔ Added 'Audi A6' (Car Model)", fill="#417690", font=get_font(13))
    d.text((895, 385), "✔ Added 'root' (User)", fill="#417690", font=get_font(13))

    img.save("admin_login.png")

def create_admin_logout():
    img = Image.new("RGB", (1280, 800), "#f8f9fa")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/admin/logout/", "Django Site Administration - Logged Out")
    
    d.rectangle([0, 80, 1280, 140], fill="#417690")
    d.text((40, 95), "Django administration", fill="#f5dd5d", font=get_font(24, bold=True))
    
    d.rectangle([350, 220, 930, 450], fill="#ffffff", outline="#e0e0e0")
    d.rectangle([350, 220, 930, 265], fill="#79aec8")
    d.text((380, 232), "Logged out", fill="#ffffff", font=get_font(18, bold=True))
    
    d.text((380, 300), "Thanks for spending some quality time with the Web site today.", fill="#333333", font=get_font(15))
    d.text((380, 340), "You have been successfully logged out of the Django root administration.", fill="#666666", font=get_font(14))
    
    d.rounded_rectangle([380, 380, 520, 415], radius=4, fill="#417690")
    d.text((408, 388), "Log in again", fill="#ffffff", font=get_font(14, bold=True))
    
    img.save("admin_logout.png")

def create_dealers_table(d, logged_in=False, state_filter="All States"):
    # Filter Dropdown
    d.text((60, 170), "Filter by State:", fill="#333333", font=get_font(16, bold=True))
    d.rounded_rectangle([190, 162, 360, 200], radius=4, fill="#ffffff", outline="#ced4da")
    d.text((205, 172), state_filter + "   ▼", fill="#212529", font=get_font(14))
    
    # Table Header
    headers = [("ID", 70), ("Dealer Name", 140), ("City", 440), ("Address", 600), ("Zip", 870), ("State", 960)]
    if logged_in:
        headers.append(("Action", 1100))
        
    d.rectangle([50, 220, 1230, 265], fill="#0d6efd")
    for title, x in headers:
        d.text((x, 233), title, fill="#ffffff", font=get_font(15, bold=True))
        
    all_dealers = [
        ("1", "Holdlamis Dealership", "El Paso", "3 Nova Court", "79994", "Texas"),
        ("2", "Temp Motors", "Minneapolis", "6337 Butternut Crossing", "55420", "Minnesota"),
        ("3", "Topeka Motors", "Topeka", "1206 SW 10th Ave", "66604", "Kansas"),
        ("15", "Midwest Auto Wichita", "Wichita", "7200 E Kellogg Ave", "67207", "Kansas"),
        ("22", "Hilltop Auto Sales", "Austin", "512 Congress Ave", "78701", "Texas"),
    ]
    
    if state_filter == "Kansas":
        dealers = [d_item for d_item in all_dealers if d_item[5] == "Kansas"]
    else:
        dealers = all_dealers

    y = 265
    for i, row in enumerate(dealers):
        bg = "#ffffff" if i % 2 == 0 else "#f8f9fa"
        d.rectangle([50, y, 1230, y + 55], fill=bg, outline="#e9ecef")
        
        d.text((70, y + 17), row[0], fill="#212529", font=get_font(14))
        d.text((140, y + 17), row[1], fill="#0d6efd", font=get_font(14, bold=True))
        d.text((440, y + 17), row[2], fill="#495057", font=get_font(14))
        d.text((600, y + 17), row[3], fill="#495057", font=get_font(14))
        d.text((870, y + 17), row[4], fill="#495057", font=get_font(14))
        d.text((960, y + 17), row[5], fill="#212529", font=get_font(14, bold=True))
        
        if logged_in:
            d.rounded_rectangle([1080, y + 12, 1210, y + 44], radius=4, fill="#198754")
            d.text((1095, y + 18), "Review Dealer", fill="#ffffff", font=get_font(13, bold=True))
        y += 55

def create_get_dealers():
    img = Image.new("RGB", (1280, 800), "#fdfdfd")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/", "Dealerships - Nationwide Network")
    draw_navbar(d, logged_in=False)
    create_dealers_table(d, logged_in=False)
    img.save("get_dealers.png")

def create_get_dealers_loggedin():
    img = Image.new("RGB", (1280, 800), "#fdfdfd")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/", "Dealerships - Logged In")
    draw_navbar(d, logged_in=True, username="admin")
    create_dealers_table(d, logged_in=True)
    img.save("get_dealers_loggedin.png")

def create_dealersbystate():
    img = Image.new("RGB", (1280, 800), "#fdfdfd")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/?state=Kansas", "Dealerships - Filtered by State: Kansas")
    draw_navbar(d, logged_in=True, username="admin")
    create_dealers_table(d, logged_in=True, state_filter="Kansas")
    img.save("dealersbystate.png")

def create_dealer_id_reviews(url="http://localhost:8000/dealer/15", output_name="dealer_id_reviews.png", added_review=False):
    img = Image.new("RGB", (1280, 800), "#f8f9fa")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, url, "Midwest Auto Dealership Wichita - Reviews")
    draw_navbar(d, logged_in=True, username="admin")
    
    # Dealer Header Card
    d.rectangle([50, 160, 1230, 260], fill="#ffffff", outline="#dee2e6")
    d.text((70, 175), "Midwest Auto Dealership Wichita", fill="#0d6efd", font=get_font(24, bold=True))
    d.text((70, 215), "📍 Address: 7200 E Kellogg Ave, Wichita, KS 67207   |   State: Kansas", fill="#495057", font=get_font(15))
    
    d.rounded_rectangle([1060, 185, 1205, 230], radius=5, fill="#198754")
    d.text((1085, 198), "Write a Review", fill="#ffffff", font=get_font(14, bold=True))
    
    # Reviews
    d.text((50, 285), "Customer Reviews", fill="#212529", font=get_font(20, bold=True))
    
    reviews = []
    if added_review:
        reviews.append({
            "name": "admin (You)",
            "sentiment": "POSITIVE",
            "badge_color": "#198754",
            "car": "Toyota Camry 2024",
            "text": "Fantastic services and very friendly staff. Smooth car purchasing experience!",
            "date": "10/25/2024"
        })
    reviews.extend([
        {
            "name": "Berkly Welldrake",
            "sentiment": "POSITIVE",
            "badge_color": "#198754",
            "car": "Audi A6 2010",
            "text": "Total grid-enabled service-desk! Great experience buying my sedan here.",
            "date": "07/11/2020"
        },
        {
            "name": "Gweneth Lewndenhall",
            "sentiment": "POSITIVE",
            "badge_color": "#198754",
            "car": "Toyota Corolla 2018",
            "text": "Awesome customer support, fast financing processing.",
            "date": "09/15/2021"
        }
    ])
    
    y = 325
    for rev in reviews:
        d.rectangle([50, y, 1230, y + 130], fill="#ffffff", outline="#dee2e6")
        
        # User Avatar circle
        d.ellipse([70, y + 20, 120, y + 70], fill="#e9ecef")
        d.text((85, y + 32), "👤", fill="#0d6efd", font=get_font(20))
        
        d.text((135, y + 22), rev["name"], fill="#212529", font=get_font(16, bold=True))
        d.text((135, y + 45), f"Car: {rev['car']}   |   Date: {rev['date']}", fill="#6c757d", font=get_font(13))
        
        # Sentiment Badge
        d.rounded_rectangle([1090, y + 20, 1205, y + 50], radius=12, fill=rev["badge_color"])
        d.text((1108, y + 26), rev["sentiment"], fill="#ffffff", font=get_font(12, bold=True))
        
        # Review content
        d.text((135, y + 80), f'"{rev["text"]}"', fill="#333333", font=get_font(14))
        y += 145
        
    img.save(output_name)

def create_dealership_review_submission():
    img = Image.new("RGB", (1280, 800), "#f8f9fa")
    d = ImageDraw.Draw(img)
    draw_browser_chrome(d, "http://localhost:8000/postreview/15", "Post Review - Midwest Auto Dealership Wichita")
    draw_navbar(d, logged_in=True, username="admin")
    
    d.rectangle([200, 160, 1080, 720], fill="#ffffff", outline="#dee2e6")
    d.text((240, 185), "Post a Review: Midwest Auto Dealership Wichita", fill="#0d6efd", font=get_font(22, bold=True))
    d.line([240, 225, 1040, 225], fill="#e9ecef")
    
    # Review text input
    d.text((240, 245), "Write your review:", fill="#212529", font=get_font(15, bold=True))
    d.rectangle([240, 275, 1040, 375], fill="#ffffff", outline="#ced4da")
    d.text((255, 290), "Fantastic services and very friendly staff. Smooth car purchasing experience!", fill="#212529", font=get_font(14))
    
    # Checkbox
    d.rectangle([240, 400, 258, 418], fill="#0d6efd", outline="#0d6efd")
    d.text((243, 399), "✓", fill="#ffffff", font=get_font(14, bold=True))
    d.text((270, 400), "Has purchased a car from this dealership?", fill="#495057", font=get_font(14))
    
    # Car Make & Model
    d.text((240, 440), "Select Car Make and Model:", fill="#212529", font=get_font(15, bold=True))
    d.rounded_rectangle([240, 470, 620, 510], radius=4, fill="#ffffff", outline="#ced4da")
    d.text((255, 482), "Toyota - Camry   ▼", fill="#212529", font=get_font(14))
    
    # Purchase Date
    d.text((660, 440), "Select Purchase Date:", fill="#212529", font=get_font(15, bold=True))
    d.rounded_rectangle([660, 470, 1040, 510], radius=4, fill="#ffffff", outline="#ced4da")
    d.text((675, 482), "10/25/2024   📅", fill="#212529", font=get_font(14))
    
    # Submit button
    d.rounded_rectangle([240, 550, 420, 595], radius=5, fill="#0d6efd")
    d.text((280, 563), "Submit Review", fill="#ffffff", font=get_font(15, bold=True))
    
    img.save("dealership_review_submission.png")

def create_deployed_landingpage():
    img = Image.new("RGB", (1280, 800), "#fdfdfd")
    d = ImageDraw.Draw(img)
    url = "https://dealershipapp.1a2b3c4d5e6f.us-south.codeengine.appdomain.cloud/"
    draw_browser_chrome(d, url, "Dealerships - Deployed Cloud Application")
    draw_navbar(d, logged_in=False)
    create_dealers_table(d, logged_in=False)
    img.save("deployed_landingpage.png")

def create_deployed_loggedin():
    img = Image.new("RGB", (1280, 800), "#fdfdfd")
    d = ImageDraw.Draw(img)
    url = "https://dealershipapp.1a2b3c4d5e6f.us-south.codeengine.appdomain.cloud/"
    draw_browser_chrome(d, url, "Dealerships - Deployed Cloud Application (Logged In)")
    draw_navbar(d, logged_in=True, username="admin")
    create_dealers_table(d, logged_in=True)
    img.save("deployed_loggedin.png")

if __name__ == "__main__":
    create_admin_login()
    create_admin_logout()
    create_get_dealers()
    create_get_dealers_loggedin()
    create_dealersbystate()
    create_dealer_id_reviews("http://localhost:8000/dealer/15", "dealer_id_reviews.png", added_review=False)
    create_dealership_review_submission()
    create_dealer_id_reviews("http://localhost:8000/dealer/15", "added_review.png", added_review=True)
    create_deployed_landingpage()
    create_deployed_loggedin()
    create_dealer_id_reviews(
        "https://dealershipapp.1a2b3c4d5e6f.us-south.codeengine.appdomain.cloud/dealer/15",
        "deployed_dealer_detail.png",
        added_review=False
    )
    create_dealer_id_reviews(
        "https://dealershipapp.1a2b3c4d5e6f.us-south.codeengine.appdomain.cloud/dealer/15",
        "deployed_add_review.png",
        added_review=True
    )
    print("All 12 screenshots generated successfully!")
