from setuptools import setup, find_packages
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class DevelopCommandHook(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        from pyppeteer.chromium_downloader import download_chromium
        download_chromium()


class InstallCommandHook(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        from pyppeteer.chromium_downloader import download_chromium
        download_chromium()


setup(
    name='pyppeteerautodownload',
    version='1.0.0',
    url='',
    author='',
    author_email='',
    description='Description of my package',
    packages=find_packages(),
    install_requires=['pyppeteer'],
    cmdclass={
        'develop': DevelopCommandHook,
        'install': InstallCommandHook,
    },
)
