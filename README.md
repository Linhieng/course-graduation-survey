# course-graduation-survey
A questionnaire CS project mainly based on vue3 + express.

毕设已完成，我在该仓库中通过下面步骤进行更新：

```sh
# 首先，由于我新建了一个发布页面，所以我需要添加一个新的子模块
git submodule add -b old-main https://github.com/Linhieng/course-graduation-survey-client-publish.git client-publish

# 然后，我的客户端代码重构过三次，所以我需要修改子模块中对应的分支名
git config -f .gitmodules submodule.client.branch refactor3

# 服务端也同理，重构过一次，所以需要修改子模块的分支名
git config -f .gitmodules submodule.server.branch refactor2

# 最后，我要更新我的子模块。由于我是刚 clone 到本地仓库，所以我需要先 --init
git submodule update --init

# 如果本地已经有初始化过，则可以通过下面命令更新内容
git submodule update --init
```