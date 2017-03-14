import { Sentiment } from './sentiment';

export class Article {
  _id: string;
  title : string;
  positivevotes : number;
  negativevotes : number;
  author : string;
  date : string;
  content : string;
  source : string;
  img_url: string;
  url : string;
  keywords : string[];
  sentiment : Sentiment[];
  reduction : number;
  positive : number;
}
