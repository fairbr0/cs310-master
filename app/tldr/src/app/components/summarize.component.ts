import { Component } from '@angular/core';
import { Article } from '../models/article';

import { ArticleService } from '../services/article.service';

@Component({
  selector : 'summarize',
  templateUrl: '../templates/summarize.component.html'
})

export class SummarizeComponent {

  constructor( private articleService : ArticleService ) {}
}
