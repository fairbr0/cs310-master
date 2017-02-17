import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { Article } from '../models/Article';

@Component({
  selector: 'home',
  templateUrl: '../templates/home.component.html'
})

export class HomeComponent implements OnInit {

  private articles : Article[];


  constructor(
    private articleService : ArticleService
  ) {}

  ngOnInit() : void {
    this.getArticles();
  }

  getArticles() : void {
    this.articleService.getArticles(0).then(response => this.articles = response);
  }
}
