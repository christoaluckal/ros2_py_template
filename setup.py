from setuptools import find_packages, setup
from glob import glob

package_name = '__TEMPLATE_PACKAGE'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='christoa',
    maintainer_email='christo12aluckal@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            '__TEMPLATE_EXEC_NAME = __TEMPLATE_PACKAGE.__TEMPLATE_ENTRY:main'
        ],
    },
)
