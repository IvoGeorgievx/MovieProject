import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [HeaderComponent, AboutComponent, HomeComponent],
  imports: [CommonModule],
  exports: [HeaderComponent, AboutComponent, HomeComponent],
})
export class CoreModule {}
