from Box2D import Box2D

import json
from random import randrange
from pathlib import Path


X_START_LEFT, X_START_RIGHT = 200, 600
Y_START_TOP, Y_START_BOTTOM = 200, 600
SIZE_MIN, SIZE_MAX = 5, 20
GROWTH_MIN, GROWTH_MAX = -1, 1
SPEED_MIN, SPEED_MAX = -3, 3


class FakeAnnotation:
    def __init__(self, frame_start, frame_end):
        self.frame_start = frame_start
        self.frame_end = frame_end

        self.x = randrange(X_START_LEFT, X_START_RIGHT)
        self.y = randrange(Y_START_TOP, Y_START_BOTTOM)
        self.width = randrange(SIZE_MIN, SIZE_MAX)
        self.height = randrange(SIZE_MIN, SIZE_MAX)

        self.speed_x = randrange(SPEED_MIN, SPEED_MAX)
        self.speed_y = randrange(SPEED_MIN, SPEED_MAX)
        self.growth = randrange(GROWTH_MIN, GROWTH_MAX)

    def create_annotations(self):
        annotations = {}
        for frame in range(self.frame_start, self.frame_end):
            box = Box2D(self.x, self.y, self.width, self.height)
            annotations[frame] = box.toDict()

            self.update_box()
        
        return annotations
    
    def update_box(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.width += self.growth
        self.height += self.growth
        if self.width < SIZE_MIN:
            self.width = SIZE_MIN
        if self.height < SIZE_MIN:
            self.height = SIZE_MIN
        if self.width > SIZE_MAX:
            self.width = SIZE_MAX
        if self.height > SIZE_MAX:
            self.height = SIZE_MAX


def annotate_file(frame_from, frame_to, annotation_list):
    annotated_file = {}
    for frame in range(frame_from, frame_to):
        frame_annotations = []
        for annotation in annotation_list:
            box = annotation.get(frame)
            if box is not None:
                frame_annotations.append(box)
        annotated_file[frame] = frame_annotations
    
    return annotated_file

if __name__ == "__main__":
    annotation_list = []
    for i in range(5):
        annotation = FakeAnnotation(5, 20)
        annotation_list.append(annotation.create_annotations())

    annotated_file = annotate_file(1, 400, annotation_list)

    with open("Annotations/test_annotation.json", "w") as f:
        json.dump(annotated_file, f, indent=3)
