#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : positional
Version  : 1.2.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/24/7e/3b1450db76eb48a54ea661a43ae00950275e11840042c5217bd3b47b478e/positional-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/24/7e/3b1450db76eb48a54ea661a43ae00950275e11840042c5217bd3b47b478e/positional-1.2.1.tar.gz
Summary  : Library to enforce positional or key-word arguments (deprecated/unmaintained)
Group    : Development/Tools
License  : Apache-2.0
Requires: positional-license = %{version}-%{release}
Requires: positional-python = %{version}-%{release}
Requires: positional-python3 = %{version}-%{release}
Requires: pbr
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : wrapt
Patch1: 0001-test.patch

%description
==========
positional
==========

A decorator which enforces only some args may be passed positionally. This library is minimally maintained and should only be used in cases of Python 2 to Python 3 conversions. Please write only Python 3 code going forward.

|PyPi|

|Build Status|

|Documentation Status|

The Basics
==========

`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

The decorator makes it easy to support Python 3 style key-word only
parameters. For example, in Python 3 it is possible to write:

.. code:: python

    >>> def fn(pos1, *, kwonly1, kwonly2=None):
    ...     ...

All named parameters after `*` must be a keyword:

.. code:: python

    >>> fn(10, 'kw1', 'kw2')  # Raises exception.
    >>> fn(10, kwonly1='kw1', kwonly2='kw2')  # Ok.

To replicate this behaviour with the positional decorator you simply specify
how many arguments may be passed positionally.

First to import the decorator we typically use:

.. code:: python

    >> from positional import positional

Replicating the Example above:

.. code:: python

    >>> @positional(1)
    ... fn(pos1, kwonly1=None, kwonly2=None):
    ...     ...

If no default value is provided to a keyword argument, it becomes a required
keyword argument:

.. code:: python

    >>> @positional(0)
    ... def fn(required_kw):
    ...     ...

This must be called with the keyword parameter:

.. code:: python

    >>> fn() # Raises exception
    >>> fn(10) # Raises Exception
    >>> fn(required_kw=10) # OK

When defining instance or class methods always remember that in python the
first positional argument passed is the instance; you will need to account for
`self` and `cls`:

.. code:: python

    >>> class MyClass(object):
    ...
    ...     @positional(2)
    ...     def my_method(self, pos1, kwonly1=None):
    ...         ...
    ...
    ...     @classmethod
    ...     @positional(2)
    ...     def my_method(cls, pos1, kwonly1=None):
    ...         ...



If you would prefer not to account for `self` and `cls` you can use the
`method` and `classmethod` helpers which do not consider the initial
positional argument. So the following class is exactly the same as the one
above:

.. code:: python

    >>> class MyClass(object):
    ...
    ...     @positional.method(1)
    ...     def my_method(self, pos1, kwonly1=None):
    ...         ...
    ...
    ...     @positional.classmethod(1)
    ...     def my_method(cls, pos1, kwonly1=None):
    ...         ...


If a value isn't provided to the decorator then it will enforce that
every variable without a default value will be required to be a kwarg:

.. code:: python

    >>> @positional()
    ... def fn(pos1, kwonly1=None):
    ...     ...
    ...
    >>> fn(10)  # Ok.
    >>> fn(10, 20)  # Raises exception.
    >>> fn(10, kwonly1=20)  # Ok.

This behaviour will work with the `positional.method` and
`positional.classmethod` helper functions as well:

.. code:: python

    >>> class MyClass(object):
    ...
    ...    @positional.classmethod()
    ...    def my_method(cls, pos1, kwonly1=None):
    ...        ...
    ...
    >>> MyClass.my_method(10)  # Ok.
    >>> MyClass.my_method(10, 20)  # Raises exception.
    >>> MyClass.my_method(10, kwonly1=20)  # Ok.

For compatibility reasons you may wish to not always raise an exception so
a WARN mode is available. Rather than raise an exception a warning will be
emitted.

.. code:: python

    >>> @positional(1, enforcement=positional.WARN):
    ... def fn(pos1, kwonly=1):
    ...     ...

Available modes are:

- positional.EXCEPT - the default, raise an exception.
- positional.WARN - emit a warning.


.. |Build Status| image:: https://travis-ci.org/morganfainberg/positional.svg?branch=master
   :target: https://travis-ci.org/morganfainberg/positional
.. |Documentation Status| image:: https://readthedocs.org/projects/positional/badge/?version=latest
   :target: http://positional.readthedocs.org/en/latest/?badge=latest
.. |PyPi| image:: https://badge.fury.io/py/positional.png
   :target: http://badge.fury.io/py/positional

%package license
Summary: license components for the positional package.
Group: Default

%description license
license components for the positional package.


%package python
Summary: python components for the positional package.
Group: Default
Requires: positional-python3 = %{version}-%{release}

%description python
python components for the positional package.


%package python3
Summary: python3 components for the positional package.
Group: Default
Requires: python3-core
Provides: pypi(positional)

%description python3
python3 components for the positional package.


%prep
%setup -q -n positional-1.2.1
cd %{_builddir}/positional-1.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583202908
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/positional
cp %{_builddir}/positional-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/positional/ab493383353f91b9ccc38085a5044fbef904b58b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/positional/ab493383353f91b9ccc38085a5044fbef904b58b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
