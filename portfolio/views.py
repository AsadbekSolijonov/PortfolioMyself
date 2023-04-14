from django.shortcuts import render, redirect

from portfolio.models.contact import Contact
from portfolio.models.home import Home
from portfolio.models.service import Services
from portfolio.models.my_work import MyWork
from portfolio.models.my_skill import MySkills
from portfolio.models.achievements import Achievements
from portfolio.models.about_me import AboutMe
from portfolio.models.testimonial import Testimonial
from portfolio.models.contact_info import ContactInfo


# Create your views here.
def index(request):
    home = Home.objects.first()
    services = Services.objects.all()
    my_works = MyWork.objects.all()
    my_skills = MySkills.objects.all()
    achievements = Achievements.objects.all()
    about_me = AboutMe.objects.first()
    testimonials = Testimonial.objects.all()
    contact_info = ContactInfo.objects.first()
    context = {
        'home': home,
        'services': services,
        'my_works': my_works,
        'my_skills': my_skills,
        'achievements': achievements,
        'about_me': about_me,
        'testimonials': testimonials,
        'contact_info': contact_info,
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            context = {
                'success': 'Message sent successfully!'
            }
            return redirect(to='index')

    return render(request, 'index.html', context=context)
