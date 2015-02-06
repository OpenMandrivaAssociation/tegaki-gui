Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki-gui
Version: 	0.3.1
Release: 	2
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/tegaki-pygtk-%version.tar.gz
URL: 		http://www.tegaki.org
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-setuptools
Requires:	tegaki >= 0.3.1
Requires:	pygtk2.0
Provides:	tegaki-pygtk = %{version}-%{release}
BuildArch:	noarch

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -qn tegaki-pygtk-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{py_puresitedir}/tegaki*
%{_datadir}/tegaki/icons/handwriting.png


%changelog
* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 592278
- import tegaki-gui

