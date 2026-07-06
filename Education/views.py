from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Course,Lesson
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .forms import LessonForm
from Accounts.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
@login_required
def dashboard(request):
   
    return render(request, 'dashboard/dashboard.html')
@login_required
def lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.data)
            form.save() # Saves data cleanly directly to database
            messages.success(request, "သင်ခန်းစာကို အောင်မြင်စွာ သိမ်းဆည်းပြီးပါဗျာလ်။")
            return redirect('dashboard_page')
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
    
