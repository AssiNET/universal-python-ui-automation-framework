#AutoIt3Wrapper_Change2CUI=y

$fileName=$CmdLine[1]
ConsoleWrite(FileExists($fileName))

While (FileExists($fileName)==0)
	sleep(2000)
WEnd

;~ FileOpen($fileName, 1)
;~ FileWrite ($fileName, "Textbox was started")
;~ FileClose($fileName)
;~ sleep(1000)

$newText=""
$oldText=""
While FileExists($fileName)=1
	$f=FileOpen($fileName)
	$newText=FileReadLine($f)
	FileClose($f)
	if ($newText <> $oldText) Then
		SplashTextOn("", $newText, 500, 15,500,0,(1+4+16+32),"",8)
		$oldText=$newText
	EndIf
	sleep(1000)
WEnd

SplashOff()

