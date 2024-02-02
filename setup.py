from setuptools import setup, find_packages

setup(
    name="NarrativeForge",
    version="0.1.1",
    description='A package for adding text and ai generated voice to videos.',
    author='supun nadeera',
    url='https://github.com/supunnadeera/NarrativeForge',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "numpy",
        "moviepy",
        "openai",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={ 
        'Source': 'https://github.com/supunnadeera/NarrativeForge',
    },
)