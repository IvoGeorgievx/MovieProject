import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { UserModule } from '../user/user.module';
import { UserRoutingModule } from '../user/user-routing.module';

@NgModule({
  declarations: [HeaderComponent, AboutComponent, HomeComponent],
  imports: [CommonModule, UserModule, UserRoutingModule],
  exports: [HeaderComponent, AboutComponent, HomeComponent],
})
export class CoreModule {}
