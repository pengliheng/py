# pyhton+AST 实现 rule engine 调研

## preprocess

1. warp_function
  在 code 外层嵌套一个函数, 用于实现 code 中的 return
2. un_warp_function
  去掉 code 外层嵌套的函数
3. add_field_declaration
  将 field 变量提取到顶部
4. remove_field_declaration
  删除顶部 field 变量

## engine

1. isIncluded 函数

## bug

1. Python 不能有多余缩进
