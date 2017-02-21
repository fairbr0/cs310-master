import { Component, OnInit } from '@angular/core';
import { Article } from '../models/article';
import { ArticleService } from '../services/article.service';


@Component({
  selector: 'keywords',
  templateUrl: '../templates/keywords.component.html'
})

export class KeywordsComponent implements OnInit {

  constructor (
    private articleService : ArticleService
  ) {}

  getKeywords() {
    this.articleService.getKeywords().then(keywords => this.keywords = keywords);
  }

  ngOnInit() : void {
    this.getKeywords();
  }

  keywords : string[]

}
