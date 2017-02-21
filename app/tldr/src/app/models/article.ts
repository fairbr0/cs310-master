import { Sentiment } from './sentiment';

export class Article {
  _id: string;
  title : string;
  author : string;
  date : string;
  content : string;
  source : string;
  url : string;
  keywords : string[];
  sentiment : Sentiment[];
  reduction : number;
}
