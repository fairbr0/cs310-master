import { Component, OnInit } from '@angular/core';
import { ArticleService } from '../services/article.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import { Article } from '../models/article';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'article',
  templateUrl: '../templates/article.component.html',
  styleUrls : ['../css/article.component.css']
})

export class ArticleComponent implements OnInit {

  article : Article;
  hasRated : boolean = false;
  vote : string = 'True';
  percentgood = 0;
  percentbad = 0;

  constructor (
    private articleService : ArticleService,
    private route : ActivatedRoute,
    private location: Location
  ) {}

  setArticle(article : Article) {
    this.article = article;
    const totalVotes = article.positivevotes + article.negativevotes;
    if (totalVotes > 0) {
      this.percentgood = Number((article.positivevotes / totalVotes).toFixed(4)) * 100;
      this.percentbad =  Number((article.negativevotes / totalVotes).toFixed(4)) * 100;
    }
    this.article.date = this.article.date.split(" ")[0];
    this.article.reduction = Number((this.article.reduction * 100).toFixed(2));
  }


  ngOnInit() : void {
    this.route.params
      .switchMap((params: Params) => this.articleService.getArticle(params['id']))
      .subscribe(article => this.setArticle(article));
  }

  goBack(): void {
    this.location.back();
  }

  submitRating() : void {
    this.hasRated = true;
    this.articleService.putArticleRating(this.article._id, this.vote);
  }


}
