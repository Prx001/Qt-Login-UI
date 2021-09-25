import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen


class QWindowCloseButton(QPushButton):
	def __init__(self, parent=None, bg_color=QColor(0, 0, 0, 0), bg_hover_color=QColor(234, 40, 56),
	             bg_press_color=QColor(241, 112, 122)):
		if parent is not None:
			super().__init__("", parent=parent)
		elif parent is None:
			super().__init__("")
		self.setFixedSize(46, 32)
		self.normal_color = bg_color
		self.hover_color = bg_hover_color
		self.press_color = bg_press_color
		self.current_color = self.normal_color

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(self.current_color, Qt.SolidPattern))
		painter.drawRect(0, 0, self.width(), self.height())
		painter.setPen(QPen(QColor(255, 255, 255), 1, Qt.SolidLine))
		painter.drawLine(18, 12, 27, 21)
		painter.drawLine(27, 12, 18, 21)
		painter.end()

	def enterEvent(self, event):
		self.current_color = self.hover_color
		self.repaint()

	def leaveEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()

	def mousePressEvent(self, event):
		self.current_color = self.press_color
		self.repaint()
		return super().mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()
		return super().mouseReleaseEvent(event)


class QWindowMinimizeButton(QPushButton):
	def __init__(self, parent=None, bg_color=QColor(0, 0, 0, 0), bg_hover_color=QColor(53, 59, 69),
	             bg_press_color=QColor(70, 79, 91)):
		if parent is not None:
			super().__init__("", parent=parent)
		elif parent is None:
			super().__init__("")
		self.setFixedSize(46, 32)
		self.normal_color = bg_color
		self.hover_color = bg_hover_color
		self.press_color = bg_press_color
		self.current_color = self.normal_color

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(QBrush(self.current_color, Qt.SolidPattern))
		painter.drawRect(0, 0, self.width(), self.height())
		painter.setPen(QPen(QColor(255, 255, 255), 1, Qt.SolidLine))
		painter.drawLine(18, 15, 27, 15)
		painter.end()

	def enterEvent(self, event):
		self.current_color = self.hover_color
		self.repaint()

	def leaveEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()

	def mousePressEvent(self, event):
		self.current_color = self.press_color
		self.repaint()
		return super().mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		self.current_color = self.normal_color
		self.repaint()
		return super().mouseReleaseEvent(event)

