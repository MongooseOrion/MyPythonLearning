[*Click here to tranlate in English* (temporarily invalid)](https://github.com/MongooseOrion/MyPythonLearning/)
# 这是为记录我的 Python 学习进程而创设的项目
***Python*** 这门语言的开放和随意早就有耳闻，百闻不如一见，终于有时间系统地接触这门语言了。我将花费将近两个月的时间来学习这门语言，祝我好运！<br><br>
尽管这是为记录我自己的学习过程创建的项目，但是所有的文件全部经过系统化的处理，备注也很齐全。我本来也是像做笔记一样来写的代码，一方面也是便于我自己经常翻阅，所以它们都拥有很高的易读性。如果你想通过本项目入门 ***Python*** 也是完全没有问题的。<br><br>
**开发环境：Windows 10(19044.1889), Visual Studio 2022(17.3.3)**
## 文件章节划分
### MyPythonLearning1
该项目中包含基础项目，如下述所示：<br>
* [01printKeyword.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/01printKeyword.py)
  > 输出函数 print 介绍
* [02escapingCharacter.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/02escapingCharacter.py)
  > 转义字符介绍
* [03EncodeANDIdentifier.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/03EncodeANDIdentifier.py)
  > 字符、标识符与关键字
* [04VariableANDdata.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/04VariableANDdata.py)
  > 变量与数据类型
* [05operator.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/05operator.py)
  > 输入函数 input 与运算符
* [06SelectStructureDesign.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/06SelectStructureDesign.py)
  > 选择语句
* [07LoopStructureDesign.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/07LoopStructureDesign.py)
  > 循环语句
* [08List_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/08List_1.py)
  > 列表 第1部分
* [09List_2.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/09List_2.py)
  > 列表 第2部分
* [10Dictionary.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/10Dictionary.py)
  > 字典
* [11TupleANDSet.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/11TupleANDSet.py)
  > 元组与集合
* [12CharacterString.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/12CharacterString.py)
  > 字符串
* [13Function.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/13Function.py)
  > 函数
* [14BugANDExceptionHandle.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/14BugANDExceptionHandle.py)
  > Python 异常处理机制
* [15Class.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/15Class.py)
  > 类与对象
* [16ObjectClass.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/16ObjectClass.py)
  > 封装、继承、多态与object类
* [17PackageANDDirectory.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/17PackageANDDirectory.py)
  > 包和目录。*请注意，使用 Visual Studio 2022 构建 Python 解决方案，目录的概念是较弱的。*
* [18OSModule.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/18OSModule.py)
  > 在 Windows 操作系统下的 OS 命令，包括 Powershell 和 CMD
  >
***请注意，上述的模块命名格式不是 Python 允许的写法，如果以上述的格式命名模块，当进行相互调用时一定会发生错误，这里作如此命名仅作为顺序排列显示之用途，可参照下述的项目 2 来了解模块的正确命名方式。***
### MyPythonLearning2
该项目中主要包含需要对模块进行相互调用的学习部分，如下述所示：<br>
* [package1](https://github.com/MongooseOrion/MyPythonLearning/tree/master/MyPythonLearning2/package1)
  > [Module_subP1_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/package1/Module_subP1_1.py): 在该模块内展示了一些自定义的函数和类，以便外部引用。<br>
  > [main.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/package1/main.py)：在该模块内展示了一些自定义的函数和类，以便外部引用。
* [Module_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_1.py)
  > 展示了如何导入并使用第三方或自定义模块。
* [Module_2.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_2.py)
  > 介绍了部分 **Python** 的内部模块和开源的外部模块，包括但不限于时间、网页、*Pyecharts*。
* [Module_3.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_3.py)
  > 展示对文件的操作，包括读、写、复制、编码等。
* [Module_4.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_4.py)
  > 展示了with 语句（上下文管理器）的用法。
* [Module_5.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_5.py)
  > 专用于编写实例小程序
* [Module_6.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_6.py)
  > 包含了一个将某一文件夹下所有 ***Excel(.xlsx)*** 文件合并为一个 ***Excel*** 文件的程序
* 其他格式的文件
  > 由上述模块生成的图标、图表和文本文件
  >
***请注意，在 Microsoft Visual Studio 中进行 Python 程序开发时，需要将安装的第三方模块存放路径加入“搜索路径”中，以便 IDE 验证从而调用。***<br><br>
通过下述命令，可以在[ Windows 终端](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=zh-cn&gl=cn)中通过 **PowerShell** 在线安装 *Python* 第三方模块：<br>
  > pip install [模块名]
### MyPythonLearning3
该项目中包含了一些复杂实例的开发文件。
