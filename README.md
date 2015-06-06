#禅道PMS辅助脚本


如果您所在的公司使用的是**禅道**项目管理系统（ZenTaoPMS, http://www.zentao.net ），该工具可能提高您的工作效率。

-------------------

#这是什么？

**禅道PMS辅助脚本**是基于[**Python2.7**](https://www.python.org/download/releases/2.7/)的桌面提示脚本。通过自动抓取您的禅道数据，并以桌面气泡的形式给予通知。大多数情况下，该脚本能够提供及时的通知同能，并将打扰降到最低。


![](http://ww2.sinaimg.cn/mw690/42a4fe0agw1estjlc12v8j20hl09wtd7.jpg)


现在，你可以查看教程，3分钟内即可投入使用。

-------------------

#使用教程

##Step 1:
Download Project，并编辑config.inf文件
```
#禅道登录账号
account:carey

#密码
password:123456

#禅道url前缀。
#例如，禅道登录地址为http://192.168.1.200:8081/zentaopms/user-login.html
#那么，host则为http://192.168.1.200:8081/zentaopms/
#注意最后包含"/"
host:http://192.168.1.200:8081/zentaopms/
```


##Step 2:
命令行进入Project目录，执行
```
$ python main.py
```
脚本即可运行。

若要终止脚本运行，命令行键入Ctrl+C即可。



#运行环境

该项目在Ubuntu14.04，Python2.7下通过测试
> **先行测试版:**
> 
>  该项目现处于Beta阶段。如果您有更好的建议，欢迎提出[**Issues**](https://github.com/AbelJoo/ChanDao-ZenTao-PMS-Auxiliary/issues)

-------------------

#博客

##[Abel Joo](http://abeljoo.github.io/)


-------------------

#LICENSE

Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
