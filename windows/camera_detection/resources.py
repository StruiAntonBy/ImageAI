from windows.image_detection.resources import NAME_LABELS

WINDOW_SIZE = (360, 320)

NAME_LABELS = list(NAME_LABELS)
NAME_LABELS[0] = "Введите индекс камеры:"
NAME_LABELS.insert(3, "Введите количество кадров в секунду:")
NAME_LABELS.insert(4, "Введите количество секунд съемки:")

SPIN_BOX_FRAMES_PER_SECOND = {
    "Range": (1, 60),
    "Default": 20,
}
SPIN_BOX_DETECTION_TIMEOUT = {
    "Range": (1, 10000),
    "Default": 5,
}
