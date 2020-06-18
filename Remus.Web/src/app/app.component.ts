import { Component } from '@angular/core';
import { ValueService } from './value.service';
import { FormControl } from '@angular/forms'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private valueService: ValueService) {}
  formValue = new FormControl();
  value;
  title = 'frontend';

  ngOnInit() {
    this.getValue();
  }

  getValue(): void {
    this.valueService.getValue().subscribe(
      response => {
        this.value = response;
      }
    );
  }

  setValue(): void {
    console.log("call1")
    this.valueService.setValue(this.formValue.value);
  }
}
