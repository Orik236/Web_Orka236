from api.models import Company, Vacancy
from django.http.response import JsonResponse

def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.short() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'company post request'})

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error', str(e)})
    if request.method == 'GET':
        return JsonResponse(company.to_json())

def company_vacancies(request, id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id = id).all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancy post request'})

def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.short() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'vacancy post request'})


def vacancy_description(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

def top_ten_vacancy(request):
    vacancies = Vacancy.objects.order_by("-salary")
    lenght = min(10, len(vacancies))
    vacancies_json = [vacancies[i].to_json() for i in range(lenght)]
    return JsonResponse(vacancies_json, safe=False)