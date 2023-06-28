import { Component } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent {

  constructor(private service:SharedService) { }

  QuestionList:any=[];

  // ModalTitle:string | undefined;
  // ActivateAddEditEmpComp:boolean=false;
  // ques:any;

  ngOnInit(): void {
    this.refreshQuesList();
  }

  refreshQuesList(){
    this.service.getQuesList().subscribe(data=>{
      this.QuestionList=data;
    })
  }

  // addClick(){
  //   this.ques
  // }
}
