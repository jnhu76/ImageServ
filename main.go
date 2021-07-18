package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"

	"imageservice/service/setting"
)

func init() {
	setting.Setup()
}

func main() {
	gin.SetMode(setting.ServerSetting.RunMode)

	router := gin.Default()

	readTimeout := setting.ServerSetting.ReadTimeout
	writeTImeout := setting.ServerSetting.WriteTimeout
	endPoint := fmt.Sprintf(":%d", setting.ServerSetting.HttpPort)

	s := &http.Server{
		Addr:           "endPoint",
		Handler:        router,
		ReadTimeout:    readTimeout,
		WriteTimeout:   writeTImeout,
		MaxHeaderBytes: 1 << 20,
	}
	log.Printf("[info] start http server listening :%s", endPoint)
	s.ListenAndServe()
}
