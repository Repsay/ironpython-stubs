# encoding: utf-8
# module Siemens.Engineering.HmiUnified.RuntimeSettings calls itself RuntimeSettings
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiLanguageAndFont(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Language and font """
    def Equals(self, obj):
        """
        Equals(self: HmiLanguageAndFont, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiLanguageAndFont, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiLanguageAndFont) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiLanguageAndFont, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiLanguageAndFont) -> str
        
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

    Enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables language and font

Get: Enable(self: HmiLanguageAndFont) -> bool

Set: Enable(self: HmiLanguageAndFont) = value
"""

    EnableForLogging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enables the language and font for logging

Get: EnableForLogging(self: HmiLanguageAndFont) -> bool

Set: EnableForLogging(self: HmiLanguageAndFont) = value
"""

    FixedFont1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixed font 1

Get: FixedFont1(self: HmiLanguageAndFont) -> str

"""

    FixedFont2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixed font 2

Get: FixedFont2(self: HmiLanguageAndFont) -> str

"""

    FixedFont3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixed font 3

Get: FixedFont3(self: HmiLanguageAndFont) -> str

"""

    FixedFont4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixed font 4

Get: FixedFont4(self: HmiLanguageAndFont) -> str

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Language name

Get: Language(self: HmiLanguageAndFont) -> str

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Order of language and font entry

Get: Order(self: HmiLanguageAndFont) -> Int16

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiLanguageAndFont) -> IEngineeringObject

"""



class HmiLanguageAndFontAssociation(object, IEngineeringAssociation, IEngineeringInstance, IEnumerable, IInternalAssociationAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[HmiLanguageAndFont], IEquatable[object]):
    """ Language and font list """
    def Contains(self, item):
        """
        Contains(self: HmiLanguageAndFontAssociation, item: HmiLanguageAndFont) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: HmiLanguageAndFontAssociation, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HmiLanguageAndFontAssociation) -> IEnumerator[HmiLanguageAndFont]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiLanguageAndFontAssociation) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: HmiLanguageAndFontAssociation, item: HmiLanguageAndFont) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: HmiLanguageAndFontAssociation) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HmiLanguageAndFont](enumerable: IEnumerable[HmiLanguageAndFont], value: HmiLanguageAndFont) -> bool """
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

Get: Count(self: HmiLanguageAndFontAssociation) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: HmiLanguageAndFontAssociation) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent..

Get: Parent(self: HmiLanguageAndFontAssociation) -> IEngineeringObject

"""



class HmiRuntimeSetting(object, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Runtime settings of hmi device """
    def Equals(self, obj):
        """
        Equals(self: HmiRuntimeSetting, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: HmiRuntimeSetting, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: HmiRuntimeSetting) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: HmiRuntimeSetting, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: HmiRuntimeSetting) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def Validate(self):
        """
        Validate(self: HmiRuntimeSetting) -> IList[HmiValidationResult]
        
            Validates RuntimeSettings
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

    LanguageAndFonts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of language and font entries

Get: LanguageAndFonts(self: HmiRuntimeSetting) -> HmiLanguageAndFontAssociation

"""

    OperateAsOpcServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether hmi device should operate as opc server

Get: OperateAsOpcServer(self: HmiRuntimeSetting) -> bool

Set: OperateAsOpcServer(self: HmiRuntimeSetting) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: HmiRuntimeSetting) -> IEngineeringObject

"""

    StartScreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the start up screen for hmi device

Get: StartScreen(self: HmiRuntimeSetting) -> str

Set: StartScreen(self: HmiRuntimeSetting) = value
"""



