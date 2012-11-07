Name:		okular
Summary:	A universal document viewer
Version: 4.9.3
Release: 1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/graphics/okular/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kdegraphics-4.6.4-okularxdg.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(qimageblitz)
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
%doc %{_kde_docdir}/HTML/en/okular/
%{_kde_bindir}/okular
%{_kde_libdir}/kde4/okularpart.so
%{_kde_applicationsdir}/okular.desktop
%{_kde_appsdir}/okular
%{_kde_datadir}/config.kcfg/okular.kcfg
%{_kde_datadir}/config.kcfg/gssettings.kcfg
%{_kde_services}/okular_part.desktop
%{_kde_servicetypes}/okularGenerator.desktop
%{_kde_iconsdir}/*/*/*/okular.*

#------------------------------------------------
%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(poppler-qt4)

%description pdf
PDF display support for Okular

%files pdf
%{_kde_libdir}/kde4/okularGenerator_poppler.so
%{_kde_services}/libokularGenerator_poppler.desktop
%{_kde_services}/okularPoppler.desktop
%{_kde_applicationsdir}/okularApplication_pdf.desktop

#------------------------------------------------
%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular

%files chm
%{_kde_libdir}/kde4/kio_msits.so
%{_kde_libdir}/kde4/okularGenerator_chmlib.so
%{_kde_services}/msits*
%{_kde_services}/libokularGenerator_chmlib.desktop
%{_kde_services}/okularChm.desktop
%{_kde_applicationsdir}/okularApplication_chm.desktop

#------------------------------------------------
%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description comicbook
ComicBook display support for Okular

%files comicbook
%{_kde_libdir}/kde4/okularGenerator_comicbook.so
%{_kde_services}/libokularGenerator_comicbook.desktop
%{_kde_services}/okularComicbook.desktop
%{_kde_applicationsdir}/okularApplication_comicbook.desktop

#------------------------------------------------
%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular

%files djvu
%{_kde_libdir}/kde4/okularGenerator_djvu.so
%{_kde_services}/libokularGenerator_djvu.desktop
%{_kde_services}/okularDjvu.desktop
%{_kde_applicationsdir}/okularApplication_djvu.desktop

#------------------------------------------------
%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description dvi
DVI display support for Okular

%files dvi
%{_kde_libdir}/kde4/okularGenerator_dvi.so
%{_kde_services}/libokularGenerator_dvi.desktop
%{_kde_services}/okularDvi.desktop
%{_kde_applicationsdir}/okularApplication_dvi.desktop

#------------------------------------------------
%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular

%files epub
%{_kde_libdir}/kde4/okularGenerator_epub.so
%{_kde_services}/libokularGenerator_epub.desktop
%{_kde_services}/okularEPub.desktop
%{_kde_applicationsdir}/okularApplication_epub.desktop

#------------------------------------------------
%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fax
Fax display support for Okular

%files fax
%{_kde_libdir}/kde4/okularGenerator_fax.so
%{_kde_services}/libokularGenerator_fax.desktop
%{_kde_services}/okularFax.desktop
%{_kde_applicationsdir}/okularApplication_fax.desktop

#------------------------------------------------
%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fb
FeedBooks display support for Okular

%files fb
%{_kde_libdir}/kde4/okularGenerator_fb.so
%{_kde_services}/libokularGenerator_fb.desktop
%{_kde_services}/okularFb.desktop
%{_kde_applicationsdir}/okularApplication_fb.desktop

#------------------------------------------------
%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular

%files postscript
%{_kde_libdir}/kde4/okularGenerator_ghostview.so
%{_kde_services}/libokularGenerator_ghostview.desktop
%{_kde_services}/okularGhostview.desktop
%{_kde_applicationsdir}/okularApplication_ghostview.desktop

#------------------------------------------------
%package kimgio
Summary:	KImgIO display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description kimgio
KImgIO display support for Okular

%files kimgio
%{_kde_libdir}/kde4/okularGenerator_kimgio.so
%{_kde_services}/libokularGenerator_kimgio.desktop
%{_kde_services}/okularKimgio.desktop
%{_kde_applicationsdir}/okularApplication_kimgio.desktop

#------------------------------------------------
%package ooo
Summary:	OpenOffice.Org/LibreOffice display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description ooo
OpenOffice.org/LibreOffice display support for Okular

%files ooo
%{_kde_libdir}/kde4/okularGenerator_ooo.so
%{_kde_services}/libokularGenerator_ooo.desktop
%{_kde_services}/okularOoo.desktop
%{_kde_applicationsdir}/okularApplication_ooo.desktop

#------------------------------------------------
%package plucker
Summary:	Plucker display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description plucker
Plucker display support for Okular

%files plucker
%{_libdir}/kde4/okularGenerator_plucker.so
%{_kde_services}/libokularGenerator_plucker.desktop
%{_kde_services}/okularPlucker.desktop
%{_kde_applicationsdir}/okularApplication_plucker.desktop

#------------------------------------------------
%package tiff
Summary:	TIFF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description tiff
TIFF display support for Okular

%files tiff
%{_kde_libdir}/kde4/okularGenerator_tiff.so
%{_kde_services}/libokularGenerator_tiff.desktop
%{_kde_services}/okularTiff.desktop
%{_kde_applicationsdir}/okularApplication_tiff.desktop

#------------------------------------------------
%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description xps
XPS display support for Okular

%files xps
%{_kde_libdir}/kde4/okularGenerator_xps.so
%{_kde_services}/libokularGenerator_xps.desktop
%{_kde_services}/okularXps.desktop
%{_kde_applicationsdir}/okularApplication_xps.desktop

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
Requires:	%{libokularcore} = %{EVRD}
Requires:	kdelibs4-devel
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

