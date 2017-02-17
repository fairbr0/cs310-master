import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';

import { AppComponent } from './components/app.component';
import { HomeComponent } from './components/home.component';
import { OutletsComponent } from './components/outlets.component';
import { SummarizeComponent } from './components/summarize.component';
import { MiniArticleComponent } from './components/mini-article.component';
import { ArticleComponent } from './components/article.component';

import { ArticleService } from './services/article.service';
import { AppRoutingModule } from './app-routing.module';


@NgModule({
  declarations: [
    AppComponent, OutletsComponent, HomeComponent, SummarizeComponent, MiniArticleComponent, ArticleComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    NgbModule.forRoot(),
    AppRoutingModule
  ],
  providers: [ ArticleService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
