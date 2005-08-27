# $Rev: 3398 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xkbutils application
Summary(pl):	Aplikacja xkbutils
Name:		xorg-app-xkbutils
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xkbutils-%{version}.tar.bz2
# Source0-md5:	4b582a91d311314c379ab10acca22540
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xkbutils-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xkbutils application.

%description -l pl
Aplikacja xkbutils.


%prep
%setup -q -n xkbutils-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
