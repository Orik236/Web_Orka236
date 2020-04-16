import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompanyListComponent } from './company-list/company-list.component';
import { CompanyPageComponent } from './company-page/company-page.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { VacancyPageComponent } from './vacancy-page/vacancy-page.component';
import { CompanyVacancyListComponent } from './company-vacancy-list/company-vacancy-list.component';

@NgModule({
  declarations: [
    AppComponent,
    CompanyListComponent,
    CompanyPageComponent,
    VacancyListComponent,
    VacancyPageComponent,
    CompanyVacancyListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
