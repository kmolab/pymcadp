<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20170812235814.1"><vh>@settings</vh>
<v t="leo.20170812235814.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="leo.20170812235814.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="leo.20170814225220.1" a="E"><vh>機械設計相關</vh>
<v t="leo.20170815093019.1"><vh>calculator 功能</vh></v>
<v t="leo.20170815093104.1"><vh>utilities 功能</vh></v>
<v t="leo.20170815225935.1"><vh>design</vh></v>
<v t="leo.20170815093208.1"><vh>flask web app 功能</vh></v>
<v t="leo.20170815093846.1" a="E"><vh>CAD and CAE</vh>
<v t="leo.20170815093353.1"><vh>2d graphics</vh></v>
<v t="leo.20170815093714.1"><vh>3d graphics</vh></v>
</v>
<v t="leo.20170815093838.1"><vh>分散運算功能</vh></v>
</v>
<v t="leo.20170815100901.1"><vh>Decorator 相關</vh></v>
<v t="leo.20170815100548.1"><vh>打包相關</vh></v>
<v t="leo.20170813232538.1" a="E"><vh>Qt 相關</vh>
<v t="leo.20170816104159.1"><vh>exec() and show()</vh></v>
<v t="leo.20170815100046.1"><vh>QThread</vh></v>
<v t="leo.20170815103206.1"><vh>QPainter</vh></v>
</v>
<v t="leo.20170815003014.1"><vh>Qt Designer</vh></v>
<v t="leo.20170815022249.1"><vh>QtWebEngineWidget</vh></v>
<v t="leo.20170814001948.1"><vh>CAD 相關</vh></v>
<v t="leo.20170814001340.1"><vh>CAE 相關</vh></v>
</vnodes>
<tnodes>
<t tx="leo.20170812235814.1"></t>
<t tx="leo.20170812235814.2">QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;'CherryPy', 'pytz', 'mako', 'beautifulsoup4', 'pymysql', 'peewee'
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="leo.20170812235814.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="leo.20170813232538.1">Qt is a comprehensiveC++framework for developing cross-platform GUI applications
using a "write once, compile anywhere" approach.

from PyQt5.QtWidgets import QApplication, QWidget

Layout 布局

show 與 exec 差異

show 顯示後控制權回到 parent

exec 執行後鎖定控制權直到執行結束

Python3 與 PyQt5 可以直接使用 exec, 因為 exec 已經不是 Python3 的關鍵字</t>
<t tx="leo.20170814001340.1">Web based FEM

https://www.ljll.math.upmc.fr/lehyaric/ffjs/15.6/

pygmsh

https://pypi.python.org/pypi/pygmsh

https://github.com/Micket/oofem/tree/master/bindings/python

https://github.com/mfem/PyMFEM (http://mfem.org/)

SWIG in mingw

http://sebsauvage.net/python/mingw.html

FEM

https://github.com/ali7line/awesome-fem

https://fenicsproject.org/ (https://fenicsproject.org/tutorial/)
</t>
<t tx="leo.20170814001948.1">https://github.com/VVS1864/SAMoCAD

其中隸屬於設計的工程設計面, 又可細分為:

選用設計, 也就是從現有的零件或配件群中選用的設計.

配置設計, 也就是根據所選擇的零配件加以組合, 以決定設計的組合順序或組合方式.

參數設計, 也就是決定內容所需的數據或尺寸.

原創設計, 也就是前所未見的配置參數設計或前所未見的整體設計.

重新設計, 也就是根據的新的需求、新的材料與元件發明, 所進行的設計.

客製化設計, 又稱為多選項設計, 也就是設計中的每一個功能, 都提供客戶不同等級的元件選擇所牽涉的設計.

功能, 經濟, 美觀

Conceptual, preliminary and detailed design

Three types of mechanical design:

1. Adaptive Design: In this the designer adapts the design and makes minor alterations or changes to suit the requirement.

2. Development Design: This is the development design from the existing design with the final product being distinct different from the existing one in terms of materials, cost, or functionality, or method of manufacturing. 

3.New Design: This involves lots of research, skills, technical ability and creativity. Such designs can generally qualify for a patent.

沿用

修改

創新</t>
<t tx="leo.20170814225220.1">所謂機械設計, 就是歷經詳細思慮考量, 完成互動元件間之精巧配置, 使其展現特定功能之具體規劃表達.

其中, 詳細思慮考量, 就是"計"的字義, 而精巧配置互動元件, 就是"機"的字義, 展現特定功能, 就是"械"的字義, 最後, 必須完成具體規劃表達則是"設"的字義.

因此機械設計共包含下列要件:

經過詳細思慮考量過程 (計)
結果為互動元件間之精巧配置 (機)
配置可展現特定功能, 用於解決所面臨問題 (械)
必須明確表達結果之具體規劃 (設)
而一般工程表達的方法, 包括口語表達, 文字表達, 2D 表達, 3D 表達, 理論解析(定性定量)表達, 實體表達等.

且上述各類表達, 會因時間、地點、參與者、團隊組織的遷流變化而衍生出各式版本, 機械產品的協同設計, 便在各式表達的版本中, 尋求各互動元件組成的可用性外, 也期望透過相同功能的不同供應者, 作為精巧配置的選項, 以降低風險.

至於機械設計的所謂互動元件, 包括固體、流體與軟體, 隨著全球化數位經濟的蓬勃發展, 直接利用雲端統合機械協同設計過程中的所有內容, 已然成為可行方案之一.

至於工程:

善其事曰工

工者巧於所能

程者物之準

工程者, 由善其事, 巧其能者所完成, 可據以為準, 依其內容執行, 可得預期之結果者曰工程.</t>
<t tx="leo.20170815003014.1">.ui 中的 Object Name 一旦決定, 儘量不要更改, 因為更改後, 必須重新產生 generated dialog code, 或手動修改對應的物件名稱

http://pyqt.sourceforge.net/Docs/PyQt5/QtWebEngineWidgets.html

 In Qt Designer, just add a QWidget to your form and promote it to QWebEngineView (base class: QWidget, header: QWebEngineView). Don't forget to add webenginewidgets to your project file.
 
 Note that the generated code (in the ui_*.py files) should never be hand-edited because any changes will be overwritten the next time pyuic4 is run</t>
<t tx="leo.20170815022249.1">#!/usr/bin/env python3

import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)

browser = QWebEngineView()
browser.load(QUrl("http://mde.tw"))
browser.show()

app.exec()</t>
<t tx="leo.20170815093019.1">simple calculator

engr calculator

hp 11c calculator</t>
<t tx="leo.20170815093104.1">選擇 student list 檔案, 依照格式分組排座位

graphics viewer

http://blog.csdn.net/u010725283/article/details/75331030

參考

http://www.cnblogs.com/codeAB/p/5019439.html

https://github.com/shantnu/PyEng

https://pynocchio.github.io/

https://github.com/mmisono/pyqt5-example

https://github.com/cadnano/cadnano2.5

https://github.com/slaclab/pydm

https://github.com/pyqt/examples

Numerical Python

https://link.springer.com/book/10.1007/978-1-4842-0553-2
</t>
<t tx="leo.20170815093208.1">利用多執行緒執行 flask 套件

lewis gear width calculation - peewee ORM SQLite3  and MySQL

cmsimfly - web based cms

pygrouf - web based groupware</t>
<t tx="leo.20170815093353.1">pythoncad

graphics files display and manipulation

pyslvs</t>
<t tx="leo.20170815093714.1">opengl stl file display

stl ASCII to Binary format conversion

stl Binary to ASCII format conversion

solvespace related

freecad related

opencascade related</t>
<t tx="leo.20170815093838.1">zmq 相關</t>
<t tx="leo.20170815093846.1"></t>
<t tx="leo.20170815100046.1">from PyQt5.Qtcore import QThread</t>
<t tx="leo.20170815100548.1">PyInstaller

pyqtdeploy - iOS and Android

先將 PyQt 程式轉為 C++ 後執行編譯打包

SIP 的功能?</t>
<t tx="leo.20170815100901.1">function decorator

class decorator

method decorator</t>
<t tx="leo.20170815103206.1">under Qt Designer how to use QPainter

use QPainter to paint onto a QGLWidget

Painting operations are translated to OpenGL calls

The result is accelerated 2D rendering

Relies on extensions for anti-aliasing, so you may be trading looks for speed
</t>
<t tx="leo.20170815225935.1">正齒輪齒面寬設計運算, peewee ORM 連結 SQLite3 與 MySQL 資料庫</t>
<t tx="leo.20170816104159.1">參考: http://www.cnblogs.com/dcb3688/p/4586373.html

Pyqt show和exec的区别

Pyqt中 QDialog  show和exec的区别

QDialog的显示有两个函数show()和exec()。他们的区别在参考文档上的解释如下：

show():
显示一个非模式对话框。控制权即刻返回给调用函数。
弹出窗口是否模式对话框，取决于modal属性的值。

原文：Shows the dialog as a modeless dialog. Control returns immediately to the calling code. 
The dialog will be modal or modeless according to the value of the modal property.

exec():
显示一个模式对话框，并且锁住程序直到用户关闭该对话框为止。函数返回一个DialogCode结果。
在对话框弹出期间，用户不可以切换同程序下的其它窗口，直到该对话框被关闭。
原文：Shows the dialog as a modal dialog, blocking until the user closes it. The function returns a DialogCode result. 
Users cannot interact with any other window in the same application until they close the dialog. 

模式与非模式

模式对话框，就是在弹出窗口的时候，整个程序就被锁定了，处于等待状态，直到对话框被关闭。这时往往是需要对话框的返回值进行下面的操作。如：确认窗口（选择“是”或“否”）。
非模式对话框，在调用弹出窗口之后，调用即刻返回，继续下面的操作。这里只是一个调用指令的发出，不等待也不做任何处理。如：查找框。

 

简单的理解：

首先这两个方法返回值不同。exec()有返回值，show()没有返回值。

其次这两个方法的作用也不同。调用show()的作用仅仅是将widget及其上的内容都显示出来，控制权即刻返回给调用函数。而调用exec()后，调用线程将会被阻塞，锁住程序直到用户关闭该对话框，期间用户不可以切换同程序下的其它窗口直到Dialog关闭。



在举一个父类点击事件弹层QDialog子窗体的例子

父类实例化子类 直接用.show()方法闪退， 所以要实例化为父类的全局变量 or 执行exec_() 方法

#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4.QtGui import *
import sys


class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)
        self.btn = QPushButton('Click1')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

        self.btn.clicked.connect(self.fireupWindows2)

    def fireupWindows2(self):
        w2 = W2()  # w2= W2(self) 在父类基础self弹框
        w2.show()  # Dialog show()  直接闪退

        # 需要通过self实例化为全局变量，不加self的话，一运行就被回收，也就无法显示。
        self.w2 = W2()
        self.w2.show()

        # 或者 直接exec_()   Dialog 可执行exec_() 方法， Widget 没有exec_()方法
        w2 = W2()
        w2.exec_()  # app.exec_()--------------消息循环结束之后，进程自然也会结束


class W2(QDialog):
    def __init__(self, parent=None):
        super(W2, self).__init__(parent)

        self.btn = QPushButton('Click2')

        vb = QVBoxLayout()
        vb.addWidget(self.btn)
        self.setLayout(vb)

        self.btn.clicked.connect(self.fireupWindows3)

    def fireupWindows3(self):
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = W1()
    w.show()
    sys.exit(app.exec_())</t>
</tnodes>
</leo_file>
