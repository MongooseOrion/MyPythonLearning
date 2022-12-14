[*点此切换为中文* ](https://github.com/MongooseOrion/MyPythonLearning/blob/master/README.md)
# This is a project created to record my *Python* learning progress.
I have known the greatful language **Python** for a long time. But I didn't have much time before. Now I am free to learning **Python**, so I plan to spend nearly 2 mothons to learn. Good luck to me!<br><br>
All files are well-structured which means you can understand every single line easily. If you are freshman in **Python**, just like me, you can use my files to help you learn. God bless you.<br><br>
## Module Divide Explanation
### MyPythonLearning1
This section contains basic part in **Python**, as shown in the following: 
* [01printKeyword.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/01printKeyword.py)
  > Output function: print() introduction
* [02escapingCharacter.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/02escapingCharacter.py)
  > Escape Character instroction
* [03EncodeANDIdentifier.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/03EncodeANDIdentifier.py)
  > Character, identifier and keywords
* [04VariableANDdata.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/04VariableANDdata.py)
  > Variable and data type
* [05operator.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/05operator.py)
  > Input function: input() and operator
* [06SelectStructureDesign.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/06SelectStructureDesign.py)
  > Select statement
* [07LoopStructureDesign.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/07LoopStructureDesign.py)
  > Looping statement
* [08List_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/08List_1.py)
  > List Part1
* [09List_2.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/09List_2.py)
  > List Part2
* [10Dictionary.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/10Dictionary.py)
  > Dictionary
* [11TupleANDSet.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/11TupleANDSet.py)
  > Tuple and Set
* [12CharacterString.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/12CharacterString.py)
  > Character string
* [13Function.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/13Function.py)
  > Function
* [14BugANDExceptionHandle.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/14BugANDExceptionHandle.py)
  > Python exception handle
* [15Class.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/15Class.py)
  > Class and objects
* [16ObjectClass.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/16ObjectClass.py)
  > Packaging, inherit, polymorphism and object class
* [17PackageANDDirectory.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/17PackageANDDirectory.py)
  > Package and dictory *Caution: Visual Studio 2022 used as default for 'solution manager view'*
* [18OSModule.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/18OSModule.py)
  > Windows native OS command，including Powershell and CMD
* [19JsonANDChart.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning1/19JsonANDChart.py)
  > Json files reading, and chart drawing

***Caution: The above-mentioned module naming format is not a writing method allowed by Python. If modules are named in the above-mentioned format, errors will occur when calling each other. The naming here is only for sequential display. Please refer to Item 2 below for the correct module naming method.***
### MyPythonLearning2
The project mainly contains learning parts that need to be called to each other for modules. The details is shown below: <br>
* [package1](https://github.com/MongooseOrion/MyPythonLearning/tree/master/MyPythonLearning2/package1)
  > [Module_subP1_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/package1/Module_subP1_1.py): Some custom functions and classes are shown inside the module for external reference. <br>
  > [main.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/package1/main.py)：Some custom functions and classes are shown inside the module for external reference.
* [Module_1.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_1.py)
  > Has shown how to import and use third-party or custom modules.
* [Module_2.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_2.py)
  > Has instroduced some of **Python** internal and open source external modules, including but not limited to the TIME, the WEB PAGES, and [*Pyecharts*](https://pyecharts.org/#/zh-cn/intro)。
* [Module_3.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_3.py)
  > Has shown operations on the files, including the READING, WRITING, COPYING, EOCODING, etc.
* [Module_4.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_4.py)
  > Has shown the use of the **with** statement (context manager).
* [Module_5.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_5.py)
  > Dedicated to writing instance funtions
* [Module_6.py](https://github.com/MongooseOrion/MyPythonLearning/blob/master/MyPythonLearning2/Module_6.py)
  > Contains a program that merges all **Excel** (.xlsx) files under a folder into signal one **Excel** file
* Other formatted files
  > Icon, chart, and text files generated by the above modules

***Caution: When developing Python programs in Microsoft Visual Studio, you need to include the installed third-party module placement path in the Search Path for IDE validation to call.*** <br><br>
By using the following command, you can install the third-party module in **Powershell** with [**Windows Terminal**](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=zh-cn&gl=cn).
  > pip install [模块名]

### MyPythonLearning3
The project contains development files for some complex instances.
