# encoding: utf-8
# module Siemens.Engineering.Library calls itself Library
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ILibrary:
    """ Base interface implemented by all libraries """
    def FindType(self, typeGuid):
        """
        FindType(self: ILibrary, typeGuid: Guid) -> LibraryType
        
            Searches the global library for a type object using a type GUID as the search criteria
        
            typeGuid: Globally unique identifier of the type object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        pass

    def FindVersion(self, versionGuid):
        """
        FindVersion(self: ILibrary, versionGuid: Guid) -> LibraryTypeVersion
        
            Searches the global library for a version object using a version GUID as the search criteria
        
            versionGuid: Globally unique identifier of the version object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        pass

    def UpdateCheck(self, project, updateCheckMode):
        """
        UpdateCheck(self: ILibrary, project: Project, updateCheckMode: UpdateCheckMode) -> UpdateCheckResult
        
            Identify all instances in a project that require updating based on the content of this library
        
            project: The project to be compared with this library
            updateCheckMode: Used to control whether or not to log out of date instances
            Returns: Siemens.Engineering.Library.Types.UpdateCheckResult
        """
        pass

    def UpdateLibrary(self, sourceTypesAndFolders, targetLibrary):
        """ UpdateLibrary(self: ILibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], targetLibrary: ILibrary) """
        pass

    def UpdateProject(self, sourceTypesAndFolders, updateProjectScopes):
        """ UpdateProject(self: ILibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], updateProjectScopes: IEnumerable[IUpdateProjectScope]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MasterCopyFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """System folder containing master copies and master copy folders

Get: MasterCopyFolder(self: ILibrary) -> MasterCopySystemFolder

"""

    TypeFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """System folder containing library types and library type folders

Get: TypeFolder(self: ILibrary) -> LibraryTypeSystemFolder

"""



class GlobalLibrary(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ITransactionSupport, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a global library """
    def Equals(self, obj):
        """
        Equals(self: GlobalLibrary, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def FindType(self, typeGuid):
        """
        FindType(self: GlobalLibrary, typeGuid: Guid) -> LibraryType
        
            Searches the global library for a type object using a type GUID as the search criteria
        
            typeGuid: Globally unique identifier of the type object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        pass

    def FindVersion(self, versionGuid):
        """
        FindVersion(self: GlobalLibrary, versionGuid: Guid) -> LibraryTypeVersion
        
            Searches the global library for a version object using a version GUID as the search criteria
        
            versionGuid: Globally unique identifier of the version object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: GlobalLibrary, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibrary) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: GlobalLibrary, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: GlobalLibrary) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def UpdateCheck(self, project, updateCheckMode):
        """
        UpdateCheck(self: GlobalLibrary, project: Project, updateCheckMode: UpdateCheckMode) -> UpdateCheckResult
        
            Identify all instances in a project that require updating based on the content of this library
        
            project: The project to be compared with this global library
            updateCheckMode: Used to control whether or not to log out of date instances
            Returns: Siemens.Engineering.Library.Types.UpdateCheckResult
        """
        pass

    def UpdateLibrary(self, sourceTypesAndFolders, targetLibrary):
        """ UpdateLibrary(self: GlobalLibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], targetLibrary: ILibrary) """
        pass

    def UpdateProject(self, sourceTypesAndFolders, updateProjectScopes):
        """ UpdateProject(self: GlobalLibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], updateProjectScopes: IEnumerable[IUpdateProjectScope]) """
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

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Author of the Global Library

Get: Author(self: GlobalLibrary) -> str

"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The global libraries comment

Get: Comment(self: GlobalLibrary) -> MultilingualText

"""

    IsModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the global library has been modified

Get: IsModified(self: GlobalLibrary) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the global library open only for read

Get: IsReadOnly(self: GlobalLibrary) -> bool

"""

    LanguageSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Global Library language settings

Get: LanguageSettings(self: GlobalLibrary) -> LanguageSettings

"""

    MasterCopyFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets master copy system folder

Get: MasterCopyFolder(self: GlobalLibrary) -> MasterCopySystemFolder

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the global library.

Get: Name(self: GlobalLibrary) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: GlobalLibrary) -> IEngineeringObject

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to this global library

Get: Path(self: GlobalLibrary) -> FileInfo

"""

    TypeFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the library type system folder

Get: TypeFolder(self: GlobalLibrary) -> LibraryTypeSystemFolder

"""



class CorporateGlobalLibrary(GlobalLibrary, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ITransactionSupport, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ A corporate global library. """
    def Equals(self, obj):
        """
        Equals(self: CorporateGlobalLibrary, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CorporateGlobalLibrary) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: CorporateGlobalLibrary) -> str
        
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

Get: Parent(self: CorporateGlobalLibrary) -> IEngineeringObject

"""



class GlobalLibraryComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[GlobalLibrary], IEquatable[object]):
    """ Composition of GlobalLibraries """
    def Contains(self, item):
        """
        Contains(self: GlobalLibraryComposition, item: GlobalLibrary) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Create(self, targetDirectory, name):
        """ Create[T](self: GlobalLibraryComposition, targetDirectory: DirectoryInfo, name: str) -> T """
        pass

    def Equals(self, obj):
        """
        Equals(self: GlobalLibraryComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GlobalLibraryComposition) -> IEnumerator[GlobalLibrary]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetGlobalLibraryInfos(self):
        """
        GetGlobalLibraryInfos(self: GlobalLibraryComposition) -> IList[GlobalLibraryInfo]
        
            Returns a list of LibraryInfo's representing preview state Global Libraries
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Library.GlobalLibraryInfo>
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibraryComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: GlobalLibraryComposition, item: GlobalLibrary) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def Open(self, *__args):
        """
        Open(self: GlobalLibraryComposition, libraryInfo: GlobalLibraryInfo) -> GlobalLibrary
        
            Opens the specified global library
        
            libraryInfo: The global library info associated with a global library to be opened
            Returns: Siemens.Engineering.Library.GlobalLibrary
        Open(self: GlobalLibraryComposition, path: FileInfo, openMode: OpenMode) -> UserGlobalLibrary
        
            Opens the specified global library
        
            path: Path to the global library
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        pass

    def OpenWithUpgrade(self, path):
        """
        OpenWithUpgrade(self: GlobalLibraryComposition, path: FileInfo) -> UserGlobalLibrary
        
            Opens the specified global library and allows for upgrade of older versions if possible.
        
            path: Path to the global library
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        pass

    def Retrieve(self, sourcePath, targetDirectory, openMode):
        """
        Retrieve(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary
        
            Retrieves an archived library
        
            sourcePath: The path of the archived library file
            targetDirectory: The path to the folder where library would be retrieved.
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        pass

    def RetrieveWithUpgrade(self, sourcePath, targetDirectory, openMode):
        """
        RetrieveWithUpgrade(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary
        
            Retrieves a library from an archive and upgrades it to the current version
        
            sourcePath: The path of the archived library file
            targetDirectory: The path to the folder where library would be retrieved.
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        pass

    def ToString(self):
        """
        ToString(self: GlobalLibraryComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GlobalLibrary](enumerable: IEnumerable[GlobalLibrary], value: GlobalLibrary) -> bool """
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

Get: Count(self: GlobalLibraryComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: GlobalLibraryComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: GlobalLibraryComposition) -> IEngineeringObject

"""



class GlobalLibraryInfo(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents information for a Global Library """
    def Equals(self, obj):
        """
        Equals(self: GlobalLibraryInfo, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: GlobalLibraryInfo, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: GlobalLibraryInfo) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: GlobalLibraryInfo, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: GlobalLibraryInfo) -> str
        
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

    IsOpen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a Boolean representing if the global library associated with this GlobalLibraryInfo is already open or not.

Get: IsOpen(self: GlobalLibraryInfo) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the globa library is currently read only.

Get: IsReadOnly(self: GlobalLibraryInfo) -> bool

"""

    LibraryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Global Library Type

Get: LibraryType(self: GlobalLibraryInfo) -> GlobalLibraryType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the global library.

Get: Name(self: GlobalLibraryInfo) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: GlobalLibraryInfo) -> IEngineeringObject

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full library path.

Get: Path(self: GlobalLibraryInfo) -> FileInfo

"""



class GlobalLibraryType(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents the GlobalLibrary Types such as System, User, or Corporate
    
    enum GlobalLibraryType, values: Corporate (1), System (0), User (2)
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

    Corporate = None
    System = None
    User = None
    value__ = None


class LibraryArchivationMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Library archivation modes
    
    enum LibraryArchivationMode, values: Compressed (1), DiscardRestorableData (2), DiscardRestorableDataAndCompressed (3), None (0)
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

    Compressed = None
    DiscardRestorableData = None
    DiscardRestorableDataAndCompressed = None
    None = None
    value__ = None


class ProjectLibrary(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents the project library """
    def Equals(self, obj):
        """
        Equals(self: ProjectLibrary, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def FindType(self, typeGuid):
        """
        FindType(self: ProjectLibrary, typeGuid: Guid) -> LibraryType
        
            Searches the global library for a type object using a type GUID as the search criteria
        
            typeGuid: Globally unique identifier of the type object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        pass

    def FindVersion(self, versionGuid):
        """
        FindVersion(self: ProjectLibrary, versionGuid: Guid) -> LibraryTypeVersion
        
            Searches the global library for a version object using a version GUID as the search criteria
        
            versionGuid: Globally unique identifier of the version object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: ProjectLibrary, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ProjectLibrary) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: ProjectLibrary, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: ProjectLibrary) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def UpdateCheck(self, project, updateCheckMode):
        """
        UpdateCheck(self: ProjectLibrary, project: Project, updateCheckMode: UpdateCheckMode) -> UpdateCheckResult
        
            Identify all instances in a project that require updating based on the content of this library
        
            project: The project to be compared with this global library
            updateCheckMode: Used to control whether or not to log out of date instances
            Returns: Siemens.Engineering.Library.Types.UpdateCheckResult
        """
        pass

    def UpdateLibrary(self, sourceTypesAndFolders, targetLibrary):
        """ UpdateLibrary(self: ProjectLibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], targetLibrary: ILibrary) """
        pass

    def UpdateProject(self, sourceTypesAndFolders, updateProjectScopes):
        """ UpdateProject(self: ProjectLibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], updateProjectScopes: IEnumerable[IUpdateProjectScope]) """
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

    MasterCopyFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets master copy system folder

Get: MasterCopyFolder(self: ProjectLibrary) -> MasterCopySystemFolder

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: ProjectLibrary) -> IEngineeringObject

"""

    TypeFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the library type system folder

Get: TypeFolder(self: ProjectLibrary) -> LibraryTypeSystemFolder

"""



class SystemGlobalLibrary(GlobalLibrary, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ITransactionSupport, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a System Library """
    def Equals(self, obj):
        """
        Equals(self: SystemGlobalLibrary, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SystemGlobalLibrary) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: SystemGlobalLibrary) -> str
        
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

Get: Parent(self: SystemGlobalLibrary) -> IEngineeringObject

"""



class UserGlobalLibrary(GlobalLibrary, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, ITransactionSupport, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Represents a User Global Library """
    def Archive(self, targetDirectory, targetName, archivationMode):
        """
        Archive(self: UserGlobalLibrary, targetDirectory: DirectoryInfo, targetName: str, archivationMode: LibraryArchivationMode)
            Archives the User Global library.
        
            targetDirectory: Directory where the library to be archived
            targetName: File name for the archived file
            archivationMode: Archivation mode
        """
        pass

    def Close(self):
        """
        Close(self: UserGlobalLibrary)
            Closes the User Library
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: UserGlobalLibrary, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: UserGlobalLibrary) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Save(self):
        """
        Save(self: UserGlobalLibrary)
            Saves the User Library
        """
        pass

    def SaveAs(self, targetDirectory):
        """
        SaveAs(self: UserGlobalLibrary, targetDirectory: DirectoryInfo)
            Save a User Library to another location
        
            targetDirectory: The target directory path to save the User Library
        """
        pass

    def ToString(self):
        """
        ToString(self: UserGlobalLibrary) -> str
        
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

Get: Parent(self: UserGlobalLibrary) -> IEngineeringObject

"""



# variables with complex values

