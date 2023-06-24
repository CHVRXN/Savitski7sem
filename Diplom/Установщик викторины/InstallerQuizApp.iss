[Setup]
AppName=Викторина по оценке знаний языка программирования Python
AppVersion=1.0
DefaultDirName={userdocs}\QuizApp
DisableDirPage=no
OutputDir=Output
OutputBaseFilename=QuizAppSetup
SetupIconFile="C:\Users\daimo\Downloads\iconquiaapp.ico"

[Files]
Source: "C:\Users\daimo\Desktop\savicapp\Savitski7sem\Diplom\Quiz-App\dist\quiz\*"; DestDir: "{app}"; Flags: recursesubdirs; Permissions: everyone-modify

[Icons]
Name: "{commondesktop}\Quiz App"; Filename: "{app}\Quiz.exe"; IconFilename: "{app}\iconquiaapp.ico"; WorkingDir: "{app}"

[Run]
Filename: "{app}\Quiz.exe"; Description: "Launch Quiz App"; Flags: postinstall