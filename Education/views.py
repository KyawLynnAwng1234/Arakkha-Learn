from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Course,Lesson
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .forms import LessonForm

# Create your views here.
def home(request):
    # Fetch core filtering parameters from template inputs
    course_id = request.GET.get('course')
    search_query = request.GET.get('search')
    # Initialize basic QuerySet
    lessons = Lesson.objects.select_related('course').all()
    # 1. Handle course dynamic selection via category boxes or select lists
    if course_id:
        lessons = lessons.filter(course_id=course_id)
        
    # 2. Handle text pattern matching inside 'title' or 'summary' textareas
    if search_query:
        lessons = lessons.filter(
            Q(title__icontains=search_query) | 
            Q(summary__icontains=search_query)
        )   
    context = {
        'courses': Course.objects.all(),
        'lessons': lessons,
    }
    return render(request, 'frontend/home.html', context)

def detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'frontend/detail.html',context)

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )
         # Debugging line to check the type of user object returned by authenticate
        if user:
            login(request, user)
            return redirect("dashboard_page")
        return render(
            request,
            "login.html",
            {
                "error":"Invalid username or password."
            }
        )
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect("login_page")

def lesson(request):
    if request.method == 'POST':
        # Pass request.FILES to handle video and file data streams
        form = LessonForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("Form is valid. Cleaned data:", form.cleaned_data)  # Debugging line to check cleaned data
            form.save() # Saves data cleanly directly to database
            messages.success(request, "သင်ခန်းစာကို အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ။")
            return redirect('dashboard_page') # Redirect back to main dashboard view
        else:
            messages.error(request, "အချက်အလက်များ ထည့်သွင်းမှု မှားယွင်းနေပါသည်။ ပြန်လည်စစ်ဆေးပါ။")
    else:
        form = LessonForm()

    # Fetch active courses to populate the dropdown menu dynamically
    courses = Course.objects.all()
    
    context = {
        'courses': courses,
        'form': form
    }
    return render(request, 'post/lesson.html', context)
    
