# encoding: utf-8
# module Siemens.Engineering.HmiUnified.HmiLogging.HmiLoggingCommon calls itself HmiLoggingCommon
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class HmiBackupMode(Enum, IComparable, IFormattable, IConvertible):
    """
    HmiBackupMode
    
    enum HmiBackupMode, values: NoBackup (0), PrimaryPath (1)
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

    NoBackup = None
    PrimaryPath = None
    value__ = None


class LogBackup(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Logging backup configuration """
    def Equals(self, obj):
        """
        Equals(self: LogBackup, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LogBackup, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LogBackup) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LogBackup, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LogBackup) -> str
        
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

    BackupMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the backup mode

Get: BackupMode(self: LogBackup) -> HmiBackupMode

Set: BackupMode(self: LogBackup) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LogBackup) -> IEngineeringObject

"""

    PrimaryPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logging backup path

Get: PrimaryPath(self: LogBackup) -> str

Set: PrimaryPath(self: LogBackup) = value
"""



class LogDuration(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Specifies the time period type """
    def Equals(self, obj):
        """
        Equals(self: LogDuration, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LogDuration, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetDoubleLogDuration(self):
        """
        GetDoubleLogDuration(self: LogDuration) -> float
        
            Return timeperiod in double
            Returns: System.Double
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LogDuration) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetStringLogDuration(self):
        """
        GetStringLogDuration(self: LogDuration) -> str
        
            Return Log Duration in String
            Returns: System.String
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LogDuration, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def SetLogDuration(self, days, hours, minutes, seconds, ticks):
        """
        SetLogDuration(self: LogDuration, days: UInt32, hours: UInt32, minutes: UInt32, seconds: UInt32, ticks: UInt32) -> str
        
            Set timeperiod in double
        
            days: Day
            hours: hours
            minutes: minutes
            seconds: seconds
            ticks: hundred nanoseconds
            Returns: System.String
        """
        pass

    def ToString(self):
        """
        ToString(self: LogDuration) -> str
        
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

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies number of days

Get: Days(self: LogDuration) -> UInt32

Set: Days(self: LogDuration) = value
"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies number of hours

Get: Hours(self: LogDuration) -> UInt32

Set: Hours(self: LogDuration) = value
"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies minutes

Get: Minutes(self: LogDuration) -> UInt32

Set: Minutes(self: LogDuration) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LogDuration) -> IEngineeringObject

"""

    Seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies seconds

Get: Seconds(self: LogDuration) -> UInt32

Set: Seconds(self: LogDuration) = value
"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hundred Nonoseconds

Get: Ticks(self: LogDuration) -> UInt32

Set: Ticks(self: LogDuration) = value
"""



class LoggingBase(HmiBase, IValidator, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Base class for Alarm and Data logging """
    def Equals(self, obj):
        """
        Equals(self: LoggingBase, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LoggingBase) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def ToString(self):
        """
        ToString(self: LoggingBase) -> str
        
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

    Backup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log backup

Get: Backup(self: LoggingBase) -> LogBackup

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LoggingBase) -> IEngineeringObject

"""

    Segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log segment for backup

Get: Segment(self: LoggingBase) -> LogSegment

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Logging settings

Get: Settings(self: LoggingBase) -> LogSettings

"""



class LogSegment(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Logging segment configuration """
    def Equals(self, obj):
        """
        Equals(self: LogSegment, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LogSegment, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LogSegment) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LogSegment, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LogSegment) -> str
        
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

Get: Parent(self: LogSegment) -> IEngineeringObject

"""

    SegmentMaxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines the maximum size of a segment of the log on the storage medium in units of megabytes. When the value is set to 0, the size of the segment is not considered.

Get: SegmentMaxSize(self: LogSegment) -> UInt32

Set: SegmentMaxSize(self: LogSegment) = value
"""

    SegmentStartTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start time of the logging segment

Get: SegmentStartTime(self: LogSegment) -> DateTime

Set: SegmentStartTime(self: LogSegment) = value
"""

    SegmentTimePeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Segment Time Period

Get: SegmentTimePeriod(self: LogSegment) -> SegmentDuration

"""



class LogSettings(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Logging configuration """
    def Equals(self, obj):
        """
        Equals(self: LogSettings, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: LogSettings, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LogSettings) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: LogSettings, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def ToString(self):
        """
        ToString(self: LogSettings) -> str
        
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

    LogMaxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum size of data storage in MB

Get: LogMaxSize(self: LogSettings) -> UInt32

Set: LogMaxSize(self: LogSettings) = value
"""

    LogTimePeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Log Time period

Get: LogTimePeriod(self: LogSettings) -> LogDuration

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: LogSettings) -> IEngineeringObject

"""

    StoragePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Path for storage

Get: StoragePath(self: LogSettings) -> str

Set: StoragePath(self: LogSettings) = value
"""



class SegmentDuration(object, IEngineeringObject, IEngineeringCompositionOrObject, IEngineeringInstance, IInternalObjectAccess, IInternalInstanceAccess, IInternalBaseAccess, IEquatable[object]):
    """ Segment duration Class """
    def Equals(self, obj):
        """
        Equals(self: SegmentDuration, obj: object) -> bool
        
            Determines whether the specified System.Object is equal to this instance.
        
            obj: The System.Object to compare with this instance.
            Returns: true if the specified System.Object is equal to this instance; otherwise, false.
        """
        pass

    def GetAttributes(self, names):
        """ GetAttributes(self: SegmentDuration, names: IEnumerable[str]) -> IList[object] """
        pass

    def GetDoubleSegmentDuration(self):
        """
        GetDoubleSegmentDuration(self: SegmentDuration) -> float
        
            Method for getting segment timeperiod
            Returns: System.Double
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SegmentDuration) -> int
        
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        pass

    def GetStringSegmentDuration(self):
        """
        GetStringSegmentDuration(self: SegmentDuration) -> str
        
            Return Segment Duration in String
            Returns: System.String
        """
        pass

    def SetAttributes(self, attributes):
        """ SetAttributes(self: SegmentDuration, attributes: IEnumerable[KeyValuePair[str, object]]) """
        pass

    def SetSegmentDuration(self, days, hours, minutes, seconds, ticks):
        """
        SetSegmentDuration(self: SegmentDuration, days: UInt32, hours: UInt32, minutes: UInt32, seconds: UInt32, ticks: UInt32) -> str
        
            Method for setting segment timeperiod
        
            days: days
            hours: hours
            minutes: minutes
            seconds: seconds
            ticks: Hundred Nanoseconds
            Returns: System.String
        """
        pass

    def ToString(self):
        """
        ToString(self: SegmentDuration) -> str
        
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

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Days

Get: Days(self: SegmentDuration) -> UInt32

Set: Days(self: SegmentDuration) = value
"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hours

Get: Hours(self: SegmentDuration) -> UInt32

Set: Hours(self: SegmentDuration) = value
"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Minutes

Get: Minutes(self: SegmentDuration) -> UInt32

Set: Minutes(self: SegmentDuration) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """EOM parent of this object

Get: Parent(self: SegmentDuration) -> IEngineeringObject

"""

    Seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Seconds

Get: Seconds(self: SegmentDuration) -> UInt32

Set: Seconds(self: SegmentDuration) = value
"""

    Ticks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hundred Nanoseconds

Get: Ticks(self: SegmentDuration) -> UInt32

Set: Ticks(self: SegmentDuration) = value
"""



