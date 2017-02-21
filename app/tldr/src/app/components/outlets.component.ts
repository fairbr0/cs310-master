import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { Outlet } from '../models/outlet';

@Component({
  selector: 'outlets',
  templateUrl: '../templates/outlets.component.html'
})

export class OutletsComponent implements OnInit {

  outlets : Outlet[];

  constructor (
    private articleService : ArticleService
  ) {}

  ngOnInit() : void {
    this.articleService.getOutlets().then(outlets => this.outlets = outlets);
  }
}
