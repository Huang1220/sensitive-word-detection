# sensitive-word-detection

Sensitive word detection - 敏感词检测

---
**由于很多网友反馈该项目bug较多，检测强度较大，检测太过于严格，该项目将会列入近两个月的排期进行更新修改**

**即将推出大版本更新，敬请期待**

---

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
