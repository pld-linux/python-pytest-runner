#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Invoke py.test as distutils command with dependency resolution
Summary(pl.UTF-8):	Wywoływanie py.test jako polecenia distutils z rozwiązywaniem zależności
Name:		python-pytest-runner
# keep 5.2.x here for python2 support
Version:	5.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-runner/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-runner/pytest-runner-%{version}.tar.gz
# Source0-md5:	e5f66b8e8e87f62c59631c35c919d321
URL:		https://github.com/pytest-dev/pytest-runner
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:31.0.1
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-pytest >= 3.5
BuildRequires:	python-pytest-black-multipy
BuildRequires:	python-pytest-cov
BuildRequires:	python-pytest-flake8
BuildRequires:	python-pytest-virtualenv
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:31.0.1
BuildRequires:	python3-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python3-pytest >= 3.5
BuildRequires:	python3-pytest-black-multipy
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-flake8
BuildRequires:	python3-pytest-virtualenv
%endif
%endif
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

%description -l pl.UTF-8
Skrypty setup mogą wykorzystywać moduł pytest-runner do dodawania
obsługi testów pytest runnera w setup.py.

%package -n python3-pytest-runner
Summary:	Invoke py.test as distutils command with dependency resolution
Summary(pl.UTF-8):	Wywoływanie py.test jako polecenia distutils z rozwiązywaniem zależności
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pytest-runner
Setup scripts can use pytest-runner to add setup.py test support for
pytest runner.

%description -n python3-pytest-runner -l pl.UTF-8
Skrypty setup mogą wykorzystywać moduł pytest-runner do dodawania
obsługi testów pytest runnera w setup.py.

%package apidocs
Summary:	pytest-runner module documentation
Summary(pl.UTF-8):	Dokumentacja modułu pytest-runner
Group:		Documentation

%description apidocs
Documentation for pytest-runner module.

%description apidocs -l pl.UTF-8
Dokumentacja modułu pytest-runner.

%prep
%setup -q -n pytest-runner-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_black_multipy,pytest_cov.plugin,pytest_flake8,pytest_virtualenv \
%{__python} -m pytest ptr.py tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_black_multipy,pytest_cov.plugin,pytest_flake8,pytest_virtualenv \
%{__python3} -m pytest ptr.py tests
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/ptr.py[co]
%{py_sitescriptdir}/pytest_runner-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-runner
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/ptr.py
%{py3_sitescriptdir}/__pycache__/ptr.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_runner-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
