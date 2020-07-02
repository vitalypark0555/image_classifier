# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class Ui_MainWindow(object):
    fileName = ""
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 691, 341))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageLabel = QLabel(self.horizontalLayoutWidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setAcceptDrops(True)
        self.imageLabel.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.imageLabel)

        self.imageBtn = QPushButton(self.horizontalLayoutWidget)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setStyleSheet("background-color: #2E303E; color: #F2EAED;")
        self.verticalLayout.addWidget(self.imageBtn)

        MainWindow.setStyleSheet("background-color: #2E303E;")
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        font = QFont()
        font.setFamily(u"Cambria")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet("color: #F2EAED;")
        self.verticalLayout_2.addWidget(self.label_4)

        self.classLabel = QLabel(self.horizontalLayoutWidget)
        self.classLabel.setObjectName(u"classLabel")
        font2 = QFont()
        font2.setFamily(u"Cambria")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.classLabel.setFont(font2)
        self.classLabel.setAutoFillBackground(True)
        self.classLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.classLabel)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setStyleSheet("color: #F2EAED;")
        self.verticalLayout_2.addWidget(self.label_3)

        self.predictBtn = QPushButton(self.horizontalLayoutWidget)
        self.predictBtn.setObjectName(u"predictBtn")
        self.predictBtn.setStyleSheet("background-color: #2E303E; color: #F2EAED; ")
        self.verticalLayout_2.addWidget(self.predictBtn)

        self.imageBtn.setIcon(QIcon(QPixmap("image.svg")));
        self.imageBtn.setIconSize(QSize(32, 32));
        self.predictBtn.setIcon(QIcon(QPixmap("predict.svg")));
        self.predictBtn.setIconSize(QSize(32, 32));
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.imageBtn.clicked.connect(self.upload_image)
        self.predictBtn.clicked.connect(self.predict)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MEDICAL IMAGE CLASSIFIER", None))
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QPixmap("upload.png"))
        self.imageLabel.setScaledContents(True)
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"Upload image...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PREDICTED CLASS:", None))
        self.classLabel.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.predictBtn.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
    # retranslateUi

    def upload_image(self):
        self.fileName,_ = QFileDialog.getOpenFileName(None, "Open Image", "~/Desktop/", "Image Files (*.png *.jpg *.bmp)")
        if self.fileName is not "":
            pixmap = QPixmap(self.fileName)
            self.imageLabel.setPixmap(pixmap)
        else:
            self.imageLabel.setPixmap(QPixmap("upload.png"))

    def predict(self):
        img_path = self.fileName
        class_labels = ['dyed-lifted-polyps', 'dyed-resection-margins', 'esophagitis', 'normal-cecum', 'normal-pylorus', 'normal-z-line','polyps','ulcerative-colitis']

        img = image.load_img(img_path, target_size=(224, 224,3))

        img = np.array(img)/255.0
        result = base_model.predict(img[np.newaxis, ...])


        predicted_class = np.argmax(result[0], axis=-1)
        predicted_class_name = class_labels[predicted_class]
        color ="#0ABDA0"
        self.classLabel.setText(str.upper(predicted_class_name))
        self.classLabel.setStyleSheet("color: {};".format(color))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    base_model = tf.keras.models.load_model('resnet.h5')
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
