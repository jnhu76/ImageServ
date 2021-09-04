<div align="center" id="top">
       <h1>Image Serv</h1>
       <h5>Image Service Online.</h5>
   <p>
       <b>Image Serv</b> is 在线图片服务。
   </p>     
</div>

## Features

* On-time Image Processing

* Image Storage

## Quick Start

1. Get Requirements.txt

   ```shell script
    poetry export -f requirements.txt --output requirements.txt --without-hashes
   ```

1. Configure project

   ```bash
   cp .env.example .env
   ```

1.  Start service
   
    ```shell script
    # debug
    uvicorn serv.main:app --reload
    # release
    uvicorn --host=0.0.0.0 --port 8000 --loop uvloop --http h11 serv.main:app
    ```

1. Fastapi docs

   docs url: http://127.0.0.1:8080

## Api

学习采用 Thumbor 的api方式，

```bash
/hmac/trim/AxB:CxD/(adaptative-)(full-)fit-in/-Ex-F/HALIGN/VALIGN/smart/filters:FILTERNAME(ARGUMENT):FILTERNAME(ARGUMENT)/*IMAGE-URI*
```

| API | Method | Parameters | Description | Request URL | 
| ---- | ---- | ---- | ---- | ---- |
| `/api/image` | `GET` | - | connection test. | `http://127.0.0.1:8000/api/image` |
| `/api/image/{image-hash}` | `GET` |  `width` `height` `rotate` `quality` `blur` `gray` `format` | Get image with parameters. | `http://127.0.0.1:8000/api/image/8bf0ff14f2b3e63bf355aefe9788eb52?width=0&height=0&rotate=360&quality=75&blur=0&gray=false&format=WebP` |
| `/api/upload` | `GET` | - | connection test. | `http://127.0.0.1:8000/api/upload` |
| `/api/upload` | `POST` | image data | upload images. | `curl -X 'POST' 'http://127.0.0.1:8000/api/upload' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@2.png;type=image/png'` |
| `/api/info/{image-hash}` | `GET` | - | Get image info. | `http://127.0.0.1:8000/api/info/8bf0ff14f2b3e63bf355aefe9788eb52` |

## Todo_Lists

1. [Bloomfilter](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)

1. API

1. 默认值的value

## Tests

todo...

# Roadmap

1. 添加Rs支持和HTTP Raw POST。

2. 添加多种Object Storage 支持。

# License

```
MIT License

Copyright (c) 2021 jm.hu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
