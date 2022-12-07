# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiTags calls itself HmiTags
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiAccessMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Hmi Tag Access Mode
    
    enum HmiAccessMode, values: AbsoluteAccess (1), None (0), SymbolicAccess (2)
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

    AbsoluteAccess = None
    None = None
    SymbolicAccess = None
    value__ = None


class HmiAcquisitionMode(Enum, IComparable, IFormattable, IConvertible):
    """
    AcquisitionMode of Hmi Tag
    
    enum HmiAcquisitionMode, values: CyclicContinuous (16), CyclicOnUse (13), None (0), OnDemand (12)
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

    CyclicContinuous = None
    CyclicOnUse = None
    None = None
    OnDemand = None
    value__ = None


class HmiLimitValueType(Enum, IComparable, IFormattable, IConvertible):
    """
    Description for limit value type
    
    enum HmiLimitValueType, values: Constant (1), None (0), Tag (2)
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

    Constant = None
    None = None
    Tag = None
    value__ = None


class HmiSubstituteValue(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Description for substitute value """
    def Equals(self, obj):
        """
        Equals(self: HmiSubstituteValue, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiSubstituteValue, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiSubstituteValue) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiSubstituteValue, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiSubstituteValue) -> str
        
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

Get: Parent(self: HmiSubstituteValue) -> IEngineeringObject

"""

    SubstituteValueUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get or set substitute value

Get: SubstituteValueUsage(self: HmiSubstituteValue) -> HmiSubstituteValueUsage

Set: SubstituteValueUsage(self: HmiSubstituteValue) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get and set substitute value

Get: Value(self: HmiSubstituteValue) -> object

Set: Value(self: HmiSubstituteValue) = value
"""



class HmiSubstituteValueUsage(Enum, IComparable, IFormattable, IConvertible):
    """
    Hmi Substitute Value Usage
    
    enum HmiSubstituteValueUsage, values: InvalidValue (1), InvalidValueOrRangeViolation (3), None (0), RangeViolation (2)
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

    InvalidValue = None
    InvalidValueOrRangeViolation = None
    None = None
    RangeViolation = None
    value__ = None


class HmiSystemTag(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Hmi system tag """
    def Equals(self, obj):
        """
        Equals(self: HmiSystemTag, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiSystemTag, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiSystemTag) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiSystemTag, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiSystemTag) -> str
        
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

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data type of the system tag

Get: DataType(self: HmiSystemTag) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of system tag

Get: Name(self: HmiSystemTag) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiSystemTag) -> IEngineeringObject

"""



class HmiSystemTagComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiSystemTag], IEquatable[object]):
    """ Collection of hmi system tag """
    def Contains(self, item):
        """
        Contains(self: HmiSystemTagComposition, item: HmiSystemTag) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiSystemTagComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiSystemTagComposition, name: str) -> HmiSystemTag
        
            Finds the hmi system tag based on the given name
        
            name: Hmi system tag name
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiSystemTag
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiSystemTagComposition) -> IEnumerator[HmiSystemTag]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiSystemTagComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiSystemTagComposition, item: HmiSystemTag) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiSystemTagComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiSystemTag](enumerable: IEnumerable[HmiSystemTag], value: HmiSystemTag) -> bool """
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

Get: Count(self: HmiSystemTagComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiSystemTagComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiSystemTagComposition) -> IEngineeringObject

"""



class HmiTag(object, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Hmi tag class """
    def Delete(self):
        """
        Delete(self: HmiTag)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiTag, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiTag, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiTag) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiTag, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiTag) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def Validate(self):
        """
        Validate(self: HmiTag) -> IList[HmiValidationResult]
        
            Validates the object
            Returns: System.Collections.Generic.IList<Siemens.Engineering.HmiUnified.Common.HmiValidationResult>
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

    AccessMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Hmi Tag Access Mode

Get: AccessMode(self: HmiTag) -> HmiAccessMode

Set: AccessMode(self: HmiTag) = value
"""

    AcquisitionCycle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Acquisition cycle attribute

Get: AcquisitionCycle(self: HmiTag) -> str

Set: AcquisitionCycle(self: HmiTag) = value
"""

    AcquisitionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hmi Tag AcquisitionMode

Get: AcquisitionMode(self: HmiTag) -> HmiAcquisitionMode

Set: AcquisitionMode(self: HmiTag) = value
"""

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Hmi Tag Address Attribute

Get: Address(self: HmiTag) -> str

Set: Address(self: HmiTag) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set comment of tag

Get: Comment(self: HmiTag) -> MultilingualText

"""

    Connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Hmi Connection

Get: Connection(self: HmiTag) -> str

Set: Connection(self: HmiTag) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DataType of the Tag

Get: DataType(self: HmiTag) -> str

Set: DataType(self: HmiTag) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set display name of tag

Get: DisplayName(self: HmiTag) -> MultilingualText

"""

    InitialMaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Upper limit

Get: InitialMaxValue(self: HmiTag) -> UpperRange

"""

    InitialMinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Lower limit

Get: InitialMinValue(self: HmiTag) -> LowerRange

"""

    InitialValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Initial value attribute

Get: InitialValue(self: HmiTag) -> object

Set: InitialValue(self: HmiTag) = value
"""

    LoggingTags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents

Get: LoggingTags(self: HmiTag) -> HmiLoggingTagComposition

"""

    MaxLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hmi tag DataTypeLength

Get: MaxLength(self: HmiTag) -> UInt32

Set: MaxLength(self: HmiTag) = value
"""

    Members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Members of the composite Hmi tag

Get: Members(self: HmiTag) -> HmiTagComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of Hmi Tag

Get: Name(self: HmiTag) -> str

Set: Name(self: HmiTag) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiTag) -> IEngineeringObject

"""

    Persistent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Persistence attribute

Get: Persistent(self: HmiTag) -> bool

Set: Persistent(self: HmiTag) = value
"""

    PlcName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Plc Name Attribute

Get: PlcName(self: HmiTag) -> str

"""

    PlcTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Plc Tag attribute

Get: PlcTag(self: HmiTag) -> str

Set: PlcTag(self: HmiTag) = value
"""

    QualityCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Hmi tag  QualityCode

Get: QualityCode(self: HmiTag) -> bool

Set: QualityCode(self: HmiTag) = value
"""

    SubstituteValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The SubstituteValue

Get: SubstituteValue(self: HmiTag) -> HmiSubstituteValue

"""

    TagTableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The parent tag table

Get: TagTableName(self: HmiTag) -> str

"""

    TagType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates different types of hmi tag

Get: TagType(self: HmiTag) -> HmiTagType

"""

    TextReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set text referenceof tag

Get: TextReference(self: HmiTag) -> MultilingualText

"""

    UpdateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Update Id Attribute

Get: UpdateId(self: HmiTag) -> UInt32

Set: UpdateId(self: HmiTag) = value
"""

    UpdateScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Update Scope

Get: UpdateScope(self: HmiTag) -> HmiUpdateScope

Set: UpdateScope(self: HmiTag) = value
"""



class HmiTagComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiTag], IEquatable[object]):
    """ Collection of hmi tags """
    def Contains(self, item):
        """
        Contains(self: HmiTagComposition, item: HmiTag) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name, tagTableName=None):
        """
        Create(self: HmiTagComposition, name: str) -> HmiTag
        
            Creates hmi tag
        
            name: Name of the hmi tag
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTag
        Create(self: HmiTagComposition, name: str, tagTableName: str) -> HmiTag
        
            Creates hmi tag under a specified tag table
        
            name: Name of the hmi tag
            tagTableName: Name of the parent hmi tagTable
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTag
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiTagComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiTagComposition, name: str) -> HmiTag
        
            Finds the hmi tag based on the given name
        
            name: Hmi tag name
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTag
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiTagComposition) -> IEnumerator[HmiTag]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiTagComposition, item: HmiTag) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiTagComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiTag](enumerable: IEnumerable[HmiTag], value: HmiTag) -> bool """
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

Get: Count(self: HmiTagComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiTagComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiTagComposition) -> IEngineeringObject

"""



class HmiTagTable(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Hmi tag tables """
    def Delete(self):
        """
        Delete(self: HmiTagTable)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiTagTable, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiTagTable, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagTable) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiTagTable, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiTagTable) -> str
        
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
    """Name of HmitagTable

Get: Name(self: HmiTagTable) -> str

Set: Name(self: HmiTagTable) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiTagTable) -> IEngineeringObject

"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hmi tag collection

Get: Tags(self: HmiTagTable) -> HmiTagComposition

"""



class HmiTagTableComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiTagTable], IEquatable[object]):
    """ HmitagTable composition """
    def Contains(self, item):
        """
        Contains(self: HmiTagTableComposition, item: HmiTagTable) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: HmiTagTableComposition, name: str) -> HmiTagTable
        
            Creates hmi tag table
        
            name: Name of Hmi tag table
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTagTable
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiTagTableComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: HmiTagTableComposition, name: str) -> HmiTagTable
        
            Finding the given tagtable
        
            name: Name of hmi tagtable
            Returns: Siemens.Engineering.HmiUnified.HmiTags.HmiTagTable
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiTagTableComposition) -> IEnumerator[HmiTagTable]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiTagTableComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiTagTableComposition, item: HmiTagTable) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiTagTableComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiTagTable](enumerable: IEnumerable[HmiTagTable], value: HmiTagTable) -> bool """
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

Get: Count(self: HmiTagTableComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiTagTableComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: HmiTagTableComposition) -> IEngineeringObject

"""



class HmiTagType(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates different types of hmi tag
    
    enum HmiTagType, values: Array (2), Simple (0), UDT (1)
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

    Array = None
    Simple = None
    UDT = None
    value__ = None


class HmiUpdateScope(Enum, IComparable, IFormattable, IConvertible):
    """
    The hmi tag Update Scope
    
    enum HmiUpdateScope, values: ClientServerWide (1), LocalHmiDevice (2), None (0)
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

    ClientServerWide = None
    LocalHmiDevice = None
    None = None
    value__ = None


class Range(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ To set value range """
    def Equals(self, obj):
        """
        Equals(self: Range, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Range, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Range) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Range, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Range) -> str
        
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

Get: Parent(self: Range) -> IEngineeringObject

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of upper/lower

Get: Value(self: Range) -> object

Set: Value(self: Range) = value
"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get and set Vlaue type

Get: ValueType(self: Range) -> HmiLimitValueType

Set: ValueType(self: Range) = value
"""



class LowerRange(Range, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Lower limit range """
    def Equals(self, obj):
        """
        Equals(self: LowerRange, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LowerRange) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: LowerRange) -> str
        
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

Get: Parent(self: LowerRange) -> IEngineeringObject

"""



class UpperRange(Range, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Range for limit high """
    def Equals(self, obj):
        """
        Equals(self: UpperRange, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UpperRange) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: UpperRange) -> str
        
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

Get: Parent(self: UpperRange) -> IEngineeringObject

"""



