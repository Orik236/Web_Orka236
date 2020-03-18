import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { TASKS } from './mock-tasks';
import { Task } from './task';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  getTasks(): Observable<Task[]>{
    return of(TASKS);
  }

  getTask(id: number): Observable<Task>{
    return of(TASKS.find(task=>task.id===id));
  }

  constructor() { }
}
