import {Component, OnInit} from '@angular/core';
import {Vacancy} from '../vacancy';
import {VacancyService} from '../vacancy.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-company-vacancy-list',
  templateUrl: './company-vacancy-list.component.html',
  styleUrls: ['./company-vacancy-list.component.css']
})
export class CompanyVacancyListComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    const companyId = +this.route.snapshot.paramMap.get('companyId');
    this.getVacancies(companyId);
  }

  getVacancies(companyId: number) {
    this.vacancyService.getCompanyVacancies(companyId).subscribe(vacancies => this.vacancies = vacancies);
  }

}