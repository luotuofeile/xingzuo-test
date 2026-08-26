# 把「隐藏星座能量」测试托管到 GitHub Pages（免费，0 元）

本目录已备好可直接上传的文件：
- `index.html` —— 测试主页（自包含，无需任何额外资源）

---

## 一、创建仓库（1 分钟）
1. 登录 [github.com](https://github.com)，右上角 **+ → New repository**。
2. **Repository name** 随便起，建议：`xingzuo-test`（英文名，别用中文）。
3. 可见性选 **Public**。
4. 其他默认，**Create repository**。

## 二、上传文件（1 分钟）
- 进仓库后点 **uploading an existing file**，把本目录里的 `index.html` 拖进去；
- 也可把 `README.md` 一起传上（可选）；
- 底部 **Commit changes** 提交。

## 三、开启 Pages（1 分钟）
1. 仓库顶部点 **Settings → Pages**（左侧边栏）。
2. **Source** 选 **Deploy from a branch**；
3. **Branch** 选 **main**，**文件夹** 选 **/ (root)**；
4. **Save**。
5. 等 **1–2 分钟**，页面会显示你的访问地址，形如：
   `https://你的用户名.github.io/xingzuo-test/`

> 直接打开这个地址，就能测了。手机浏览器同样可用。

## 四、接进公众号（你已有菜单配置文档）
把上面这个 `https://用户名.github.io/xingzuo-test/` 链接，填进公众号后台
「自定义菜单 → 测一测」的跳转网址即可。

---

## 重要提醒（微信环境）
- **微信内打开外链会被拦截**：用户从公众号菜单点进来一般能直接开；但若从聊天里点，
  微信可能提示「在浏览器打开」。属微信正常限制，不是 GitHub 的问题。
- 如果想让体验更顺，可在结果页引导「点击右上角 ··· 在浏览器打开 / 收藏」。
- **自定义域名**：GitHub Pages 支持免费绑定自己的域名（需你会配 DNS），不绑定也完全够用。

## 更新内容怎么办
改完 `index.html` 后重新上传覆盖、或 `Commit` 新版本即可，Pages 会自动重新部署（通常几十秒）。
