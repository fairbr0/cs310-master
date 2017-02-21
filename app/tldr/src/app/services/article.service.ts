import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Article } from '../models/article';
import { Outlet } from '../models/outlet';

import { ARTICLES } from '../resources/dummy/articles';
import { OUTLETS } from '../resources/dummy/outlets';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class ArticleService {

  private articleBaseUrl = 'http://localhost:5200';

  constructor (
    private http : Http
  ) {}

  getArticles(id:number) : Promise<Article[]> {
    //return Promise.resolve(ARTICLES);
    const url = this.articleBaseUrl + '/getrecent/' + id;
    return this.http.get(url).toPromise()
      .then(response => response.json().response.articles as Article[])
      .catch(this.handleError);
  }

  getOutlets() : Promise<Outlet[]> {
    //return Promise.resolve(OUTLETS);
    const url = this.articleBaseUrl + '/outlets';
    return this.http.get(url).toPromise()
      .then(response => response.json().outlets as Outlet[])
      .catch(this.handleError);
  }

  getArticle(id:string) : Promise<Article> {
    const url = this.articleBaseUrl + '/article/' + id;
    return this.http.get(url).toPromise()
      .then(response => response.json().response as Article)
      .catch(this.handleError);
  }

  getArticlesByOutlet(id:number, outlet:string) {
    const url = this.articleBaseUrl + '/outlet/' + outlet + '/' + id;
    return this.http.get(url).toPromise()
      .then(response => response.json().response.articles as Article[])
      .catch(this.handleError);
  }

  getOutlet(id:string) : Promise<Outlet> {
    var outlet : Outlet;
    for (var i = 0; i < OUTLETS.length; i++) {
      if (OUTLETS[i]['name'] == id) {
        outlet = OUTLETS[i];
      }
    }
    return Promise.resolve(outlet);
  }

  getArticlesByKeyword(count:number, id : string) : Promise<Article[]> {
    const url = this.articleBaseUrl + '/keywords/' + id;
    return this.http.get(url).toPromise()
      .then(response => response.json().response.articles as Article[])
      .catch(this.handleError);
  }

  getKeywords() : Promise<string[]> {
    const url = this.articleBaseUrl + '/keywords';
    return this.http.get(url).toPromise()
      .then(response => response.json().response.keywords as string[])
      .catch(this.handleError);
  }

  private handleError(error : any) : Promise<any> {
    console.error('An error occured:', error);
    return Promise.reject(error.message || error);
  }

}
