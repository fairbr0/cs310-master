import { Component, OnInit } from '@angular/core';
import { Article } from '../models/article';
import { ArticleService } from '../services/article.service';


@Component({
  selector: 'keywords',
  templateUrl: '../templates/keywords.component.html',
  styleUrls : ['../css/keywords.component.css']
})

export class KeywordsComponent implements OnInit {

  constructor (
    private articleService : ArticleService
  ) {}

  setKeywords(keywords : string[]) : void {
    this.keywords = keywords;
    this.originalKeywords = keywords;
  }

  getKeywords() {
    this.articleService.getKeywords().then(keywords => this.setKeywords(keywords));
  }

  ngOnInit() : void {
    this.getKeywords();
  }

  searchKeywords() : void {
    var searchTerm = this.searchTerm.toLowerCase();
    if (searchTerm != "") {
      this.articleService.searchKeywords(searchTerm).then(keywords => this.setKeywords(keywords));
    } else {
      this.articleService.getKeywords().then(keywords => this.setKeywords(keywords));
    }
  }

  keywords : string[];
  originalKeywords : string[];
  selectedKeyword : string;
  searchTerm : string;

}
