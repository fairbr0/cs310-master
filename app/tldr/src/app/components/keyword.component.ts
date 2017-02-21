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

  setKeyword(keyword : string) : void {
    this.keyword = keyword;
    this.articleService.getArticlesByKeyword(0, this.keyword).then(articles => this.articles = articles);
  }

  ngOnInit() : void {
    this.route.params.subscribe((params: Params) => {
        this.setKeyword(params['id']);
      });
  }

  keyword : string;
  articles : Article[];
}
