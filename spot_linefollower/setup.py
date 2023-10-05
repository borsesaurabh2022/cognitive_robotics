from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'spot_linefollower'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srb-jarvis',
    maintainer_email='srb-jarvis@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spot_linefollower = spot_linefollower.spot_linefollower:main',
            'spot_linefollower_rev2 = spot_linefollower.spot_linefollower_rev2:main',
        ],
    },
)
