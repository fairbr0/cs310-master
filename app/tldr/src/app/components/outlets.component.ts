import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { Outlet } from '../models/outlet';

@Component({
  selector: 'outlets',
  templateUrl: '../templates/outlets.component.html',
  styleUrls : ['../css/outlets.component.css']
})

export class OutletsComponent implements OnInit {

  outlets : Outlet[];
  originalOutlets : Outlet[]
  selectedOutlet : Outlet;
  searchTerm : string;

  constructor (
    private articleService : ArticleService
  ) {}

  selectOutlet(outlet : Outlet) : void {
    this.selectedOutlet = outlet;
  }

  searchOutlets() : void {
    var searchTerm = this.searchTerm.toLowerCase();
    this.articleService.searchOutlets(searchTerm).then(response => this.setOutlets(response));
  }

  setOutletListHeight() : void {
  }

  setOutlets(outlets : Outlet[]) : void {
    console.log(outlets);
    this.outlets = outlets;
    this.originalOutlets = outlets;
  }

  ngOnInit() : void {
    this.setOutletListHeight();
    this.articleService.getOutlets().then(outlets => this.setOutlets(outlets));
  }
}
