from setuptools import setup

APP = ['overlay_app.py']
OPTIONS = {
    'packages': ['Cocoa'],
    'strip': False,  # 👈 prevent SIP-related strip errors
    'plist': {
        'CFBundleName': 'PrivateOverlay',
        'CFBundleIdentifier': 'com.mani.privateoverlay',
        'CFBundleShortVersionString': '0.1.0',
        'NSHighResolutionCapable': True,
    },
}
setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
