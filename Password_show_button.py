from PyQt5.QtCore import Qt, QRect, pyqtSignal, pyqtSlot, pyqtProperty, QPropertyAnimation, QParallelAnimationGroup
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor


class ShowPasswordButton(QPushButton):
	visibilityChanged = pyqtSignal()

	def __init__(self, parent, bg_color=QColor(217, 217, 217), hover_bg_color=QColor(199, 199, 199),
	             press_bg_color=QColor(179, 179, 179)):
		if parent is not None:
			super().__init__("", parent=parent)
		elif parent is None:
			super().__init__("")
		self.setFixedSize(20, 20)
		self.enabled = False
		self.click = False
		self.normal_color = bg_color
		self.hover_color = hover_bg_color
		self.press_color = press_bg_color
		self.current_color = self.normal_color
		self._over_line_x = 20
		self._over_line_y = 0
		self.over_line_x_anim = QPropertyAnimation(self, b"over_line_x")
		self.over_line_x_anim.setDuration(200)
		self.over_line_y_anim = QPropertyAnimation(self, b"over_line_y")
		self.over_line_y_anim.setDuration(200)
		self.anims = QParallelAnimationGroup()
		self.anims.addAnimation(self.over_line_x_anim)
		self.anims.addAnimation(self.over_line_y_anim)

	def get_over_line_x(self):
		return self._over_line_x

	@pyqtSlot(int)
	def set_over_line_x(self, value):
		self._over_line_x = value
		self.repaint()

	over_line_x = pyqtProperty(int, get_over_line_x, set_over_line_x)

	def get_over_line_y(self):
		return self._over_line_y

	@pyqtSlot(int)
	def set_over_line_y(self, value):
		self._over_line_y = value
		self.repaint()

	over_line_y = pyqtProperty(int, get_over_line_y, set_over_line_y)

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(self.current_color, Qt.SolidPattern))
		painter.drawRoundedRect(0, 0, self.width(), self.height(), 4, 4)
		painter.setPen(QPen(QColor(0, 0, 0), 1.2, Qt.SolidLine))
		painter.setBrush(Qt.NoBrush)
		painter.drawArc(QRect(2, 4, 16, 16), 0 * 16, 180 * 16)
		painter.drawEllipse(8, 8, 4, 4)
		if self._over_line_x != 20 and self._over_line_y != 0:
			painter.drawLine(20, 0, self._over_line_x, self._over_line_y)
		painter.end()

	def enterEvent(self, event):
		self.current_color = self.hover_color
		self.repaint()
		return super().enterEvent(event)

	def leaveEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()
		return super().leaveEvent(event)

	def mousePressEvent(self, event):
		self.click = True
		self.current_color = self.press_color
		self.repaint()

	def mouseReleaseEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()
		if self.click:
			self.click_event()
			self.click = False

	def click_event(self):
		if not self.enabled:
			self.enabled = True
			self.anims.animationAt(0).setEndValue(2)
			self.anims.animationAt(1).setEndValue(18)
			self.anims.start()
			self.visibilityChanged.emit()
		elif self.enabled:
			self.enabled = False
			self.anims.animationAt(0).setEndValue(20)
			self.anims.animationAt(1).setEndValue(0)
			self.anims.start()
			self.visibilityChanged.emit()
