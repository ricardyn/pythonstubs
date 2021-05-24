from typing import Tuple, Set, Iterable, List


class EventArgs:
    @property
    def DataType(self) -> Guid: ...


class EventInfoArgs:
    @property
    def DataType(self) -> Guid: ...
    @property
    def EventInfoPtr(self) -> IntPtr: ...


class ProviderIds:
    def __init__(self): ...
    @property
    def ContentChildSlot() -> Guid: ...
    @property
    def ContentDatabase() -> Guid: ...
    @property
    def ContentDisplayCollection() -> Guid: ...
    @property
    def ContentEditorSettings() -> Guid: ...
    @property
    def ContentLookup() -> Guid: ...
    @property
    def ContentParam() -> Guid: ...
    @property
    def ContentPreviewRendered() -> Guid: ...
    @property
    def ContentSelection() -> Guid: ...
    @property
    def ContentSelectionForSetParams() -> Guid: ...
    @property
    def ContentUIs() -> Guid: ...
    @property
    def ContentUpdatePreviewMarkersEventInfo() -> Guid: ...
    @property
    def CurrentEnvironment() -> Guid: ...
    @property
    def Decals() -> Guid: ...
    @property
    def Dithering() -> Guid: ...
    @property
    def GroundPlane() -> Guid: ...
    @property
    def ImageFileInfo() -> Guid: ...
    @property
    def LinearWorkflow() -> Guid: ...
    @property
    def NamedItem() -> Guid: ...
    @property
    def NewContentControlAssignBy() -> Guid: ...
    @property
    def NullGuid() -> Guid: ...
    @property
    def PreviewSettings() -> Guid: ...
    @property
    def RdkEdit() -> Guid: ...
    @property
    def RdkRendering() -> Guid: ...
    @property
    def RdkRenderingGamma() -> Guid: ...
    @property
    def RdkRenderingPostEffectBloom() -> Guid: ...
    @property
    def RdkRenderingPostEffectDOF() -> Guid: ...
    @property
    def RdkRenderingPostEffectFog() -> Guid: ...
    @property
    def RdkRenderingPostEffectGlare() -> Guid: ...
    @property
    def RdkRenderingPostEffectGlow() -> Guid: ...
    @property
    def RdkRenderingPostEffects() -> Guid: ...
    @property
    def RdkRenderingProgress() -> Guid: ...
    @property
    def RdkRenderingToneMapping() -> Guid: ...
    @property
    def RenderChannels() -> Guid: ...
    @property
    def RhinoSettings() -> Guid: ...
    @property
    def SelectionNavigator() -> Guid: ...
    @property
    def Skylight() -> Guid: ...
    @property
    def Sun() -> Guid: ...
    @property
    def Undo() -> Guid: ...
    @property
    def UndoRecord() -> Guid: ...
