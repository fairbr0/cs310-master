import { Component, Input} from '@angular/core';
import { Article } from '../models/article';

@Component({
  selector: 'mini-article',
  templateUrl: '../templates/mini-article.component.html',
  styleUrls: ['../css/mini-article.component.css']
})

export class MiniArticleComponent {

  @Input() article : Article;
}
