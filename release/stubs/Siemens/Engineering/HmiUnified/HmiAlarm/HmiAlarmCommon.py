# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmCommon calls itself HmiAlarmCommon
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AlarmBase(HmiBase, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ This is base class for AnalogAlarm and DiscreteAlarm """
    def Equals(self, obj):
        """
        Equals(self: AlarmBase, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: AlarmBase) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: AlarmBase) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlarmClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the alarm class

Get: AlarmClass(self: AlarmBase) -> str

Set: AlarmClass(self: AlarmBase) = value
"""

    AlarmParameterTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the alarm pararmeters

Get: AlarmParameterTags(self: AlarmBase) -> object

Set: AlarmParameterTags(self: AlarmBase) = value
"""

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the area of the alarm

Get: Area(self: AlarmBase) -> str

Set: Area(self: AlarmBase) = value
"""

    EventText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies event/alarm text of alarm.

Get: EventText(self: AlarmBase) -> MultilingualText

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alarm row identification Number

Get: Id(self: AlarmBase) -> UInt32

Set: Id(self: AlarmBase) = value
"""

    InfoText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the multilingual InfoText of the alarm

Get: InfoText(self: AlarmBase) -> MultilingualText

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the origin of the alarm

Get: Origin(self: AlarmBase) -> str

Set: Origin(self: AlarmBase) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: AlarmBase) -> IEngineeringObject

"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the alarm priority

Get: Priority(self: AlarmBase) -> Byte

Set: Priority(self: AlarmBase) = value
"""

    RaisedStateTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the tag that raise/trigger the alarm

Get: RaisedStateTag(self: AlarmBase) -> str

Set: RaisedStateTag(self: AlarmBase) = value
"""



class AlarmStatusVisuals(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Specifies the alarm status visuals """
    def Equals(self, obj):
        """
        Equals(self: AlarmStatusVisuals, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: AlarmStatusVisuals, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: AlarmStatusVisuals) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: AlarmStatusVisuals, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: AlarmStatusVisuals) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BackColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the background color

Get: BackColor(self: AlarmStatusVisuals) -> Color

Set: BackColor(self: AlarmStatusVisuals) = value
"""

    Flashing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the flashing color

Get: Flashing(self: AlarmStatusVisuals) -> bool

Set: Flashing(self: AlarmStatusVisuals) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: AlarmStatusVisuals) -> IEngineeringObject

"""

    TextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the text color

Get: TextColor(self: AlarmStatusVisuals) -> Color

Set: TextColor(self: AlarmStatusVisuals) = value
"""



class HmiAcknowledgedClearedState(AlarmStatusVisuals, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiAcknowledgedClearedState """
    def Equals(self, obj):
        """
        Equals(self: HmiAcknowledgedClearedState, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAcknowledgedClearedState) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAcknowledgedClearedState) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiAcknowledgedClearedState) -> IEngineeringObject

"""



class HmiAcknowledgedState(AlarmStatusVisuals, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiAcknowledgedState """
    def Equals(self, obj):
        """
        Equals(self: HmiAcknowledgedState, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAcknowledgedState) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAcknowledgedState) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiAcknowledgedState) -> IEngineeringObject

"""



class HmiAlarmCondition(Enum, IComparable, IFormattable, IConvertible):
    """
    HmiAlarmCondition
    
    enum HmiAlarmCondition, values: Equal (2), LowerLimit (0), LowerLimitOrEqual (4), NotEqual (3), UpperLimit (1), UpperLimitOrEqual (5)
    """
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

    Equal = None
    LowerLimit = None
    LowerLimitOrEqual = None
    NotEqual = None
    UpperLimit = None
    UpperLimitOrEqual = None
    value__ = None


class HmiAlarmStateMachine(Enum, IComparable, IFormattable, IConvertible):
    """
    HmiAlarmStateMachine
    
    enum HmiAlarmStateMachine, values: Raise (0), RaiseClear (3), RaiseClearOptionalAcknowledgement (6), RaiseClearRequiresAcknowledgement (7), RaiseClearRequiresAcknowledgementAndReset (15), RaiseRequiresAcknowledgement (5)
    """
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

    Raise = None
    RaiseClear = None
    RaiseClearOptionalAcknowledgement = None
    RaiseClearRequiresAcknowledgement = None
    RaiseClearRequiresAcknowledgementAndReset = None
    RaiseRequiresAcknowledgement = None
    value__ = None


class HmiClearedState(AlarmStatusVisuals, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiClearedState """
    def Equals(self, obj):
        """
        Equals(self: HmiClearedState, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiClearedState) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiClearedState) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiClearedState) -> IEngineeringObject

"""



class HmiDiscreteAlarmTriggerMode(Enum, IComparable, IFormattable, IConvertible):
    """
    HmiDiscreteAlarmTriggerMode
    
    enum HmiDiscreteAlarmTriggerMode, values: OnFallingEdge (1), OnRisingEdge (0)
    """
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

    OnFallingEdge = None
    OnRisingEdge = None
    value__ = None


class HmiRaisedState(AlarmStatusVisuals, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiRaisedState """
    def Equals(self, obj):
        """
        Equals(self: HmiRaisedState, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiRaisedState) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiRaisedState) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiRaisedState) -> IEngineeringObject

"""



