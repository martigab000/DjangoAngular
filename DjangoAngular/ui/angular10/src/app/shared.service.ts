import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, tap } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000";
// readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http:HttpClient) { }

  private _refreshrequired=new Subject<void>();

  get Refreshrequired(){
    return this._refreshrequired;
  }

  getDepList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/department/');
  }

  addDepartment(val:any){
    return this.http.post(this.APIUrl + '/department/',val);
  }

  updateDepartment(val:any){
    return this.http.put(this.APIUrl + '/department/',val);
  }

  deleteDepartment(val:any){
    return this.http.delete(this.APIUrl + '/department/'+val);
  }


  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

  addEmployee(val:any){
    return this.http.post(this.APIUrl + '/employee/',val);
  }

  updateQuestion(val:any){
    return this.http.put(this.APIUrl + '/question/',val);
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

  updateEmployee(val:any){
    return this.http.put(this.APIUrl + '/employee/',val);
  }

  deleteEmployee(val:any){
    return this.http.delete(this.APIUrl + '/employee/'+val);
  }

  // UploadPhoto(val:any){
  //   return this.http.post(this.APIUrl+'/SaveFile',val);
  // }

  getAllDepartmentNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/department/');
  }


}
