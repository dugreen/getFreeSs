# 获取免费ss账号脚本

### 使用手册

**需提前安装好python3,requests库,bs4库**

这个脚本是爬取 https://global.ishadowx.net 上的免费ss配置。

```shell
$ python3 getFreeSs.py
$ sslocal -c ss_config_number.json
```

之后配置网络代理即可。如果是翻墙新手可参考我之前写的一篇[博客](https://dugreen.github.io/2018/01/26/overTheWall/).

![](/img/image.png)

## tips

* **gui-config.json** debian系列ss的json配置文件格式
* **gui-config_copy.json** redhat系列ss的json配置文件格式
