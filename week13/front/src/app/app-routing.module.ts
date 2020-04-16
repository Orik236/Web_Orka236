import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CompanyListComponent} from './company-list/company-list.component';
import {CompanyPageComponent} from './company-page/company-page.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { VacancyPageComponent } from './vacancy-page/vacancy-page.component';
import {CompanyVacancyListComponent} from './company-vacancy-list/company-vacancy-list.component';


const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'api/companies'},
  { path: 'api/companies', component: CompanyListComponent},
  { path: 'api/vacancies', component: VacancyListComponent},
  { path: 'api/vacancies/:vacancyId', component: VacancyPageComponent},
  { path: 'api/companies/:companyId/vacancies', component: CompanyVacancyListComponent},
  { path: 'api/companies/:companyId', component: CompanyPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
