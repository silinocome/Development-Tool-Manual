.. role:: raw-html-m2r(raw)
   :format: html


GitPractice
===========

`查看annotation <https://www.jetbrains.com/help/pycharm/investigate-changes.html#annotate_blame>`_
------------------------------------------------------------------------------------------------------


* 
  `for pycharm <https://www.jetbrains.com/help/pycharm/investigate-changes.html#annotate_blame>`_

* 
  命令行

.. prompt:: bash $,# auto

   $ git blame <file_name>

登录
----

设置\ `access token <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token>`_\ (PAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210929101344512.png
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210929101344512.png
   :alt: image-20210929101344512


.. note:: 注意若登录失效，或检查一下token是否过期


`github ssh免密登录 <https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh/checking-for-existing-ssh-keys>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

http使用push和pull都需要显式在命令行输入口令（账号、密码），ssh则不用


* 或涉及的命令行操作

.. prompt:: bash $,# auto

   # 显示现有ssh密钥（公钥后缀为pub）
   $ ls -al ~/.ssh
   # 生成新ssh密钥（可以不加-t，默认选项为rsa）
   $ ssh-keygen -t ed25519 -C "github电子邮件地址"


* `添加ssh公钥于github <https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_
* 测试git hub ssh连接

.. prompt:: bash $,# auto

   $ ssh -T git@github.com

Hook
----


* git ``hook``\ 是一个脚本（bash或者python均可），是执行一些git的操作前或者操作后需要运行的脚本
* ``hook``\ 可以根据触发的时机分为两类：客户端(clien-side)或者服务端(server-side)，前者如git commit/merge，后者如服务端接收到推送的commit
* 执行\ ``git init``\ 后会有一系列的hook模板在\ ``.git/hooks``\ 下生成，以供参考，可以在此基础上进行修改

.. prompt:: bash $,# auto

   ~/.git/hooks$ tree
   .
   ├── applypatch-msg.sample
   ├── commit-msg.sample
   ├── fsmonitor-watchman.sample
   ├── post-update.sample
   ├── pre-applypatch.sample
   ├── pre-commit.sample
   ├── pre-merge-commit.sample
   ├── prepare-commit-msg.sample
   ├── pre-push.sample
   ├── pre-rebase.sample
   ├── pre-receive.sample
   └── update.sample

.. attention:: 使用前面提到的 `git/hook` 中的脚本，并不能同步到远程仓


`Precommit <https://pre-commit.com/#install>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用gitcommit可以生成本地的git hook

.. prompt:: bash $,# auto

   # 安装
   $ pip install pre-commit
   # run pre-commit install to set up the git hook scripts
   $ pre-commit install
   # 手动触发precommit
   $ pre-commit run --all-files

----

**案例**


* `precommit 添加isort <https://www.architecture-performance.fr/ap_blog/some-pre-commit-git-hooks-for-python/>`_
* `怎样防止同事用QQ邮箱提交公司代码 <https://mp.weixin.qq.com/s/nTujGu1tbde--X3KEO22WA>`_

----

`删除历史记录中不合适的数据 <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`_
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

参考资料
^^^^^^^^


#. 
   `简书example <https://www.jianshu.com/p/6c3f28d41c5e>`_

#. 
   `github docs <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`_

BFG
^^^

以下说明一个github官方推荐的工具 ``BFK`` ，不同于官方教程的 ``git clone`` ，此处推荐\ `直接下载jar包 <https://rtyley.github.io/bfg-repo-cleaner/>`_

:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210821090411342.png" alt="image-20210821090411342" style="zoom:67%; " />`


* 其相关的功能包括：删除大文件、删除包含某些敏感信息的文件、删除某个文件夹。具体的使用可参考\ `简书example <https://www.jianshu.com/p/6c3f28d41c5e>`_\ ，\ `官方实例 <https://rtyley.github.io/bfg-repo-cleaner/>`_\ ，不赘述

:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210821091001917.png" alt="image-20210821091001917" style="zoom:67%; " />`

.. prompt:: bash $,# auto

   # 同时删除多个文件夹
   $ bfg --delete-folders "{List of folder separated by comma}" <file path for Git repository to clean>

.. attention:: BFG并不能删除特定的文件夹和文件，只能删除同名的文件夹和文件。要实现上述目的，可以使用git filter-repo


`git filter-repo <https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`常用命令行 <https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $,# auto

   # 安装
   $ pip3 install git-filter-repo
   # 去到git工作空间
   $ cd ~/Sleipnir/
   # To remove ~/Sleipnir/data/ from every revision in history:
   # 使用的为相对路径
   $ git filter-repo --invert-paths --path data/

   # 更新远程仓
   $ git push origin --force --all

   # 更新本地仓（触发回收机制）
   $ git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
   $ git reflog expire --expire=now --all
   $ git gc --prune=now

:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210911011120408.png" alt="image-20210911011120408" style="zoom: 67%; " />`

.. note:: `--invert_paths` 需要和 `--paths` 一起使用的，单纯 `--paths` 指的是保留，否则是反选


获取clean工作空间
-----------------

从工作空间中清除没参与版本管理的文件（remove untracked files from the working tree）

.. prompt:: bash $,# auto

   $ git clean
   # -q, --quiet           不打印删除的文件名
   # -n, --dry-run         dry run
   # -f, --force           force
   # -i, --interactive     交换式的清除，有选择项
   # -d                    清除因此而空的空目录
   # -e, --exclude <pattern> add <pattern> to ignore rules
   # -x                    连带删除被ignore的文件
   # -X                    只删除被ignore的文件

对某些文件不进行版本管理(ignore)
--------------------------------


* 相应的配置文件为 ``.git/info/exclude`` 和 ``.gitignore`` ，前者为 ``git init`` 时创建；后者一般上传至远程仓，跟别人共享一份配置
* J家 IDE可以用\ ``.ignore``\ 插件来生成.ignore模板文件
* `.ignore中的一些语法 <https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository>`_\ ：遵从通配符模式找文件，\ **默认递归**\ 地查找工作空间的文件；开头加上\ ``/``\ 表示\ **取消递归**

回溯到某个commit
----------------

.. prompt:: bash $,# auto

   $ git checkout <commit_id>

取消待进行的merge操作
---------------------

有时暂时不想解决文件冲突问题，想取消merge操作，还原之前的状态

.. prompt:: bash $,# auto

   # --abort abort the current in-progress merge
   $ git merge --abort

.. note:: 有时不解决文件冲突则无法进行某些操作，比如 `reset --soft` 操作


压缩commit记录
--------------

为减小git仓的大小、去冗余、让commit记录更漂亮

修改message (of last commit)
----------------------------


* 当本地文件内容 = 暂存区内容 = 本地仓内容时

.. prompt:: bash $,# auto

   $ git commit --amend -m "<修改后的message>"


* 
  pycharm IDE中的实现：

  :raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210209114613082.png" alt="image-20210209114613082" style="zoom: 67%; " />`

选择性地挑选文件的changes进行commit
-----------------------------------


* for pycharm：


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210222010451820.png
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210222010451820.png
   :alt: image-20210222010451820


时光倒流（版本回溯）
--------------------

reset
^^^^^

git reset: Reset current HEAD to the specified state

.. prompt:: bash $,# auto

   # 回溯到对应的commit
   $ git reset [option] [commit_id]
   --soft  ：同步HEAD(difference不会commit)
   --mixed ：同步HEAD和INDEX区(difference会commit)
   --hard  ：同步HEAD、INDEX和工作空间

:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20210827192811107.png" alt="image-20210827192811107" style="zoom: 80%; " />`


* reset --hard一般可用于删除commit，如删除当前的commit

.. prompt:: bash $,# auto

   $ git reset --hard HEAD~1


* reset --soft一般用于修正历史树(commit tree)，如让其线性化

revert
^^^^^^

通过提交一个commit去撤销某次commit

删除文件
--------

一般可用来解决如下报错： ``already exists in the index``

.. prompt:: bash $,# auto

   # 删除文件在暂存区和工作区的相关文件和文件夹
   $ git rm <文件/文件夹>
   # 只删除其在暂存区的相关文件和文件夹
   $ git rm --cached <文件/文件夹>

.. note:: `git rm` 只能删除已在暂存区的文件


远程仓
------

显示和配置本地仓的远程仓属性
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   # 显示 usl alias/shortname
   $ git remote
   # -v: show url <=> 等价于 git remote get-url <alias>

   # 重设远程仓url
   $ git remote set-url <name> <newurl>

   # 重命名远程仓别名
   $ git remote rename <old> <new>
   # git remove rename origin main

从远程仓拉取数据
^^^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git fetch <url/alias>

剔除本地仓与远程仓的关联
^^^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git remote remove origin

覆写本地仓
^^^^^^^^^^


* 根据远程仓覆写本地仓

.. prompt:: bash $,# auto

   # 获取远程仓的历史树
   $ git fetch
   # 版本回溯
   $ git reset --hard <remote_branch_name>

上传本地仓数据到远程仓
^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git push <url> branch

覆写远程服务器上的git仓（暴力解决方案）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* 在本地修正完本地仓的历史后，强制将本地仓的历史覆写到远程仓中

.. prompt:: bash $,# auto

   $ git push -f

本地仓添加子仓
^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git submodule add <url> [待添加的工作路径]

本地仓克隆子仓
~~~~~~~~~~~~~~

.. prompt:: bash $,# auto

   $ git clone <url>
   $ git submodule init --recursive
   # 或者直接一步到位
   $ git clone <url> --recursive

`vcstool <https://github.com/dirk-thomas/vcstool>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* 
  该工具用于替换git submodule来管理子模块（实测，在国内使用体感不太好，容易下载失败）

* 
  `autoware example <https://github.com/tier4/AutowareArchitectureProposal.proj/blob/main/autoware.proj.repos>`_

.. prompt:: bash $,# auto

   $ sudo apt install -y python3-vcstool
   $ vcs import src < autoware.proj.repos

分支
----

分支创建与切换
^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   # 创建分支
   $ git branch <branch_name>
   # 切换分支
   $ git checkout/swtich <branch_name>

分支合并
^^^^^^^^

一般用得较多的就是对远程仓分支和本地仓分支的合并 ``merge`` ，merge有几种情况，一种是不需要解决冲突的，一种是需要解决冲突的

删除分支
^^^^^^^^

.. prompt:: bash $,# auto

   # 删除已合并(merge)的分支
   $ git branch -d <branch_name>
   # 删除分支
   $ git branch -D <branch_name>
   # 删除远程分支
   $ git branch -r -D <branch_name>

子仓库
------

参考\ ``man gitsubmodules``


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220317085145018.png
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220317085145018.png
   :alt: image-20220317085145018


.. prompt:: bash $,# auto

   # 移除子仓库在.gitlink和.gitmodules中相关的元数据、还有其工作空间
   $ git rm <submodule path> && git commit
   # 手动移除子仓库的git文件
   $ rm -rf <GIT_DIR>/modules/<name>

环境变量
--------

设置环境变量
^^^^^^^^^^^^

.. prompt:: bash $,# auto

   # 设置身份验证cache状态 (保持验证状态5min)
   $ git config --global credential.help 'cache --timeout 300'
   # 取消cache状态
   $ git config --global unset credential.help
   # 配置commit时的IDx信息
   $ git config --global user.name  "spongebob"
   $ git config --global user.email "spongebob@mail2.gdut.edu.cn"
   # 配置push / pull时远程仓时使用的代理服务
   $ git config --global http.proxy <e.g.: 127.0.0.1:12333>
   $ git config --global https.proxy <e.g.: 127.0.0.1:12333>
   # 设置默认文本编辑器
   $ git config --global core.editor vim

----

**NOTE**

git的环境变量可存在于三个配置文件下，其中的环境变量适用对象不同


* ``/etc/gitconfig``\ ：适用于linux 系统所有用户。\ ``--system``
* ``~/.gitconfig``\ ：适用于当前登录用户。\ ``--global``
* ``.git/config``\ ：位于和适用于本地仓。\ ``--local(default)``
* 对于同一环境变量，三个配置文件对环境变量覆写的优先级是1<2<3

----

查看配置参数
^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git config --list or -l
   --show-origin: 查看来源（配置文档路径）

查看当前配置参数的来源
^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash $,# auto

   $ git config -l --show-origin 

   # >>> 
   # file:/home/helios/.gitconfig   core.editor=vim 
   # file:/home/helios/.gitconfig   core.autocrlf=input 
   # file:.git/config     core.repositoryformatversion=0 
   # file:.git/config     core.filemode=true 
   # file:.git/config     core.bare=false 
   # file:.git/config     core.logallrefupdates=true 
   # file:.git/config     submodule.active=.
   # <<<

IDE
---

pycharm
^^^^^^^

添加github账号
~~~~~~~~~~~~~~


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/HtN38T0ZZSrGVcBN.png!thumbnail
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/HtN38T0ZZSrGVcBN.png!thumbnail
   :alt: img


README
------

图片
^^^^


* typora上传的图片在github上不能缩放


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/zoom-issue.png
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/zoom-issue.png
   :alt: img



* 几种图片格式方案：

:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/prusa_vs_ender.png" alt="img" width=50% height=50% align="right"/>`


.. raw:: html

   <p align="center">
   <img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/prusa_vs_ender.png" alt="img" width=20% height=20% />
   </p>


:raw-html-m2r:`<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/prusa_vs_ender.png" alt="img" width=200 height=100 align="left"/>`


* `gif图片图破 <http://progsharing.blogspot.com/2018/06/gifs-on-github-pages-content-length.html>`_\ ：链接的gif图不能超过5Mb


.. image:: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220115094459924.png
   :target: https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20220115094459924.png
   :alt: image-20220115094459924


`术语 <https://git-scm.com/docs/gitglossary>`_
--------------------------------------------------

拓展资料
--------


#. `github command line <https://github.com/cli/cli>`_
#. `开发常用缩写，你能看懂几个 <https://www.163.com/dy/article/GO2L19AP0518R7MO.html>`_
#. `github cheat sheet <https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md>`_
#. `git flight rules <https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md>`_
