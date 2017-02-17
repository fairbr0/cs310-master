import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Article } from '../models/article';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'article',
  templateUrl: '../templates/article.component.html',
})

export class ArticleComponent implements OnInit {

  article : Article;

  constructor (
    private articleService : ArticleService,
    private route : ActivatedRoute,
    private location: Location
  ) {}

  ngOnInit() : void {
    this.route.params
      .switchMap((params: Params) => this.articleService.getArticle(params['id']))
      .subscribe(article => this.article = article);
  }

  goBack(): void {
    this.location.back();
  }
}
