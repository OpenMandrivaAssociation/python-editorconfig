%define module editorconfig

Name:		python-editorconfig
Version:	0.17.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz
Summary:	EditorConfig File Locator and Interpreter for Python
URL:		https://pypi.org/project/editorconfig/
License:	PSF-2.0 AND BSD-2-Clause
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
EditorConfig File Locator and Interpreter for Python

%files
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
