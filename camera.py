class Camera:
    def __init__(self):
        self.x, self.y = 0, 0

    def apply(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y

    def update(self, target):
        self.x = -(target.rect.x + target.rect.w // 2 - 1920 // 2)
        self.y = -(target.rect.y + target.rect.h // 2 - 1080 // 2)
