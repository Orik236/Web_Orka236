import { Injectable } from '@angular/core';
import { CATEGORIES } from './categories'
import { Observable, of } from 'rxjs';
import { Category } from './category';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {
  getCategories(): Observable<Category[]>{
    return of(CATEGORIES);
  }
  constructor() { }
}
