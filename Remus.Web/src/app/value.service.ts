import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ValueService {

  constructor(private http: HttpClient) { }

  getValue() {
    return this.http.get("http://localhost:56042/api/getvalue");
  }

  setValue(value) {
    console.log(value)
    const headers = {'Content-Type': 'application/json'};
    this.http.post("http://localhost:56042/api/setvalue", value, {headers}).subscribe(response => {
      console.log(response.toString)
    });
  }
}
