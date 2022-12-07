# encoding: utf-8
# module Siemens.Engineering.Cax calls itself Cax
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CaxImportOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Cax Import Merge options
    
    enum CaxImportOptions, values: MoveToParkingLot (0), OverwriteTiaDevice (1), RetainTiaDevice (2)
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

    MoveToParkingLot = None
    OverwriteTiaDevice = None
    RetainTiaDevice = None
    value__ = None


class CaxProvider(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Service Provider for CAx Export/Import operations """
    def Equals(self, obj):
        """
        Equals(self: CaxProvider, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def Export(self, *__args):
        """
        Export(self: CaxProvider, deviceToExport: Device, exportFilePath: FileInfo, logFilePath: FileInfo) -> bool
        
            Command to CAx Export at Device level
        
            deviceToExport: Device to Export
            exportFilePath: Export file path
            logFilePath: Log file path
            Returns: System.Boolean
        Export(self: CaxProvider, projectToExport: Project, exportFilePath: FileInfo, logFilePath: FileInfo) -> bool
        
            Command to CAx Export at Project level
        
            projectToExport: Project to Export
            exportFilePath: Export file Path
            logFilePath: Log file Path
            Returns: System.Boolean
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: CaxProvider, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CaxProvider) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def Import(self, importFilePath, logFilePath, importOption):
        """
        Import(self: CaxProvider, importFilePath: FileInfo, logFilePath: FileInfo, importOption: CaxImportOptions) -> bool
        
            Command to CAx Import
        
            importFilePath: Import file path
            logFilePath: Log file path
            importOption: Cax Import Merge options
            Returns: System.Boolean
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: CaxProvider, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: CaxProvider) -> str
        
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

Get: Parent(self: CaxProvider) -> IEngineeringObject

"""



