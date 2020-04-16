import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {CompanyService} from '../company.service';
import {Company} from '../company';
import {VacancyService} from '../vacancy.service';

@Component({
  selector: 'app-company-page',
  templateUrl: './company-page.component.html',
  styleUrls: ['./company-page.component.css']
})
export class CompanyPageComponent implements OnInit {
  company: Company;

  constructor(private companyService: CompanyService, 
    private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany(){
    const id = +this.route.snapshot.paramMap.get('companyId');

    this.companyService.getCompany(id).subscribe(company=>this.company=company);
  }
}