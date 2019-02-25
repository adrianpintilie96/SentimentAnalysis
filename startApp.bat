@echo off
python %~dp0\sentenceToEmojiService\sentenceToEmojiService.py %*
python %~dp0\sentenceToEmojiWebApp\sentenceToEmojiWebApp.py %*
pause
