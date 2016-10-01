import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';


@Component({
  selector: 'app-signup',
  templateUrl: 'signup.component.html',
  styles: [
  `
  	ng-invalid{
  		border: 1px solid red important!;
  	}
  `
  ]
})

export class SignupComponent {
	user = {
		"username": "Haviz",
		"email": ""
	};

	onSubmit(form:NgForm){
		alert(form.value.name);
	}

}
