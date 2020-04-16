import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {VacancyService} from '../vacancy.service';
import {Vacancy} from '../vacancy';

@Component({
  selector: 'app-vacancy-page',
  templateUrl: './vacancy-page.component.html',
  styleUrls: ['./vacancy-page.component.css']
})
export class VacancyPageComponent implements OnInit {
  vacancy: Vacancy;

  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancy();
  }

  getVacancy(){
    const id = +this.route.snapshot.paramMap.get('vacancyId');
    
    this.vacancyService.getVacancy(id).subscribe(vacancy=>this.vacancy=vacancy);
  }

}
