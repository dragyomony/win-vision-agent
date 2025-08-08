import cv2, numpy as np, pyautogui as pag

def screenshot():
    img = pag.screenshot()
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def match_template(screen_bgr, template_bgr, threshold=0.85):
    res = cv2.matchTemplate(screen_bgr, template_bgr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    h, w = template_bgr.shape[:2]
    if max_val >= threshold:
        x, y = max_loc
        center = (x + w // 2, y + h // 2)
        return center, max_val
    return None, max_val

def find_on_screen(template_path, threshold=0.85):
    screen = screenshot()
    tmpl = cv2.imread(template_path)
    return match_template(screen, tmpl, threshold)
