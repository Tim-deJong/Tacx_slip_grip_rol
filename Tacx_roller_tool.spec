# -*- mode: python -*-

block_cipher = None


a = Analysis(['Tacx_roller_tool.py'],
             pathex=['C:\\Windows\\System32\\downlevel\\', 'C:\\Users\\Jelle\\PycharmProjects\\Tacx_Simulant_Verificatie_Script_GIT\\Tacx_slip_grip_rol', 'C:\\Users\\Jelle\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\scipy\\extra-dll\\', 'C:\\Users\\Jelle\\PycharmProjects\\Tacx_Simulant_Verificatie_Script_GIT\\Tacx_Simulant_Verificatie_Script'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('tacx-logo.png', 'C:\\Users\\Jelle\\PycharmProjects\\Tacx_Simulant_Verificatie_Script_GIT\\Tacx_Simulant_Verificatie_Script\\tacx-logo.png', 'Data')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Tacx_roller_tool',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Tacx_roller_tool')
