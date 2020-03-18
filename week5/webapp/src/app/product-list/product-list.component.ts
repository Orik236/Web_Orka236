import { Component } from '@angular/core';
import { products } from '../products';
import { CategoriesService } from '../categories.service';
import { Category } from '../category'
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent {
  products = products;
  categories: Category[];
  selectedCategory: Category = {
    category:'all'
  };

  getCategories(): void{
    this.categoriesService.getCategories().subscribe(categories => this.categories=categories)
  }

  share() {
    window.alert('The product has been shared!');
  }

  constructor(private categoriesService: CategoriesService, private activateRoute: ActivatedRoute){ }

  ngOnInit(){
    this.getCategories();
    this.activateRoute.paramMap.subscribe(params=>{
      this.selectedCategory.category = params.get('category');
    })
  }
}