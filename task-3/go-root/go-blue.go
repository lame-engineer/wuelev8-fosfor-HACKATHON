package main

import (
    "fmt"
    "net/http"
)

func helloWorld(w http.ResponseWriter, r *http.Request){
    fmt.Fprintf(w, "Hello World - internal context")
}


func main() {
    http.HandleFunc("/internal", helloWorld)
    http.ListenAndServe(":8080", nil)
}