from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("template/", views.templates, name="index"),
    path("dekanat/", views.dekanat, name="index"),
    path("spec/", views.spec, name="specialization"),
    path("abitur/", views.abitur, name="abitur"),
    path("info/", views.info, name="info"),
    path("alums/", views.alums_list, name="alums_list"),
    path("alums/<slug:alum>/", views.alum_detail, name="alum_detail",),
    path("faculty/", views.faculty, name="faculty"),
    path("enter/", views.enter, name="enter"),
    path("cooperation/", views.cooperation, name="cooperation"),
    path("science/", views.science, name="science"),
    path("education/", views.education, name="education"),
    path("contacts/", views.contacts, name="contacts"),
    path("departments/", views.departments, name="departments"),
    path("council/", views.council, name="council"),
    path("one-window/", views.oneWindow, name="one window"),
    path("map/", views.mapApi, name="map"),
    path("faculty/documents/", views.NwordDocuments, name="documents"),
    path("worldwide/", views.internationalConnection, name="international"),
    re_path(r".+/language_en", views.language_switch_en, name="language_en"),
    re_path(r".+/language_ru", views.language_switch_ru, name="language_ru"),
    path("en_main/", views.language_switch_en_main, name="lang_en_main"),
    path("ru_main/", views.language_switch_ru_main, name="lang_ru_main"),
    path("time/", views.timetable, name="info"),
    path("time/mag/", views.timetableMag, name="info"),
    path("time-exams/", views.timetableExams, name="info"),
    path("mezzija/", views.timofey, name="info"),
    path("edi/", views.edi, name="info"),
    path("ckp/", views.ckpMain, name="ckp"),
    path("ckp/lines-of-researches/", views.linesOfResearches, name="ckp"),
    path("ckp/measurement-procedures/", views.measurementProcedures, name="ckp"),
    path("ckp/equipment/", views.equipment, name="ckp"),
    path("ckp/contacts/", views.contactsCKP, name="ckp"),
    path("ckp/scientific-services/", views.scientificServices, name="ckp"),
    path("key-pub/", views.keyPublicationsListAll, name="info"),
    path("conferences/", views.conferences, name="conferences"),
    path("science-directions/", views.nilAndScienceDirections, name="info"),
    path("edu-proc/", views.eduProcess, name="info"),
    path("test/", views.test, name="info"),
    path("dod/", views.dod, name="dod"),
    path("second-stage/", views.secondStage, name="second stage"),
    path("aver/", views.servicePage, name="service"),
    path("olimp2021/", views.studOlimp2021, name="service"),
    path("abiturOlimp2021/", views.abiturOlimp2021, name="service"),
    path("raspred/", views.raspred, name="raspred"),
    path("wellcome/", views.wellcome, name="raspred"),
    path("tutor/", views.tutor, name="raspred"),
    path("educations/", views.educations, name="raspred"),
    path("services/", views.services, name="raspred"),
    path("wbg-project/", views.worldbank, name="raspred"),
    path("educations/build-squad/", views.build_squad, name="build-squad"),
    path("aboba/", views.aboba, name="aboba"),
    path("educations/trade-union/", views.tradeUnion, name="trade union"),
    path("developments/", views.development, name="development"),
]
