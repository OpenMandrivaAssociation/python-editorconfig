Name:		python-editorconfig
Version:	0.17.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/e/editorconfig/editorconfig-%{version}.tar.gz
Summary:	EditorConfig File Locator and Interpreter for Python
URL:		https://pypi.org/project/editorconfig/
License:	PSF-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
EditorConfig File Locator and Interpreter for Python

%files
%{_bindir}/editorconfig
%{py_sitedir}/editorconfig
%{py_sitedir}/editorconfig-*.*-info
