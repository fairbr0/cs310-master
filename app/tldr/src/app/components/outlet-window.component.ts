import { Component, OnChanges, Input, SimpleChanges } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { Outlet } from '../models/outlet';
import { Article } from '../models/article';

@Component({
  selector: 'outlet-window',
  templateUrl: '../templates/outlet-window.component.html',
  styles : [`
    .central {
      position : relative;
      top: 50%;
      text-align:center;
      transform: translateY(-50%);
      -webkit-transform: translateY(-50%);
      -ms-transform: translateY(-50%);
    }
    `]
})

export class OutletWindowComponent implements OnChanges {

  @Input() outlet : Outlet;
  nothingSelected : boolean = false;
  count = 0;
  showBack : boolean = false;

  constructor(
    private articleService : ArticleService,
  ) {}

  ngOnChanges(changes : SimpleChanges ) {
    console.log(changes['outlet'].currentValue);
    if (this.outlet) {
      this.nothingSelected = true;
      this.count = 0;
      this.getArticlesByOutlet();
    }
  }

  getArticlesByOutlet() : void {
    this.articleService.getArticlesByOutlet(this.count, [this.outlet.name]).then(articles => this.setArticles(articles));
  }

  setArticles(response) : void {
    this.count += response.length;
    if (this.count > 0) {
      this.showBack = true;
    }
    for (var i = 0; i < response.length; i++) {
      response[i].date = response[i].date.split(" ")[0];
    }
    this.articles = response;
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

  articles : Article[];

}
