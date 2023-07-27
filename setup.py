from setuptools import setup

APP = ['TThrottling.py']
DATA_FILES = ['osx-cpu-temp']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'logo.icns',
    'plist': {
        'CFBundleShortVersionString': '0.0.1',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='TThrottling',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
