import cv2
import numpy as np
import tempfile

def analyze_hand(image_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(image_file.read())
        tmp_path = tmp.name

    img = cv2.imread(tmp_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Đếm số đường nét phát hiện được
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=10)
    num_lines = len(lines) if lines is not None else 0

    # Mô tả đơn giản hoá
    description = "Tôi phát hiện khoảng {} đường chỉ tay nổi bật. ".format(num_lines)
    if num_lines > 10:
        description += "Đây có thể là bàn tay với đường sinh mệnh, trí tuệ và tình cảm rõ ràng."
    elif num_lines > 3:
        description += "Các đường chỉ tay hơi mờ, cần góc chụp tốt hơn để phân tích kỹ."
    else:
        description += "Ảnh không rõ, đề nghị chụp lại bàn tay ở điều kiện sáng rõ hơn."

    return description
