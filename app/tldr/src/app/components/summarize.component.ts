import { Component } from '@angular/core';
import { Article } from '../models/article';

import { SummarizeService } from '../services/summarize.service';

@Component({
  selector : 'summarize',
  templateUrl: '../templates/summarize.component.html'
})

export class SummarizeComponent {

  content : string;
  summary : Article = new Article();

  constructor( private summarizeService : SummarizeService ) {}

  summarize() : void {
    this.summarizeService.getSummary(this.content).then(response => this.summary = response);
  }
}
