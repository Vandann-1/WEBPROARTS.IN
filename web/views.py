from django.shortcuts import render

from django.db import models
from django.utils.text import slugify
from django.shortcuts import render, get_object_or_404
from .models import ContactMessage, BlogPost
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import ContactMessage

@csrf_protect
def contact_form_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Basic Validation
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message', '')

            if not all([first_name, last_name, email, subject]):
                return JsonResponse({"status": "error", "error": "All fields are required."}, status=400)

            # Save to Database
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
                message=message
            )

            return JsonResponse({"status": "success", "message": "Data saved successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=500)
            
    return JsonResponse({"status": "error", "error": "Invalid request method"}, status=400)







def digital_marketing(request):
    return render(request, 'digital-marketing.html')

def web_design(request):
    return render(request, 'web-design.html')

def video_Editing(request):
    return render(request, 'video-editing.html')

def social_media(request):
    return render(request, 'social-media.html')

def garphic_design(request):
    return render(request, 'garphic.html')

def policy(request):
    return render(request, 'policy.html')

def term(request):
    return render(request, 'term.html')


def webdev(request):
    return render(request, 'webdev.html')




from django.shortcuts import render, Http404

POSTS_DATA = {
    '1': {
        'id': 1,
        'title': 'The Hook Method: Viral Video Secrets',
        'category': 'Production',
        'image': 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?q=80&w=800',
        'excerpt': 'Learn how we engineer the first 3 seconds of social content to stop the scroll...',
        'content': """
            <p>To win on social media today, the first 3 seconds are everything. At Web Pro Arts, we don't just call it an opening; we call it <strong>"The Hook."</strong> In an era of infinite scroll and diminishing attention spans, the hook is the difference between a viral brand and a digital ghost.</p>
            <h3>The Anatomy of the 3-Second Rule</h3>
            <p>The human brain processes visual information 60,000 times faster than text. When a user is scrolling, their thumb moves at a constant rhythm. To break that rhythm, we must trigger a "Pattern Interrupt." This forces the brain to switch from passive consumption to active observation.</p>
            <ul>
                <li><strong>Visual Velocity:</strong> Rapid scene transitions in the first 1.5 seconds.</li>
                <li><strong>High-Contrast Overlays:</strong> Bold typography that tells the viewer exactly what they are going to learn.</li>
                <li><strong>The Curiosity Gap:</strong> Starting with a statement that can only be answered by watching further.</li>
            </ul>
            <h3>Why High-Contrast Text Overlays Matter</h3>
            <p>Over 80% of social media users consume video with the sound muted. This statistic alone dictates that your visual storytelling must be self-sufficient. We utilize high-contrast overlays—typically using our signature Cyan (#28b8d9) and Navy (#16598a) palette—to ensure readability against any background.</p>
            <h3>The Science of Rapid Scene Transitions</h3>
            <p>Static shots are the death of retention. In our editing suite, we follow the "2-Second Cut" rule. Every two seconds, something on the screen must change. This constant stream of new visual stimuli prevents the brain from entering a "boredom state." For performance marketing, this translates directly into higher View-Through Rates (VTR).</p>
            <p><strong>Summary:</strong> Your video's hook is your brand's digital first impression. Win the first 3 seconds, and you win the customer.</p>
        """
    },
    '2': {
        'id': 2,
        'title': 'Psychology of Color in SaaS Branding',
        'category': 'Branding',
        'image': 'https://i.pinimg.com/originals/bd/80/92/bd8092c59bcf3ae83117e910afbe12dc.jpg',
        'excerpt': 'Why top tech companies use high-contrast blue and aqua tones for trust...',
        'content': """
            <p>Colors aren't just aesthetic; they are emotional triggers that speak directly to the subconscious. In SaaS, where a user decides to stay or bounce in seconds, color is your most powerful tool. At <strong>Web Pro Arts</strong>, our foundation in Blue and Aqua is a calculated strategic move designed to project stability and innovation.</p>
            <h3>The Science of Visual Trust</h3>
            <p>Because users "rent" software, they need to feel it is secure. Blue has historically been the choice for tech giants like IBM and Intel because it lowers the heart rate and creates a sense of professional calm.</p>
            <h3>The "Action Color" Strategy</h3>
            <p>One of the biggest mistakes is using brand colors for everything. If your website is blue and your "Sign Up" button is also blue, it becomes invisible. We advocate for the <strong>Isolation Effect</strong>. By using a high-contrast accent—like our bright Cyan—against a dark Navy background, we create a visual "shout."</p>
            <h3>The Dark Mode Revolution</h3>
            <p>In 2026, Dark Mode is a requirement. When designing for dark mode, bright colors like Aqua become luminous, creating a futuristic aesthetic that resonates with tech-savvy founders.</p>
            <p><strong>Summary:</strong> People don't just buy what your software does; they buy how it makes them <em>feel</em>. Use color to make them feel powerful and secure.</p>
        """
    },
    '3': {
        'id': 3,
        'title': 'Mastering Meta Ads in the AI Era',
        'category': 'Performance',
        'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800',
        'excerpt': 'How Advantage+ campaigns are changing the way agencies manage budgets...',
        'content': """
            <p>The landscape of performance marketing has shifted. We are no longer in the era of manual "Interest Targeting." In 2026, the algorithm is the smartest person in the room. At <strong>Web Pro Arts</strong>, we’ve moved away from micro-managing audiences and toward <strong>Creative-Led Growth</strong>.</p>

            <h3>The Death of Interest Targeting</h3>
            <p>For years, media buyers spent hours selecting interests like "Entrepreneurs" or "Luxury Travel." Today, Meta’s AI—specifically the <strong>Advantage+</strong> suite—can identify your perfect customer better than any human. By using Broad Targeting, we allow the AI to analyze millions of data points to find the person most likely to convert.</p>

            <h3>The New Role of Creative Assets</h3>
            <p>If the AI handles the targeting, what does the agency do? We handle the <strong>Creative Strategy</strong>. In the modern era, your <em>ad creative is your targeting</em>. If we show a video about "High-Performance Servers," the AI will observe who watches that video and automatically find more people like them. The visual asset tells the machine who the customer is.</p>

            <h3>The Advantage+ Shopping Loop</h3>
            <p>For our e-commerce clients, we utilize <strong>Advantage+ Shopping Campaigns (ASC)</strong>. This automated system combines prospecting and re-targeting into a single campaign. It continuously tests different combinations of hooks, headlines, and descriptions to find the winning "Winner" ad that scales your ROAS (Return on Ad Spend).</p>

            <h3>Data-Driven Iteration</h3>
            <p>Success in paid media is no longer about "Setting and Forgetting." It is about a constant loop of <strong>Test -> Analyze -> Pivot</strong>. We look at metrics like:</p>
            <ul>
                <li><strong>Thumb-Stop Ratio:</strong> How many people watched the first 3 seconds?</li>
                <li><strong>Hold Rate:</strong> How many people stayed until the middle?</li>
                <li><strong>Conversion Rate (CVR):</strong> How many people actually clicked the "Buy" button?</li>
            </ul>

            <h3>Summary: Feed the Machine</h3>
            <p>To win with Meta Ads in 2026, you must stop fighting the AI and start feeding it. By providing the algorithm with high-quality video hooks and strategic brand messaging, Web Pro Arts ensures your budget is never wasted on the wrong audience.</p>
            <p><strong>Remember:</strong> Don't try to outsmart the machine; out-create your competition.</p>
        """}
}


def blog_detail(request, post_id):
    post = POSTS_DATA.get(str(post_id))
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})

def blogs(request):
    return render(request, 'blog.html', {'posts': POSTS_DATA})

def blog_detail(request, post_id):
    # Retrieve the specific post using the ID from the URL
    post = POSTS_DATA.get(str(post_id))
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog_detail.html', {'post': post})

