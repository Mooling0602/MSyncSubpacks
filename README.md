For English users, you have to use translate tools at present.

# MSyncSubpacks
MatrixSync的子包源码仓库，不包括其他开发者制作的子包或对接MatrixSync的独立插件。

## 用法
从Release中下载，然后按正常MCDR插件加载即可。

部分插件含有额外的Pypi、MCDR依赖，可以等待其上架官方插件仓库或自行处理依赖关系。

## 设计规范
插件的元数据中，属性`id`的值应以"msync_"为开头，且必须声明依赖`matrix_sync>=2.5`；插件文件名应为MSync.<插件名称>-v<版本号>.mcdr