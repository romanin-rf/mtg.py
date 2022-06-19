import mtg2
import os
import setuptools

# * Функция получения полных путей к файлам в папках и подпапках
def globalizer(dirpath: str) -> list:
    files = []
    folder_abspath = os.path.abspath(dirpath)
    if os.path.isdir(folder_abspath):
        for i in os.listdir(folder_abspath):
            path = folder_abspath + os.sep + i
            if os.path.isdir(path):
                for _i in globalizer(path):
                    files.append(_i)
            elif os.path.isfile(path):
                files.append(path)
    elif os.path.isfile(folder_abspath):
        files.append(folder_abspath)
    return files

# * Setup
setuptools.setup(
	name=mtg2.__name__,
	version=mtg2.__version__,
	description='A tablet generator from Minecraft.',
	keywords=[mtg2.__name__],
	packages=setuptools.find_packages(),
	author_email=mtg2.__email__,
	url="https://github.com/romanin-rf/mtg.py",
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
	long_description_content_type="text/markdown",
	package_data={
        "mtg2": globalizer(
            os.path.join(os.path.dirname(__file__), "mtg2", "mtgdata")
        )
    },
	include_package_data=True,
	author=mtg2.__author__,
	license='MIT',
	install_requires=["pillow"],
    setup_requires=["pillow"]
)