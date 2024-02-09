from django.shortcuts import render, redirect
from .models import Package, Place
from django.http import HttpResponse

def tour(request):
    if request.method == 'POST':
        # Get form data from POST request
        package_name = request.POST.get('packageName')
        rate = request.POST.get('rate')
        date_from = request.POST.get('dateFrom')
        date_to = request.POST.get('dateTo')
        contact_number = request.POST.get('contactNumber')

        # Create a new Package object and save it to the database
        new_package = Package(
            name=package_name,
            rate=rate,
            date_from=date_from,
            date_to=date_to,
            contact_no=contact_number
        )
        new_package.save()

        # Redirect to the same page after adding the package
        return redirect('tour')
    data= Package.objects.all()

    # If it's not a POST request, render the page
    return render(request, 'page1.html',{'data':data})

def add(request,key):
    package=Package.objects.get(pk=key)

    if request.method == 'POST':
        # Get the list of place names from the POST data
        places = request.POST.getlist('places')
        print(places)
        for place_name in places:
            # Check if a place with the same name already exists for the current package
            existing_place = Place.objects.filter(package=package, name=place_name).first()

            if not existing_place:
                # If the place doesn't exist, create a new record
                new_place = Place(package=package, name=place_name)
                new_place.save()
    places=Place.objects.filter(package=package)
    return render(request,'page2.html',{'package':package,'places':places})
