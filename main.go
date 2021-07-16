package main

import (
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func init() {

}

func main() {
	router := gin.Default()

	s := &http.Server{
		Addr:           ":8080",
		Handler:        router,
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}
	log.Printf("[info] start http server listening %s", endpoint)
	s.ListenAndServe()
}
