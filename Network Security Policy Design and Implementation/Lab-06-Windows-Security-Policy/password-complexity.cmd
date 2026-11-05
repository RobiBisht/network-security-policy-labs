@echo off
REM Run as Administrator

REM Export security policy
secedit /export /cfg C:\sec.cfg

REM Open the exported policy
notepad C:\sec.cfg

REM Change PasswordComplexity = 0 to PasswordComplexity = 1
REM Save C:\sec.cfg after editing

REM Apply the security policy
secedit /configure /db C:\Windows\security\local.sdb /cfg C:\sec.cfg /areas SECURITYPOLICY

REM Refresh Group Policy
gpupdate /force
