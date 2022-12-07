# encoding: utf-8
# module Siemens.Engineering.MC.Drives.DFI calls itself DFI
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConfigurationEntry(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ It stores data about parameter """
    def Equals(self, obj):
        """
        Equals(self: ConfigurationEntry, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ConfigurationEntry, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationEntry) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ConfigurationEntry, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ConfigurationEntry) -> str
        
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

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The description of the configuration entry

Get: Description(self: ConfigurationEntry) -> str

"""

    EnumValueList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of possible labels of the enum parameters

Get: EnumValueList(self: ConfigurationEntry) -> IDictionary[int, str]

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum value of the configuration entry

Get: MaxValue(self: ConfigurationEntry) -> object

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minimum value of the configuration entry

Get: MinValue(self: ConfigurationEntry) -> object

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the configuration entry

Get: Name(self: ConfigurationEntry) -> str

"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Numeric representation of the configuration entry name

Get: Number(self: ConfigurationEntry) -> UInt32

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ConfigurationEntry) -> IEngineeringObject

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unit of the configuration entry

Get: Unit(self: ConfigurationEntry) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the configuration entry

Get: Value(self: ConfigurationEntry) -> object

Set: Value(self: ConfigurationEntry) = value
"""



class ConfigurationEntryComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ConfigurationEntry], IEquatable[object]):
    """ Composition of configuration entries """
    def Contains(self, item):
        """
        Contains(self: ConfigurationEntryComposition, item: ConfigurationEntry) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ConfigurationEntryComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, *__args):
        """
        Find(self: ConfigurationEntryComposition, name: str) -> ConfigurationEntry
        
            Find configuration entry by name
        
            name: Name of the configuration entry
            Returns: Siemens.Engineering.MC.Drives.DFI.ConfigurationEntry
        Find(self: ConfigurationEntryComposition, number: UInt32) -> ConfigurationEntry
        
            Find a configuration entry by numeric values
        
            number: Numeric representation of the configuration entry name
            Returns: Siemens.Engineering.MC.Drives.DFI.ConfigurationEntry
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ConfigurationEntryComposition) -> IEnumerator[ConfigurationEntry]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ConfigurationEntryComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ConfigurationEntryComposition, item: ConfigurationEntry) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ConfigurationEntryComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationEntry](enumerable: IEnumerable[ConfigurationEntry], value: ConfigurationEntry) -> bool """
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

Get: Count(self: ConfigurationEntryComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ConfigurationEntryComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ConfigurationEntryComposition) -> IEngineeringObject

"""



class DriveDomainFunctions(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ This class is responsible to execute domain functions on the Drive """
    def Equals(self, obj):
        """
        Equals(self: DriveDomainFunctions, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveDomainFunctions, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveDomainFunctions) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def PerformFactoryReset(self, resetMode):
        """
        PerformFactoryReset(self: DriveDomainFunctions, resetMode: ResetMode) -> bool
        
            Perform a factory reset
        
            resetMode: Reset mode (normal or safety)
            Returns: System.Boolean
        """
        pass

    def PerformRAMtoROMCopyAllDriveObject(self):
        """
        PerformRAMtoROMCopyAllDriveObject(self: DriveDomainFunctions) -> bool
        
            Perform a RAM to ROM copy in all DriveObject
            Returns: System.Boolean
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveDomainFunctions, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveDomainFunctions) -> str
        
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

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveDomainFunctions) -> IEngineeringObject

"""



class DriveFunctionInterface(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ An interface for calling drive functions """
    def Equals(self, obj):
        """
        Equals(self: DriveFunctionInterface, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveFunctionInterface, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveFunctionInterface) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveFunctionInterface, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveFunctionInterface) -> str
        
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

    DriveObjectFunctions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DriveObjectFunctions object

Get: DriveObjectFunctions(self: DriveFunctionInterface) -> DriveObjectFunctions

"""

    HardwareProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the HardwareProjection object

Get: HardwareProjection(self: DriveFunctionInterface) -> HardwareProjection

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveFunctionInterface) -> IEngineeringObject

"""



class DriveObjectActivation(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ This class is responsible for activating and deactivating the DriveObject """
    def ChangeActivationState(self, activationState):
        """
        ChangeActivationState(self: DriveObjectActivation, activationState: DriveObjectActivationState) -> bool
        
            Changes the activation state of the DriveObject
        
            activationState: Requested activation state
            Returns: System.Boolean
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DriveObjectActivation, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveObjectActivation, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectActivation) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveObjectActivation, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectActivation) -> str
        
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

    ActivationState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the activation

Get: ActivationState(self: DriveObjectActivation) -> DriveObjectActivationState

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the DriveObject is active

Get: IsActive(self: DriveObjectActivation) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObjectActivation) -> IEngineeringObject

"""



class DriveObjectFunctions(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Interface for calling drive object functions """
    def Equals(self, obj):
        """
        Equals(self: DriveObjectFunctions, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveObjectFunctions, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectFunctions) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveObjectFunctions, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectFunctions) -> str
        
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

    DriveObjectActivation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DriveObjectActivation object

Get: DriveObjectActivation(self: DriveObjectFunctions) -> DriveObjectActivation

"""

    DriveObjectTypeHandler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DriveObjectTypeHandler object

Get: DriveObjectTypeHandler(self: DriveObjectFunctions) -> DriveObjectTypeHandler

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObjectFunctions) -> IEngineeringObject

"""



class DriveObjectType(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ It stores data about DriveObjectType """
    def Equals(self, obj):
        """
        Equals(self: DriveObjectType, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveObjectType, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectType) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveObjectType, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectType) -> str
        
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the DriveObjectType

Get: Name(self: DriveObjectType) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObjectType) -> IEngineeringObject

"""



class DriveObjectTypeComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[DriveObjectType], IEquatable[object]):
    """ Composition of DriveObjectTypes """
    def Contains(self, item):
        """
        Contains(self: DriveObjectTypeComposition, item: DriveObjectType) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DriveObjectTypeComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: DriveObjectTypeComposition, name: str) -> DriveObjectType
        
            Find DriveObjectType by name
        
            name: Name of the DriveObjectType
            Returns: Siemens.Engineering.MC.Drives.DFI.DriveObjectType
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DriveObjectTypeComposition) -> IEnumerator[DriveObjectType]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectTypeComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: DriveObjectTypeComposition, item: DriveObjectType) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectTypeComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DriveObjectType](enumerable: IEnumerable[DriveObjectType], value: DriveObjectType) -> bool """
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

Get: Count(self: DriveObjectTypeComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: DriveObjectTypeComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: DriveObjectTypeComposition) -> IEngineeringObject

"""



class DriveObjectTypeHandler(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ This class is responsible for change and get the possible types of the current DriveObject """
    def ChangeDriveObjectType(self, targetDriveObjectType):
        """
        ChangeDriveObjectType(self: DriveObjectTypeHandler, targetDriveObjectType: DriveObjectType) -> bool
        
            Changes the type of the DriveObject
        
            targetDriveObjectType: Required type of the DriveObject
            Returns: System.Boolean
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DriveObjectTypeHandler, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DriveObjectTypeHandler, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DriveObjectTypeHandler) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DriveObjectTypeHandler, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DriveObjectTypeHandler) -> str
        
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

    CurrentDriveObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the current DriveObject

Get: CurrentDriveObjectType(self: DriveObjectTypeHandler) -> DriveObjectType

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DriveObjectTypeHandler) -> IEngineeringObject

"""

    PossibleDriveObjectTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Possible DriveObjectTypes of the current DriveObject

Get: PossibleDriveObjectTypes(self: DriveObjectTypeHandler) -> DriveObjectTypeComposition

"""



class EncoderConfiguration(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ EncoderConfiguration is used for storing non siemens encoder data """
    def Equals(self, obj):
        """
        Equals(self: EncoderConfiguration, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: EncoderConfiguration, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: EncoderConfiguration) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: EncoderConfiguration, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: EncoderConfiguration) -> str
        
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

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: EncoderConfiguration) -> IEngineeringObject

"""

    RequiredConfigurationEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Accessible configuration entries on this EncoderConfiguration

Get: RequiredConfigurationEntries(self: EncoderConfiguration) -> ConfigurationEntryComposition

"""



class HardwareProjection(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ This DFI are used for creating non siemens hardware elements on Sinamics drives """
    def Equals(self, obj):
        """
        Equals(self: HardwareProjection, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HardwareProjection, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetCurrentEncoderConfiguration(self, encoderNumber):
        """
        GetCurrentEncoderConfiguration(self: HardwareProjection, encoderNumber: UInt16) -> EncoderConfiguration
        
            Get the currently existing configuration container according to the encoder dataset number
        
            encoderNumber: Requested encoder number
            Returns: Siemens.Engineering.MC.Drives.DFI.EncoderConfiguration
        """
        pass

    def GetCurrentMotorConfiguration(self, driveDataSetNumber):
        """
        GetCurrentMotorConfiguration(self: HardwareProjection, driveDataSetNumber: UInt16) -> MotorConfiguration
        
            Get the currently existing configuration container according to the motor dataset number
        
            driveDataSetNumber: Requested drive data set number
            Returns: Siemens.Engineering.MC.Drives.DFI.MotorConfiguration
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HardwareProjection) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ProjectEncoderConfiguration(self, encoderConfiguration, encoderNumber):
        """
        ProjectEncoderConfiguration(self: HardwareProjection, encoderConfiguration: EncoderConfiguration, encoderNumber: UInt16) -> bool
        
            Project a configuration for the encoder
        
            encoderConfiguration: Encoder configuration object
            encoderNumber: Requested encoder number
            Returns: System.Boolean
        """
        pass

    def ProjectMotorConfiguration(self, motorConfiguration, driveDataSetNumber):
        """
        ProjectMotorConfiguration(self: HardwareProjection, motorConfiguration: MotorConfiguration, driveDataSetNumber: UInt16) -> bool
        
            Project a configuration for the motor
        
            motorConfiguration: Motor configuration object
            driveDataSetNumber: Requested drive data set number
            Returns: System.Boolean
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HardwareProjection, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def SetEncoder(self, encoderInterface, encoderType, absoluteIncrementalFlag, rotaryLinearFlag, encoderNumber):
        """
        SetEncoder(self: HardwareProjection, encoderInterface: EncoderInterface, encoderType: EncoderType, absoluteIncrementalFlag: AbsoluteIncrementalFlag, rotaryLinearFlag: RotaryLinearFlag, encoderNumber: UInt16) -> bool
        
            Set the encoder
        
            encoderInterface: Requested encoder interface
            encoderType: Requested encoder type
            absoluteIncrementalFlag: Requested absolute incremental flag
            rotaryLinearFlag: Requested rotary linear flag
            encoderNumber: Requested encoder number
            Returns: System.Boolean
        """
        pass

    def SetMotorType(self, motorType, driveDataSetNumber):
        """
        SetMotorType(self: HardwareProjection, motorType: MotorType, driveDataSetNumber: UInt16) -> bool
        
            Set the motor type
        
            motorType: Requested motor type
            driveDataSetNumber: Requested drive data set number
            Returns: System.Boolean
        """
        pass

    def ToString(self):
        """
        ToString(self: HardwareProjection) -> str
        
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

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HardwareProjection) -> IEngineeringObject

"""



class MotorConfiguration(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ MotorConfiguration is used for storing non siemens motor data """
    def Equals(self, obj):
        """
        Equals(self: MotorConfiguration, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: MotorConfiguration, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: MotorConfiguration) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: MotorConfiguration, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: MotorConfiguration) -> str
        
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

    OptionalConfigurationEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Accessible configuration entries on this MotorConfiguration

Get: OptionalConfigurationEntries(self: MotorConfiguration) -> ConfigurationEntryComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: MotorConfiguration) -> IEngineeringObject

"""

    RequiredConfigurationEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Accessible configuration entries on this MotorConfiguration

Get: RequiredConfigurationEntries(self: MotorConfiguration) -> ConfigurationEntryComposition

"""



class OnlineDriveFunctionInterface(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ An interface for calling online drive functions """
    def Equals(self, obj):
        """
        Equals(self: OnlineDriveFunctionInterface, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: OnlineDriveFunctionInterface, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: OnlineDriveFunctionInterface) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: OnlineDriveFunctionInterface, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: OnlineDriveFunctionInterface) -> str
        
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

    DriveDomainFunctions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DriveDomainFunctions object

Get: DriveDomainFunctions(self: OnlineDriveFunctionInterface) -> DriveDomainFunctions

"""

    DriveObjectFunctions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the DriveObjectFunctions object

Get: DriveObjectFunctions(self: OnlineDriveFunctionInterface) -> DriveObjectFunctions

"""

    HardwareProjection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the HardwareProjection object

Get: HardwareProjection(self: OnlineDriveFunctionInterface) -> HardwareProjection

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: OnlineDriveFunctionInterface) -> IEngineeringObject

"""



