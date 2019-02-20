from typing import Tuple, Set, Iterable, List

class IGH_ListItem:
    def ComputeSize (self, layoutWidth : int) -> Size: ...
    @property
    def BoundingBox (self) -> Rectangle: ...
    @BoundingBox.setter
    def BoundingBox (self, Value : Rectangle) -> None: ...
    def RenderItem (self, G : Graphics, destination : Rectangle) -> None: ...
class GH_SimpleListItem:
    def __init__(self): ...
    @property
    def BoundingBox (self) -> Rectangle: ...
    @BoundingBox.setter
    def BoundingBox (self, Value : Rectangle) -> None: ...
    @property
    def Text (self) -> str: ...
    @Text.setter
    def Text (self, Value : str) -> None: ...
    @property
    def Colour (self) -> Color: ...
    @Colour.setter
    def Colour (self, Value : Color) -> None: ...
    @property
    def Alignment (self) -> StringAlignment: ...
    @Alignment.setter
    def Alignment (self, Value : StringAlignment) -> None: ...
    def ComputeSize (self, layoutWidth : int) -> Size: ...
    def RenderItem (self, G : Graphics, destination : Rectangle) -> None: ...
class GH_FormattedListItem(GH_SimpleListItem):
    def __init__(self): ...
    @property
    def Font (self) -> Font: ...
    @Font.setter
    def Font (self, Value : Font) -> None: ...
    @property
    def Type (self) -> int: ...
    @Type.setter
    def Type (self, Value : int) -> None: ...
    @property
    def Wrap (self) -> bool: ...
    @Wrap.setter
    def Wrap (self, Value : bool) -> None: ...
    def ComputeSize (self, layoutWidth : int) -> Size: ...
    def RenderItem (self, G : Graphics, destination : Rectangle) -> None: ...