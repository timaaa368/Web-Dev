import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  header = [
    {
      logo:'',
      one:"Подровнее",
      two:"Корзина",
      three:'Войти'
    }
  ]
}
