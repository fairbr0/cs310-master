import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Outlet } from '../models/outlet';
import { Article } from '../models/article';

import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'outlet',
  templateUrl: '../templates/keyword.component.html'
})

export class KeywordComponent implements OnInit {

  constructor(
    private articleService : ArticleService,
    private route : ActivatedRoute,
    private location : Location
  ) {}

  goBack() : void {
    this.location.back();
  }

  setArticles(articles : Article[]) {
    this.articles = articles;
    if (articles.length > 0) {
      this.keywordExists = true;
    }
    this.count += articles.length;
    if (this.count > 0) {
      this.showBack = true;
    }
  }

  getArticlesByKeyword() : void {
    this.articleService.getArticlesByKeyword(this.count, this.keyword).then(articles => this.setArticles(articles));

  }

  setKeyword(keyword : string) : void {
    this.keyword = keyword;
    this.keywordExists = true;
    this.getArticlesByKeyword();
  }

  ngOnInit() : void {
    this.route.params.subscribe((params: Params) => {
        this.setKeyword(params['id']);
      });
  }


  next() : void {
    this.getArticlesByKeyword();
  }

  back() : void {
    this.count -= 20;
    if (this.count <= 0) {
      this.count = 0;
    }
    this.getArticlesByKeyword();
    this.count -= 20;
    if (this.count < 0) {
      this.count = 0;
      this.showBack = false
    }
  }

  keyword : string;
  articles : Article[];
  keywordExists : boolean = false;
  count = 0;
  showBack : boolean = false;
}
