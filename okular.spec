%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A universal document viewer
Name:		okular
Version:	15.04.2
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/okular/
Source0:	fhttp://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kdegraphics-4.6.4-okularxdg.patch
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(kscreen)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
BuildRequires:	pkgconfig(QJson)
Requires:	%{name}-pdf = %{EVRD}
Requires:	%{name}-postscript = %{EVRD}
Suggests:	%{name}-chm = %{EVRD}
Suggests:	%{name}-comicbook = %{EVRD}
Suggests:	%{name}-djvu = %{EVRD}
Suggests:	%{name}-dvi = %{EVRD}
Suggests:	%{name}-epub = %{EVRD}
Suggests:	%{name}-fax = %{EVRD}
Suggests:	%{name}-fb = %{EVRD}
Suggests:	%{name}-kimgio = %{EVRD}
Suggests:	%{name}-mobipocket = %{EVRD}
Suggests:	%{name}-ooo = %{EVRD}
Suggests:	%{name}-plucker = %{EVRD}
Suggests:	%{name}-tiff = %{EVRD}
Suggests:	%{name}-txt = %{EVRD}
Suggests:	%{name}-xps = %{EVRD}

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
%{_kde_libdir}/kde4/imports/org/kde/okular
%{_kde_applicationsdir}/okular.desktop
%{_kde_appsdir}/okular
%{_kde_appsdir}/kconf_update/okular.upd
%{_kde_datadir}/config.kcfg/okular.kcfg
%{_kde_datadir}/config.kcfg/gssettings.kcfg
%{_kde_datadir}/config.kcfg/okular_core.kcfg
%{_kde_services}/okular_part.desktop
%{_kde_servicetypes}/okularGenerator.desktop
%{_kde_iconsdir}/*/*/*/okular.*
%{_kde_mandir}/man1/okular.1*

#------------------------------------------------

%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(poppler-qt4)

%description pdf
PDF display support for Okular.

%files pdf
%{_kde_datadir}/config.kcfg/pdfsettings.kcfg
%{_kde_libdir}/kde4/okularGenerator_poppler.so
%{_kde_services}/libokularGenerator_poppler.desktop
%{_kde_services}/okularPoppler.desktop
%{_kde_applicationsdir}/okularApplication_pdf.desktop
%{_kde_applicationsdir}/active-documentviewer_pdf.desktop

#------------------------------------------------

%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular.

%files chm
%{_kde_libdir}/kde4/kio_msits.so
%{_kde_libdir}/kde4/okularGenerator_chmlib.so
%{_kde_services}/msits*
%{_kde_services}/libokularGenerator_chmlib.desktop
%{_kde_services}/okularChm.desktop
%{_kde_applicationsdir}/okularApplication_chm.desktop
%{_kde_applicationsdir}/active-documentviewer_chm.desktop

#------------------------------------------------

%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description comicbook
ComicBook display support for Okular.

%files comicbook
%{_kde_libdir}/kde4/okularGenerator_comicbook.so
%{_kde_services}/libokularGenerator_comicbook.desktop
%{_kde_services}/okularComicbook.desktop
%{_kde_applicationsdir}/okularApplication_comicbook.desktop
%{_kde_applicationsdir}/active-documentviewer_comicbook.desktop

#------------------------------------------------

%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular.

%files djvu
%{_kde_libdir}/kde4/okularGenerator_djvu.so
%{_kde_services}/libokularGenerator_djvu.desktop
%{_kde_services}/okularDjvu.desktop
%{_kde_applicationsdir}/okularApplication_djvu.desktop
%{_kde_applicationsdir}/active-documentviewer_djvu.desktop

#------------------------------------------------

%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description dvi
DVI display support for Okular.

%files dvi
%{_kde_libdir}/kde4/okularGenerator_dvi.so
%{_kde_services}/libokularGenerator_dvi.desktop
%{_kde_services}/okularDvi.desktop
%{_kde_applicationsdir}/okularApplication_dvi.desktop
%{_kde_applicationsdir}/active-documentviewer_dvi.desktop

#------------------------------------------------

%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular.

%files epub
%{_kde_libdir}/kde4/okularGenerator_epub.so
%{_kde_services}/libokularGenerator_epub.desktop
%{_kde_services}/okularEPub.desktop
%{_kde_applicationsdir}/okularApplication_epub.desktop
%{_kde_applicationsdir}/active-documentviewer_epub.desktop

#------------------------------------------------

%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fax
Fax display support for Okular.

%files fax
%{_kde_libdir}/kde4/okularGenerator_fax.so
%{_kde_services}/libokularGenerator_fax.desktop
%{_kde_services}/okularFax.desktop
%{_kde_applicationsdir}/okularApplication_fax.desktop
%{_kde_applicationsdir}/active-documentviewer_fax.desktop

#------------------------------------------------

%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fb
FeedBooks display support for Okular.

%files fb
%{_kde_libdir}/kde4/okularGenerator_fb.so
%{_kde_services}/libokularGenerator_fb.desktop
%{_kde_services}/okularFb.desktop
%{_kde_applicationsdir}/okularApplication_fb.desktop
%{_kde_applicationsdir}/active-documentviewer_fb.desktop

#------------------------------------------------

%package kimgio
Summary:	KImgIO display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(libkexiv2)

%description kimgio
KImgIO display support for Okular.

%files kimgio
%{_kde_libdir}/kde4/okularGenerator_kimgio.so
%{_kde_services}/libokularGenerator_kimgio.desktop
%{_kde_services}/okularKimgio.desktop
%{_kde_applicationsdir}/okularApplication_kimgio.desktop
%{_kde_applicationsdir}/active-documentviewer_kimgio.desktop

#------------------------------------------------

%package mobipocket
Summary:	Mobipocket display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	qmobipocket-devel
Conflicts:	kdegraphics-mobipocket < 2:4.12.1

%description mobipocket
Mobipocket display support for Okular.

%files mobipocket
%{_kde_libdir}/kde4/okularGenerator_mobi.so
%{_kde_services}/libokularGenerator_mobi.desktop
%{_kde_services}/okularMobi.desktop
%{_kde_applicationsdir}/okularApplication_mobi.desktop

#------------------------------------------------

%package ooo
Summary:	OpenOffice.Org/LibreOffice display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description ooo
OpenOffice.org/LibreOffice display support for Okular.

%files ooo
%{_kde_libdir}/kde4/okularGenerator_ooo.so
%{_kde_services}/libokularGenerator_ooo.desktop
%{_kde_services}/okularOoo.desktop
%{_kde_applicationsdir}/okularApplication_ooo.desktop
%{_kde_applicationsdir}/active-documentviewer_ooo.desktop

#------------------------------------------------

%package plucker
Summary:	Plucker display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description plucker
Plucker display support for Okular.

%files plucker
%{_libdir}/kde4/okularGenerator_plucker.so
%{_kde_services}/libokularGenerator_plucker.desktop
%{_kde_services}/okularPlucker.desktop
%{_kde_applicationsdir}/okularApplication_plucker.desktop
%{_kde_applicationsdir}/active-documentviewer_plucker.desktop

#------------------------------------------------

%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular.

%files postscript
%{_kde_libdir}/kde4/okularGenerator_ghostview.so
%{_kde_services}/libokularGenerator_ghostview.desktop
%{_kde_services}/okularGhostview.desktop
%{_kde_applicationsdir}/okularApplication_ghostview.desktop
%{_kde_applicationsdir}/active-documentviewer_ghostview.desktop

#------------------------------------------------

%package tiff
Summary:	TIFF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description tiff
TIFF display support for Okular.

%files tiff
%{_kde_libdir}/kde4/okularGenerator_tiff.so
%{_kde_services}/libokularGenerator_tiff.desktop
%{_kde_services}/okularTiff.desktop
%{_kde_applicationsdir}/okularApplication_tiff.desktop
%{_kde_applicationsdir}/active-documentviewer_tiff.desktop

#------------------------------------------------

%package txt
Summary:	TXT display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description txt
TXT display support for Okular.

%files txt
%{_kde_libdir}/kde4/okularGenerator_txt.so
%{_kde_services}/libokularGenerator_txt.desktop
%{_kde_services}/okularTxt.desktop
%{_kde_applicationsdir}/active-documentviewer_txt.desktop
%{_kde_applicationsdir}/okularApplication_txt.desktop

#------------------------------------------------

%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description xps
XPS display support for Okular.

%files xps
%{_kde_libdir}/kde4/okularGenerator_xps.so
%{_kde_services}/libokularGenerator_xps.desktop
%{_kde_services}/okularXps.desktop
%{_kde_applicationsdir}/okularApplication_xps.desktop
%{_kde_applicationsdir}/active-documentviewer_xps.desktop

#------------------------------------------------

%define okularcore_major 6
%define libokularcore %mklibname okularcore %{okularcore_major}

%package -n %{libokularcore}
Summary:	Runtime library for okular
Group:		System/Libraries
Obsoletes:	%{_lib}okularcore1 < 2:4.10.0
Obsoletes:	%{_lib}okularcore2 < 2:4.11.0
Obsoletes:	%{_lib}okularcore3 < 2:4.13.0
Obsoletes:	%{_lib}okularcore4 < 2:4.14.0

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
based on Okular.

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
