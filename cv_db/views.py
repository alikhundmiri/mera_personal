from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import document_data


def resume(request):
    today = timezone.now().date()
    experiance_list = document_data.objects.iee()
    almamater_list = document_data.objects.alma()
    achievement_list = document_data.objects.achievements()
    aoi_list = document_data.objects.aoi()
    eduactiv_list = document_data.objects.eduActiv()
    skill_list = document_data.objects.skill()
    lectures_list = document_data.objects.lectures()
    books_list = document_data.objects.books()
    special_list = document_data.objects.special()
    competition_list = document_data.objects.competition()
    f13_list = document_data.objects.blank1()
    f14_list = document_data.objects.blank2()

    context = {
        # "website": website_list,
        "today":today,
        "experience": experiance_list,
        "almamater": almamater_list,
        "achievement":achievement_list,
        'aoi':aoi_list,
        "eduActiv":eduactiv_list,
        "skill":skill_list,
        "lecture":lectures_list,
        "books":books_list,
        "special":special_list,
        "competition":competition_list,
        "f13":f13_list,
        "f14":f14_list
    }
    return render(request, 'cv_db/resume.html', context)


def cv(request):
    today = timezone.now().date()
    experiance_list = document_data.objects.iee()
    almamater_list = document_data.objects.alma()
    achievement_list = document_data.objects.achievements()
    aoi_list = document_data.objects.aoi()
    eduactiv_list = document_data.objects.eduActiv()
    skill_list = document_data.objects.skill()
    lectures_list = document_data.objects.lectures()
    books_list = document_data.objects.books()
    special_list = document_data.objects.special()
    competition_list = document_data.objects.competition()
    f13_list = document_data.objects.blank1()
    f14_list = document_data.objects.blank2()

    context = {
        # "website": website_list,
        "today": today,
        "experience": experiance_list,
        "almamater": almamater_list,
        "achievement": achievement_list,
        'aoi': aoi_list,
        "eduActiv": eduactiv_list,
        "skill": skill_list,
        "lecture": lectures_list,
        "books": books_list,
        "special": special_list,
        "competition": competition_list,
        "f13": f13_list,
        "f14": f14_list
    }
    return render(request, 'cv_db/cv.html', context)
