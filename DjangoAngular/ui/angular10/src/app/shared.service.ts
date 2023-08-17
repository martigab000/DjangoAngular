import { JsonPipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, tap, interval, startWith, distinctUntilChanged, map } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://192.168.1.156:8000";
// readonly APIUrl = "192.168.70.162:1436"
private previousValue: any;
// readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http:HttpClient) { }

  private _refreshrequired=new Subject<void>();

  get Refreshrequired(){
    return this._refreshrequired;
  }

  updateQuestion(val:any){
    return this.http.put(this.APIUrl + '/question/',val);
  }

  getOneQues(val:any){
    return this.http.get(this.APIUrl + '/question/'+val);
  }

  deleteQuestion(val:any){
    return this.http.delete(this.APIUrl + '/question/'+val);
  }

  getQuesList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/question/');
  }

  addQuestion(val:any){
    return this.http.post(this.APIUrl + '/question/',val).pipe(
      tap(()=>{
        this.Refreshrequired.next();
      })
    );
  }


}
