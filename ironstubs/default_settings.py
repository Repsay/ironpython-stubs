
PATHS = ["C:\\Program Files\\Siemens\\Automation\\Portal V15_1\\PublicAPI\\V15.1"]

ASSEMBLIES = [
    'System',
    'System.Runtime.Serialization',
    "Siemens.Engineering",
    'Siemens.Engineering.Hmi',
    'Siemens.Engineering.AddIn',
]

BUILTINS = ["clr", "wpf"]

ASSEMBLIES.extend(BUILTINS)
ASSEMBLIES.sort()
