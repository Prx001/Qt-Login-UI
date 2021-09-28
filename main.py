import sys

from PyQt5.QtCore import Qt, QEvent, QPoint, QPropertyAnimation, QParallelAnimationGroup, QSettings, QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QColor

from Main_widget import Ui_Form
from Password_show_button import ShowPasswordButton
from QWindowButtons import QWindowCloseButton, QWindowMinimizeButton
from Loading_widget import LoadingWidget


class Form(QMainWindow, Ui_Form):
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		self.init_ui()

	def init_ui(self):
		self.define_animations()
		self.username_label.clicked.connect(self.username_line_edit.setFocus)
		self.password_label.clicked.connect(self.password_line_edit.setFocus)
		self.username_line_edit.installEventFilter(self)
		self.password_line_edit.installEventFilter(self)
		self.show_password_button = ShowPasswordButton(self, bg_color=QColor(0, 0, 0, 0))
		self.show_password_button.move(320, 295)
		self.show_password_button.visibilityChanged.connect(lambda: self.password_line_edit.setEchoMode(
			QLineEdit.Normal) if self.show_password_button.enabled else self.password_line_edit.setEchoMode(
			QLineEdit.Password))
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.window_close_button = QWindowCloseButton(self)
		self.window_close_button.move(self.width() - self.window_close_button.width(), 0)
		self.window_close_button.clicked.connect(self.close)
		self.window_minimize_button = QWindowMinimizeButton(self, bg_hover_color=QColor(101, 101, 101),
		                                                    bg_press_color=QColor(117, 117, 117))
		self.window_minimize_button.move(
			self.width() - self.window_close_button.width() - self.window_minimize_button.width(), 0)
		self.window_minimize_button.clicked.connect(self.showMinimized)
		self.log_in_button.clicked.connect(self.login)
		self.loading_widget = LoadingWidget(self, back_circle_color=QColor(67, 0, 202),
		                                    front_arc_color=QColor(255, 255, 255))
		self.loading_widget.move(185, 392)
		self.loading_widget.hide()

		self.settings = QSettings("Parsa.py", "Qt-Login-UI")
		if self.settings.contains("username") and self.settings.contains("password"):
			self.username_line_edit.setText(self.settings.value("username"))
			self.password_line_edit.setText(self.settings.value("password"))
			self.username_label_anims.start()
			self.password_label_anims.start()
			self.checkBox.setChecked(True)
			self.seconds = 10
			self.log_in_button.setText(f"Login ({self.seconds})")
			self.timer = QBasicTimer()
			self.username_line_edit.textEdited.connect(self.timer.stop)
			self.username_line_edit.textEdited.connect(lambda: self.log_in_button.setText("Login"))
			self.password_line_edit.textEdited.connect(self.timer.stop)
			self.password_line_edit.textEdited.connect(lambda: self.log_in_button.setText("Login"))
			self.timer.start(1000, self)
		self.show()

	def timerEvent(self, timer_event):
		if self.seconds > 0:
			self.seconds -= 1
			self.log_in_button.setText(f"Login ({self.seconds})")
		elif self.seconds == 0:
			self.login()
			self.timer.stop()
		return super().timerEvent(timer_event)

	def login(self):
		try:
			self.timer.stop()
		except AttributeError:
			pass
		self.log_in_button.setText("")
		self.loading_widget.show()

		if self.checkBox.isChecked():
			self.settings.setValue("username", self.username_line_edit.text())
			self.settings.setValue("password", self.password_line_edit.text())
		elif not self.checkBox.isChecked():
			self.settings.clear()

	def define_animations(self):
		self.username_label_anim = QPropertyAnimation(self.username_label, b"pos")
		self.username_label_anim.setDuration(150)
		self.username_label_anim.setStartValue(QPoint(62, 232))
		self.username_label_anim.setEndValue(QPoint(54, 220))

		self.username_label_anim_reverse = QPropertyAnimation(self.username_label, b"pos")
		self.username_label_anim_reverse.setDuration(150)
		self.username_label_anim_reverse.setStartValue(QPoint(54, 220))
		self.username_label_anim_reverse.setEndValue(QPoint(62, 232))

		self.username_label_font_anim = QPropertyAnimation(self.username_label, b"point_size")
		self.username_label_font_anim.setDuration(150)
		self.username_label_font_anim.setStartValue(9)
		self.username_label_font_anim.setEndValue(6)

		self.username_label_font_anim_reverse = QPropertyAnimation(self.username_label, b"point_size")
		self.username_label_font_anim_reverse.setDuration(150)
		self.username_label_font_anim_reverse.setStartValue(6)
		self.username_label_font_anim_reverse.setEndValue(9)

		self.password_label_anim = QPropertyAnimation(self.password_label, b"pos")
		self.password_label_anim.setDuration(150)
		self.password_label_anim.setStartValue(QPoint(62, 295))
		self.password_label_anim.setEndValue(QPoint(54, 283))

		self.password_label_anim_reverse = QPropertyAnimation(self.password_label, b"pos")
		self.password_label_anim_reverse.setDuration(150)
		self.password_label_anim_reverse.setStartValue(QPoint(54, 283))
		self.password_label_anim_reverse.setEndValue(QPoint(62, 295))

		self.password_label_font_anim = QPropertyAnimation(self.password_label, b"point_size")
		self.password_label_font_anim.setDuration(150)
		self.password_label_font_anim.setStartValue(9)
		self.password_label_font_anim.setEndValue(6)

		self.password_label_font_anim_reverse = QPropertyAnimation(self.password_label, b"point_size")
		self.password_label_font_anim_reverse.setDuration(150)
		self.password_label_font_anim_reverse.setStartValue(6)
		self.password_label_font_anim_reverse.setEndValue(9)

		self.username_label_anims = QParallelAnimationGroup()
		self.username_label_anims.addAnimation(self.username_label_anim)
		self.username_label_anims.addAnimation(self.username_label_font_anim)

		self.username_label_anims2 = QParallelAnimationGroup()
		self.username_label_anims2.addAnimation(self.username_label_anim_reverse)
		self.username_label_anims2.addAnimation(self.username_label_font_anim_reverse)

		self.password_label_anims = QParallelAnimationGroup()
		self.password_label_anims.addAnimation(self.password_label_anim)
		self.password_label_anims.addAnimation(self.password_label_font_anim)

		self.password_label_anims2 = QParallelAnimationGroup()
		self.password_label_anims2.addAnimation(self.password_label_anim_reverse)
		self.password_label_anims2.addAnimation(self.password_label_font_anim_reverse)

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass

	def eventFilter(self, object, event):
		if object == self.username_line_edit:
			if event.type() == QEvent.FocusIn and self.username_line_edit.text() == "":
				self.username_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.username_line_edit.text() == "":
				self.username_label_anims2.start()
		elif object == self.password_line_edit:
			if event.type() == QEvent.FocusIn and self.password_line_edit.text() == "":
				self.password_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.password_line_edit.text() == "":
				self.password_label_anims2.start()
		return super().eventFilter(object, event)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
