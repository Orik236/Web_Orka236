import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TasksListComponent } from './tasks-list/tasks-list.component';
import {TaskDescriptionComponent} from './task-description/task-description.component';


const routes: Routes = [
  {path: '', redirectTo: '/tasks', pathMatch:'full'},
  {path: 'tasks', component: TasksListComponent},
  {path:'tasks/:id', component: TaskDescriptionComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
