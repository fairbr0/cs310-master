import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Article } from '../models/article';

import 'rxjs/add/operator/toPromise';

@Injectable()

export class SummarizeService {

  private baseUrl = 'http://localhost:6200';

  constructor (
    private http : Http
  ) {}

  getSummary(content : string) : Promise<Article> {
    const url = this.baseUrl + '/summarize';
    const body = 'content='+ content;
    var headers = new Headers();
    headers.append('Content-Type', 'application/x-www-form-urlencoded');
    return this.http.post(url, body, {headers : headers}).toPromise()
      .then(response => response.json().response as Article)
      .catch(this.handleError)
  }

  private handleError(error : any) : Promise<any> {
    console.error('An error occured:', error);
    return Promise.reject(error.message || error);
  }

}
