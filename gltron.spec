Summary:	Game known from movie Tron
Summary(pl):	Gra znana z filmu Tron
Name:		gltron
Version:	0.61
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/gltron/%{name}-%{version}-source.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://www.gltron.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%define		_datadir	%{_prefix}/share/%{name}
%define		_mandir		%{_prefix}/man

%description
Network game in which you steer a futuristic bike, called lightcycle.
Combat takes place in a rectangular arena. Your bike leaves a trail
behind, which is like a wall. The goal is to force the other players
to drive into a wall. The winner is the last player alive.

%description -l pl
Sieciowa gra w której sterujesz futurystycznym motorem nazywanym
¶wietlny-motor. Walki tocz± siê na prostok±tnej arenie. Twój motor
pozostawia za sob± ¶lad, który jest jak mur. Celem gry jest zmuszenie
przeciwników do wjechania w ten mur. Wygrywa ostatni ¿yj±cy gracz.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
CPPFLAGS="-I%{_includedir}"; export CPPFLAGS
%configure \
	%{?debug:--enable-debug} \
	--disable-optimize
# doesn't compile at this moment
#	--enable-network

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

%{makeinstall}

gzip -9nf CHANGELOG CREDITS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}
