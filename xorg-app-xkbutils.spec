Summary:	xkbutils applications: xkbbell, xkbvleds, xkbwatch
Summary(pl.UTF-8):	Aplikacje xkbutils: xkbbell, xkbvleds, xkbwatch
Name:		xorg-app-xkbutils
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xkbutils-%{version}.tar.bz2
# Source0-md5:	502b14843f610af977dffc6cbf2102d5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%{_mandir}/man1/xkbbell.1x*
%{_mandir}/man1/xkbvleds.1x*
%{_mandir}/man1/xkbwatch.1x*
