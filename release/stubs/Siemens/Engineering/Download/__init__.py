# encoding: utf-8
# module Siemens.Engineering.Download calls itself Download
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DownloadConfigurationDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ DownloadConfigurationDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, downloadConfiguration, callback, object):
        """ BeginInvoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current delegate.-or- 
             
                    ll, if the method represented by the current delegate does not require arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DownloadConfigurationDelegate, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, downloadConfiguration):
        """ Invoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to the specified 
             delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without value in its 
             invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class DownloadOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible download options
    
    enum (flags) DownloadOptions, values: Hardware (1), None (0), Software (2)
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

    Hardware = None
    None = None
    Software = None
    value__ = None


class DownloadProvider(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Service provides download functionality """
    def Download(self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions):
        """
        Download(self: DownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult
        
            Downloads hardware and software to the device
        
            configuration: Connection cofiguration path to a device.
            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.
            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.
            downloadOptions: Download options
            Returns: Siemens.Engineering.Download.DownloadResult
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DownloadProvider, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DownloadProvider, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DownloadProvider) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DownloadProvider, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DownloadProvider) -> str
        
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

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Connection Configuration.

Get: Configuration(self: DownloadProvider) -> ConnectionConfiguration

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DownloadProvider) -> IEngineeringObject

"""



class DownloadResult(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ The results of a download """
    def Equals(self, obj):
        """
        Equals(self: DownloadResult, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DownloadResult, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResult) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DownloadResult, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DownloadResult) -> str
        
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

    ErrorCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of errors in a given download scenario

Get: ErrorCount(self: DownloadResult) -> int

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Collection of output messages for the result of a given download scenario.

Get: Messages(self: DownloadResult) -> DownloadResultMessageComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DownloadResult) -> IEngineeringObject

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Final state of a given compile scenario

Get: State(self: DownloadResult) -> DownloadResultState

"""

    WarningCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of warnings in a given download scenario

Get: WarningCount(self: DownloadResult) -> int

"""



class DownloadResultMessage(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Download result message """
    def Equals(self, obj):
        """
        Equals(self: DownloadResultMessage, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: DownloadResultMessage, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResultMessage) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: DownloadResultMessage, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: DownloadResultMessage) -> str
        
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

    DateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Date and time in a download message

Get: DateTime(self: DownloadResultMessage) -> DateTime

"""

    ErrorCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of errors in a download message

Get: ErrorCount(self: DownloadResultMessage) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Description or content of a download message

Get: Message(self: DownloadResultMessage) -> str

"""

    Messages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Access to the download messages for a given download scenario

Get: Messages(self: DownloadResultMessage) -> DownloadResultMessageComposition

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: DownloadResultMessage) -> IEngineeringObject

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Final state in a download message

Get: State(self: DownloadResultMessage) -> DownloadResultState

"""

    WarningCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of warnings in a download message

Get: WarningCount(self: DownloadResultMessage) -> int

"""



class DownloadResultMessageComposition(object, IEngineeringComposition, IEngineeringCompositionOrObject, IEngineeringInstance, IEnumerable, IInternalCompositionAccess, IInternalCollectionAccess, IInternalInstanceAccess, IInternalBaseAccess, IEnumerable[DownloadResultMessage], IEquatable[object]):
    """ Composition of download result messages. """
    def Contains(self, item):
        """
        Contains(self: DownloadResultMessageComposition, item: DownloadResultMessage) -> bool
        
            Determines if item is contained within.
        
            item: The item being sought.
            Returns: true if item is contained within; otherwise false.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: DownloadResultMessageComposition, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: DownloadResultMessageComposition) -> IEnumerator[DownloadResultMessage]
        
            Returns an enumerator that iterates through a collection.
            Returns: A System.Collections.Generic.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: DownloadResultMessageComposition) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def IndexOf(self, item):
        """
        IndexOf(self: DownloadResultMessageComposition, item: DownloadResultMessage) -> int
        
            Searches for item and returns the zero-based index of the first occurrence within.
        
            item: The item for which an index is sought.
            Returns: The zero-based index of item of the first occurrence within.
        """
        pass

    def ToString(self):
        """
        ToString(self: DownloadResultMessageComposition) -> str
        
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DownloadResultMessage](enumerable: IEnumerable[DownloadResultMessage], value: DownloadResultMessage) -> bool """
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

Get: Count(self: DownloadResultMessageComposition) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this instance is read only.

Get: IsReadOnly(self: DownloadResultMessageComposition) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent.

Get: Parent(self: DownloadResultMessageComposition) -> IEngineeringObject

"""



class DownloadResultState(Enum, IComparable, IFormattable, IConvertible):
    """
    The list of possible compiler result options
    
    enum DownloadResultState, values: Error (3), Information (1), Success (0), Warning (2)
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

    Error = None
    Information = None
    Success = None
    value__ = None
    Warning = None


class RHDownloadProvider(object, IEngineeringService, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Service provides download functionality for R/H systems """
    def DownloadToBackup(self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions):
        """
        DownloadToBackup(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult
        
            Downloads hardware and software to the backup device
        
            configuration: Connection cofiguration path to a device.
            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.
            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.
            downloadOptions: Download options
            Returns: Siemens.Engineering.Download.DownloadResult
        """
        pass

    def DownloadToPrimary(self, configuration, preDownloadConfigurationDelegate, postDownloadConfigurationDelegate, downloadOptions):
        """
        DownloadToPrimary(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult
        
            Downloads hardware and software to the primary device
        
            configuration: Connection cofiguration path to a device.
            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.
            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.
            downloadOptions: Download options
            Returns: Siemens.Engineering.Download.DownloadResult
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: RHDownloadProvider, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: RHDownloadProvider) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: RHDownloadProvider) -> str
        
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

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Connection Configuration.

Get: Configuration(self: RHDownloadProvider) -> ConnectionConfiguration

"""



# variables with complex values

