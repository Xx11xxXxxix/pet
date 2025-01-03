from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class PetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.dragging = False
        self.timer = QTimer()
        # self.timer.timeout.connect(self.update_frame)
        self.load_animations()

    def init_ui(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

    def load_animations(self):
        self.animations = {
            'idle': [QPixmap(f"assets/animations/idle/frame_{i}.png") for i in range(1, 5)],

            'happy': [QPixmap(f"assets/animations/happy/frame_{i}.png") for i in range(1, 5)],
            'sad': [QPixmap(f"assets/animations/sad/frame_{i}.png") for i in range(1, 5)],
            'sick': [QPixmap(f"assets/animations/sick/frame_{i}.png") for i in range(1, 5)]
        }
        max_size=self.gat_max_frame_size()
        for state in self.animations:
            for i in range(len(self.animations[state])):
                if self.animations[state][i].size()!=max_size:
                    self.animations[state][i]=self.animations[state][i].scaled(
                        max_size,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )

        self.current_animation = 'idle'
        self.current_frame = 0

        self.label.setFixedSize(max_size)
        self.setFixedSize(max_size)

        if self.animations['idle']:
            self.label.setPixmap(self.animations['idle'][0])

        self.timer.start(222)

    def gat_max_frame_size(self):
        max_width=0
        max_height=0
        for frames in self.animations.values():
            for frame in frames:
                max_width=max(max_width,frame.width())
                max_height=max(max_height,frame.height())
        return QPixmap(max_width,max_height).size()


    def update_frame(self):
        frames = self.animations.get(self.current_animation, [])
        if frames:
            next_frame=(self.current_frame+1)%len(frames)
            next_pixmap=frames[next_frame]
            self.label.setPixmap(next_pixmap)
            self.current_frame=next_frame

    def play_animation(self, state):
        if state in self.animations and state != self.current_animation:
            self.current_animation = state
            self.current_frame=0
            if self.animations[state]:
                self.label.setPixmap(self.animations[state][0])

    def update_pet_status(self, mood, health):
        if mood >= 80 and health >= 80:
            self.play_animation('happy')
        elif mood >= 50 and health >= 50:
            self.play_animation('idle')
        elif mood >= 30 or health >= 30:
            self.play_animation('sad')
        else:
            self.play_animation('sick')

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.window().pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.window().move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        self.dragging = False
