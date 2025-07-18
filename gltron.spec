Summary:	Game known from movie Tron
Summary(pl.UTF-8):	Gra znana z filmu Tron
Name:		gltron
Version:	0.70
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gltron/%{name}-%{version}-source.tar.gz
# Source0-md5:	300e54914844f36c199415d6d8b0372a
Patch0:		%{name}-configure.patch
URL:		http://www.gltron.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_sound-devel >= 1.0.1
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Network game in which you steer a futuristic bike, called lightcycle.
Combat takes place in a rectangular arena. Your bike leaves a trail
behind, which is like a wall. The goal is to force the other players
to drive into a wall. The winner is the last player alive.

%description -l pl.UTF-8
Sieciowa gra w której sterujesz futurystycznym motorem nazywanym
świetlny-motor. Walki toczą się na prostokątnej arenie. Twój motor
pozostawia za sobą ślad, który jest jak mur. Celem gry jest zmuszenie
przeciwników do wjechania w ten mur. Wygrywa ostatni żyjący gracz.

%prep
%setup -q
%patch -P0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
CPPFLAGS="-I/usr/X11R6/include"
LDFLAGS="-L/usr/X11R6/%{_lib}"
%configure \
	%{?debug:--enable-debug} \
	--disable-optimize
#	--enable-network

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gltron
#%{_mandir}/man?/*
