package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"imageservice/service/upload"

	"imageservice/routers/api"
)

func InitRouter() *gin.Engine {
	r := gin.New()

	r.Use(gin.Logger())
	r.Use(gin.Recovery())

	r.StaticFS("/upoad/images", http.Dir(upload.GetImageFullPath()))

	r.POST("/upload", api.UploadImage)

	// api settings.

	return r
}
