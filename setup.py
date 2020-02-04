from setuptools import setup, find_packages
import os

install_requires = ["flask", "wheel"]
try:
    [os.system(f'"pip install {package}"') for package in install_requires]
finally:
    os.system('"echo Starting Server"')

setup(name="",
      version="0.0.0",
      description="Stripe Test Server",
      author="SIS-IEC",
      author_email="suva.saha@jci.com",
      packages=["stripe_test_sever"],
      license="GNU General Public License",
      install_requires=install_requires,
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Development Status :: 1 - Beta",
                   "Intended Audience :: Users",
                   "Operating System :: OS Independent",
                   ],
      entry_points={'console_scripts': ['Stripe-Test = App:main']
                    }
      )
