
[Setup]
AppId={{A81B6F42-6B21-4C52-9D17-0B8D1E25F010}
AppName=OrbitLang
AppVersion=0.1.0
DefaultDirName={autopf}\OrbitLang
DefaultGroupName=OrbitLang
OutputDir=..\dist
OutputBaseFilename=OrbitLang-Setup-0.1.0
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
UninstallDisplayName=OrbitLang

[Files]
Source: "..\dist\orbit.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\OrbitLang"; Filename: "{app}\orbit.exe"
