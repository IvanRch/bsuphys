from django.shortcuts import render

def observatoryMain(request):
    return render(request, "observatoryMain.html")


def observatoryEmployee(request):
    return render(request, "observatoryEmployee.html")


def observatoryEquipment(request):
    return render(request, "observatoryEquipment.html")


def observatoryContacts(request):
    return render(request, "observatoryContacts.html")


def observatoryPopular(request):
    return render(request, "observatoryPopular.html")


def observatoryPopularLections(request):
    return render(request, "observatoryPopularLections.html")


def observatoryPublications(request):
    return render(request, "observatoryPublications.html")


def observatoryPublicationsArticle(request):
    return render(request, "observatoryPublications.html")


def observatoryPublicationsBooks(request):
    return render(request, "observatoryPublicationsBooks.html")


def observatoryPublicationsConference(request):
    return render(request, "observatoryPublications.html")


def observatoryPublicationsWiki(request):
    return render(request, "observatoryPublications.html")