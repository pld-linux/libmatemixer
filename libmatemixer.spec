Summary:	MATE mixer libraries
Summary(pl.UTF-8):	Biblioteki MATE do obsługi miksera
Name:		libmatemixer
Version:	1.28.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# Source0-md5:	028324acb24c0ff30a740c435333fece
URL:		https://github.com/mate-desktop/libmatemixer
BuildRequires:	alsa-lib-devel >= 1.0.5
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libtool >= 2:2.2
BuildRequires:	mate-common >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 5.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xz
Requires:	glib2 >= 1:2.50.0
# alsa module
Requires:	alsa-lib >= 1.0.5
# pulse module
Requires:	pulseaudio-libs >= 5.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmatemixer is a mixer library for MATE desktop. It provides an
abstract API allowing access to mixer functionality available in the
PulseAudio, ALSA and OSS sound systems.

%description -l pl.UTF-8
libmatemixer to biblioteka MATE do obsługi miksera. Udostępnia
abstrakcyjne API pozwalające na dostęp do funkcji miksera dostępnych w
systemach dźwięku PulseAudio, ALSA i OSS.

%package devel
Summary:	Development files for libmatemixer library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libmatemixer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0

%description devel
Development files for libmatemixer library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libmatemixer.

%package apidocs
Summary:	API documentation for libmatemixer library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmatemixer
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libmatemixer library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmatemixer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-oss \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmatemixer.la \
	$RPM_BUILD_ROOT%{_libdir}/libmatemixer/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,jv,ku_IQ,pms}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmatemixer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatemixer.so.0
%dir %{_libdir}/libmatemixer
%attr(755,root,root) %{_libdir}/libmatemixer/libmatemixer-alsa.so
%attr(755,root,root) %{_libdir}/libmatemixer/libmatemixer-null.so
%attr(755,root,root) %{_libdir}/libmatemixer/libmatemixer-oss.so
%attr(755,root,root) %{_libdir}/libmatemixer/libmatemixer-pulse.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatemixer.so
%{_includedir}/mate-mixer
%{_pkgconfigdir}/libmatemixer.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmatemixer
