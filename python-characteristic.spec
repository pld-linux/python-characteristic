#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python attributes without boilerplate
Summary(pl.UTF-8):	Atrybuty w Pythonie bez ramowego kodu
Name:		python-characteristic
Version:	14.3.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/characteristic/
Source0:	https://files.pythonhosted.org/packages/source/c/characteristic/characteristic-%{version}.tar.gz
# Source0-md5:	b249368dd021fde1c06b4802867c0913
Patch0:		%{name}-setup.patch
URL:		https://characteristic.readthedocs.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools >= 1:7.0
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 1:7.0
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
characteristic is an MIT-licensed Python package with class decorators
that ease the chores of implementing the most common attribute-related
object protocols.

You just specify the attributes to work with and characteristic gives
you any or all of:
 - a nice human-readable __repr__,
 - a complete set of comparison methods,
 - immutability for attributes,
 - and a kwargs-based initializer (that cooperates with your existing
   one and optionally even checks the types of the arguments)

without writing dull boilerplate code again and again.

%description -l pl.UTF-8
characteristic to udostępniony na licencji MIT moduł Pythona z
dekoratorami klas ułatwiający implementowanie większości popularnych
protokołów związanych z atrybutami.

Wystarczy podać atrybuty, a characteristic daje dowolne lub wszystkie
z następujących cech:
 - czytelne dla człowieka __repr__,
 - pełny zestaw metod porównujących,
 - niezmienność atrybutów,
 - konstruktor oparty na kwargs (współpracujący z istniejącym,
   opcjonalnie nawet sprawdzający typy argumentów)

bez pisania ciągle nudnego kodu ramowego.

%package -n python3-characteristic
Summary:	Python attributes without boilerplate
Summary(pl.UTF-8):	Atrybuty w Pythonie bez ramowego kodu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-characteristic
characteristic is an MIT-licensed Python package with class decorators
that ease the chores of implementing the most common attribute-related
object protocols.

You just specify the attributes to work with and characteristic gives
you any or all of:
 - a nice human-readable __repr__,
 - a complete set of comparison methods,
 - immutability for attributes,
 - and a kwargs-based initializer (that cooperates with your existing
   one and optionally even checks the types of the arguments)

without writing dull boilerplate code again and again.

%description -n python3-characteristic -l pl.UTF-8
characteristic to udostępniony na licencji MIT moduł Pythona z
dekoratorami klas ułatwiający implementowanie większości popularnych
protokołów związanych z atrybutami.

Wystarczy podać atrybuty, a characteristic daje dowolne lub wszystkie
z następujących cech:
 - czytelne dla człowieka __repr__,
 - pełny zestaw metod porównujących,
 - niezmienność atrybutów,
 - konstruktor oparty na kwargs (współpracujący z istniejącym,
   opcjonalnie nawet sprawdzający typy argumentów)

bez pisania ciągle nudnego kodu ramowego.

%package apidocs
Summary:	API documentation for Python characteristic module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona characteristic
Group:		Documentation

%description apidocs
API documentation for Python characteristic module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona characteristic.

%prep
%setup -q -n characteristic-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/test_characteristic.py*
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/test_characteristic.py \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/__pycache__/test_characteristic.*.py* \
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst LICENSE README.rst
%{py_sitescriptdir}/characteristic.py[co]
%{py_sitescriptdir}/characteristic-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-characteristic
%defattr(644,root,root,755)
%doc AUTHORS.rst LICENSE README.rst
%{py3_sitescriptdir}/characteristic.py
%{py3_sitescriptdir}/__pycache__/characteristic.cpython-*.py[co]
%{py3_sitescriptdir}/characteristic-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
