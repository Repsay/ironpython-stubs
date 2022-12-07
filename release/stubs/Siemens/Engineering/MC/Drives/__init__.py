# encoding: utf-8
# module Siemens.Engineering.MC.Drives calls itself Drives
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DriveObject(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Represents a DriveObject """
    def Equals(self, obj):
        """
        Equals(self: DriveObject, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveObject, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObject) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveObject, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveObject) -> str
        
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

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Accessible parameters on this DriveObject

Get: Parameters(self: DriveObject) -> DriveParameterComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObject) -> IEngineeringObject

"""

    Telegrams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Telegrams

Get: Telegrams(self: DriveObject) -> TelegramComposition

"""



class DriveObjectComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[DriveObject], IEquatable[object]):
    """ Composition of DriveObjects """
    def Contains(self, item):
        """
        Contains(self: DriveObjectComposition, item: DriveObject) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DriveObjectComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DriveObjectComposition) -> IEnumerator[DriveObject]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: DriveObjectComposition, item: DriveObject) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DriveObject](enumerable: IEnumerable[DriveObject], value: DriveObject) -> bool """
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

Get: Count(self: DriveObjectComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: DriveObjectComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: DriveObjectComposition) -> IEngineeringObject

"""



class DriveObjectContainer(DeviceItemFeature, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IEngineeringService):
    """ Container of DriveObjects """
    def Equals(self, obj):
        """
        Equals(self: DriveObjectContainer, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectContainer) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectContainer) -> str
        
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

    DriveObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of DriveObjects

Get: DriveObjects(self: DriveObjectContainer) -> DriveObjectComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObjectContainer) -> IEngineeringObject

"""



class DriveParameter(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a DriveParameter """
    def Equals(self, obj):
        """
        Equals(self: DriveParameter, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveParameter, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveParameter) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveParameter, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveParameter) -> str
        
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

    ArrayIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index of an array parameter

Get: ArrayIndex(self: DriveParameter) -> int

"""

    ArrayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of array elements on array parameter parents

Get: ArrayLength(self: DriveParameter) -> int

"""

    Bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bits of this parameter

Get: Bits(self: DriveParameter) -> DriveParameterComposition

"""

    EnumValueList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of possible labels of the enum parameters

Get: EnumValueList(self: DriveParameter) -> IDictionary[int, str]

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum value of the parameter

Get: MaxValue(self: DriveParameter) -> object

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum value of the parameter

Get: MinValue(self: DriveParameter) -> object

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the parameter

Get: Name(self: DriveParameter) -> str

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Numeric representation of the parameter name

Get: Number(self: DriveParameter) -> int

"""

    ParameterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description of the parameter

Get: ParameterText(self: DriveParameter) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveParameter) -> IEngineeringObject

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unit of the parameter

Get: Unit(self: DriveParameter) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the parameter

Get: Value(self: DriveParameter) -> object

Set: Value(self: DriveParameter) = value
"""



class DriveParameterComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[DriveParameter], IEquatable[object]):
    """ Composition of parameters """
    def Contains(self, item):
        """
        Contains(self: DriveParameterComposition, item: DriveParameter) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DriveParameterComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: DriveParameterComposition, name: str) -> DriveParameter
        
            Find Parameter
        
            name: Name of the parameter
            Returns: Siemens.Engineering.MC.Drives.DriveParameter
        Find(self: DriveParameterComposition, number: int, arrayIndex: int) -> DriveParameter
        
            Find parameter by numeric values
        
            number: Numeric representation of the parameter name
            arrayIndex: Index of an array parameter
            Returns: Siemens.Engineering.MC.Drives.DriveParameter
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DriveParameterComposition) -> IEnumerator[DriveParameter]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveParameterComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: DriveParameterComposition, item: DriveParameter) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveParameterComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DriveParameter](enumerable: IEnumerable[DriveParameter], value: DriveParameter) -> bool """
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

Get: Count(self: DriveParameterComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: DriveParameterComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: DriveParameterComposition) -> IEngineeringObject

"""



class OnlineDriveObject(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Service of the online parameters """
    def Equals(self, obj):
        """
        Equals(self: OnlineDriveObject, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: OnlineDriveObject, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObject) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: OnlineDriveObject, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: OnlineDriveObject) -> str
        
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

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of Parameters

Get: Parameters(self: OnlineDriveObject) -> DriveParameterComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: OnlineDriveObject) -> IEngineeringObject

"""



class OnlineDriveObjectComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[OnlineDriveObject], IEquatable[object]):
    """ Composition of OnlineDriveObjects """
    def Contains(self, item):
        """
        Contains(self: OnlineDriveObjectComposition, item: OnlineDriveObject) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: OnlineDriveObjectComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: OnlineDriveObjectComposition) -> IEnumerator[OnlineDriveObject]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObjectComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: OnlineDriveObjectComposition, item: OnlineDriveObject) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: OnlineDriveObjectComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[OnlineDriveObject](enumerable: IEnumerable[OnlineDriveObject], value: OnlineDriveObject) -> bool """
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

Get: Count(self: OnlineDriveObjectComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: OnlineDriveObjectComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: OnlineDriveObjectComposition) -> IEngineeringObject

"""



class OnlineDriveObjectContainer(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Container of OnlineDriveObjects """
    def Equals(self, obj):
        """
        Equals(self: OnlineDriveObjectContainer, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: OnlineDriveObjectContainer, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveObjectContainer) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: OnlineDriveObjectContainer, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: OnlineDriveObjectContainer) -> str
        
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

    OnlineDriveObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of OnlineDriveObjects

Get: OnlineDriveObjects(self: OnlineDriveObjectContainer) -> OnlineDriveObjectComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: OnlineDriveObjectContainer) -> IEngineeringObject

"""



class Telegram(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a Telegram """
    def CanChangeSize(self, direction, size, keepOriginalAddress):
        """
        CanChangeSize(self: Telegram, direction: AddressIoType, size: int, keepOriginalAddress: bool) -> bool
        
            Returns true if the size of proper channel of the telegram can be changed.
        
            direction: Actual value channel specific size
            size: Setpoint channel specific size
            keepOriginalAddress: Keeps original address if true.
            Returns: System.Boolean
        """
        pass

    def CanChangeTelegram(self, telegramNumber):
        """
        CanChangeTelegram(self: Telegram, telegramNumber: int) -> bool
        
            Returns true if the telegram can be changed to the given standard telegram type.
        
            telegramNumber: Telegram identifier
            Returns: System.Boolean
        """
        pass

    def ChangeSize(self, direction, size, keepOriginalAddress):
        """
        ChangeSize(self: Telegram, direction: AddressIoType, size: int, keepOriginalAddress: bool) -> bool
        
            Change size of the telegram
        
            direction: Actual value channel specific size
            size: Setpoint channel specific size
            keepOriginalAddress: Keeps original address if true.
            Returns: System.Boolean
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Telegram, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttribute(self, name):
        """
        GetAttribute(self: Telegram, name: str) -> object
        
            Gets an attribute with the given name.
        
            name: The name of the attribute to get.
            Returns: The attribute with the given name; otherwise, null.
        """
        pass

    def GetAttributeInfos(self):
        """
        GetAttributeInfos(self: Telegram) -> IList[EngineeringAttributeInfo]
        
            Returns a collection of EngineeringAttributeInfo objects describing the different attributes on this object.
            Returns: A collection of EngineeringAttributeInfo objects describing the different attributes on this object.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Telegram, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Telegram) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetSize(self, direction):
        """
        GetSize(self: Telegram, direction: AddressIoType) -> int
        
            Returns size of the proper channel.
        
            direction: Direction of the channel. Can be Input or Output.
            Returns: System.Int32
        """
        pass

    def SetAttribute(self, name, value):
        """
        SetAttribute(self: Telegram, name: str, value: object)
            Sets value of the attribute.
        
            name: The name of the attribute to set.
            value: The value of the attribute to set.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Telegram, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Telegram) -> str
        
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

    Addresses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Addresses of the specified Telegram

Get: Addresses(self: Telegram) -> AddressComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Telegram) -> IEngineeringObject

"""

    PKW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PKW relevant ActualValue channel

Get: PKW(self: Telegram) -> Telegram

"""

    TelegramNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Telegram identifier

Get: TelegramNumber(self: Telegram) -> int

Set: TelegramNumber(self: Telegram) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of telegram

Get: Type(self: Telegram) -> TelegramType

"""



class TelegramComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[Telegram], IEquatable[object]):
    """ Composition of telegrams: telegrams of a DriveObject """
    def CanInsertAdditionalTelegram(self, inputSize, outputSize):
        """
        CanInsertAdditionalTelegram(self: TelegramComposition, inputSize: int, outputSize: int) -> bool
        
            Checks if adding a new Additional telegram with the given sizes to the drive object would be possible.
        
            inputSize: Size of the input channel.
            outputSize: Size of the output channel.
            Returns: System.Boolean
        """
        pass

    def CanInsertSafetyTelegram(self, telegramNumber):
        """
        CanInsertSafetyTelegram(self: TelegramComposition, telegramNumber: int) -> bool
        
            Checks if adding a new Safety telegram with the given number to the drive object would be possible.
        
            telegramNumber: Number of the safety telegram
            Returns: System.Boolean
        """
        pass

    def CanInsertSupplementaryTelegram(self, telegramNumber):
        """
        CanInsertSupplementaryTelegram(self: TelegramComposition, telegramNumber: int) -> bool
        
            Checks if adding a new Supplementary telegram with the given number to the drive object would be possible.
        
            telegramNumber: Number of the supplementary telegram
            Returns: System.Boolean
        """
        pass

    def CanInsertTorqueTelegram(self, telegramNumber):
        """
        CanInsertTorqueTelegram(self: TelegramComposition, telegramNumber: int) -> bool
        
            Checks if adding a new Torque telegram with the given number to the drive object would be possible.
        
            telegramNumber: Number of the safety telegram
            Returns: System.Boolean
        """
        pass

    def Contains(self, item):
        """
        Contains(self: TelegramComposition, item: Telegram) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: TelegramComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def EraseTelegram(self, telegramType):
        """
        EraseTelegram(self: TelegramComposition, telegramType: TelegramType)
            Removes the telegram of the given type.
        
            telegramType: Type of the telegram to be removed
        """
        pass

    def Find(self, type):
        """
        Find(self: TelegramComposition, type: TelegramType) -> Telegram
        
            Finds telegram by type
        
            type: Telegram type
            Returns: Siemens.Engineering.MC.Drives.Telegram
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TelegramComposition) -> IEnumerator[Telegram]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: TelegramComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: TelegramComposition, item: Telegram) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def InsertAdditionalTelegram(self, inputSize, outputSize):
        """
        InsertAdditionalTelegram(self: TelegramComposition, inputSize: int, outputSize: int)
            Adds a new Additional telegram with the given sizes to the drive object.
        
            inputSize: Size of the input channel.
            outputSize: Size of the output channel.
        """
        pass

    def InsertSafetyTelegram(self, telegramNumber):
        """
        InsertSafetyTelegram(self: TelegramComposition, telegramNumber: int)
            Adds a new Safety telegram with the given number to the drive object.
        
            telegramNumber: Number of the safety telegram
        """
        pass

    def InsertSupplementaryTelegram(self, telegramNumber):
        """
        InsertSupplementaryTelegram(self: TelegramComposition, telegramNumber: int)
            Adds a new Supplementary telegram with the given number to the drive object.
        
            telegramNumber: Number of the supplementary telegram
        """
        pass

    def InsertTorqueTelegram(self, telegramNumber):
        """
        InsertTorqueTelegram(self: TelegramComposition, telegramNumber: int)
            Adds a new Torque telegram with the given number to the drive object.
        
            telegramNumber: Number of the safety telegram
        """
        pass

    def ToString(self):
        """
        ToString(self: TelegramComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Telegram](enumerable: IEnumerable[Telegram], value: Telegram) -> bool """
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

Get: Count(self: TelegramComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: TelegramComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: TelegramComposition) -> IEngineeringObject

"""



# variables with complex values

