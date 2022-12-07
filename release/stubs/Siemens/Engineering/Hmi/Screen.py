# encoding: utf-8
# module Siemens.Engineering.Hmi.Screen calls itself Screen
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Screen(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEngineeringServiceProvider, IServiceProvider, IEquatable[object]):
    """ Represents a screen """
    def Delete(self):
        """
        Delete(self: Screen)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Screen, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: Screen, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a screen
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: Screen, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Screen) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetService(self):
# Error generating skeleton for function GetService: Method must be called on a Type for which Type.IsGenericParameter is false.

    def SetAttributes(self, attributes):
        """ SetAttributes(self: Screen, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: Screen) -> str
        
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
    """The name of the screen

Get: Name(self: Screen) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: Screen) -> IEngineeringObject

"""



class ScreenComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[Screen], IEquatable[object]):
    """ Composition of Screens """
    def Contains(self, item):
        """
        Contains(self: ScreenComposition, item: Screen) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def CreateFrom(self, *__args):
        """
        CreateFrom(self: ScreenComposition, libraryTypeVersion: ScreenLibraryTypeVersion) -> Screen
        
            Create screen from type version
        
            libraryTypeVersion: screen version
            Returns: Siemens.Engineering.Hmi.Screen.Screen
        CreateFrom(self: ScreenComposition, sourceMasterCopy: MasterCopy) -> Screen
        
            Create Screen from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenComposition, name: str) -> Screen
        
            Finds a given screen
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenComposition) -> IEnumerator[Screen]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: ScreenComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Screen]
        
            Simatic ML import of a screen
        
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.Screen>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenComposition, item: Screen) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Screen](enumerable: IEnumerable[Screen], value: Screen) -> bool """
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

Get: Count(self: ScreenComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenComposition) -> IEngineeringObject

"""



class ScreenFolder(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a screen folder """
    def Equals(self, obj):
        """
        Equals(self: ScreenFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenFolder, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenFolder, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen user folders

Get: Folders(self: ScreenFolder) -> ScreenUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen folder

Get: Name(self: ScreenFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenFolder) -> IEngineeringObject

"""

    Screens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screens

Get: Screens(self: ScreenFolder) -> ScreenComposition

"""



class ScreenGlobalElements(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents the screen global elements """
    def Equals(self, obj):
        """
        Equals(self: ScreenGlobalElements, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: ScreenGlobalElements, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of screen global elements
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenGlobalElements, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenGlobalElements) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenGlobalElements, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenGlobalElements) -> str
        
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

Get: Parent(self: ScreenGlobalElements) -> IEngineeringObject

"""



class ScreenLibraryType(LibraryType, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type made from a screen """
    def Equals(self, obj):
        """
        Equals(self: ScreenLibraryType, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenLibraryType) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenLibraryType) -> str
        
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

Get: Name(self: ScreenLibraryType) -> str

Set: Name(self: ScreenLibraryType) = value
"""



class ScreenLibraryTypeVersion(LibraryTypeVersion, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type version made from a screen """
    def Equals(self, obj):
        """
        Equals(self: ScreenLibraryTypeVersion, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenLibraryTypeVersion) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenLibraryTypeVersion) -> str
        
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


class ScreenOverview(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Editor for elements in the overview """
    def Equals(self, obj):
        """
        Equals(self: ScreenOverview, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: ScreenOverview, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a screen overview
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenOverview, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenOverview) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenOverview, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenOverview) -> str
        
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

Get: Parent(self: ScreenOverview) -> IEngineeringObject

"""



class ScreenPopup(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Pop-up screen """
    def Delete(self):
        """
        Delete(self: ScreenPopup)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenPopup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: ScreenPopup, path: FileInfo, exportOptions: ExportOptions)
            Common export
        
            path: Path to the Simatic ML file
            exportOptions: Determines whether the default values are exported or not
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenPopup, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenPopup, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopup) -> str
        
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
    """Gets or sets the screen name.

Get: Name(self: ScreenPopup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenPopup) -> IEngineeringObject

"""



class ScreenPopupComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenPopup], IEquatable[object]):
    """ Composition of popup screens. """
    def Contains(self, item):
        """
        Contains(self: ScreenPopupComposition, item: ScreenPopup) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: ScreenPopupComposition, sourceMasterCopy: MasterCopy) -> ScreenPopup
        
            Create ScreenPopup from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenPopupComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenPopupComposition, name: str) -> ScreenPopup
        
            Finds a given screen popup
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenPopupComposition) -> IEnumerator[ScreenPopup]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: ScreenPopupComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenPopup]
        
            Import Action
        
            path: Path to the Simatic ML file
            importOptions: Options to use for the Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenPopup>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenPopupComposition, item: ScreenPopup) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopupComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenPopup](enumerable: IEnumerable[ScreenPopup], value: ScreenPopup) -> bool """
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

Get: Count(self: ScreenPopupComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenPopupComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenPopupComposition) -> IEngineeringObject

"""



class ScreenPopupFolder(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Folder containing screen popups """
    def Equals(self, obj):
        """
        Equals(self: ScreenPopupFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenPopupFolder, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenPopupFolder, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopupFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popup user folders

Get: Folders(self: ScreenPopupFolder) -> ScreenPopupUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen popup folder

Get: Name(self: ScreenPopupFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenPopupFolder) -> IEngineeringObject

"""

    ScreenPopups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popups

Get: ScreenPopups(self: ScreenPopupFolder) -> ScreenPopupComposition

"""



class ScreenPopupSystemFolder(ScreenPopupFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopyTarget):
    """ System folder containing screen popups """
    def Equals(self, obj):
        """
        Equals(self: ScreenPopupSystemFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupSystemFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopupSystemFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popup user folders

Get: Folders(self: ScreenPopupSystemFolder) -> ScreenPopupUserFolderComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenPopupSystemFolder) -> IEngineeringObject

"""

    ScreenPopups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popups

Get: ScreenPopups(self: ScreenPopupSystemFolder) -> ScreenPopupComposition

"""



class ScreenPopupUserFolder(ScreenPopupFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopySource, IMasterCopyTarget):
    """ User folder containing screen popups """
    def Delete(self):
        """
        Delete(self: ScreenPopupUserFolder)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenPopupUserFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupUserFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopupUserFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popup user folders

Get: Folders(self: ScreenPopupUserFolder) -> ScreenPopupUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen template user folder

Get: Name(self: ScreenPopupUserFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenPopupUserFolder) -> IEngineeringObject

"""

    ScreenPopups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen popups

Get: ScreenPopups(self: ScreenPopupUserFolder) -> ScreenPopupComposition

"""



class ScreenPopupUserFolderComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenPopupUserFolder], IEquatable[object]):
    """ Composition of ScreenPopupUserFolders """
    def Contains(self, item):
        """
        Contains(self: ScreenPopupUserFolderComposition, item: ScreenPopupUserFolder) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: ScreenPopupUserFolderComposition, name: str) -> ScreenPopupUserFolder
        
            Creates a screen popup user folder
        
            name: Name of folder to be created
            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopupUserFolder
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenPopupUserFolderComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenPopupUserFolderComposition, name: str) -> ScreenPopupUserFolder
        
            Finds a given screen popup user folder
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopupUserFolder
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenPopupUserFolderComposition) -> IEnumerator[ScreenPopupUserFolder]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenPopupUserFolderComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenPopupUserFolderComposition, item: ScreenPopupUserFolder) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenPopupUserFolderComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenPopupUserFolder](enumerable: IEnumerable[ScreenPopupUserFolder], value: ScreenPopupUserFolder) -> bool """
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

Get: Count(self: ScreenPopupUserFolderComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenPopupUserFolderComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenPopupUserFolderComposition) -> IEngineeringObject

"""



class ScreenSlidein(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Slide-In screen """
    def Equals(self, obj):
        """
        Equals(self: ScreenSlidein, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: ScreenSlidein, path: FileInfo, exportOptions: ExportOptions)
            Common export
        
            path: Path to the Simatic ML file
            exportOptions: Determines whether the default values are exported or not
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenSlidein, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlidein) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenSlidein, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenSlidein) -> str
        
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

Get: Parent(self: ScreenSlidein) -> IEngineeringObject

"""

    SlideinType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of a Slide-In screen.

Get: SlideinType(self: ScreenSlidein) -> SlideinType

"""



class ScreenSlideinComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenSlidein], IEquatable[object]):
    """ Composition of slidein screens. """
    def Contains(self, item):
        """
        Contains(self: ScreenSlideinComposition, item: ScreenSlidein) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenSlideinComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, slideinType):
        """
        Find(self: ScreenSlideinComposition, slideinType: SlideinType) -> ScreenSlidein
        
            Find a slidein screen.
        
            slideinType: Slidein to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenSlidein
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenSlideinComposition) -> IEnumerator[ScreenSlidein]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlideinComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: ScreenSlideinComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenSlidein]
        
            Import Action
        
            path: Path to the Simatic ML file
            importOptions: Options to use for the Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenSlidein>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenSlideinComposition, item: ScreenSlidein) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenSlideinComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenSlidein](enumerable: IEnumerable[ScreenSlidein], value: ScreenSlidein) -> bool """
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

Get: Count(self: ScreenSlideinComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenSlideinComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenSlideinComposition) -> IEngineeringObject

"""



class ScreenSlideinSystemFolder(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Folder for slide-in screens """
    def Equals(self, obj):
        """
        Equals(self: ScreenSlideinSystemFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenSlideinSystemFolder, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSlideinSystemFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenSlideinSystemFolder, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenSlideinSystemFolder) -> str
        
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

Get: Parent(self: ScreenSlideinSystemFolder) -> IEngineeringObject

"""

    ScreenSlideins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a collection of slide-in screens in that folder.

Get: ScreenSlideins(self: ScreenSlideinSystemFolder) -> ScreenSlideinComposition

"""



class ScreenSystemFolder(ScreenFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopyTarget, ILibraryTypeInstantiationTarget):
    """ System folder containing screens """
    def Equals(self, obj):
        """
        Equals(self: ScreenSystemFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenSystemFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenSystemFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen user folders

Get: Folders(self: ScreenSystemFolder) -> ScreenUserFolderComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenSystemFolder) -> IEngineeringObject

"""

    Screens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screens

Get: Screens(self: ScreenSystemFolder) -> ScreenComposition

"""



class ScreenTemplate(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IMasterCopySource, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a screen template """
    def Delete(self):
        """
        Delete(self: ScreenTemplate)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenTemplate, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, path, exportOptions):
        """
        Export(self: ScreenTemplate, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a screen template
        
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenTemplate, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplate) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenTemplate, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplate) -> str
        
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
    """The name of the screen template

Get: Name(self: ScreenTemplate) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenTemplate) -> IEngineeringObject

"""



class ScreenTemplateComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenTemplate], IEquatable[object]):
    """ Composition of ScreenTemplates """
    def Contains(self, item):
        """
        Contains(self: ScreenTemplateComposition, item: ScreenTemplate) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def CreateFrom(self, sourceMasterCopy):
        """
        CreateFrom(self: ScreenTemplateComposition, sourceMasterCopy: MasterCopy) -> ScreenTemplate
        
            Create ScreenTemplate from MasterCopy
        
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenTemplateComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenTemplateComposition, name: str) -> ScreenTemplate
        
            Finds a given screen template
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenTemplateComposition) -> IEnumerator[ScreenTemplate]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, path, importOptions):
        """
        Import(self: ScreenTemplateComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenTemplate]
        
            Simatic ML import of a screen template
        
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenTemplate>
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenTemplateComposition, item: ScreenTemplate) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplateComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenTemplate](enumerable: IEnumerable[ScreenTemplate], value: ScreenTemplate) -> bool """
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

Get: Count(self: ScreenTemplateComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenTemplateComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenTemplateComposition) -> IEngineeringObject

"""



class ScreenTemplateFolder(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Folder containing screen templates """
    def Equals(self, obj):
        """
        Equals(self: ScreenTemplateFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ScreenTemplateFolder, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ScreenTemplateFolder, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplateFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen template user folders

Get: Folders(self: ScreenTemplateFolder) -> ScreenTemplateUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen template folder

Get: Name(self: ScreenTemplateFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenTemplateFolder) -> IEngineeringObject

"""

    ScreenTemplates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen templates

Get: ScreenTemplates(self: ScreenTemplateFolder) -> ScreenTemplateComposition

"""



class ScreenTemplateSystemFolder(ScreenTemplateFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopyTarget):
    """ System folder containing screen templates """
    def Equals(self, obj):
        """
        Equals(self: ScreenTemplateSystemFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateSystemFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplateSystemFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen template user folders

Get: Folders(self: ScreenTemplateSystemFolder) -> ScreenTemplateUserFolderComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenTemplateSystemFolder) -> IEngineeringObject

"""

    ScreenTemplates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen templates

Get: ScreenTemplates(self: ScreenTemplateSystemFolder) -> ScreenTemplateComposition

"""



class ScreenTemplateUserFolder(ScreenTemplateFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopySource, IMasterCopyTarget):
    """ User folder containing screen templates """
    def Delete(self):
        """
        Delete(self: ScreenTemplateUserFolder)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenTemplateUserFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateUserFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplateUserFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen template user folders

Get: Folders(self: ScreenTemplateUserFolder) -> ScreenTemplateUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen template user folder

Get: Name(self: ScreenTemplateUserFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenTemplateUserFolder) -> IEngineeringObject

"""

    ScreenTemplates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen templates

Get: ScreenTemplates(self: ScreenTemplateUserFolder) -> ScreenTemplateComposition

"""



class ScreenTemplateUserFolderComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenTemplateUserFolder], IEquatable[object]):
    """ Composition of ScreenTemplateUserFolders """
    def Contains(self, item):
        """
        Contains(self: ScreenTemplateUserFolderComposition, item: ScreenTemplateUserFolder) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: ScreenTemplateUserFolderComposition, name: str) -> ScreenTemplateUserFolder
        
            Creates a screen template user folder
        
            name: Name of folder to be created
            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplateUserFolder
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenTemplateUserFolderComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenTemplateUserFolderComposition, name: str) -> ScreenTemplateUserFolder
        
            Finds a given screen template user folder
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplateUserFolder
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenTemplateUserFolderComposition) -> IEnumerator[ScreenTemplateUserFolder]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenTemplateUserFolderComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenTemplateUserFolderComposition, item: ScreenTemplateUserFolder) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenTemplateUserFolderComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenTemplateUserFolder](enumerable: IEnumerable[ScreenTemplateUserFolder], value: ScreenTemplateUserFolder) -> bool """
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

Get: Count(self: ScreenTemplateUserFolderComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenTemplateUserFolderComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenTemplateUserFolderComposition) -> IEngineeringObject

"""



class ScreenUserFolder(ScreenFolder, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object], IMasterCopySource, IMasterCopyTarget, ILibraryTypeInstantiationTarget):
    """ User folder containing screens """
    def Delete(self):
        """
        Delete(self: ScreenUserFolder)
            Deletes this instance.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenUserFolder, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenUserFolder) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenUserFolder) -> str
        
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

    Folders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screen user folders

Get: Folders(self: ScreenUserFolder) -> ScreenUserFolderComposition

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the screen user folder

Get: Name(self: ScreenUserFolder) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ScreenUserFolder) -> IEngineeringObject

"""

    Screens = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Composition of screens

Get: Screens(self: ScreenUserFolder) -> ScreenComposition

"""



class ScreenUserFolderComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[ScreenUserFolder], IEquatable[object]):
    """ Composition of ScreenUserFolders """
    def Contains(self, item):
        """
        Contains(self: ScreenUserFolderComposition, item: ScreenUserFolder) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, name):
        """
        Create(self: ScreenUserFolderComposition, name: str) -> ScreenUserFolder
        
            Creates a screen user folder
        
            name: Name of folder to be created
            Returns: Siemens.Engineering.Hmi.Screen.ScreenUserFolder
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: ScreenUserFolderComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Find(self, name):
        """
        Find(self: ScreenUserFolderComposition, name: str) -> ScreenUserFolder
        
            Finds a given screen user folder
        
            name: Name to find
            Returns: Siemens.Engineering.Hmi.Screen.ScreenUserFolder
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScreenUserFolderComposition) -> IEnumerator[ScreenUserFolder]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ScreenUserFolderComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: ScreenUserFolderComposition, item: ScreenUserFolder) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: ScreenUserFolderComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenUserFolder](enumerable: IEnumerable[ScreenUserFolder], value: ScreenUserFolder) -> bool """
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

Get: Count(self: ScreenUserFolderComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: ScreenUserFolderComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: ScreenUserFolderComposition) -> IEngineeringObject

"""



class SlideinType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines the available Slide-In screen types.
    
    enum SlideinType, values: Bottom (1), Left (2), Right (3), Top (0)
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

    Bottom = None
    Left = None
    Right = None
    Top = None
    value__ = None


class StyleLibraryType(LibraryType, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type made from a style """
    def Equals(self, obj):
        """
        Equals(self: StyleLibraryType, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: StyleLibraryType) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: StyleLibraryType) -> str
        
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

Get: Name(self: StyleLibraryType) -> str

Set: Name(self: StyleLibraryType) = value
"""



class StyleLibraryTypeVersion(LibraryTypeVersion, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type version made from a style """
    def Equals(self, obj):
        """
        Equals(self: StyleLibraryTypeVersion, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: StyleLibraryTypeVersion) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: StyleLibraryTypeVersion) -> str
        
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


class StyleSheetLibraryType(LibraryType, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibraryTypeOrFolderSelection, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type made from a style sheet """
    def Equals(self, obj):
        """
        Equals(self: StyleSheetLibraryType, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: StyleSheetLibraryType) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: StyleSheetLibraryType) -> str
        
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

Get: Name(self: StyleSheetLibraryType) -> str

Set: Name(self: StyleSheetLibraryType) = value
"""



class StyleSheetLibraryTypeVersion(LibraryTypeVersion, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a library type version made from a style sheet """
    def Equals(self, obj):
        """
        Equals(self: StyleSheetLibraryTypeVersion, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: StyleSheetLibraryTypeVersion) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: StyleSheetLibraryTypeVersion) -> str
        
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


class VisibilityModes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defindes the VisibilityModes
    
    enum VisibilityModes, values: FadeOut (0), ShowAlways (1), ShowNever (2)
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

    FadeOut = None
    ShowAlways = None
    ShowNever = None
    value__ = None


