from PyQt5.QtCore import pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtWidgets import QLabel


class PlaceHolderLabel(QLabel):
	clicked = pyqtSignal()

	def __init__(self, text="", parent=None):
		if parent is not None:
			super().__init__(text, parent=parent)
		elif parent is None:
			super().__init__(text)
		self.new_font = self.font()
		self._point_size = self.font().pointSize()
		self.click = None

	def setFont(self, font):
		super().setFont(font)
		self._point_size = self.font().pointSize()

	def get_point_size(self):
		return self._point_size

	@pyqtSlot(int)
	def set_point_size(self, value):
		self._point_size = value
		self.new_font.setPointSize(self._point_size)
		self.setFont(self.new_font)
		self.resize(self.sizeHint())

	point_size = pyqtProperty(int, get_point_size, set_point_size)

	def mousePressEvent(self, event):
		self.click = False
		return super().mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		if self.click is not None:
			self.clicked.emit()
			self.click = None
		return super().mouseReleaseEvent(event)
