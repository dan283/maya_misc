import maya.cmds as cmds

class RotateAndKeyframeUI:
    def __init__(self):
        self.window_name = "RotateAndKeyframeUI"
        
    def create_window(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name, window=True)
        
        cmds.window(self.window_name, title="Rotate and Keyframe", sizeable=False)
        cmds.columnLayout(adjustableColumn=True)
        
        cmds.text(label="Rotation Settings", align="center")
        self.degrees_field = cmds.intField(value=0, minValue=0, width=200)
        self.frames_field = cmds.intField(value=1, minValue=1, width=200)
        
        cmds.button(label="Rotate and Keyframe", command=self.rotate_and_keyframe)
        
        cmds.showWindow(self.window_name)
        
def rotate_and_keyframe(self, *args):
    degrees = cmds.intField(self.degrees_field, query=True, value=True)
    frames = cmds.intField(self.frames_field, query=True, value=True)
    
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("Please select an object to rotate.")
        return
    
    for obj in selected_objects:
        current_rotation = cmds.getAttr(obj + ".rotateY")
        end_frame = int(cmds.playbackOptions(q=True, max=True))
        for frame in range(1, end_frame + 1, frames):
            cmds.setKeyframe(obj, attribute="rotateY", t=frame, value=current_rotation)
            current_rotation += degrees

            # Switch to step tangents
            cmds.keyTangent(obj, attribute="rotateY", itt="step", ott="step")


ui = RotateAndKeyframeUI()
ui.create_window()
