import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SidebarComponent, SidebarModule} from './sidebar/sidebar.component';


@NgModule({
  imports: [
    CommonModule,
    SidebarModule
  ],
  exports: [SidebarComponent]
})
export class CoreModule {
}
