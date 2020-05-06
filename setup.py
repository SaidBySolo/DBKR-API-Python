import setuptools

setuptools.setup(
    name="dbkrpy",
    version="0.4.2",
    license='MIT',
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    description="DBKR Api wrapped with aiohttp",
    long_description=open('README.md', 'rt', encoding='UTF8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SaidBySolo/DBKR-API-Python",
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp[speedup]',
    ],
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
