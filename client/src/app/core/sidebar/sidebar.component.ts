import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  EventEmitter,
  NgModule,
  OnInit,
  Output
} from '@angular/core';
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SidebarComponent implements OnInit {
  expanded = false;

  @Output()
  readonly toggleEvent = new EventEmitter();

  constructor(private cdr: ChangeDetectorRef) {
    //
  }

  ngOnInit(): void {
  }

  toggle(): void {
    this.expanded = !this.expanded;
    this.toggleEvent.emit(this.expanded);
    this.cdr.markForCheck();

    window.requestAnimationFrame(() => {
      window.dispatchEvent(new Event("resize"));
    });
  }
}

@NgModule({
  imports: [CommonModule],
  exports: [SidebarComponent],
  declarations: [SidebarComponent]
})
export class SidebarModule {
}
