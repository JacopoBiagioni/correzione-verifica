import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'google-maps';

  center : google.maps.LatLngLiteral = { lat: 40.70840010689748, lng: -74.04284125121363}

  constructor ( public http:HttpClient ) {
  


  }


  this.http.get<Prova[]>("https://5000-jacopobiagi-correzionev-uo2zf51dfx6.ws-eu97.gitpod.io/all").subscribe(data =>{
     
    })



}
