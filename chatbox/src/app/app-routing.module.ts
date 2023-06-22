//esponsible for configuring the routing module in your Angular application.
import { NgModule } from '@angular/core'; // It is used to define Angular modules.
import { RouterModule, Routes } from '@angular/router'; //They are used for configuring and defining routes in Angular applications.

const routes: Routes = []; //This array will be used to define the routes for your application.

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
//Overall, this code sets up the routing module in your Angular application and provides a placeholder for defining your routes.
