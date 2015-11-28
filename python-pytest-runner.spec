#
# Conditional build:
%bcond_without	doc	# documentation (uses python2)
%bcond_with	tests	# perform "make test" (broken with \--build-base)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%if %{without python2}
%undefine	with_doc
%endif
Summary:	Invoke py.test as distutils command with dependency resolution
Summary(pl.UTF-8):	Wywoływanie py.test jako polecenia distutils z rozwiązywaniem zależności
Name:		python-pytest-runner
Version:	2.5.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/pytest-runner
Source0:	https://pypi.python.org/packages/source/p/pytest-runner/pytest-runner-%{version}.zip
# Source0-md5:	2eef117c2f9db55d6639f5ef733575a6
URL:		https://bitbucket.org/pytest-dev/pytest-runner
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.616
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%{?with_doc:BuildRequires:	sphinx-pdg}
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%endif
Requires:	python-modules
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
Requires:	python3-modules

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
%py_build %{?with_tests:test}

%if %{with doc}
%{__python} setup.py build_sphinx
%endif
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%doc CHANGES.txt README.txt
%{py_sitescriptdir}/ptr.py[co]
%{py_sitescriptdir}/pytest_runner-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-runner
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{py3_sitescriptdir}/ptr.py
%{py3_sitescriptdir}/__pycache__/ptr.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_runner-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc build/sphinx/html/*
%endif
