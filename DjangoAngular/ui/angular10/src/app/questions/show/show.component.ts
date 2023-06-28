import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
// import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent {
  // pdfUrl!: SafeResourceUrl;private sanitizer: DomSanitizer

  constructor(private service:SharedService,) { }


  @Input() que:any;
  QuestionID:string | undefined;
  Input:string | undefined;
  Response:string | undefined;
  Date:string | undefined;

  QuestionList:any=[];

  
  
  addQuestion(){
    var currentDate = new Date();
    var val = {
      QuestionID:this.QuestionID,
      Input:this.Input,
      Response: "none",
      Date:currentDate.toISOString().slice(0, 10) 
    };

    this.service.addQuestion(val).subscribe(res=>{
      alert(res.toString());
      this.refreshQuesList();
    });
  }

  deleteQuestion(item:{ QuestionID: any; }){
      if(confirm('Are you sure?')){
        this.service.deleteQuestion(item.QuestionID).subscribe(data=>{
          alert(data.toString());
          this.refreshQuesList();
        })
      }
  }

  ngOnInit(): void {
    // this.pdfUrl = this.sanitizer.bypassSecurityTrustResourceUrl('./form1500.pdf');
    this.refreshQuesList();
  }

  refreshQuesList(){
    this.service.getQuesList().subscribe(data=>{
      this.QuestionList=data;
    })
  }

}
