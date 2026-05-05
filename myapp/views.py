import os
from django.shortcuts import render          # line 2 - Http404 வேண்டாம் இங்க
from django.http import JsonResponse, Http404  # line 4 - ✅ இங்க add பண்ணுங்க
import google.generativeai as genai


# ✅ Configure Gemini API Key (Direct + ENV fallback)
API_KEY = os.getenv("GEMINI_API_KEY")

# ⚠️ If ENV not set, fallback key (testing only)
if not API_KEY:
    API_KEY = "AIzaSyAbod6F2tHHMl73kMLB_GMROtTCXM8XNCM"

genai.configure(api_key=API_KEY)

# ✅ EVENTS DATA - March 14 mattum
EVENTS = [
    {
        "id": 1,
        "title": "Teachers Excellence Award",
        "date": "March 14th, 2026",
        "month": "MAR",
        "day": "14",
    "image": "assets/images/image1.jpg",
        "description": "JVM Engineering College proudly presents the Teachers Award for Excellence in honour of Founders Day. Vote for your favourite teacher! Event held at Krissh Auditorium from 3:00 PM to 5:00 PM.",
        "time": "3:00 PM to 5:00 PM",
        "venue": "Krissh Auditorium",
    },
]

# ===== Pages =====
def index(request):
    return render(request, 'index.html', {'events': EVENTS})

def event_detail(request, event_id):
    event = next((e for e in EVENTS if e["id"] == event_id), None)
    if not event:
        raise Http404("Event not found")
    return render(request, 'event-detail.html', {'event': event})

def meetings(request):
    return render(request, 'meetings.html')

def meeting_details(request):
    return render(request, 'meeting-details.html')

def scholarship(request):
    return render(request, 'scholarship.html')

# ===== College Data =====
COLLEGE_INFO = """
SHIFT-I
UG COURSES:
- B.Com. (General)
- B.Com. (Accounting & Finance)
- B.Com. (Corporate Secretaryship)
- B.Com. (Computer Applications)
- B.Com. (Information System Management)
- B.Com. (Bank Management)
- B.Com. (Honours)
- B.B.A. (Business Administration)
- B.A. (Business Economics)
- B.A. (English)
- B.C.A. (Computer Applications)
- B.Sc. (Computer Science)
- B.Sc. (Mathematics)
- B.Sc. (Computer Science with Data Science)

PG COURSES:
- M.A. (Human Resource Management)
- M.Sc. (Computer Science)
- M.Com. (General)
- M.A. (English)
- Ph.D. in Commerce

SHIFT-II
UG COURSES:
- B.Com. (General)
- B.Com. (Corporate Secretaryship)

CERTIFICATE COURSES:
1. Accounting using Excel
2. Advanced Excel and PHP
3. Artificial Intelligence
4. AI/ML Programming
5. AR-VR Programming
6. Building Exam Competence
7. Business Analyst
8. Business Statistics
9. Corporate Skills
10. Computerised Accounting
11. Communication Skills
12. Competitive Exams: TNPSC/UGC-NET, SET/TANCET
13. Data Science
14. Data Analytics-Basic
15. Data Visualization using Python
16. Digital Banking
17. Digital Marketing
18. Ethical Hacking
19. Entrepreneurship Management
20. Fundamentals of C and C++ Programming
21. Full Stack Web Development
22. Internet of Things
23. IBPS
24. Logistics
25. Naan Mudhalvan
26. Power BI
27. Python for Beginners Level-I
28. Quantitative Aptitude and Logical Reasoning
29. Screenplay and Script Writing
30. Tally Prime
31. UI/UX Coding
32. Website Designing with Java Script

COLLEGE TIMING:
- Shift I: 8:30 a.m. to 1:30 p.m. (Work on 2nd & 4th Saturdays)
- Shift II: 1:30 p.m. to 5:30 p.m. (Work most Saturdays 9:00 a.m. to 5:00 p.m.)

ATTENDANCE & LEAVE:
- Minimum attendance required: 75%
- 65%–75% can be condoned by paying ₹250 per exam.
- Below 65% (but >50%) not eligible for condonation.

FACILITIES:
- 6 Computer Labs (UG & PG) + Research Lab
- Wi-Fi enabled campus
- ERP system implemented
- Library (KOHA ILMS 22:05, 13,121 books, 53 journals, 11 magazines)
- Krissh Auditorium (1000 seating capacity)

=========================
FEES STRUCTURE (Sample)
=========================
UG FEES (Per Year - Approx):
- B.Com (General): ₹____
- B.Com (A&F): ₹____
- BCA: ₹____
- B.Sc CS: ₹____
(Other courses: ₹____)

PG FEES (Per Year - Approx):
- M.Com: ₹____
- M.Sc CS: ₹____
- M.A English: ₹____

=========================
💰 FEES STRUCTURE (Per Year Approx)
=========================

UG FEES:

Commerce Courses:
- B.Com (General): ₹35,000
- B.Com (Accounting & Finance): ₹38,000
- B.Com (Corporate Secretaryship): ₹40,000
- B.Com (Computer Applications): ₹42,000
- B.Com (Information System Management): ₹41,000
- B.Com (Bank Management): ₹39,000
- B.Com (Honours): ₹45,000

Management Courses:
- B.B.A (Business Administration): ₹44,000

Arts Courses:
- B.A (Business Economics): ₹30,000
- B.A (English): ₹28,000

Computer & Science Courses:
- B.C.A (Computer Applications): ₹48,000
- B.Sc (Computer Science): ₹50,000
- B.Sc (Mathematics): ₹32,000
- B.Sc (Computer Science with Data Science): ₹55,000


=========================
🎓 PG FEES (Per Year Approx)
=========================

- M.Com (General): ₹55,000
- M.Sc (Computer Science): ₹60,000
- M.A (English): ₹50,000
- M.A (Human Resource Management): ₹58,000
- Ph.D Commerce: ₹70,000 (Research Fee Depends)


=========================
📜 CERTIFICATE COURSE FEES
=========================

Short Term Certificate Programs:
- Basic Courses: ₹5,000 – ₹8,000
- Advanced Courses: ₹10,000 – ₹15,000
(Example: AI/ML, Data Science, Full Stack Development)


=========================
🏠 HOSTEL FEES (Per Year)
=========================

Hostel Facilities Available for Boys & Girls.

Hostel Fee Details:
- Room Rent: ₹25,000
- Mess Fees: ₹5,000
- Total Hostel Fees: ₹30,000

Hostel Includes:
- 24/7 Security
- Clean Drinking Water
- Study Area
- Wi-Fi Facility
- Separate Hostel for Boys & Girls


=========================
🎓 OTHER FEES (Optional)
=========================

- Admission Fee (One Time): ₹5,000
- Exam Fee (Per Semester): ₹2,000 – ₹4,000
- Library Fee (Annual): ₹1,000
- Lab Fee (Science/CS): ₹3,000
- Sports Fee (Annual): ₹1,500
"""

# ✅ Simple Rule-Based Answers (Works Without Gemini)
def offline_reply(msg):
    msg = msg.lower()

    # Courses
    if "ug" in msg or "undergraduate" in msg or "course" in msg:
        return "📚 UG Courses: B.Com, BBA, BA English, BCA, B.Sc CS, B.Sc Maths and more."

    if "pg" in msg or "postgraduate" in msg:
        return "🎓 PG Courses: M.Com, M.Sc CS, MA English, MA HRM, PhD Commerce."

    # Timing
    if "timing" in msg or "time" in msg:
        return "⏰ College Timing: Shift I (8:30 AM–1:30 PM), Shift II (1:30 PM–5:30 PM)."

    # Facilities
    if "facility" in msg or "lab" in msg or "auditorium" in msg:
        return "🏫 Facilities: 6 computer labs, research lab, Wi-Fi campus, ERP, library, auditorium."

    if "library" in msg:
        return "📖 Library: KOHA ILMS, 13,121 books, 53 journals, 11 magazines, NDLI/N-LIST access."

    # ✅ Hostel FIRST (Important Fix)
    if "hostel" in msg or "mess" in msg:
        return "🏠 Hostel Fees: Room Rent ₹25,000 + Mess Fees ₹5,000 = Total ₹30,000 per year."

    # ✅ Fees AFTER Hostel
    if "fees" in msg or "fee" in msg:
        return "💰 UG/PG Fees available. Ask like: 'BCA fees' or 'M.Com fees'."

    return None


# ✅ Chatbot API
def chatbot_api(request):
    user_msg = request.GET.get("msg", "").strip()

    if not user_msg:
        return JsonResponse({"reply": "Hi 👋 Welcome! Ask me about courses, timings, facilities..."})

    # ✅ Step 1: Offline FAQ reply first
    reply = offline_reply(user_msg)
    if reply:
        return JsonResponse({"reply": reply})

    # ✅ Step 2: Gemini fallback (only if needed)
    try:
        model = genai.GenerativeModel("models/gemini-flash-lite-latest")

        prompt = f"""
You are a college enquiry chatbot.
Answer ONLY using the COLLEGE DATA below.

COLLEGE DATA:
{COLLEGE_INFO}

USER QUESTION:
{user_msg}
"""

        response = model.generate_content(prompt)
        return JsonResponse({"reply": (response.text or "").strip()})

    except Exception as e:

        # ✅ Handle Quota Error
        if "429" in str(e):
            return JsonResponse({
                "reply": "⚠️ Gemini quota exceeded. Please wait 1 minute or enable billing."
            })

        return JsonResponse({"reply": f"Error: {str(e)}"})
