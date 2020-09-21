# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_sweep.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editSweep(object):
    def setupUi(self, editSweep):
        editSweep.setObjectName("editSweep")
        editSweep.resize(342, 282)
        self.buttonBox = QtWidgets.QDialogButtonBox(editSweep)
        self.buttonBox.setGeometry(QtCore.QRect(240, 170, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(editSweep)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.scanHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.scanHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scanHorizontalLayout.setObjectName("scanHorizontalLayout")
        self.scanLabelLayout = QtWidgets.QVBoxLayout()
        self.scanLabelLayout.setObjectName("scanLabelLayout")
        self.paramLabel = QtWidgets.QLabel(self.layoutWidget)
        self.paramLabel.setObjectName("paramLabel")
        self.scanLabelLayout.addWidget(self.paramLabel)
        self.startLabel = QtWidgets.QLabel(self.layoutWidget)
        self.startLabel.setObjectName("startLabel")
        self.scanLabelLayout.addWidget(self.startLabel)
        self.endLabel = QtWidgets.QLabel(self.layoutWidget)
        self.endLabel.setObjectName("endLabel")
        self.scanLabelLayout.addWidget(self.endLabel)
        self.stepLabel = QtWidgets.QLabel(self.layoutWidget)
        self.stepLabel.setObjectName("stepLabel")
        self.scanLabelLayout.addWidget(self.stepLabel)
        self.stepsecLabel = QtWidgets.QLabel(self.layoutWidget)
        self.stepsecLabel.setObjectName("stepsecLabel")
        self.scanLabelLayout.addWidget(self.stepsecLabel)
        self.scanHorizontalLayout.addLayout(self.scanLabelLayout)
        self.scanValuesLayout = QtWidgets.QVBoxLayout()
        self.scanValuesLayout.setObjectName("scanValuesLayout")
        self.paramBox = QtWidgets.QComboBox(self.layoutWidget)
        self.paramBox.setObjectName("paramBox")
        self.scanValuesLayout.addWidget(self.paramBox)
        self.startEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.startEdit.setReadOnly(False)
        self.startEdit.setObjectName("startEdit")
        self.scanValuesLayout.addWidget(self.startEdit)
        self.endEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.endEdit.setObjectName("endEdit")
        self.scanValuesLayout.addWidget(self.endEdit)
        self.stepEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.stepEdit.setObjectName("stepEdit")
        self.scanValuesLayout.addWidget(self.stepEdit)
        self.stepsecEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.stepsecEdit.setObjectName("stepsecEdit")
        self.scanValuesLayout.addWidget(self.stepsecEdit)
        self.scanHorizontalLayout.addLayout(self.scanValuesLayout)
        self.deleteButton = QtWidgets.QPushButton(editSweep)
        self.deleteButton.setGeometry(QtCore.QRect(240, 240, 81, 21))
        self.deleteButton.setObjectName("deleteButton")
        self.layoutWidget_2 = QtWidgets.QWidget(editSweep)
        self.layoutWidget_2.setGeometry(QtCore.QRect(200, 20, 122, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.sweepOptionsLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.sweepOptionsLayout.setContentsMargins(0, 0, 0, 0)
        self.sweepOptionsLayout.setObjectName("sweepOptionsLayout")
        self.bidirectionalBox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.bidirectionalBox.setObjectName("bidirectionalBox")
        self.sweepOptionsLayout.addWidget(self.bidirectionalBox)
        self.continualBox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.continualBox.setObjectName("continualBox")
        self.sweepOptionsLayout.addWidget(self.continualBox)
        self.saveLayout = QtWidgets.QHBoxLayout()
        self.saveLayout.setObjectName("saveLayout")
        self.saveBox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.saveBox.setChecked(True)
        self.saveBox.setObjectName("saveBox")
        self.saveLayout.addWidget(self.saveBox)
        self.sweepOptionsLayout.addLayout(self.saveLayout)
        self.livePlotBox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.livePlotBox.setChecked(True)
        self.livePlotBox.setObjectName("livePlotBox")
        self.sweepOptionsLayout.addWidget(self.livePlotBox)
        self.plotbinLayout = QtWidgets.QHBoxLayout()
        self.plotbinLayout.setObjectName("plotbinLayout")
        self.plotbinLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.plotbinLabel.setObjectName("plotbinLabel")
        self.plotbinLayout.addWidget(self.plotbinLabel)
        self.plotbinEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.plotbinEdit.setObjectName("plotbinEdit")
        self.plotbinLayout.addWidget(self.plotbinEdit)
        self.sweepOptionsLayout.addLayout(self.plotbinLayout)
        self.followParamWidget = QtWidgets.QListWidget(editSweep)
        self.followParamWidget.setGeometry(QtCore.QRect(20, 180, 201, 81))
        self.followParamWidget.setObjectName("followParamWidget")
        self.followParamLabel = QtWidgets.QLabel(editSweep)
        self.followParamLabel.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.followParamLabel.setObjectName("followParamLabel")

        self.retranslateUi(editSweep)
        self.buttonBox.accepted.connect(editSweep.accept)
        self.buttonBox.rejected.connect(editSweep.reject)
        QtCore.QMetaObject.connectSlotsByName(editSweep)

    def retranslateUi(self, editSweep):
        _translate = QtCore.QCoreApplication.translate
        editSweep.setWindowTitle(_translate("editSweep", "Dialog"))
        self.paramLabel.setText(_translate("editSweep", "Set parameter:"))
        self.startLabel.setText(_translate("editSweep", "Start"))
        self.endLabel.setText(_translate("editSweep", "End"))
        self.stepLabel.setText(_translate("editSweep", "Step"))
        self.stepsecLabel.setText(_translate("editSweep", "Step/sec"))
        self.deleteButton.setText(_translate("editSweep", "Delete"))
        self.bidirectionalBox.setText(_translate("editSweep", "Bidirectional"))
        self.continualBox.setText(_translate("editSweep", "Continual"))
        self.saveBox.setText(_translate("editSweep", "Save data"))
        self.livePlotBox.setText(_translate("editSweep", "Live plot"))
        self.plotbinLabel.setText(_translate("editSweep", "Plot bin"))
        self.plotbinEdit.setText(_translate("editSweep", "1"))
        self.followParamLabel.setText(_translate("editSweep", "Followed Parameters:"))
