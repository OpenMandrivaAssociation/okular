%define snapshot 20160531
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A universal document viewer
Name:		okular
Version:	16.06
%if 0%{snapshot}
Release:	0.%{snapshot}.1
Source0:	%{name}-%{snapshot}.tar.xz
%else
Release:	1
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
%endif
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/graphics/okular
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5JS)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(QMobipocket)
BuildRequires:	cmake(Qca-qt5)
Requires:	%{name}-pdf = %{EVRD}
Requires:	%{name}-postscript = %{EVRD}
Suggests:	%{name}-chm = %{EVRD}
Suggests:	%{name}-comicbook = %{EVRD}
Suggests:	%{name}-djvu = %{EVRD}
Suggests:	%{name}-dvi = %{EVRD}
Suggests:	%{name}-epub = %{EVRD}
Suggests:	%{name}-fax = %{EVRD}
Suggests:	%{name}-fb = %{EVRD}
Obsoletes:	%{name}-kimgio < %{EVRD}
Obsoletes:	%{name}-mobipocket < %{EVRD}
Suggests:	%{name}-ooo = %{EVRD}
Suggests:	%{name}-plucker = %{EVRD}
Suggests:	%{name}-tiff = %{EVRD}
Suggests:	%{name}-txt = %{EVRD}
Suggests:	%{name}-xps = %{EVRD}

%description
Okular is a universal document viewer based on KPDF for KDE 5.

Okular combines the excellent functionalities of KPDF with the versatility
of supporting different kind of documents, like PDF, Postscript, DjVu, CHM,
and others.

The document format handlers page has a chart describing in more detail
the supported formats and the features supported in each of them.

%files
%doc AUTHORS COPYING TODO
%doc %{_docdir}/HTML/en/okular/
%{_sysconfdir}/xdg/okular.categories
%{_bindir}/okular
%{_libdir}/qt5/plugins/okularpart.so
%{_libdir}/qt5/qml/org/kde/okular
%{_datadir}/applications/org.kde.okular.desktop
%{_datadir}/applications/org.kde.mobile.okular.desktop
%{_datadir}/kpackage/genericqml/org.kde.mobile.okular
%{_datadir}/kservices5/okular_part.desktop
%{_datadir}/kservicetypes5/okularGenerator.desktop
%{_datadir}/kxmlgui5/okular
%{_datadir}/okular
%{_datadir}/kconf_update/okular.upd
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config.kcfg/gssettings.kcfg
%{_datadir}/config.kcfg/okular_core.kcfg
%{_datadir}/icons/*/*/*/okular.*
%{_mandir}/man1/okular.1*

#------------------------------------------------

%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(poppler-qt5)

%description pdf
PDF display support for Okular.

%files pdf
%{_datadir}/config.kcfg/pdfsettings.kcfg
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_poppler.so
%{_datadir}/applications/okularApplication_pdf.desktop
%{_datadir}/applications/org.kde.mobile.okular_pdf.desktop

#------------------------------------------------

%package plucker
Summary:	Plucker display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description plucker
Plucker display support for Okular.

%files plucker
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_plucker.so
%{_datadir}/applications/okularApplication_plucker.desktop
%{_datadir}/applications/org.kde.mobile.okular_plucker.desktop

#------------------------------------------------

%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular.

%files chm
%{_libdir}/qt5/plugins/kio_msits.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_chmlib.so
%{_datadir}/kservices5/msits*
%{_datadir}/applications/okularApplication_chm.desktop
%{_datadir}/applications/org.kde.mobile.okular_chm.desktop

#------------------------------------------------

%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description comicbook
ComicBook display support for Okular.

%files comicbook
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_comicbook.so
%{_datadir}/applications/okularApplication_comicbook.desktop
%{_datadir}/applications/org.kde.mobile.okular_comicbook.desktop

#------------------------------------------------

%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular.

%files djvu
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_djvu.so
%{_datadir}/applications/okularApplication_djvu.desktop
%{_datadir}/applications/org.kde.mobile.okular_djvu.desktop

#------------------------------------------------

%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description dvi
DVI display support for Okular.

%files dvi
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_dvi.so
%{_datadir}/applications/okularApplication_dvi.desktop
%{_datadir}/applications/org.kde.mobile.okular_dvi.desktop

#------------------------------------------------

%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular.

%files epub
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_epub.so
%{_datadir}/applications/okularApplication_epub.desktop
%{_datadir}/applications/org.kde.mobile.okular_epub.desktop

#------------------------------------------------

%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fax
Fax display support for Okular.

%files fax
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fax.so
%{_datadir}/applications/okularApplication_fax.desktop
%{_datadir}/applications/org.kde.mobile.okular_fax.desktop

#------------------------------------------------

%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fb
FeedBooks display support for Okular.

%files fb
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fb.so
%{_datadir}/applications/okularApplication_fb.desktop
%{_datadir}/applications/org.kde.mobile.okular_fb.desktop

#------------------------------------------------
# This may come back in a future release
%if 0
%package mobipocket
Summary:	Mobipocket display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	qmobipocket-devel
Conflicts:	kdegraphics-mobipocket < 2:4.12.1

%description mobipocket
Mobipocket display support for Okular.

%files mobipocket
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_mobi.so
%{_datadir}/applications/okularApplication_mobi.desktop
%endif

#------------------------------------------------

%package ooo
Summary:	OpenOffice.Org/LibreOffice display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description ooo
OpenOffice.org/LibreOffice display support for Okular.

%files ooo
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_ooo.so
%{_datadir}/applications/okularApplication_ooo.desktop
%{_datadir}/applications/org.kde.mobile.okular_ooo.desktop

#------------------------------------------------

%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular.

%files postscript
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_ghostview.so
%{_datadir}/applications/okularApplication_ghostview.desktop
%{_datadir}/applications/org.kde.mobile.okular_ghostview.desktop

#------------------------------------------------

%package tiff
Summary:	TIFF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description tiff
TIFF display support for Okular.

%files tiff
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_tiff.so
%{_datadir}/applications/okularApplication_tiff.desktop
%{_datadir}/applications/org.kde.mobile.okular_tiff.desktop

#------------------------------------------------

%package txt
Summary:	TXT display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description txt
TXT display support for Okular.

%files txt
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_txt.so
%{_datadir}/applications/org.kde.mobile.okular_txt.desktop
%{_datadir}/applications/okularApplication_txt.desktop

#------------------------------------------------

%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description xps
XPS display support for Okular.

%files xps
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_xps.so
%{_datadir}/applications/okularApplication_xps.desktop
%{_datadir}/applications/org.kde.mobile.okular_xps.desktop

#------------------------------------------------

%define okularcore_major 7
%define libokularcore %mklibname Okular5Core %{okularcore_major}

%package -n %{libokularcore}
Summary:	Runtime library for okular
Group:		System/Libraries
Obsoletes:	%{_lib}okularcore1 < 2:4.10.0
Obsoletes:	%{_lib}okularcore2 < 2:4.11.0
Obsoletes:	%{_lib}okularcore3 < 2:4.13.0
Obsoletes:	%{_lib}okularcore4 < 2:4.14.0
Obsoletes:	%{_lib}okularcore5 < 2:15.12.1
Obsoletes:	%{_lib}okularcore6 < 2:15.12.1
Obsoletes:	%{_lib}okularcore7 < 2:16.06

%description -n %{libokularcore}
Runtime library for Okular.

%files -n %{libokularcore}
%{_libdir}/libOkular5Core.so.%{okularcore_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for kdegraphics
Group:		Development/KDE and Qt
Conflicts:	kdegraphics4-devel < 2:4.6.90
Requires:	%{libokularcore} = %{EVRD}
Requires:	chmlib-devel
Requires:	ebook-tools-devel

%description devel
This package contains header files needed if you wish to build applications
based on Okular.

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/Okular5
%{_libdir}/libOkular5Core.so

#----------------------------------------------------------------------

%prep
%if 0%{snapshot}
%setup -qn %{name}
%else
%setup -q
%endif

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
