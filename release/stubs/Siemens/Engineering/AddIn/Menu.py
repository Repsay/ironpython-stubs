# encoding: utf-8
# module Siemens.Engineering.AddIn.Menu calls itself Menu
# from Siemens.Engineering.AddIn, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# functions

def ActionItem(*args, **kwargs): # real signature unknown
    """  """
    pass

def MenuSelectionProvider(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class ActionItemStyle(object):
    """  """

class CheckBoxActionItemStyle(ActionItemStyle):
    """  """
    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: State(self: CheckBoxActionItemStyle) -> CheckBoxState

Set: State(self: CheckBoxActionItemStyle) = value
"""



class CheckBoxState(Enum, IComparable, IFormattable, IConvertible):
    """ enum CheckBoxState, values: Checked (1), Unchecked (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Checked = None
    Unchecked = None
    value__ = None


class ChildItemFactory(object, IMenuItemFactoryPrivate, ISubmenuFactoryPrivate, IActionItemFactoryPrivate):
    """  """
    def AddActionItem(self, defaultLabelText, clickDelegate, updateStatusDelegate=None):
        """
        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject]
        AddActionItem[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject]
        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItem[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        AddActionItem[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        pass

    def AddActionItemWithCheckBox(self, defaultLabelText, clickDelegate, updateStatusDelegate):
        """
        AddActionItemWithCheckBox[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject]
        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItemWithCheckBox[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, CheckBoxActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        pass

    def AddActionItemWithRadioButton(self, defaultLabelText, clickDelegate, updateStatusDelegate):
        """
        AddActionItemWithRadioButton[TSelectedObject](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject]
        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2]
        AddActionItemWithRadioButton[(TSelectedObject1, TSelectedObject2, TSelectedObject3)](self: ChildItemFactory, defaultLabelText: str, clickDelegate: OnClickDelegate, updateStatusDelegate: OnUpdateStatusDelegate[TSelectedObject1, TSelectedObject2, TSelectedObject3, RadioButtonActionItemStyle]) -> ActionItem[TSelectedObject1, TSelectedObject2, TSelectedObject3]
        """
        pass

    def AddSubmenu(self, defaultLabelText):
        """ AddSubmenu(self: ChildItemFactory, defaultLabelText: str) -> Submenu """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ContextMenuAddIn(object):
    """  """
    def BuildContextMenuItems(self, *args): #cannot find CLR method
        """ BuildContextMenuItems(self: ContextMenuAddIn, addInRootSubmenu: Submenu) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, displayName: str) """
        pass


class MenuItem(object):
    """  """

class MenuStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum MenuStatus, values: Disabled (1), Enabled (0), Hidden (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Disabled = None
    Enabled = None
    Hidden = None
    value__ = None


class RadioButtonActionItemStyle(ActionItemStyle):
    """  """
    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: State(self: RadioButtonActionItemStyle) -> RadioButtonState

Set: State(self: RadioButtonActionItemStyle) = value
"""



class RadioButtonState(Enum, IComparable, IFormattable, IConvertible):
    """ enum RadioButtonState, values: Selected (1), Unselected (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Selected = None
    Unselected = None
    value__ = None


class Submenu(MenuItem, IMenuItemContainerPrivate):
    """  """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultLabelText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: DefaultLabelText(self: Submenu) -> str

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Items(self: Submenu) -> ChildItemFactory

"""



