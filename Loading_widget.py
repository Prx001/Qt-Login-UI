from PyQt5.QtCore import Qt, QRect, pyqtSlot, pyqtProperty, QPropertyAnimation
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen


class LoadingWidget(QWidget):
	def __init__(self, parent=None, back_circle_color=QColor(160, 160, 164), front_arc_color=QColor(0, 0, 0)):
		if parent is not None:
			super().__init__(parent=parent)
		elif parent is None:
			super().__init__()
		self.back_color = back_circle_color
		self.front_color = front_arc_color
		self.setFixedSize(30, 30)
		self._rotation_degree = 0
		self.anim = QPropertyAnimation(self, b"rotation_degree")
		self.anim.setDuration(1000)
		self.anim.setStartValue(0)
		self.anim.setEndValue(-360)
		self.anim.finished.connect(self.anim.start)
		self.anim.start()

	def get_rotation_degree(self):
		return self._rotation_degree

	@pyqtSlot(int)
	def set_rotation_degree(self, value):
		self._rotation_degree = value
		self.repaint()

	rotation_degree = pyqtProperty(int, get_rotation_degree, set_rotation_degree)

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.HighQualityAntialiasing)
		painter.setPen(QPen(self.back_color, 2, Qt.SolidLine))
		painter.setBrush(Qt.NoBrush)
		painter.drawEllipse(QRect(5, 5, 20, 20))
		painter.setPen(QPen(self.front_color, 2, Qt.SolidLine))
		painter.drawArc(QRect(5, 5, 20, 20), self._rotation_degree * 16, 90 * 16)
		painter.end()
