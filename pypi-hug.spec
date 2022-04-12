#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hug
Version  : 2.6.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/9e/b2/0549ffd2f6bdeb37e5cbee7119830e0928ca0df12c16ab8ed68078c69239/hug-2.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/b2/0549ffd2f6bdeb37e5cbee7119830e0928ca0df12c16ab8ed68078c69239/hug-2.6.1.tar.gz
Summary  : A Python framework that makes developing APIs as simple as possible, but no simpler.
Group    : Development/Tools
License  : MIT
Requires: pypi-hug-bin = %{version}-%{release}
Requires: pypi-hug-license = %{version}-%{release}
Requires: pypi-hug-python = %{version}-%{release}
Requires: pypi-hug-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(falcon)
BuildRequires : pypi(requests)

%description
===================

%package bin
Summary: bin components for the pypi-hug package.
Group: Binaries
Requires: pypi-hug-license = %{version}-%{release}

%description bin
bin components for the pypi-hug package.


%package license
Summary: license components for the pypi-hug package.
Group: Default

%description license
license components for the pypi-hug package.


%package python
Summary: python components for the pypi-hug package.
Group: Default
Requires: pypi-hug-python3 = %{version}-%{release}

%description python
python components for the pypi-hug package.


%package python3
Summary: python3 components for the pypi-hug package.
Group: Default
Requires: python3-core
Provides: pypi(hug)
Requires: pypi(falcon)
Requires: pypi(requests)

%description python3
python3 components for the pypi-hug package.


%prep
%setup -q -n hug-2.6.1
cd %{_builddir}/hug-2.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649760637
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hug
cp %{_builddir}/hug-2.6.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-hug/c6ca637152f3dab4f58fb699f328ef27a7c3eb00
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hug

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hug/c6ca637152f3dab4f58fb699f328ef27a7c3eb00

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
