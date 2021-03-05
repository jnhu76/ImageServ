# 图像处理

使用 fastapi 和 tortoise-orm 框架搭建的图像api服务，后续将设计成图像处理服务和图像搜索服务。

## 图像处理

1. 图像信息

   ```python
   info = {
     "width": 124,
     "height": 323,
     "size": 1221,
     "format": "jpeg",
     "quanlity": 80
   }
   ```

2. 图像处理

   - rotate
   - size -> width, height
     - p=1, 等比例
     - p=2, 手动处理
     - p=3, 百分比缩放
   - format: png, jpeg, git, webp
   - quality
   

## TODO

- [ ] 添加 redis，从参考[这一篇](https://blog.csdn.net/wgPython/article/details/107668521)
- [ ] 添加图像处理
- [ ] 添加celery
- [ ] 添加 dhash 计算
