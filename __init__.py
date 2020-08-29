bl_info = {
    "name": "Sync Render with Viewport",
    "author": "Nayunis",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "View3D",
    "description": "When clicking on the button it will snychronise all render ports (render/don't render) with the current state of the view ports (visible/not visible). This means anything visible will be rendered and anything invisible will not be rendered.",
    "category": "Interface",
}

import bpy

classes = []

class SyncRenderWithView(bpy.types.Operator):
	"""Synchronise all render ports (render/don't render) with the current state of the view ports (visible/not visible)"""
	bl_idname = "view3d.sync_render_with_viewport"
	bl_label = ""
	
	def execute(self,context):
		for ob in bpy.context.scene.objects: ob.hide_render = ob.hide_get()
		return {"FINISHED"}

classes.append(SyncRenderWithView)

def draw_sync_render_with_view(self, context):
	self.layout.operator("view3d.sync_render_with_viewport",icon="FILE_REFRESH")

def register():
	for cls in classes:
		bpy.utils.register_class(cls)
		
	bpy.types.OUTLINER_HT_header.append(draw_sync_render_with_view)
 
def unregister():
	for cls in reversed(classes):
		bpy.utils.unregister_class(cls)
	
	bpy.types.OUTLINER_HT_header.remove(draw_sync_render_with_view)

if __name__ == "__main__":
    register()
