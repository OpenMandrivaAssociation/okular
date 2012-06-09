Name:		okular
Summary:	A universal document viewer
Version:	4.8.4
Release:	2
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/graphics/okular/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kdegraphics-4.6.4-okularxdg.patch
BuildRequires:	kdelibs4-devel >= 2:%{version}
BuildRequires:	qimageblitz-devel
Suggests:	%{name}-pdf = %{EVRD}
Suggests:	%{name}-postscript = %{EVRD}

%description
Okular is a universal document viewer based on KPDF for KDE 4.

Okular combines the excellent functionalities of KPDF with the versatility
of supporting different kind of documents, like PDF, Postscript, DjVu, CHM,
and others.

The document format handlers page has a chart describing in more detail
the supported formats and the features supported in each of them.

%files
%doc AUTHORS COPYING TODO VERSION
%{_kde_bindir}/okular
%{_kde_libdir}/kde4/okularpart.so
%{_kde_datadir}/applications/kde4/okular.desktop
%{_kde_appsdir}/okular
%{_kde_datadir}/config.kcfg/okular.kcfg
%{_kde_datadir}/config.kcfg/gssettings.kcfg
%{_kde_datadir}/kde4/services/okular_part.desktop
%{_kde_datadir}/kde4/servicetypes/okularGenerator.desktop
%{_kde_iconsdir}/*/*/*/okular.*
%doc %{_kde_docdir}/HTML/en/okular/

#------------------------------------------------
%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release
BuildRequires:	pkgconfig(poppler-qt4) >= 0.20.0

%description pdf
PDF display support for Okular

%files pdf
%_libdir/kde4/okularGenerator_poppler.so
%_datadir/kde4/services/libokularGenerator_poppler.desktop
%_datadir/kde4/services/okularPoppler.desktop
%_datadir/applications/kde4/okularApplication_pdf.desktop

#------------------------------------------------
%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular

%files chm
%_kde_libdir/kde4/kio_msits.so
%_kde_libdir/kde4/okularGenerator_chmlib.so
%_kde_datadir/kde4/services/msits*
%_kde_datadir/kde4/services/libokularGenerator_chmlib.desktop
%_kde_datadir/kde4/services/okularChm.desktop
%_kde_datadir/applications/kde4/okularApplication_chm.desktop

#------------------------------------------------
%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description comicbook
ComicBook display support for Okular

%files comicbook
%_libdir/kde4/okularGenerator_comicbook.so
%_datadir/kde4/services/libokularGenerator_comicbook.desktop
%_datadir/kde4/services/okularComicbook.desktop
%_datadir/applications/kde4/okularApplication_comicbook.desktop

#------------------------------------------------
%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular

%files djvu
%_libdir/kde4/okularGenerator_djvu.so
%_datadir/kde4/services/libokularGenerator_djvu.desktop
%_datadir/kde4/services/okularDjvu.desktop
%_datadir/applications/kde4/okularApplication_djvu.desktop

#------------------------------------------------
%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description dvi
DVI display support for Okular

%files dvi
%_libdir/kde4/okularGenerator_dvi.so
%_datadir/kde4/services/libokularGenerator_dvi.desktop
%_datadir/kde4/services/okularDvi.desktop
%_datadir/applications/kde4/okularApplication_dvi.desktop

#------------------------------------------------
%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular

%files epub
%_libdir/kde4/okularGenerator_epub.so
%_datadir/kde4/services/libokularGenerator_epub.desktop
%_datadir/kde4/services/okularEPub.desktop
%_datadir/applications/kde4/okularApplication_epub.desktop

#------------------------------------------------
%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description fax
Fax display support for Okular

%files fax
%_libdir/kde4/okularGenerator_fax.so
%_datadir/kde4/services/libokularGenerator_fax.desktop
%_datadir/kde4/services/okularFax.desktop
%_datadir/applications/kde4/okularApplication_fax.desktop

#------------------------------------------------
%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description fb
FeedBooks display support for Okular

%files fb
%_libdir/kde4/okularGenerator_fb.so
%_datadir/kde4/services/libokularGenerator_fb.desktop
%_datadir/kde4/services/okularFb.desktop
%_datadir/applications/kde4/okularApplication_fb.desktop

#------------------------------------------------
%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular

%files postscript
%_libdir/kde4/okularGenerator_ghostview.so
%_datadir/kde4/services/libokularGenerator_ghostview.desktop
%_datadir/kde4/services/okularGhostview.desktop
%_datadir/applications/kde4/okularApplication_ghostview.desktop

#------------------------------------------------
%package kimgio
Summary:	KImgIO display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description kimgio
KImgIO display support for Okular

%files kimgio
%_libdir/kde4/okularGenerator_kimgio.so
%_datadir/kde4/services/libokularGenerator_kimgio.desktop
%_datadir/kde4/services/okularKimgio.desktop
%_datadir/applications/kde4/okularApplication_kimgio.desktop

#------------------------------------------------
%package ooo
Summary:	OpenOffice.Org/LibreOffice display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description ooo
OpenOffice.org/LibreOffice display support for Okular

%files ooo
%_libdir/kde4/okularGenerator_ooo.so
%_datadir/kde4/services/libokularGenerator_ooo.desktop
%_datadir/kde4/services/okularOoo.desktop
%_datadir/applications/kde4/okularApplication_ooo.desktop

#------------------------------------------------
%package plucker
Summary:	Plucker display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description plucker
Plucker display support for Okular

%files plucker
%_libdir/kde4/okularGenerator_plucker.so
%_datadir/kde4/services/libokularGenerator_plucker.desktop
%_datadir/kde4/services/okularPlucker.desktop
%_datadir/applications/kde4/okularApplication_plucker.desktop

#------------------------------------------------
%package tiff
Summary:	TIFF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description tiff
TIFF display support for Okular

%files tiff
%_libdir/kde4/okularGenerator_tiff.so
%_datadir/kde4/services/libokularGenerator_tiff.desktop
%_datadir/kde4/services/okularTiff.desktop
%_datadir/applications/kde4/okularApplication_tiff.desktop

#------------------------------------------------
%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%name = %epoch:%version-%release

%description xps
XPS display support for Okular

%files xps
%_libdir/kde4/okularGenerator_xps.so
%_datadir/kde4/services/libokularGenerator_xps.desktop
%_datadir/kde4/services/okularXps.desktop
%_datadir/applications/kde4/okularApplication_xps.desktop

#------------------------------------------------

%define okularcore_major 1
%define libokularcore %mklibname okularcore %{okularcore_major}

%package -n %{libokularcore}
Summary:	Runtime library for okular
Group:		System/Libraries

%description -n %{libokularcore}
Runtime library for Okular.

%files -n %{libokularcore}
%{_kde_libdir}/libokularcore.so.%{okularcore_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for kdegraphics
Group:		Development/KDE and Qt
Conflicts:	kdegraphics4-devel < 2:4.6.90
Requires:	%{libokularcore} = %{epoch}:%{version}-%{release}
Requires:	kdelibs4-devel >= 2:%{version}
Requires:	chmlib-devel
Requires:	ebook-tools-devel

%description devel
This package contains header files needed if you wish to build applications
based on okular.

%files devel
%{_includedir}/%{name}
%{_kde_libdir}/cmake/Okular/OkularConfig.cmake
%{_kde_libdir}/cmake/Okular/OkularConfigVersion.cmake
%{_kde_libdir}/libokularcore.so

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p2

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


