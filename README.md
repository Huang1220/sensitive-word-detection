# sensitive-word-detection

Sensitive word detection - 敏感词检测

附有词库大约5W

python库依赖：
- jieba
- flask

可以随意修改

默认跑起来服务位于http://127.0.0.1:81/api/check

传参: http://127.0.0.1:81/api/check?input=content

返回示例: 
~~~json
{
  "divide" : "哈哈",
  "pass" : true,
  "time" : 0.00537023871
}
~~~
