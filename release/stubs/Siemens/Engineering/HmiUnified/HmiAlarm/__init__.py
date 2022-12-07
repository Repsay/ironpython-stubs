# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiAlarm calls itself HmiAlarm
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiAlarmClass(HmiBase, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Specifies alarm class. """
    def Delete(self):
        """
        Delete(self: HmiAlarmClass)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiAlarmClass, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAlarmClass) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAlarmClass) -> str
        
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

    AcknowledgedClearedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies Alarm incoming outgoing acknowledge or AcknowledgedCleared status

Get: AcknowledgedClearedState(self: HmiAlarmClass) -> HmiAcknowledgedClearedState

"""

    AcknowledgedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies Alarm incoming acknowledge or acknowledged status

Get: AcknowledgedState(self: HmiAlarmClass) -> HmiAcknowledgedState

"""

    ClearedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies Alarm coming going or cleared status

Get: ClearedState(self: HmiAlarmClass) -> HmiClearedState

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the alarm class number that identifies the alarm class in runtime

Get: Id(self: HmiAlarmClass) -> UInt32

"""

    IsSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies if alarm class is system provided

Get: IsSystem(self: HmiAlarmClass) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name

Get: Name(self: HmiAlarmClass) -> str

Set: Name(self: HmiAlarmClass) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiAlarmClass) -> IEngineeringObject

"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the alarm priority

Get: Priority(self: HmiAlarmClass) -> Byte

Set: Priority(self: HmiAlarmClass) = value
"""

    RaisedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alarm incoming or raised status

Get: RaisedState(self: HmiAlarmClass) -> HmiRaisedState

"""

    StateMachine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the statemachine of the alarm class

Get: StateMachine(self: HmiAlarmClass) -> HmiAlarmStateMachine

Set: StateMachine(self: HmiAlarmClass) = value
"""



class HmiAlarmClassComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiAlarmClass], IEquatable[object]):
    """ HmiAlarmClassComposition """
    def Contains(self, item):
        """
        Contains(self: HmiAlarmClassComposition, item: HmiAlarmClass) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: HmiAlarmClassComposition, name: str) -> HmiAlarmClass
        
            Create new object
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmClass
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiAlarmClassComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiAlarmClassComposition, name: str) -> HmiAlarmClass
        
            Find
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAlarmClass
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiAlarmClassComposition) -> IEnumerator[HmiAlarmClass]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAlarmClassComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiAlarmClassComposition, item: HmiAlarmClass) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAlarmClassComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiAlarmClass](enumerable: IEnumerable[HmiAlarmClass], value: HmiAlarmClass) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: HmiAlarmClassComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiAlarmClassComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiAlarmClassComposition) -> IEngineeringObject

"""



class HmiAnalogAlarm(AlarmBase, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiAnalogAlarm """
    def Delete(self):
        """
        Delete(self: HmiAnalogAlarm)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiAnalogAlarm, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAnalogAlarm) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAnalogAlarm) -> str
        
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

    Condition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies Limit Mode.

Get: Condition(self: HmiAnalogAlarm) -> HmiAlarmCondition

Set: Condition(self: HmiAnalogAlarm) = value
"""

    ConditionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Condition Value can be specified as constant value.

Get: ConditionValue(self: HmiAnalogAlarm) -> object

Set: ConditionValue(self: HmiAnalogAlarm) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name

Get: Name(self: HmiAnalogAlarm) -> str

Set: Name(self: HmiAnalogAlarm) = value
"""



class HmiAnalogAlarmComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiAnalogAlarm], IEquatable[object]):
    """ HmiAnalogAlarm Composition """
    def Contains(self, item):
        """
        Contains(self: HmiAnalogAlarmComposition, item: HmiAnalogAlarm) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: HmiAnalogAlarmComposition, name: str) -> HmiAnalogAlarm
        
            Create
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAnalogAlarm
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiAnalogAlarmComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiAnalogAlarmComposition, name: str) -> HmiAnalogAlarm
        
            Find
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiAnalogAlarm
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiAnalogAlarmComposition) -> IEnumerator[HmiAnalogAlarm]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiAnalogAlarmComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiAnalogAlarmComposition, item: HmiAnalogAlarm) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiAnalogAlarmComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiAnalogAlarm](enumerable: IEnumerable[HmiAnalogAlarm], value: HmiAnalogAlarm) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: HmiAnalogAlarmComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiAnalogAlarmComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiAnalogAlarmComposition) -> IEngineeringObject

"""



class HmiDiscreteAlarm(AlarmBase, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ HmiDiscreteAlarm """
    def Delete(self):
        """
        Delete(self: HmiDiscreteAlarm)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiDiscreteAlarm, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiDiscreteAlarm) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiDiscreteAlarm) -> str
        
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name

Get: Name(self: HmiDiscreteAlarm) -> str

Set: Name(self: HmiDiscreteAlarm) = value
"""

    RaisedStateTagBitNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Trigger bit on the trigger tag

Get: RaisedStateTagBitNumber(self: HmiDiscreteAlarm) -> UInt32

Set: RaisedStateTagBitNumber(self: HmiDiscreteAlarm) = value
"""

    TriggerMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specify trigger mode for discrete alarm

Get: TriggerMode(self: HmiDiscreteAlarm) -> HmiDiscreteAlarmTriggerMode

Set: TriggerMode(self: HmiDiscreteAlarm) = value
"""



class HmiDiscreteAlarmComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiDiscreteAlarm], IEquatable[object]):
    """ HmiDiscreteAlarmComposition """
    def Contains(self, item):
        """
        Contains(self: HmiDiscreteAlarmComposition, item: HmiDiscreteAlarm) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: HmiDiscreteAlarmComposition, name: str) -> HmiDiscreteAlarm
        
            Create
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiDiscreteAlarm
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiDiscreteAlarmComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiDiscreteAlarmComposition, name: str) -> HmiDiscreteAlarm
        
            Find
        
            name: Name
            Returns: Siemens.Engineering.HmiUnified.HmiAlarm.HmiDiscreteAlarm
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiDiscreteAlarmComposition) -> IEnumerator[HmiDiscreteAlarm]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiDiscreteAlarmComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiDiscreteAlarmComposition, item: HmiDiscreteAlarm) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiDiscreteAlarmComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiDiscreteAlarm](enumerable: IEnumerable[HmiDiscreteAlarm], value: HmiDiscreteAlarm) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: HmiDiscreteAlarmComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiDiscreteAlarmComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiDiscreteAlarmComposition) -> IEngineeringObject

"""



# variables with complex values

