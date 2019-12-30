class Cube:

    def __init__(self, status, pos_x, pos_y):
        self.status = status
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 80
        self.height = 80

    def is_selected(self, cursor_x, cursor_y):
        """
        If the actual Cube has benn clicked by the cursor
        """
        cube_length = self.pos_x + self.width
        cube_height = self.pos_y + self.height
        if cube_length > cursor_x > self.pos_x:
            if cube_height > cursor_y > self.pos_y:
                return True
        return False
