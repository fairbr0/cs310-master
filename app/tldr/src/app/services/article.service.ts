import { Injectable } from '@angular/core';
import { Article } from '../models/article';
import { Outlet } from '../models/outlet';

import { ARTICLES } from '../resources/dummy/articles';
import { OUTLETS } from '../resources/dummy/outlets';

@Injectable()
export class ArticleService {

  getArticles(id:number) : Promise<Article[]> {
    return Promise.resolve(ARTICLES);
  }

  getOutlets() : Promise<Outlet[]> {
    return Promise.resolve(OUTLETS);
  }

  getArticle(id:string) : Promise<Article> {
    var article : Article;
    for (var i = 0; i < ARTICLES.length; i++) {
      if (ARTICLES[i]['id'] == id) {
        article = ARTICLES[i];
      }
    }
    return Promise.resolve(article);
  }

}
