import { Component, OnInit } from '@angular/core';
import {VacancyService} from '../vacancy.service';
import {Vacancy} from '../vacancy';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies(){
    this.vacancyService.getVacancies().subscribe(vacancies=>{
      this.vacancies = vacancies
    });
  }

}
