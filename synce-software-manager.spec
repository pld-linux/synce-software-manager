Summary:	Software manager for Pocket PC
Summary(pl):	Narzêdzie do zarz±dzania oprogramowaniem w Pocket PC
Name:		synce-software-manager
Version:	0.9.0
Release:	1
License:	MIT
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	d9fd5f5dceff3e7eb0ded05d0a395f7e
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	synce-librapi2-devel >= 0.9.0
Requires:	synce-librapi2 >= 0.9.0
ExcludeArch:	alpha amd64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical tool for installing and removing software on a Pocket PC
device.

%description -l pl
Graficzne narzêdzie do instalacji i deinstalacji oprogramowania na
urz±dzeniach Pocket PC.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
# dir shared with synce-rra, synce-gnomevfs, synce-trayicon
%dir %{_datadir}/synce
%{_datadir}/synce/*.glade
