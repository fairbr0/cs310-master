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

  setOutlet(outlet : Outlet) : void {
    this.outlet = outlet;
    this.articleService.getArticlesByOutlet(0, this.outlet.name).then(articles => this.articles = articles);
  }

  ngOnInit() : void {
    this.route.params
      .switchMap((params: Params) => this.articleService.getOutlet(params['id']))
      .subscribe(outlet => this.setOutlet(outlet));
  }

  outlet : Outlet;
  articles : Article[];
}
