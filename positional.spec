#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : positional
Version  : 1.1.1
Release  : 6
URL      : http://pypi.debian.net/positional/positional-1.1.1.tar.gz
Source0  : http://pypi.debian.net/positional/positional-1.1.1.tar.gz
Summary  : Library to enforce positional or key-word arguments
Group    : Development/Tools
License  : Apache-2.0
Requires: positional-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: 0001-test.patch

%description
==========
positional
==========
A decorator which enforces only some args may be passed positionally.

%package python
Summary: python components for the positional package.
Group: Default

%description python
python components for the positional package.


%prep
%setup -q -n positional-1.1.1
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
