import { Component } from '@angular/core';
import { GoogleMap } from '@angular/google-maps';
import { HttpClient } from '@angular/common/http';
import { Marker } from './model/marker.model';
import { Coords } from './model/coord.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'google-maps';

  center: google.maps.LatLngLiteral = {lat: 35.68051015980639, lng: 139.69876694123647};
  markerOptions! : { icon : google.maps.Icon };
  markers!: Marker[];
  zoom: number = 10;
  bottone: boolean = true

  constructor ( public http: HttpClient){

    this.markers = []
    //richiesta HTTP GET all'URL, per ottenere un array di coordinate (Coords[])
    this.http.get<Coords[]>('')
  }
}
