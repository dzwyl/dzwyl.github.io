<p>1-1-1 HTTP基本原理
URI Uniform Resourse Identifier 统一资源标识符
URL --Locator  统一资源定位符
URN --Name 统一资源名称
scheme：//[username:password@]hostname[:port][/path][;parameters][?query][#fragment]
scheme协议 常用http、https、ftp
hostname 主机地址  port 端口  path 路径  paraments 参数  query 查询  fragment 片段

1-1-2 HTTP Hypertext Transfer Protocol  超文本传输协议
HTTPS 在HTTP下加入SSL层加密  客户端给请求request--服务器给响应response
name：请求的名称，一般用URL的最后一部分作为名称    Status：响应的状态码，200正常   Protocol：请求的协议类型  type：

1-1-4请求
方法：get：请求的参数包含在url里，最多1024字节
post：数据通过表单形式传输，包含在请求体中
请求头：cookie辨别用户进行会话跟踪存储在用户本地的数据
Referer:标识请求从哪个页面发过来的，做源统计和防盗链处理
User-agent：操作系统，浏览器版本，伪装成浏览器

1-1-5响应response
响应状态码，响应头，响应体  200成功，404未找到
响应头：包含服务器对请求的应答信息，爬虫要解析的内容就是响应体在preview中

1-2-1 web网页基础
三部分 1.HTML骨架 2.CSS皮肤 Cascading Style Sheets 3.JAVAScript肌肉,交互动画效果

1-2-2网页结构

1-3爬虫基本原理
获取网页-提取数据-分析数据-保存数据 

1-4 session和cookie
1-4-1静态网页和动态网页