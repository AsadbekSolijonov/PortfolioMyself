from django.contrib import admin
from portfolio.models.home import Home
from portfolio.models.service import Services
from portfolio.models.my_work import MyWork
from portfolio.models.my_skill import MySkills
from portfolio.models.testimonial import Testimonial
from portfolio.models.achievements import Achievements
from portfolio.models.about_me import AboutMe
from portfolio.models.contact import Contact
from portfolio.models.contact_info import ContactInfo

admin.site.register([Home, Services, MyWork, MySkills, Testimonial, Achievements, AboutMe, Contact, ContactInfo])
