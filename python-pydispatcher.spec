%global         srcname  PyDispatcher

%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:           python-pydispatcher
Version:        2.0.5
Release:        1%{?dist}
Summary:        PyDispatcher Library
License:        BSD
URL:            https://pypi.python.org/pypi/PyDispatcher
Source0:        https://pypi.python.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/%{srcname}-%{version}.tar.gz

BuildRequires: python
%if %{with python3}
BuildRequires: python34
%endif

BuildArch:      noarch

%{!?py2_build: %global py2_build CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build}
%{!?py2_install: %global py2_install %{__python} setup.py install --skip-build --root %{buildroot}}
%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}

%package -n python2-pydispatcher
Summary:        %{summary}
%{?python_provide:%python_provide python2-pydispatcher}


%description
Python library implementing a multi-producer-multi-consumer signal dispatching mechanism.

%description -n python2-pydispatcher
Python 2 library implementing a multi-producer-multi-consumer signal dispatching mechanism.

%if %{with python3}
%package -n python3-pydispatcher
Summary:        %{summary}
%{?python_provide:%python_provide python3-pydispatcher}

%description -n python3-pydispatcher
Python 3 library implementing a multi-producer-multi-consumer signal dispatching mechanism.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
# Do python3 first so bin ends up from py2
%py3_install
%endif
%py2_install


%check
echo "Running tests..."
echo %{__python2} setup.py test
%{__python2} setup.py test
%if %{with python3}
echo %{__python3} setup.py test
%{__python3} setup.py test
%endif
echo "Done"

%files -n python2-pydispatcher
%{python2_sitelib}/pydispatch
%{python2_sitelib}/%{srcname}-%{version}*.egg-info

%if %{with python3}
%files -n python3-pydispatcher
%{python3_sitelib}/pydispatch
%{python3_sitelib}/%{srcname}-%{version}*.egg-info
%endif

