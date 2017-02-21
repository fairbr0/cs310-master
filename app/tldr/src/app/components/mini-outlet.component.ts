import { Component, Input } from '@angular/core';
import { Outlet } from '../models/outlet';

@Component({
  selector : 'mini-outlet',
  templateUrl : '../templates/mini-outlet.component.html',
  styleUrls: ['../css/mini-outlet.component.css']
})

export class MiniOutletComponent {

  @Input() outlet : Outlet;
}
