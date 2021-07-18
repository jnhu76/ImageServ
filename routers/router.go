package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"imageservice/routers/api"
)

func InitRouter() *gin.Engine {
	r := gin.New()

	r.Use(gin.Logger())
	r.Use(gin.Recovery())

	r.StaticFS("/upoad/images", http.Dir())

	// api settings.

	return r
}
