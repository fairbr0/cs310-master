import { Sentiment } from './sentiment';

export class Article {
  id: string;
  title : string;
  author : string;
  date : string;
  content : string;
  source : string;
  url : string;
  keywords : string[];
  sentiment : Sentiment[];
}
