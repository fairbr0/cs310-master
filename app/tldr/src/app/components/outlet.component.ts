import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Outlet } from '../models/outlet';
import { Article } from '../models/article';

import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'outlet',
  templateUrl: '../templates/outlet.component.html'
})

export class OutletComponent implements OnInit {

  constructor(
    private articleService : ArticleService,
    private route : ActivatedRoute,
    private location : Location
  ) {}

  goBack() : void {
    this.location.back();
  }

  getArticlesByOutlet() : void {
    this.articleService.getArticlesByOutlet(this.count, [this.outlet.name]).then(articles => this.setArticles(articles));
  }

  setArticles(articles) : void {
    this.count += articles.length;
    if (this.count > 0) {
      this.showBack = true;
    }
    this.articles = articles;
  }

  setOutlet(outlet : Outlet) : void {
    this.outlet = outlet;
    this.getArticlesByOutlet();
  }

  next() : void {
    this.getArticlesByOutlet();
  }

  back() : void {
    this.count -= 20;
    if (this.count <= 0) {
      this.count = 0;
    }
    this.getArticlesByOutlet();
    this.count -= 20;
    if (this.count < 0) {
      this.count = 0;
      this.showBack = false
    }
  }

  ngOnInit() : void {
    this.outletname = this.route.params['id'];
    this.route.params
      .switchMap((params: Params) => this.articleService.getOutlet(params['id']))
      .subscribe(outlet => this.setOutlet(outlet));
  }

  outlet : Outlet;
  articles : Article[];
  outletname : string;
  count = 0;
  showBack : boolean = false;

}
