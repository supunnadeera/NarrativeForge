from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="NarrativeForge",
    version="0.1.7",
    description='A package for adding text and ai generated voice to videos.',
    author='supun nadeera',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/supunnadeera/NarrativeForge',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "moviepy",
        "openai==1.10.0",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "NarrativeForge=NarrativeForge.text_to_video:main",
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={ 
        'Source': 'https://github.com/supunnadeera/NarrativeForge',
    },
)