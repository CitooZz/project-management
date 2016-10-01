import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { SigninComponent } from './signin';
import { SignupComponent } from './signup';

const APP_ROUTES: Routes = [
	{ path: '', redirectTo: '/login', pathMatch: 'full' },
	{ path: 'login', component: SigninComponent },
	{ path: 'signup', component: SignupComponent },

	// 404 URL return to login
	{ path: '**', redirectTo: 'login', pathMatch: 'full' },
]

export const APP_ROUTES_PROVIDER = RouterModule.forRoot(APP_ROUTES);