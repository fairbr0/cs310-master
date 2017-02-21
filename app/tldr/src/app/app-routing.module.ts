import { NgModule }      from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

/*import any components to route to here */
import { HomeComponent } from './components/home.component';
import { OutletsComponent } from './components/outlets.component';
import { SummarizeComponent } from './components/summarize.component';
import { ArticleComponent } from './components/article.component';
import { OutletComponent } from './components/outlet.component';
import { KeywordsComponent } from './components/keywords.component';
import { KeywordComponent } from './components/keyword.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  /*add in any extra paths here*/
  { path: 'home', component: HomeComponent },
  { path: 'outlets', component: OutletsComponent },
  { path: 'summarize', component: SummarizeComponent },
  { path: 'article/:id', component: ArticleComponent },
  { path: 'outlet/:id', component: OutletComponent },
  { path: 'keywords', component: KeywordsComponent },
  { path: 'keyword/:id', component: KeywordComponent}

];

@NgModule({
    imports:      [ RouterModule.forRoot(routes)],
    exports:      [ RouterModule]
})
export class AppRoutingModule { }
