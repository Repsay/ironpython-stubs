# encoding: utf-8
# module Siemens.Engineering.SW calls itself SW
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Fingerprint(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ fingerprint """
    def Equals(self, obj):
        """
        Equals(self: Fingerprint, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Fingerprint, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Fingerprint) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Fingerprint, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Fingerprint) -> str
        
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

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID of the fingerprint

Get: Id(self: Fingerprint) -> FingerprintId

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Fingerprint) -> IEngineeringObject

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """fingerprint data

Get: Value(self: Fingerprint) -> str

"""



class FingerprintId(Enum, IComparable, IFormattable, IConvertible):
    """
    fingerprint id
    
    enum FingerprintId, values: Alarms (5), Code (0), Comments (1), Events (8), Interface (2), LibraryType (3), Properties (10), Supervisions (6), TechnologyObject (7), Texts (4), TextualInterface (9)
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

    Alarms = None
    Code = None
    Comments = None
    Events = None
    Interface = None
    LibraryType = None
    Properties = None
    Supervisions = None
    TechnologyObject = None
    Texts = None
    TextualInterface = None
    value__ = None


class FingerprintProvider(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Provides fingerprints. """
    def Equals(self, obj):
        """
        Equals(self: FingerprintProvider, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: FingerprintProvider, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetFingerprints(self):
        """
        GetFingerprints(self: FingerprintProvider) -> IList[Fingerprint]
        
            Read Fingerprint
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Fingerprint>
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FingerprintProvider) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: FingerprintProvider, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: FingerprintProvider) -> str
        
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

Get: Parent(self: FingerprintProvider) -> IEngineeringObject

"""



class ISoftwareCompareTarget:
    """ Access to the controller in a compare scenario """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PlcChecksumProvider(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Provides checksums. """
    def Equals(self, obj):
        """
        Equals(self: PlcChecksumProvider, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: PlcChecksumProvider, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcChecksumProvider) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: PlcChecksumProvider, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: PlcChecksumProvider) -> str
        
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

Get: Parent(self: PlcChecksumProvider) -> IEngineeringObject

"""

    Software = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Software checksum

Get: Software(self: PlcChecksumProvider) -> str

"""



class PlcSoftware(Software, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IInstanceSearchScope, IUpdateProjectScope, ISoftwareCompareTarget, IEngineeringServiceProvider, IServiceProvider):
    """ Represents the software components of a Plc """
    def CompareTo(self, compareTarget):
        """
        CompareTo(self: PlcSoftware, compareTarget: ISoftwareCompareTarget) -> CompareResult
        
            Compare the PLC software to the given target
        
            compareTarget: The target to compare to the PLC software
            Returns: Siemens.Engineering.Compare.CompareResult
        """
        pass

    def CompareToOnline(self):
        """
        CompareToOnline(self: PlcSoftware) -> CompareResult
        
            Compare the PLC software to the online target
            Returns: Siemens.Engineering.Compare.CompareResult
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: PlcSoftware, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: PlcSoftware) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def ToString(self):
        """
        ToString(self: PlcSoftware) -> str
        
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

    BlockGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Plc block system group

Get: BlockGroup(self: PlcSoftware) -> PlcBlockSystemGroup

"""

    ExternalSourceGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Plc external source system group

Get: ExternalSourceGroup(self: PlcSoftware) -> PlcExternalSourceSystemGroup

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the Plc software

Get: Name(self: PlcSoftware) -> str

"""

    TagTableGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Plc tag table system group

Get: TagTableGroup(self: PlcSoftware) -> PlcTagTableSystemGroup

"""

    TechnologicalObjectGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This system folder can contain technological objects

Get: TechnologicalObjectGroup(self: PlcSoftware) -> TechnologicalInstanceDBGroup

"""

    TypeGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets Plc type system group

Get: TypeGroup(self: PlcSoftware) -> PlcTypeSystemGroup

"""

    WatchAndForceTableGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Plc watch table system group

Get: WatchAndForceTableGroup(self: PlcSoftware) -> PlcWatchAndForceTableSystemGroup

"""



class SWImportOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible sw importoptions for Import
    
    enum (flags) SWImportOptions, values: IgnoreMissingReferencedObjects (2), IgnoreStructuralChanges (1), None (0)
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

    IgnoreMissingReferencedObjects = None
    IgnoreStructuralChanges = None
    None = None
    value__ = None


# variables with complex values

