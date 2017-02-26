import { Component } from '@angular/core';
import { Article } from '../models/article';

import { SummarizeService } from '../services/summarize.service';

@Component({
  selector : 'summarize',
  templateUrl: '../templates/summarize.component.html',
  styleUrls : ['../css/summarize.component.css']
})

export class SummarizeComponent {

  content : string;
  summary : Article = new Article();
  isLoading : boolean = false;

  constructor( private summarizeService : SummarizeService ) {}

  formatReduction(reduction) : number {
    var num = Number(reduction.toFixed(2));
    return num;
  }

  finishedLoad(response) {
    this.summary = response;
    this.isLoading = false;
    this.summary.reduction = this.formatReduction(this.summary.reduction)
  }

  summarize() : void {
    this.isLoading = true;
    this.summarizeService.getSummary(this.content).then(response => this.finishedLoad(response));
  }

  clear() : void {
    this.summary = new Article();
    this.content = "";
  }
}
