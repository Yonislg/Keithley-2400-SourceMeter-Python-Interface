# -*- mode: python -*-

block_cipher = None


a = Analysis(['trace_gui.py'],
             pathex=['C:\\Users\\Usuario\\PycharmProjects\\Keithley-2400-SourceMeter-Python-Interface'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='trace_gui',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Usuario\\PycharmProjects\\Keithley-2400-SourceMeter-Python-Interface\\langmuir_plasma_2xG_icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='trace_gui')
