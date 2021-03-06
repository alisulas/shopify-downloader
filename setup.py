from setuptools import setup, find_packages

setup(
    name='shopify-downloader',
    version='1.0.1',

    description="Downloads data from the Shopify API to local files",

    install_requires=[
        'ShopifyAPI==2.5.0',
        'click>=6.0'
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={
        'console_scripts': [
            'download-shopify-data=shopify_downloader.cli:download_data'
        ]
    }
)
