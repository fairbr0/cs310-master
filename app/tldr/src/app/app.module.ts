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
import { OutletComponent } from './components/outlet.component';
import { MiniOutletComponent } from './components/mini-outlet.component';
import { KeywordsComponent } from './components/keywords.component';
import { KeywordComponent } from './components/keyword.component';
import { FooterComponent } from './components/footer.component';
import { OutletWindowComponent } from './components/outlet-window.component';

import { ArticleService } from './services/article.service';
import { SummarizeService } from './services/summarize.service';
import { AppRoutingModule } from './app-routing.module';


@NgModule({
  declarations: [
    AppComponent,
    OutletsComponent,
    HomeComponent,
    SummarizeComponent,
    MiniArticleComponent,
    ArticleComponent,
    MiniOutletComponent,
    OutletComponent,
    KeywordsComponent,
    KeywordComponent,
    FooterComponent,
    OutletWindowComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    NgbModule.forRoot(),
    AppRoutingModule
  ],
  providers: [ ArticleService, SummarizeService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
