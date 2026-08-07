from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Idea database by category
IDEAS = {
    "business": [
        "Start a subscription box for Nigerian university students containing monthly study + self-care essentials.",
        "Build a marketplace for verified second-hand luxury items in Lagos.",
        "Create a personal branding consultancy for African tech professionals.",
        "Launch a sustainable packaging business for Nigerian e-commerce brands.",
        "Start a niche content creation agency for Afrobeats artists.",
        "Build a logistics app connecting small businesses to courier services.",
        "Create an online tutoring platform for STEM subjects in Nigerian schools.",
        "Start a virtual assistant service for busy entrepreneurs.",
        "Launch a beauty supply wholesale platform for beauty entrepreneurs.",
        "Create a meal prep delivery service targeting corporate offices.",
    ],
    "content": [
        "Write a thread about the psychology of why people doom-scroll.",
        "Create a carousel about 5 productivity myths that are actually hurting you.",
        "Make a video showing your morning routine breakdown (time, habits, apps).",
        "Write a brutally honest review of a product you actually use daily.",
        "Create a 'things nobody tells you about [your field]' post.",
        "Share a failure story and what you learned from it.",
        "Make a guide: how to negotiate your first [your industry] deal.",
        "Write about a skill you learned in 30 days.",
        "Create a comparison: what changed in your life when you started [habit].",
        "Share your actual numbers: revenue, followers, hours worked.",
    ],
    "gift": [
        "A personalized Spotify playlist with a handwritten tracklist.",
        "A custom illustration of their most embarrassing moment.",
        "A 'reasons why you're my friend' jar with 52 cards.",
        "A vintage book from their birth year + first edition if possible.",
        "A custom print of their favorite song's lyrics in calligraphy.",
        "A scrapbook of screenshots from your text conversations.",
        "A 'coupon book' for favors (coffee runs, vent sessions, etc).",
        "A Polaroid camera with instant film + pre-shot photos.",
        "A plant in a pot they've painted themselves.",
        "A custom-blend coffee or tea with a personalized label.",
    ],
    "study": [
        "Create a study guide using only memes and simplified diagrams.",
        "Record yourself explaining the concept as if teaching a 10-year-old.",
        "Build a flashcard deck using spaced repetition for exam prep.",
        "Start a study group focused on teaching others instead of solo cramming.",
        "Create a mind map connecting this topic to things you already know.",
        "Write practice exam questions and swap with a study partner.",
        "Use the Feynman Technique: explain it, identify gaps, simplify, teach it.",
        "Create a video summary of the week's lesson in under 5 minutes.",
        "Build a timeline or visual hierarchy of concepts.",
        "Teach it to someone who knows nothing about the subject.",
    ],
    "meal": [
        "Sheet pan dinner: marinated chicken thighs + roasted vegetables + lemon.",
        "Quick stir-fry: whatever vegetables you have + garlic + soy sauce + noodles.",
        "One-pot jollof rice with smoked turkey and peppers.",
        "Breakfast for dinner: scrambled eggs, plantains, avocado, tomato sauce.",
        "Protein bowl: grilled fish + quinoa + roasted beets + tahini dressing.",
        "Quick pasta: garlic oil, canned tomatoes, spinach, parmesan, done in 20 mins.",
        "Slow cooker stew: beef, potatoes, carrots, leave it for 4 hours.",
        "Rice and beans with caramelized onions and grilled sausage.",
        "Lettuce wraps: ground meat, ginger, soy sauce, crispy lettuce cups.",
        "Simple soup: blend roasted vegetables, add cream, top with crispy onions.",
    ],
    "brand": [
        "Lumina Studios",
        "Prism & Co",
        "Forge Creative",
        "Beacon Labs",
        "Catalyst Goods",
        "Apex Collective",
        "Ember Ventures",
        "Zenith Digital",
        "Velocity Brand House",
        "Arcane Creative Studio",
    ],
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate/<category>")
def generate(category):
    category = category.lower()
    
    if category == "surprise":
        category = random.choice(list(IDEAS.keys()))
        idea = random.choice(IDEAS[category])
        return jsonify({
            "idea": idea,
            "category": category
        })
    
    if category not in IDEAS:
        return jsonify({"error": "Category not found"}), 404
    
    idea = random.choice(IDEAS[category])
    return jsonify({
        "idea": idea,
        "category": category
    })

if __name__ == "__main__":
    app.run(debug=True)
