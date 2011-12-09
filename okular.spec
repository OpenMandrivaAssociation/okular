Name: okular
Summary: A universal document viewer
Version: 4.7.90
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org/applications/graphics/okular/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: qimageblitz-devel
BuildRequires: pkgconfig(poppler-qt4) >= 0.8.0
BuildRequires: pkgconfig(libspectre)
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: chmlib-devel
BuildRequires: ebook-tools-devel

%description
Okular is a universal document viewer based on KPDF for KDE 4.

Okular combines the excellent functionalities of KPDF with the versatility
of supporting different kind of documents, like PDF, Postscript, DjVu, CHM,
and others.

The document format handlers page has a chart describing in more detail
the supported formats and the features supported in each of them.

%files
%doc AUTHORS COPYING TODO VERSION
%_kde_bindir/okular
%_kde_libdir/kde4/okularGenerator_*
%_kde_libdir/kde4/okularpart.so
%_kde_libdir/kde4/kio_msits.so
%_kde_datadir/applications/kde4/okular*
%_kde_appsdir/okular
%_kde_datadir/config.kcfg/okular.kcfg
%_kde_datadir/config.kcfg/gssettings.kcfg
%_kde_datadir/kde4/services/libokularGenerator_*
%_kde_datadir/kde4/services/okular*
%_kde_datadir/kde4/services/msits*
%_kde_datadir/kde4/servicetypes/okularGenerator.desktop
%_kde_iconsdir/*/*/*/okular.*
%doc %_kde_docdir/HTML/en/okular/

#------------------------------------------------	

%define okularcore_major 1
%define libokularcore %mklibname okularcore %okularcore_major

%package -n %libokularcore
Summary: Runtime library for okular
Group: System/Libraries

%description -n %libokularcore
Runtime library for Okular.

%files -n %libokularcore
%_kde_libdir/libokularcore.so.%{okularcore_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdegraphics
Group: Development/KDE and Qt
Conflicts: kdegraphics4-devel < 2:4.6.90
Requires: %libokularcore = %epoch:%version-%release
Requires: kdelibs4-devel >= 2:%{version}
Requires: chmlib-devel
Requires: ebook-tools-devel

%description devel
This package contains header files needed if you wish to build applications
based on okular.

%files devel
%{_includedir}/%{name}
%_kde_libdir/cmake/Okular/OkularConfig.cmake
%_kde_libdir/cmake/Okular/OkularConfigVersion.cmake
%_kde_libdir/libokularcore.so

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


