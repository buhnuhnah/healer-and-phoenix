transform blur_bg_show:
    blur 20.0

transform blur_bg_hide:
    blur 0.0

transform mm_button_hover:
    on idle:
        linear .25 yoffset 0
    on hover:
        linear .25 yoffset 10

image white = "#ffffff"

# SPRITE POSITIONS
transform flip:
    xzoom -1.0

transform center:
    xzoom 1.0 xalign 0.5 yalign 1.0
transform flipCenter:
    xzoom -1.0 xalign 0.5 yalign 1.0

transform leftish:
    xzoom 1.0 xalign 0.3 yalign 1.0
transform flipLeftish:
    xzoom -1.0 xalign 0.3 yalign 1.0

transform rightish:
    xzoom 1.0 xalign 0.65 yalign 1.0
transform flipRightish:
    xzoom -1.0 xalign 0.65 yalign 1.0

transform farleft:
    xzoom 1.0 xalign 0.0 yalign 1.0
transform flipFarleft:
    xzoom -1.0 xalign 0.0 yalign 1.0

transform farright:
    xzoom 1.0 xalign 0.95 yalign 1.0
transform flipFarright:
    xzoom -1.0 xalign 0.95 yalign 1.0

transform flipLeft:
    xzoom -1.0 xalign 0 yalign 1.0
transform left:
    xzoom 1.0 xalign 0 yalign 1.0

transform flipRight:
    xzoom -1.0 xalign 1.0 yalign 1.0
transform right:
    xzoom 1.0 xalign 1.0 yalign 1.0
