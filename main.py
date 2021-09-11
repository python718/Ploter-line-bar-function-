import sys
from sys import argv, exit
try:
    from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
    from PyQt5.QtGui import (QStandardItem, QStandardItemModel, QIcon, QPixmap, QDoubleValidator, QCloseEvent,
                             QMouseEvent)
    from PyQt5.QtWidgets import (QApplication, QDialog, QListWidget, QTreeView, QHBoxLayout, QVBoxLayout, QLabel,
                                 QWidget, QLineEdit, QPushButton, QCheckBox, QComboBox, QMessageBox, QToolButton,
                                 QDialogButtonBox, QGroupBox, QTabWidget, QSpinBox, QDesktopWidget, QGridLayout,
                                 QTreeWidget, QTreeWidgetItem, QAbstractItemView)
except ModuleNotFoundError:
    from os import system
    system(sys.executable + " -m pip install -i https://pypi.douban.com/simple PyQt5")
    from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
    from PyQt5.QtGui import (QStandardItem, QStandardItemModel, QIcon, QPixmap, QDoubleValidator, QCloseEvent,
                             QMouseEvent)
    from PyQt5.QtWidgets import (QApplication, QDialog, QListWidget, QTreeView, QHBoxLayout, QVBoxLayout, QLabel,
                                 QWidget, QLineEdit, QPushButton, QCheckBox, QComboBox, QMessageBox, QToolButton,
                                 QDialogButtonBox, QGroupBox, QTabWidget, QSpinBox, QDesktopWidget, QGridLayout,
                                 QTreeWidget, QTreeWidgetItem, QAbstractItemView)
try:
    from matplotlib.font_manager import FontProperties
    from matplotlib.pyplot import figure, bar, ylabel, plot, savefig, xticks, show, xlabel, text, title, close
except ModuleNotFoundError:
    from os import system
    system(sys.executable + " -m pip install -i https://pypi.douban.com/simple matplotlib")
    from matplotlib.font_manager import FontProperties
    from matplotlib.pyplot import figure, bar, ylabel, plot, savefig, xticks, show, xlabel, text, title, close
try:
    from numpy import arange, linspace, sin, cos, tan
except ModuleNotFoundError:
    from os import system
    system(sys.executable + " -m pip install -i https://pypi.douban.com/simple matplotlib")
    from numpy import arange, linspace, sin, cos, tan
from time import strftime, localtime

print("加载中…")
lineDict = {
    "实线": "-",
    "虚线": "--",
    "虚点线": "-.",
    "点线": ":"
}
spotDict = {
    "无标记": "",
    "点标记": ".",
    "像素标记": ",",
    "圆标记": "o",
    "反三角标记": "v",
    "三角标记": "^",
    "方形标记": "s",
    "五角标记": "p",
    "星星标记": "*",
    "加号标记": "+",
    "减号标记": "- "
}
colorDict = {
    "蓝色": "b",
    "青色": "c",
    "绿色": "g",
    "黑色": "k",
    "品红": "m",
    "红色": "r",
    "白色": "w",
    "黄色": "y"
}
app = QApplication(argv)
icon = QIcon()
validator = QDoubleValidator()
lineSetting, functionSetting, barSetting = [[] for i in range(3)]
font = FontProperties(fname="SimHei.ttf")


class NewDialog(QDialog):
    def __init__(self, parent=None):
        self.cancel = True
        super(NewDialog, self).__init__(parent)

    def closeEvent(self, a0: QCloseEvent):
        if not function.delete and self.cancel:
            function.function.pop()
        return super(NewDialog, self).closeEvent(a0)


class UiForm(object):
    def __init__(self):
        self.comboBox_2 = QComboBox()
        self.comboBox_2.addItems(spotDict.keys())
        self.comboBox_2.setCurrentText(functionSetting[-1])
        self.label_8 = QLabel()
        self.label_3 = QLabel()
        self.label_7 = QLabel()
        self.comboBox = QComboBox()
        self.comboBox.addItems(lineDict.keys())
        self.comboBox.setCurrentText(functionSetting[-2])
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setText(functionSetting[0])
        self.lineEdit_3 = QLineEdit()
        self.lineEdit_3.setText(functionSetting[2])
        self.label_6 = QLabel()
        self.spinBox_2 = QSpinBox()
        self.spinBox_2.setValue(functionSetting[1])
        self.spinBox_3 = QSpinBox()
        self.spinBox_3.setValue(functionSetting[3])
        self.label_5 = QLabel()
        self.label_4 = QLabel()
        self.gridLayout = QGridLayout()

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(400, 300)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_3.setMaximum(30)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 6, 1, 1, 1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 4, 1, 1, 1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 1, 1, 1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 7, 1, 1, 1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 8, 1, 1, 1)
        form.setLayout(self.gridLayout)
        self.translate_ui(form)
        QMetaObject.connectSlotsByName(form)

    def translate_ui(self, form):
        _translate = QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "x轴标题字体大小："))
        self.label_5.setText(_translate("Form", "默认y轴标题："))
        self.label_6.setText(_translate("Form", "y轴标题字体大小"))
        self.label_7.setText(_translate("Form", "线条类型"))
        self.label_3.setText(_translate("Form", "默认x轴标题："))
        self.label_8.setText(_translate("Form", "标记类型"))


def late(self):
    self.latex = "$y="
    if not self.function:
        self.latex += "0$"
        return self.latex
    for i in self.function:
        va = list(i.values())[0]
        ke = list(i.keys())[0]
        if ke == "sqrt":
            self.latex += "\\sqrt" + ("[" + str(va[0]) + "]" if ke[0] != 1 else "") + "{" + \
                          (str(va[1]) if va[1] != 1 else "") + "x" + \
                          ("^{" + str(va[2]) + "}" if va[2] != 1 else "") + "}+"
        elif ke == "axb":
            self.latex += (str(va[0]) if va[0] != 1 else "") + "x" + \
                          ("^{" + str(va[1]) + "}" if va[1] != 1 else "") + "+"
        elif ke == "ax":
            self.latex += (str(va[0]) if va[0] != 1 else "") + "x+"
        elif ke == "c":
            self.latex += str(va) + "+"
        else:
            self.latex += (str(va[0]) if va[0] != 1 else "") + "\\" + ke + ("(" + str(va[1]) + "x)" if va[1] != 1
                                                                            else "x") + "+"
    self.latex = list(self.latex)
    self.latex.pop()
    self.latex = "".join(self.latex)
    self.latex += "$"
    return self.latex


def type_to_image(str_latex, out_file, font_size=16):
    width = 1
    width += (len(str_latex) - 4) * 0.15
    fig = figure(figsize=(width, 0.5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    text(0.5, 0.5, str_latex, fontsize=font_size, verticalalignment="center", horizontalalignment="center")
    savefig(out_file, pad_inches="tight", bbox_inches=0)
    close(fig)


def number(string):
    return int(string) if float(string) % 1 == 0 else float(string)


def read_settings():
    global lineSetting, functionSetting, barSetting
    with open("setting.txt", encoding="utf-8") as file:
        data = file.read().split("\n")
    barSetting = [data[0], int(data[1]),
                  data[2], int(data[3]),
                  data[4], int(data[5]),
                  bool(data[6])]
    lineSetting = [data[7], int(data[8]),
                   data[9], int(data[10]),
                   data[11], int(data[12]),
                   data[13], data[14],
                   bool(data[15])]
    functionSetting = [data[16], int(data[17]),
                       data[18], int(data[19]),
                       data[20], data[21]]
    del data


class PlotBarWinTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.response = None

    def mousePressEvent(self, event):
        self.response = super().mousePressEvent(event)
        if self.currentIndex().data() is not None:
            plotBarWin.editButton.setEnabled(True)
            plotBarWin.removeButton.setEnabled(True)
        return self.response


read_settings()
settingIcon = QIcon("设置.png")
type_to_image("$y=0$", "函数式.png")
helpIcon = QIcon("帮助.jpeg")


class PlotLineWinListWidget(QListWidget):
    def __init__(self, parent):
        super(PlotLineWinListWidget, self).__init__(parent)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if self.currentIndex().data() is not None:
            plotLineWin.editBtn.setEnabled(True)
            plotLineWin.removeBtn.setEnabled(True)
        return None


class PlotBarWin(QWidget):
    def __init__(self):
        super(PlotBarWin, self).__init__()
        self.barDict = {}
        self.mirrorBarDict = {}
        self.setWindowTitle("柱状图")
        self.setWindowIcon(icon)
        self.resize(400, 575)
        self.totalLayout = QVBoxLayout()
        self.layout = QHBoxLayout()
        self.nameLabel = QLabel("第1个元素名")
        self.layout.addWidget(self.nameLabel)
        self.key2, self.value2 = 0, 0
        self.nameVar = QLineEdit()
        self.layout.addWidget(self.nameVar)
        self.totalLayout.addLayout(self.layout)
        self.layout2 = QHBoxLayout()
        self.valueLabel = QLabel("第1个元素值")
        self.layout2.addWidget(self.valueLabel)
        self.valueVar = QLineEdit()
        self.valueVar.setValidator(validator)
        self.layout2.addWidget(self.valueVar)
        self.totalLayout.addLayout(self.layout2)
        self.addButton = QPushButton("添加元素")
        self.addButton.clicked.connect(self.add)
        self.totalLayout.addWidget(self.addButton)
        self.newValueVar = None
        self.OkBtn = None
        self.CancelBtn = None
        self.NAME, self.VALUE = range(2)
        self.layout3 = QHBoxLayout()
        self.layout4 = QVBoxLayout()
        self.tree = PlotBarWinTreeView()
        self.tree.setRootIsDecorated(False)
        self.tree.setAlternatingRowColors(True)
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.NAME, Qt.Horizontal, "元素名")
        self.model.setHeaderData(self.VALUE, Qt.Horizontal, "元素值")
        self.model.setData(self.model.index(0, self.NAME), [])
        self.model.setData(self.model.index(0, self.VALUE), [])
        self.tree.setModel(self.model)
        self.tree.resize(280, 125)
        self.layout3.addWidget(self.tree)
        self.editButton = QPushButton("编辑")
        self.removeButton = QPushButton("移除")
        self.editButton.setEnabled(False)
        self.removeButton.setEnabled(False)
        self.editWin = None
        self.removeButton.clicked.connect(self.try_remove)
        self.editButton.clicked.connect(self.edit)
        self.layout4.addWidget(self.removeButton)
        self.layout4.addWidget(self.editButton)
        self.layout3.addLayout(self.layout4)
        self.totalLayout.addLayout(self.layout3)
        self.newNameVar = None
        self.addButton = QPushButton("添加元素")
        self.addButton.clicked.connect(self.add)
        self.plotBarButton = QPushButton("画图", self)
        self.plotBarButton.clicked.connect(self.plot_bar)
        self.plotBarButton.setShortcut("shift+p")
        self.check = QCheckBox("画图后清除原数据")
        self.colorComboBox = QComboBox(self)
        self.colorComboBox.setFixedHeight(30)
        self.colorComboBox.addItems(colorDict.keys())
        self.layout4 = QHBoxLayout()
        self.layout4.addStretch(1)
        self.layout4.addWidget(self.colorComboBox)
        self.layout4.addStretch(1)
        self.totalLayout.addLayout(self.layout4)
        self.layout5 = QHBoxLayout()
        self.check.setChecked(True)
        self.check.resize(200, 40)
        self.layout5.addStretch(1)
        self.layout5.addWidget(self.check)
        self.layout5.addStretch(1)
        self.totalLayout.addLayout(self.layout5)
        self.layout6 = QHBoxLayout()
        self.layout6.addStretch(1)
        self.layout6.addWidget(self.plotBarButton)
        self.layout6.addStretch(1)
        self.totalLayout.addLayout(self.layout6)
        self.setLayout(self.totalLayout)

    def try_remove(self):
        def remove(_class):
            if _class.tree.currentIndex().data() in _class.barDict.keys():
                key = _class.tree.currentIndex().data()
                value = _class.barDict[_class.tree.currentIndex().data()]
            else:
                key = self.mirrorBarDict[number(_class.tree.currentIndex().data())]
                value = number(_class.tree.currentIndex().data())
            index = list(_class.barDict.items()).index((key, value))
            _class.model.removeRow(index)
            del _class.barDict[key]
            del _class.mirrorBarDict[value]
            _class.nameLabel.setText("第" + str(len(self.barDict) + 1) + "个元素值")
            _class.valueLabel.setText("第" + str(len(self.barDict) + 1) + "个元素值")

        if barSetting[-1]:
            box = QMessageBox(QMessageBox.Question, "", "您确定删除吗？")
            box.setWindowIcon(icon)
            check = QCheckBox()
            check.setChecked(False)
            check.setText("不再提示")
            box.setCheckBox(check)
            box.addButton("确定", QMessageBox.YesRole)
            box.addButton("取消", QMessageBox.NoRole)
            box.show()
            if box.exec_() == 0:
                remove(_class=self)
            if box.checkBox().isChecked():
                with open("setting.txt", encoding="utf-8") as file:
                    setting = file.read().split("\n")
                    setting[6] = ""
                with open("setting.txt", "w", encoding="utf-8") as file:
                    file.write("\n".join(setting))
                read_settings()
        else:
            remove(_class=self)

    def edit(self):
        self.editWin = QDialog(self)
        self.editWin.setWindowModality(Qt.WindowModal)
        self.newNameVar = QLineEdit(self.editWin)
        self.newValueVar = QLineEdit(self.editWin)
        self.newValueVar.setValidator(validator)
        self.CancelBtn = QPushButton("取消", self.editWin)
        self.CancelBtn.clicked.connect(self.editWin.close)
        self.CancelBtn.setDefault(False)
        self.OkBtn = QPushButton("确定", self.editWin)
        self.OkBtn.clicked.connect(self.ok)
        self.CancelBtn.setDefault(True)
        self.CancelBtn.move(100, 150)
        self.OkBtn.move(200, 150)
        self.editWin.setGeometry(234, 365, 400, 200)
        QLabel("元素名：", self.editWin).move(10, 30)
        QLabel("元素值：", self.editWin).move(10, 100)
        self.editWin.setWindowTitle("修改元素")
        self.editWin.setWindowIcon(icon)
        if self.tree.currentIndex().data() in self.barDict.keys():
            self.newNameVar.setText(self.tree.currentIndex().data())
            self.newValueVar.setText(str(self.barDict[self.newNameVar.text()]))
        else:
            self.newNameVar.setText(self.mirrorBarDict[number(self.tree.currentIndex().data())])
            self.newValueVar.setText(self.tree.currentIndex().data())
        self.key2, self.value2 = self.newNameVar.text(), self.newValueVar.text()
        self.newValueVar.selectAll()
        self.newNameVar.resize(150, 40)
        self.newValueVar.resize(150, 40)
        self.newNameVar.move(100, 30)
        self.newValueVar.move(100, 100)
        self.editWin.exec_()

    def ok(self):
        if self.newNameVar.text() == self.key2:
            index = list(self.barDict.keys()).index(self.key2)
            items = list(self.barDict.items())[index:]
            for del_k, del_v in items:
                self.model.removeRow(list(self.barDict.keys()).index(del_k))
            self.barDict[self.key2] = number(self.newValueVar.text())
            self.mirrorBarDict[number(self.newValueVar.text())] = self.key2
            items[0] = (self.key2, number(self.newValueVar.text()))
            for new_k, new_v in items:
                print(new_v)
                self.model.appendRow([QStandardItem(new_k), QStandardItem(str(new_v))])
        elif self.newValueVar.text() == self.value2:
            index = list(self.barDict.keys()).index(self.key2)
            items = list(self.barDict.items())[index:]
            self.mirrorBarDict[number(self.value2)] = self.newNameVar.text()
            self.barDict = {}
            for k, v in self.mirrorBarDict.items():
                self.barDict[v] = k
            items[0] = list(self.barDict.items())[0]
            for del_k, del_v in items:
                self.model.removeRow(list(self.barDict.values()).index(del_v))
            for new_k, new_v in items:
                self.model.appendRow([QStandardItem(new_k), QStandardItem(str(new_v))])
        else:
            index = list(self.barDict.keys()).index(self.key2)
            items = list(self.barDict.items())[index:]
            for del_k, del_v in items:
                self.model.removeRow(list(self.barDict.keys()).index(del_k))
                del self.barDict[del_k]
                del self.mirrorBarDict[del_v]
            items[0] = (self.newNameVar.text(), number(self.newValueVar.text()))
            for new_k, new_v in items:
                self.barDict[new_k] = new_v
            for new_k, new_v in items:
                self.model.appendRow([QStandardItem(new_k), QStandardItem(str(new_v))])
        self.editWin.close()

    def add(self):
        if self.nameVar.text() in self.barDict.keys():
            QMessageBox.warning(self, "", "该元素已经存在", QMessageBox.Ok)
            return None
        try:
            key = self.nameVar.text()
            value = number(self.valueVar.text())
            self.barDict[key] = value
            self.mirrorBarDict[value] = key
            self.nameLabel.setText("第" + str(len(self.barDict) + 1) + "个元素名")
            self.valueLabel.setText("第" + str(len(self.barDict) + 1) + "个元素值")
            self.nameVar.setText("")
            self.valueVar.setText("")
            self.model.appendRow([QStandardItem(key), QStandardItem(str(value))])
        except ValueError:
            QMessageBox.critical(self, "", "输入元素有误", QMessageBox.Ok)
            self.valueVar.setText("")

    def plot_bar(self):
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(str({"name": "条形统计图", "color": self.colorComboBox.currentText(),
                            "time": strftime("%y年%m月%d日 %H:%M", localtime()), "data": self.barDict}) + "\n")
        x = arange(len(self.barDict))
        bar(x, self.barDict.values(), color=colorDict[self.colorComboBox.currentText()])
        xticks(x, self.barDict.keys(), fontproperties=font)
        title(barSetting[0], fontsize=barSetting[1], fontproperties=font)
        xlabel(barSetting[2], fontsize=barSetting[3], fontproperties=font)
        ylabel(barSetting[4], fontsize=barSetting[5], fontproperties=font)
        history.change()
        show()
        if self.check.isChecked():
            for i in range(len(self.barDict)):
                self.model.removeRow(0)
            self.barDict = {}
            self.nameLabel.setText("第1个元素名")
            self.valueLabel.setText("第1个元素值")


class PlotLineWin(QWidget):
    def __init__(self):
        super(PlotLineWin, self).__init__()
        self.list = []
        self.setWindowTitle("折线统计图")
        self.setWindowIcon(icon)
        self.setGeometry(100, 110, 400, 500)
        self.mainLayout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.label = QLabel("第1个元素：", self)
        self.layout1.addWidget(self.label)
        self.var = QLineEdit(self)
        self.var.setValidator(validator)
        self.layout1.addWidget(self.var)
        self.mainLayout.addLayout(self.layout1)
        self.addButton = QPushButton("添加", self)
        self.addButton.clicked.connect(self.add)
        self.mainLayout.addWidget(self.addButton)
        self.layout2 = QHBoxLayout()
        self.view = PlotLineWinListWidget(self)
        self.view.resize(250, 200)
        self.view.setAlternatingRowColors(True)
        self.layout2.addWidget(self.view)
        self.editWin = QDialog(self)
        self.editWin.setWindowModality(Qt.WindowModal)
        self.editWin.setWindowTitle("修改元素")
        self.editWin.resize(400, 200)
        self.newLabel = QLabel("在此输入元素：", self.editWin)
        self.editBtn = QPushButton("修改", self)
        self.editBtn.setEnabled(False)
        self.editBtn.clicked.connect(self.editWin.exec_)
        self.removeBtn = QPushButton("删除", self)
        self.newNameVar = QLineEdit(self.editWin)
        self.newNameVar.setValidator(validator)
        self.cancelBtn = QPushButton(self.editWin)
        self.okBtn = QPushButton(self.editWin)
        self.okBtn.setText("确定")
        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.editWin.close)
        self.cancelBtn.setText("取消")
        self.removeBtn.setEnabled(False)
        self.removeBtn.clicked.connect(self.try_remove)
        self.layout3 = QVBoxLayout()
        self.layout3.addWidget(self.editBtn)
        self.layout3.addWidget(self.removeBtn)
        self.layout2.addLayout(self.layout3)
        self.mainLayout.addLayout(self.layout2)
        self.layout4 = QHBoxLayout()
        self.layout4.addStretch(1)
        self.colorBox = QComboBox()
        self.colorBox.addItems(colorDict.keys())
        self.layout4.addWidget(self.colorBox)
        self.layout4.addStretch(1)
        self.layout5 = QHBoxLayout()
        self.check = QCheckBox("画图后清除原数据")
        self.check.setChecked(True)
        self.layout5.addStretch(1)
        self.layout5.addWidget(self.check)
        self.layout5.addStretch(1)
        self.layout6 = QHBoxLayout()
        self.plotBtn = QPushButton("画图", self)
        self.plotBtn.clicked.connect(self.plot)
        self.layout6.addStretch(1)
        self.layout6.addWidget(self.plotBtn)
        self.layout6.addStretch(1)
        self.mainLayout.addLayout(self.layout4)
        self.mainLayout.addLayout(self.layout5)
        self.mainLayout.addLayout(self.layout6)
        self.setLayout(self.mainLayout)
        self.editLayout = QVBoxLayout()
        self.editLayout.addWidget(self.newLabel)
        self.editLayout.addStretch(1)
        self.editLayout.addWidget(self.newNameVar)
        self.lay = QHBoxLayout()
        self.lay.addWidget(self.okBtn)
        self.lay.addWidget(self.cancelBtn)
        self.editLayout.addStretch(1)
        self.editLayout.addLayout(self.lay)
        self.editWin.setLayout(self.editLayout)

    def add(self):
        try:
            self.list.append(number(self.var.text()))
            self.view.addItem(self.var.text())
            self.var.setText("")
            self.label.setText("第" + str(len(self.list) + 1) + "个元素：")
        except ValueError:
            QMessageBox.critical(self, "错误", "输入元素有误", QMessageBox.Ok)
            self.var.clear()

    def try_remove(self):
        def remove(_class):
            _class.view.takeItem(_class.view.currentIndex().row())
            _class.list.pop(_class.view.currentIndex().row())
            self.label.setText("第" + str(len(self.list) + 1) + "个元素")

        if lineSetting[-1]:
            box = QMessageBox(QMessageBox.Question, "", "您确定删除吗？")
            box.setWindowIcon(icon)
            box.addButton("确定", QMessageBox.YesRole)
            check = QCheckBox()
            check.setChecked(False)
            check.setText("不再提示")
            box.setCheckBox(check)
            box.addButton("取消", QMessageBox.NoRole)
            box.show()
            if box.exec_() == 0:
                remove(_class=self)
            if box.checkBox().isChecked():
                with open("setting.txt", encoding="utf-8") as file:
                    setting = file.read().split("\n")
                    setting[15] = ""
                with open("setting.txt", "w", encoding="utf-8") as file:
                    file.write("\n".join(setting))
                read_settings()
        else:
            remove(_class=self)

    def plot(self):
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(str({"name": "折线统计图", "time": strftime("%y年%m月%d日 %H:%M", localtime()),
                            "color": self.colorBox.currentText(), "data": self.list}) + "\n")
        plot(arange(len(self.list)), self.list, colorDict[self.colorBox.currentText()] + lineDict[lineSetting[6]]
             + spotDict[lineSetting[7]])
        title(lineSetting[0], fontsize=lineSetting[1], fontproperties=font)
        xlabel(lineSetting[2], fontsize=lineSetting[3], fontproperties=font)
        ylabel(lineSetting[4], fontsize=lineSetting[5], fontproperties=font)
        history.change()
        show()
        if self.check.isChecked():
            for _ in self.list:
                self.view.takeItem(0)
            self.list = []
            self.label.setText("第1个元素：")

    def ok(self):
        index = self.view.currentIndex().row()
        if number(self.newNameVar.text()) % 1 == 0:
            self.list[index] = int(self.newNameVar.text())
        else:
            self.list[index] = number(self.newNameVar.text())
        for i in range(len(self.list) - index):
            self.view.takeItem(self.view.count() - 1)
        for i in self.list[index:]:
            self.view.addItem(str(i))
        self.editWin.close()


class Function(QWidget):
    def __init__(self):
        super().__init__()
        self.latex = "$y=0$"
        self.comboBox = QComboBox()
        self.edit3 = QLineEdit()
        self.edit2 = QLineEdit()
        self.label2 = QLabel()
        self.dialog = QDialog(self)
        self.delete = False
        self.edit = QLineEdit()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.resize(300, 400)
        self.setWindowTitle("函数画图")
        self.label = QLabel()
        self.label.setPixmap(QPixmap("normal.png"))
        self.btn = QToolButton()
        self.btn.setIcon(QIcon("ax.png"))
        self.btn.clicked.connect(self.ax)
        self.width = int(300 / 13)
        self.height = self.width * 2
        self.btn.setIconSize(QSize(self.width * 2, self.height))
        self.btn.setAutoRaise(True)
        self.btn2 = QToolButton()
        self.btn2.setIcon(QIcon("ax^b.png"))
        self.btn2.clicked.connect(self.axb)
        self.btn2.setIconSize(QSize(self.width * 2, self.height))
        self.btn2.setAutoRaise(True)
        self.btn3 = QToolButton()
        self.btn3.setIcon(QIcon("sin.png"))
        self.btn3.setToolTip("三角函数")
        self.btn3.clicked.connect(self.tri_function)
        self.btn3.setIconSize(QSize(self.width * 4, self.height))
        self.btn3.setAutoRaise(True)
        self.btn4 = QToolButton()
        self.btn4.setIcon(QIcon("c.png"))
        self.btn4.setIconSize(QSize(self.width, self.height))
        self.btn4.setAutoRaise(True)
        self.btn5 = QToolButton()
        self.btn5.setIcon(QIcon("sqrt.png"))
        self.btn5.clicked.connect(self.sqrt)
        self.function = []
        self.btn5.setIconSize(QSize(self.width * 4, self.height))
        self.btn5.setAutoRaise(True)
        self.layout_h = QHBoxLayout()
        self.layout_h.addWidget(self.btn)
        self.layout_h.addWidget(self.btn2)
        self.layout_h.addWidget(self.btn5)
        self.layout_h.addWidget(self.btn3)
        self.layout_h.addWidget(self.btn4)
        self.plotBtn = QPushButton("画图")
        self.plotBtn.clicked.connect(self.plot)
        self.btn4.clicked.connect(self.c)
        self.layout.addLayout(self.layout_h)
        self.layout.addWidget(self.label)
        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(colorDict.keys())
        self.layout3 = QHBoxLayout()
        self.layout3.addStretch(1)
        self.layout3.addWidget(self.comboBox1)
        self.layout3.addStretch(1)
        self.checkBox = QCheckBox("画图后清除原数据")
        self.checkBox.setChecked(True)
        self.layout2 = QHBoxLayout()
        self.layout2.addStretch(1)
        self.layout2.addWidget(self.checkBox)
        self.layout2.addStretch(1)
        self.layout.addLayout(self.layout3)
        self.layout.addLayout(self.layout2)
        self.layout.addWidget(self.plotBtn)

    def ax(self):
        try:
            self.dialog = NewDialog()
            self.dialog.setWindowTitle("ax")
            type_to_image(self.late(), "函数式.png")
            group_box = QGroupBox("函数式")
            self.label2 = QLabel()
            self.delete = False
            self.label2.setPixmap(QPixmap("函数式.png"))
            group_box.setLayout(QVBoxLayout())
            group_box.layout().addWidget(self.label2)
            layout = QVBoxLayout()
            self.dialog.setLayout(layout)
            layout.addWidget(group_box)
            self.edit = QLineEdit()
            self.edit.setPlaceholderText("系数（a）")
            group_box2 = QGroupBox("参数")
            layout.addWidget(group_box2)
            group_box2.setLayout(QVBoxLayout())
            dic = {"ax": 0}
            self.function.append(dic)
            self.edit.textChanged.connect(self.change)
            self.edit.setValidator(validator)
            group_box2.layout().addWidget(self.edit)
            layout.addWidget(group_box2)
            dialog_button = QDialogButtonBox()
            dialog_button.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            dialog_button.button(QDialogButtonBox.Ok).setText("确定")
            dialog_button.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
            dialog_button.button(QDialogButtonBox.Cancel).setText("取消")
            dialog_button.button(QDialogButtonBox.Cancel).clicked.connect(self.dialog.close)
            layout.addWidget(dialog_button)
            self.dialog.exec_()
        except Exception as err:
            print(err)

    def c(self):
        self.dialog = NewDialog(self)
        self.dialog.setWindowTitle("常数")
        self.dialog.setWindowModality(Qt.WindowModal)
        type_to_image(self.late(), "函数式.png")
        group_box = QGroupBox("函数式")
        self.label2 = QLabel()
        self.delete = False
        self.label2.setPixmap(QPixmap("函数式.png"))
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(self.label2)
        layout = QVBoxLayout()
        self.dialog.setLayout(layout)
        layout.addWidget(group_box)
        self.edit = QLineEdit()
        group_box2 = QGroupBox("常数值")
        layout.addWidget(group_box2)
        group_box2.setLayout(QVBoxLayout())
        dic = {"c": 0}
        self.function.append(dic)
        self.edit.textChanged.connect(self.change)
        self.edit.setValidator(validator)
        group_box2.layout().addWidget(self.edit)
        dialog_button = QDialogButtonBox()
        dialog_button.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dialog_button.button(QDialogButtonBox.Cancel).setText("取消")
        dialog_button.button(QDialogButtonBox.Ok).setText("确定")
        dialog_button.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        dialog_button.button(QDialogButtonBox.Cancel).clicked.connect(self.dialog.close)
        layout.addWidget(dialog_button)
        self.dialog.exec_()

    def sqrt(self):
        self.dialog = NewDialog()
        self.dialog.setWindowTitle("sqrt")
        type_to_image(self.late(), "函数式.png")
        group_box = QGroupBox("函数式")
        self.label2 = QLabel()
        self.delete = False
        self.label2.setPixmap(QPixmap("函数式.png"))
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(self.label2)
        layout = QVBoxLayout()
        self.dialog.setLayout(layout)
        layout.addWidget(group_box)
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("a次方根")
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("系数（b）")
        self.edit3 = QLineEdit()
        self.edit3.setPlaceholderText("指数（c）")
        group_box2 = QGroupBox("参数")
        layout.addWidget(group_box2)
        group_box2.setLayout(QVBoxLayout())
        dic = {"sqrt": [1, 0, 0]}
        self.function.append(dic)
        self.edit.textChanged.connect(self.change)
        self.edit.setValidator(validator)
        self.edit2.setValidator(validator)
        self.edit2.textChanged.connect(self.change)
        self.edit3.setValidator(validator)
        self.edit3.textChanged.connect(self.change)
        group_box2.layout().addWidget(self.edit)
        group_box2.layout().addWidget(self.edit2)
        group_box2.layout().addWidget(self.edit3)
        layout.addWidget(group_box2)
        dialog_button = QDialogButtonBox()
        dialog_button.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dialog_button.button(QDialogButtonBox.Ok).setText("确定")
        dialog_button.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        dialog_button.button(QDialogButtonBox.Cancel).setText("取消")
        dialog_button.button(QDialogButtonBox.Cancel).clicked.connect(self.dialog.close)
        layout.addWidget(dialog_button)
        self.dialog.exec_()

    def axb(self):
        self.dialog = NewDialog()
        self.dialog.setWindowTitle("ax^b")
        type_to_image(self.late(), "函数式.png")
        group_box = QGroupBox("函数式")
        self.label2 = QLabel()
        self.delete = False
        self.label2.setPixmap(QPixmap("函数式.png"))
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(self.label2)
        layout = QVBoxLayout()
        self.dialog.setLayout(layout)
        layout.addWidget(group_box)
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("系数（a）")
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("指数（b）")
        group_box2 = QGroupBox("参数")
        layout.addWidget(group_box2)
        group_box2.setLayout(QVBoxLayout())
        dic = {"axb": [0, 0]}
        self.function.append(dic)
        self.edit.textChanged.connect(self.change)
        self.edit.setValidator(validator)
        self.edit2.setValidator(validator)
        self.edit2.textChanged.connect(self.change)
        group_box2.layout().addWidget(self.edit)
        group_box2.layout().addWidget(self.edit2)
        layout.addWidget(group_box2)
        dialog_button = QDialogButtonBox()
        dialog_button.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dialog_button.button(QDialogButtonBox.Ok).setText("确定")
        dialog_button.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        dialog_button.button(QDialogButtonBox.Cancel).setText("取消")
        dialog_button.button(QDialogButtonBox.Cancel).clicked.connect(self.dialog.close)
        layout.addWidget(dialog_button)
        self.dialog.exec_()

    def tri_function(self):
        self.dialog = NewDialog()
        self.dialog.setWindowTitle("三角函数")
        type_to_image(self.late(), "函数式.png")
        group_box = QGroupBox("函数式")
        self.label2 = QLabel()
        self.delete = False
        self.label2.setPixmap(QPixmap("函数式.png"))
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(self.label2)
        layout = QVBoxLayout()
        self.dialog.setLayout(layout)
        layout.addWidget(group_box)
        self.comboBox = QComboBox()
        self.comboBox.addItems(["sin", "cos", "tan", "cot", "sec", "csc"])
        self.comboBox.currentTextChanged.connect(self.change)
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("三角函数系数（a）")
        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("x系数（b）")
        group_box2 = QGroupBox("参数")
        layout.addWidget(group_box2)
        group_box2.setLayout(QVBoxLayout())
        dic = {"sin": [0, 0]}
        self.function.append(dic)
        self.edit.textChanged.connect(self.change)
        self.edit.setValidator(validator)
        self.edit2.setValidator(validator)
        self.edit2.textChanged.connect(self.change)
        group_box2.layout().addWidget(self.comboBox)
        group_box2.layout().addWidget(self.edit)
        group_box2.layout().addWidget(self.edit2)
        layout.addWidget(group_box2)
        dialog_button = QDialogButtonBox()
        dialog_button.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dialog_button.button(QDialogButtonBox.Ok).setText("确定")
        dialog_button.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        dialog_button.button(QDialogButtonBox.Cancel).setText("取消")
        dialog_button.button(QDialogButtonBox.Cancel).clicked.connect(self.dialog.close)
        layout.addWidget(dialog_button)
        self.dialog.exec_()

    def plot(self):
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(str({"name": "函数图像", "time": strftime("%y年%m月%d日 %H:%M", localtime()),
                            "color": self.comboBox1.currentText(), "data": self.function}) + "\n")
        x = linspace(-10, 10, 10000)
        y = linspace(0, 0, 10000)

        def cot(num):
            return 1 / tan(num)

        def csc(num):
            return 1 / sin(num)

        def sec(num):
            return 1 / cos(num)

        for i in self.function:
            if list(i.keys())[0] in ["sin", "cos", "tan", "cot", "sec", "csc"]:
                y += list(i.values())[0][0] * eval(list(i.keys())[0] + "(" + str(list(i.values())[0][1]) + "*x)")
            elif "sqrt" in i.keys():
                ab = list(i.values())[0][1] * x ** list(i.values())[0][2]
                y += ab ** (1 / list(i.values())[0][0])
            elif "axb" in i.keys():
                y += list(i.values())[0][0] * x ** list(i.values())[0][1]
            elif "ax" in i.keys():
                y += list(i.values())[0] * x
            else:
                y += list(i.values())[0]
        title(self.late())
        plot(x, y, colorDict[self.comboBox1.currentText()] + lineDict[functionSetting[-2]] +
             spotDict[functionSetting[-1]])
        xlabel(functionSetting[0], fontsize=functionSetting[1], fontproperties=font)
        ylabel(functionSetting[2], fontsize=functionSetting[3], fontproperties=font)
        if self.checkBox.isChecked():
            self.function = []
            self.latex = "$y=0$"
            self.label.setPixmap(QPixmap("normal.png"))
        history.change()
        show()

    def late(self):
        self.latex = "$y="
        if not self.function:
            self.latex += "0$"
            return self.latex
        for i in self.function:
            va = list(i.values())[0]
            ke = list(i.keys())[0]
            if ke == "sqrt":
                self.latex += "\\sqrt" + ("[" + str(va[0]) + "]" if ke[0] != 1 else "") + "{" + \
                              (str(va[1]) if va[1] != 1 else "") + "x" + \
                              ("^{" + str(va[2]) + "}" if va[2] != 1 else "") + "}+"
            elif ke == "axb":
                self.latex += (str(va[0]) if va[0] != 1 else "") + "x" + \
                              ("^{" + str(va[1]) + "}" if va[1] != 1 else "") + "+"
            elif ke == "ax":
                self.latex += (str(va) if va != 1 else "") + "x+"
            elif ke == "c":
                self.latex += str(va) + "+"
            else:
                self.latex += (str(va[0]) if va[0] != 1 else "") + "\\" + ke + ("(" + str(va[1]) + "x)" if va[1] != 1
                                                                                else "x") + "+"
        self.latex = list(self.latex)
        self.latex.pop()
        self.latex = "".join(self.latex)
        self.latex += "$"
        return self.latex

    def ok(self):
        if "sqrt" in self.function[-1].keys() and not list(self.function[-1].values())[0][0]:
            QMessageBox.critical(self.dialog, "", "a不能为0")
            return None
        type_to_image(self.late(), "函数式.png")
        self.label.setPixmap(QPixmap("函数式.png"))
        self.dialog.cancel = False
        self.dialog.close()

    def change(self):
        if not self.edit.text() and self.dialog.windowTitle() != "三角函数":
            self.function.pop()
            self.delete = True
        elif not self.edit.text() and self.dialog.windowTitle() == "三角函数":
            last = self.function[-1]
            self.function.pop()
            type_to_image(self.late(), "函数式.png")
            self.label2.setPixmap(QPixmap("函数式.png"))
            self.function.append(last)
        else:
            if self.dialog.windowTitle() == "常数":
                if self.delete:
                    self.delete = False
                    self.function.append({"c": 0})
                self.function[-1]["c"] = number(self.edit.text().strip("."))
            elif self.dialog.windowTitle() == "ax^b":
                if self.delete:
                    self.delete = False
                    self.function.append({"axb": [0, 0]})
                self.function[-1]["axb"] = [number(i.text().strip(".")) if i.text() else 0
                                            for i in [self.edit, self.edit2]]
            elif self.dialog.windowTitle() == "ax":
                if self.delete:
                    self.delete = False
                    self.function.append({"ax": 0})
                self.function[-1]["ax"] = number(self.edit.text().strip("."))
            elif self.dialog.windowTitle() == "三角函数":
                if self.edit.text():
                    self.function.pop()
                    self.function.append({self.comboBox.currentText(): [number(i.text().strip(".")) if i.text() else 0
                                                                        for i in [self.edit, self.edit2]]})
                    type_to_image(self.late(), "函数式.png")
                    self.label2.setPixmap(QPixmap("函数式.png"))
            else:
                if self.delete:
                    self.delete = False
                    self.function.append({"sqrt": [1, 0, 0]})
                self.function[-1]["sqrt"] = [number(i.text().strip(".")) if i.text() else
                                             (0 if i in [self.edit2, self.edit3] else 1)
                                             for i in [self.edit, self.edit2, self.edit3]]
        if self.dialog.windowTitle() != "三角函数":
            type_to_image(self.late(), "函数式.png")
            self.label2.setPixmap(QPixmap("函数式.png"))


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("画图器")
        self.setWindowIcon(icon)
        self.resize(400, 400)
        self.qr = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.cp)
        self.move(self.qr.topLeft())
        self.plotBarButton = QPushButton("柱状图", self)
        self.plotBarButton.clicked.connect(plotBarWin.show)
        self.plotLineButton = QPushButton("折线统计图", self)
        self.plotLineButton.clicked.connect(plotLineWin.show)
        self.functionButton = QPushButton("函数画图", self)
        self.functionButton.clicked.connect(function.show)
        self.settingButton = QPushButton("设置", self)
        self.settingButton.clicked.connect(settingWin.show)
        self.historyButton = QPushButton("历史记录", self)
        self.historyButton.clicked.connect(history.show)
        self.layout = QVBoxLayout()
        self.box = QMessageBox(QMessageBox.Question, "确认", "您确定退出吗？")
        self.box.addButton("确定", QMessageBox.YesRole)
        self.box.addButton("取消", QMessageBox.NoRole)
        self.box.setWindowIcon(icon)
        self.layout.addWidget(self.plotBarButton)
        self.layout.addWidget(self.plotLineButton)
        self.layout.addWidget(self.functionButton)
        self.layout.addWidget(self.settingButton)
        self.layout.addWidget(self.historyButton)
        self.setLayout(self.layout)

    def closeEvent(self, q_close_event):
        self.box.show()
        if self.box.exec_() == 0:
            q_close_event.accept()
            exit(0)
        else:
            q_close_event.ignore()


class HistoryView(QTreeWidget):
    def __init__(self, parent=None):
        super(HistoryView, self).__init__(parent)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        super(HistoryView, self).mousePressEvent(e)
        history.item = self.selectedItems()
        for i in history.item:
            if not i.text(0)[0].isalnum():
                history.item.remove(i)
        if history.item:
            history.button2.setEnabled(True)
            history.button3.setEnabled(True)
        else:
            history.button2.setEnabled(False)
            history.button3.setEnabled(False)


class History(QWidget):
    def __init__(self):
        super(History, self).__init__()
        self.setWindowTitle("历史记录")
        self.resize(700, 400)
        self.setWindowIcon(icon)
        self.bar2, self.line2, self.function2, self.item, self.hi = ([] for _ in range(5))
        self.widget = HistoryView()
        self.widget.setHeaderLabels(["时间", "数据", "颜色"])
        self.bar = QTreeWidgetItem()
        self.line = QTreeWidgetItem()
        self.function = QTreeWidgetItem()
        self.button = QPushButton("清除所有历史记录")
        self.button.clicked.connect(self.change)
        self.change()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button2.setEnabled(False)
        self.button2.setText("画图")
        self.button2.clicked.connect(self.plot)
        self.button3.setEnabled(False)
        self.button3.setText("删除")
        self.button3.clicked.connect(self.delete)
        self.widget.addTopLevelItems([self.bar, self.line, self.function])
        self.widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.widget.setColumnWidth(0, 200)
        self.widget.setColumnWidth(1, 350)
        self.widget.expandAll()
        self.layout = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.button2)
        self.layout2.addWidget(self.button3)
        self.layout.addLayout(self.layout2)
        self.layout.addWidget(self.widget)
        self.layout.addWidget(self.button)
        self.latex = ""
        self.setLayout(self.layout)
        self.barDict, self.list, self.fun = (None for _ in range(3))

    def late(self):
        self.latex = "$y="
        if not self.fun:
            self.latex += "0$"
            return self.latex
        for i in self.fun:
            va = list(i.values())[0]
            ke = list(i.keys())[0]
            if ke == "sqrt":
                self.latex += "\\sqrt" + ("[" + str(va[0]) + "]" if ke[0] != 1 else "") + "{" + \
                              (str(va[1]) if va[1] != 1 else "") + "x" + \
                              ("^{" + str(va[2]) + "}" if va[2] != 1 else "") + "}+"
            elif ke == "axb":
                self.latex += (str(va[0]) if va[0] != 1 else "") + "x" + \
                              ("^{" + str(va[1]) + "}" if va[1] != 1 else "") + "+"
            elif ke == "ax":
                self.latex += (str(va) if va != 1 else "") + "x+"
            elif ke == "c":
                self.latex += str(va) + "+"
            else:
                self.latex += (str(va[0]) if va[0] != 1 else "") + "\\" + ke + ("(" + str(va[1]) + "x)" if va[1] != 1
                                                                                else "x") + "+"
        self.latex = list(self.latex)
        self.latex.pop()
        self.latex = "".join(self.latex)
        self.latex += "$"
        return self.latex

    def plot(self):
        for i in self.item:
            if i.parent().text(0).startswith("条"):
                self.barDict = eval(i.text(1))
                x = arange(len(self.barDict))
                bar(x, self.barDict.values(), color=colorDict[i.text(2)])
                xticks(x, self.barDict.keys(), fontproperties=font)
                title(barSetting[0], fontsize=barSetting[1], fontproperties=font)
                xlabel(barSetting[2], fontsize=barSetting[3], fontproperties=font)
                ylabel(barSetting[4], fontsize=barSetting[5], fontproperties=font)
                show()
            elif i.parent().text(0).startswith("函"):
                self.fun = eval(i.text(1))
                x = linspace(-10, 10, 10000)
                y = linspace(0, 0, 10000)

                def cot(num):
                    return 1 / tan(num)

                def csc(num):
                    return 1 / sin(num)

                def sec(num):
                    return 1 / cos(num)

                for item in self.fun:
                    if list(item.keys())[0] in ["sin", "cos", "tan", "cot", "sec", "csc"]:
                        y += list(item.values())[0][0] * eval(
                            list(item.keys())[0] + "(" + str(list(item.values())[0][1]) + "*x)")
                    elif "sqrt" in item.keys():
                        ab = list(item.values())[0][1] * x ** list(item.values())[0][2]
                        y += ab ** (1 / list(item.values())[0][0])
                    elif "axb" in item.keys():
                        y += list(item.values())[0][0] * x ** list(item.values())[0][1]
                    elif "ax" in item.keys():
                        y += list(item.values())[0] * x
                    else:
                        y += list(item.values())[0]
                title(self.late())
                plot(x, y, colorDict[i.text(2)] + lineDict[functionSetting[-2]] +
                     spotDict[functionSetting[-1]])
                xlabel(functionSetting[0], fontsize=functionSetting[1], fontproperties=font)
                ylabel(functionSetting[2], fontsize=functionSetting[3], fontproperties=font)
                show()
            else:
                self.list = eval(i.text(1))
                plot(arange(len(self.list)), self.list,
                     colorDict[i.text(2)] + lineDict[lineSetting[6]]
                     + spotDict[lineSetting[7]])
                title(lineSetting[0], fontsize=lineSetting[1], fontproperties=font)
                xlabel(lineSetting[2], fontsize=lineSetting[3], fontproperties=font)
                ylabel(lineSetting[4], fontsize=lineSetting[5], fontproperties=font)
                show()

    def delete(self):
        for i in self.item:
            x = {"name": i.parent().text(0).split("（")[0], "time": i.text(0), "color": i.text(2), "data":
                 eval(i.text(1))}
            self.hi.remove(x)
        if self.hi:
            with open("history.txt", "w", encoding="utf-8") as file:
                file.write("\n".join([str(i) for i in self.hi]) + "\n")
        else:
            with open("history.txt", "w", encoding="utf-8") as file:
                file.write("")
        self.change()

    def change(self):
        if self.sender() == self.button:
            with open("history.txt", "w", encoding="utf-8") as file:
                file.write("")
        try:
            with open("history.txt", encoding="utf-8") as f:
                self.hi = f.read().split("\n")
                self.hi.pop()
                self.hi = [eval(i) for i in self.hi]
                self.hi.reverse()
        except FileNotFoundError:
            open("history.txt", "w").close()
        self.bar2.clear()
        self.line2.clear()
        self.function2.clear()
        self.bar.takeChildren()
        self.line.takeChildren()
        self.function.takeChildren()
        for i in self.hi:
            if i["name"] == "函数图像":
                self.function2.append(i)
            elif i["name"] == "折线统计图":
                self.line2.append(i)
            else:
                self.bar2.append(i)
        self.bar.setText(0, "条形统计图（共" + str(len(self.bar2)) + "条）")
        self.line.setText(0, "折线统计图（共" + str(len(self.line2)) + "条）")
        self.function.setText(0, "函数图像（共" + str(len(self.function2)) + "条）")
        for i in self.bar2:
            child = QTreeWidgetItem(self.bar)
            child.setText(0, i["time"])
            child.setText(1, str(i["data"]))
            child.setText(2, i["color"])
        for i in self.line2:
            child = QTreeWidgetItem(self.line)
            child.setText(0, i["time"])
            child.setText(1, str(i["data"]))
            child.setText(2, i["color"])
        for i in self.function2:
            child = QTreeWidgetItem(self.function)
            child.setText(0, i["time"])
            child.setText(1, str(i["data"]))
            child.setText(2, i["color"])
        self.widget.update()


class SettingWin(QWidget):
    def __init__(self):
        super(SettingWin, self).__init__()
        self.setWindowTitle("设置")
        self.setWindowIcon(icon)
        self.tab = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.ui = UiForm()
        self.ui.setup_ui(self.tab3)
        self.tab.addTab(self.tab1, "柱状图")
        self.tab.addTab(self.tab2, "折线统计图")
        self.tab.addTab(self.tab3, "函数画图")
        self.mainLayout1 = QVBoxLayout()
        self.mainLayout2 = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.titleLabel1 = QLabel("默认图标标题：")
        self.titleEntry1 = QLineEdit()
        self.titleEntry1.setText(barSetting[0])
        self.titleSizeLabel1 = QLabel("图标标题字体大小：")
        self.titleSizeEntry1 = QSpinBox()
        self.titleSizeEntry1.setRange(0, 30)
        self.titleSizeEntry1.setValue(barSetting[1])
        self.xLabel1 = QLabel("默认x轴标题：")
        self.xEntry1 = QLineEdit()
        self.xEntry1.setText(barSetting[2])
        self.xSizeLabel1 = QLabel("x轴标题字体大小：")
        self.xSizeEntry1 = QSpinBox()
        self.xSizeEntry1.setRange(0, 30)
        self.xSizeEntry1.setValue(barSetting[3])
        self.yLabel1 = QLabel("默认y轴标题：")
        self.yEntry1 = QLineEdit()
        self.yEntry1.setText(barSetting[4])
        self.ySizeLabel1 = QLabel("y轴标题字体大小：")
        self.ySizeEntry1 = QSpinBox()
        self.ySizeEntry1.setRange(0, 30)
        self.ySizeEntry1.setValue(barSetting[5])
        self.checkBox1 = QCheckBox()
        self.checkBox1.setText("点击删除后确认")
        self.latex = "$y=0$"
        self.checkBox1.setChecked(barSetting[-1])
        self.leftLayout1 = QVBoxLayout()
        self.leftLayout1.addWidget(self.titleLabel1)
        self.leftLayout1.addWidget(self.titleSizeLabel1)
        self.leftLayout1.addWidget(self.xLabel1)
        self.leftLayout1.addWidget(self.xSizeLabel1)
        self.leftLayout1.addWidget(self.yLabel1)
        self.leftLayout1.addWidget(self.ySizeLabel1)
        self.layout1.addLayout(self.leftLayout1)
        self.rightLayout1 = QVBoxLayout()
        self.rightLayout1.addWidget(self.titleEntry1)
        self.rightLayout1.addWidget(self.titleSizeEntry1)
        self.rightLayout1.addWidget(self.xEntry1)
        self.rightLayout1.addWidget(self.xSizeEntry1)
        self.rightLayout1.addWidget(self.yEntry1)
        self.rightLayout1.addWidget(self.ySizeEntry1)
        self.layout1.addLayout(self.rightLayout1)
        self.mainLayout1.addLayout(self.layout1)
        self.mainLayout1.addWidget(self.checkBox1)
        self.tab1.setLayout(self.mainLayout1)
        self.titleLabel2 = QLabel("默认图标标题：")
        self.titleEntry2 = QLineEdit()
        self.titleEntry2.setText(lineSetting[0])
        self.titleSizeLabel2 = QLabel("图标标题字体大小：")
        self.titleSizeEntry2 = QSpinBox()
        self.titleSizeEntry2.setRange(0, 30)
        self.titleSizeEntry2.setValue(lineSetting[1])
        self.xLabel2 = QLabel("默认x轴标题：")
        self.xEntry2 = QLineEdit()
        self.xEntry2.setText(lineSetting[2])
        self.xSizeLabel2 = QLabel("x轴标题字体大小：")
        self.xSizeEntry2 = QSpinBox()
        self.xSizeEntry2.setRange(0, 30)
        self.xSizeEntry2.setValue(lineSetting[3])
        self.yLabel2 = QLabel("默认y轴标题：")
        self.yEntry2 = QLineEdit()
        self.yEntry2.setText(lineSetting[4])
        self.ySizeLabel2 = QLabel("y轴标题字体大小：")
        self.ySizeEntry2 = QSpinBox()
        self.ySizeEntry2.setRange(0, 30)
        self.ySizeEntry2.setValue(lineSetting[5])
        self.lineLabel2 = QLabel("线条类型")
        self.lineComboBox2 = QComboBox()
        self.lineComboBox2.addItems(lineDict.keys())
        self.lineComboBox2.setCurrentText(lineSetting[6])
        self.spotLabel2 = QLabel("标记类型")
        self.spotComboBox2 = QComboBox()
        self.spotComboBox2.addItems(spotDict.keys())
        self.spotComboBox2.setCurrentText(lineSetting[7])
        self.checkBox2 = QCheckBox()
        self.checkBox2.setText("点击删除后确认")
        self.checkBox2.setChecked(lineSetting[-1])
        self.leftLayout2 = QVBoxLayout()
        self.leftLayout2.addWidget(self.titleLabel2)
        self.leftLayout2.addWidget(self.titleSizeLabel2)
        self.leftLayout2.addWidget(self.xLabel2)
        self.leftLayout2.addWidget(self.xSizeLabel2)
        self.leftLayout2.addWidget(self.yLabel2)
        self.leftLayout2.addWidget(self.ySizeLabel2)
        self.leftLayout2.addWidget(self.lineLabel2)
        self.leftLayout2.addWidget(self.spotLabel2)
        self.layout2.addLayout(self.leftLayout2)
        self.rightLayout2 = QVBoxLayout()
        self.rightLayout2.addWidget(self.titleEntry2)
        self.rightLayout2.addWidget(self.titleSizeEntry2)
        self.rightLayout2.addWidget(self.xEntry2)
        self.rightLayout2.addWidget(self.xSizeEntry2)
        self.rightLayout2.addWidget(self.yEntry2)
        self.rightLayout2.addWidget(self.ySizeEntry2)
        self.rightLayout2.addWidget(self.lineComboBox2)
        self.rightLayout2.addWidget(self.spotComboBox2)
        self.layout2.addLayout(self.rightLayout2)
        self.mainLayout2.addLayout(self.layout2)
        self.mainLayout2.addWidget(self.checkBox2)
        self.tab2.setLayout(self.mainLayout2)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.tab)
        self.button = QPushButton("确定")
        self.button.clicked.connect(self.que)
        self.mainLayout.addWidget(self.button)
        self.setLayout(self.mainLayout)

    def que(self):
        try:
            setting_list = [self.titleEntry1.text(), self.titleSizeEntry1.text(), self.xEntry1.text(),
                            self.xSizeEntry1.text(), self.yEntry1.text(), self.ySizeEntry1.text(),
                            int(self.checkBox1.isChecked()) * " ", self.titleEntry2.text(), self.titleSizeEntry2.text(),
                            self.xEntry2.text(), self.xSizeEntry2.text(), self.yEntry2.text(), self.ySizeEntry2.text(),
                            self.lineComboBox2.currentText(), self.spotComboBox2.currentText(),
                            int(self.checkBox2.isChecked()) * " ", self.ui.lineEdit_2.text(), self.ui.spinBox_2.text(),
                            self.ui.lineEdit_3.text(), self.ui.spinBox_3.text(), self.ui.comboBox.currentText(),
                            self.ui.comboBox_2.currentText()]
            file = open("setting.txt", "w", encoding="utf-8")
            file.write("\n".join(setting_list))
            file.close()
            read_settings()
            self.close()
        except OSError as err:
            if err == OSError("[Errno 28] No space left on device"):
                box = QMessageBox(QMessageBox.Critical, "", "空间不足，无法保存")
                box.addButton("确定", QMessageBox.OkRole)
                box.setWindowIcon(icon)
                box.show()
                box.exec_()


if __name__ == "__main__":
    plotBarWin = PlotBarWin()
    plotLineWin = PlotLineWin()
    function = Function()
    settingWin = SettingWin()
    history = History()
    mainWindow = MainWindow()
    mainWindow.show()
    print("加载成功！")
    exit(app.exec_())
