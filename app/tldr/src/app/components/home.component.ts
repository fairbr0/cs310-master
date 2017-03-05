import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { Article } from '../models/Article';

@Component({
  selector: 'home',
  templateUrl: '../templates/home.component.html',
  styleUrls: ['../css/home.component.css']
})

export class HomeComponent implements OnInit {

  private articles : Article[];
  private count = 0;
  private showBack = false;
  private topArticles : Article[];

  constructor(
    private articleService : ArticleService
  ) {}

  ngOnInit() : void {
    this.getArticles();
    this.getTopArticles();
  }

  getArticles() : void {
    this.articleService.getArticles(this.count).then(response => this.setArticles(response));
  }

  getTopArticles() : void {
    this.articleService.getMostRead().then(response => this.topArticles = response);
  }

  setArticles(response) : void {
    this.count += response.length;
    if (this.count > 0) {
      this.showBack = true;
    }
    this.articles = response;
  }

  next() : void {
    this.getArticles();
  }

  back() : void {
    this.count -= 20;
    if (this.count <= 0) {
      this.count = 0;
    }
    this.getArticles();
    this.count -= 20;
    if (this.count < 0) {
      this.count = 0;
      this.showBack = false
    }
  }
}
