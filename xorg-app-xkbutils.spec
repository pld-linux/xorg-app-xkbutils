Summary:	xkbutils applications: xkbbell, xkbvleds, xkbwatch
Summary(pl.UTF-8):   Aplikacje xkbutils: xkbbell, xkbvleds, xkbwatch
Name:		xorg-app-xkbutils
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbutils-%{version}.tar.bz2
# Source0-md5:	84396a3dd75337caaae29d8fa5616fb1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbutils applications: xkbbell, xkbvleds, xkbwatch.

%description -l pl.UTF-8
Aplikacje xkbutils: xkbbell, xkbvleds, xkbwatch.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
