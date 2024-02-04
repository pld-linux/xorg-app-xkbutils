Summary:	xkbutils applications: xkbbell, xkbvleds, xkbwatch
Summary(pl.UTF-8):	Aplikacje xkbutils: xkbbell, xkbvleds, xkbwatch
Name:		xorg-app-xkbutils
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xkbutils-%{version}.tar.xz
# Source0-md5:	07483ddfe1d83c197df792650583ff20
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbutils is a collection of small utilities utilizing the XKeyboard
(XKB) extension to the X11 protocol. It includes:
- xkbbell: generate XKB bell events
- xkbvleds: display the state of LEDs on an XKB keyboard in a window
- xkbwatch: reports changes in the XKB keyboard state

%description -l pl.UTF-8
xkbutils to zbiór małych narzędzi wykorzystujących rozszerzenie XKB
(XKeyboard) protokołu X11. Zawiera:
- xkbbell - generujące zdarzenia dzwonka XKB
- xkbvleds - wyświetlające w okienku stan diod na klawiaturze XKB
- xkbwatch - zgłaszające zmiany stanu klawiatury XKB

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%{_mandir}/man1/xkbbell.1*
%{_mandir}/man1/xkbvleds.1*
%{_mandir}/man1/xkbwatch.1*
