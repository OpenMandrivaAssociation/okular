%define snapshot %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%ifarch aarch64
%global optflags %{optflags} -fuse-ld=bfd
%endif

Summary:	A universal document viewer
Name:		okular
Version:	19.12.1
Release:	3
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libmarkdown)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JS)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(Qca-qt5)
BuildRequires:	cmake(KF5KExiv2)
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

%files -f okular.lang -f org.kde.active.documentviewer.lang -f okular_markdown.lang
%doc AUTHORS COPYING TODO
%{_datadir}/qlogging-categories5/okular.categories
%{_bindir}/okular
%{_libdir}/qt5/plugins/okularpart.so
%{_libdir}/qt5/qml/org/kde/okular
%{_datadir}/applications/org.kde.okular.desktop
%{_datadir}/metainfo/org.kde.okular.appdata.xml
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

%package mobile
Summary:	Mobile-friendly alternative UI for Okular
Group:		Graphical desktop/KDE

%description mobile
An alternative user interface for Okular, targeting mobile
devices rather than traditional desktops

%files mobile
%{_bindir}/okularkirigami
%{_datadir}/applications/org.kde.okular.kirigami.desktop
%{_datadir}/metainfo/org.kde.okular.kirigami.appdata.xml

#------------------------------------------------

%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(poppler-qt5)

%description pdf
PDF display support for Okular.

%files pdf -f okular_poppler.lang
%{_datadir}/config.kcfg/pdfsettings.kcfg
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_poppler.so
%{_datadir}/applications/okularApplication_pdf.desktop
%{_datadir}/applications/org.kde.mobile.okular_pdf.desktop
%{_datadir}/metainfo/org.kde.okular-poppler.metainfo.xml
%{_datadir}/kservices5/okularPoppler.desktop

#------------------------------------------------

%package plucker
Summary:	Plucker display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description plucker
Plucker display support for Okular.

%files plucker -f okular_plucker.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_plucker.so
%{_datadir}/applications/okularApplication_plucker.desktop
%{_datadir}/applications/org.kde.mobile.okular_plucker.desktop
%{_datadir}/metainfo/org.kde.okular-plucker.metainfo.xml
%{_datadir}/kservices5/okularPlucker.desktop

#------------------------------------------------

%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular.

%files chm -f okular_chm.lang
%{_libdir}/qt5/plugins/kio_msits.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_chmlib.so
%{_datadir}/kservices5/ms-its.protocol
%{_datadir}/applications/okularApplication_chm.desktop
%{_datadir}/applications/org.kde.mobile.okular_chm.desktop
%{_datadir}/metainfo/org.kde.okular-chm.metainfo.xml
%{_datadir}/kservices5/okularChm.desktop

#------------------------------------------------

%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description comicbook
ComicBook display support for Okular.

%files comicbook -f okular_comicbook.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_comicbook.so
%{_datadir}/applications/okularApplication_comicbook.desktop
%{_datadir}/applications/org.kde.mobile.okular_comicbook.desktop
%{_datadir}/metainfo/org.kde.okular-comicbook.metainfo.xml
%{_datadir}/kservices5/okularComicbook.desktop

#------------------------------------------------

%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular.

%files djvu -f okular_djvu.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_djvu.so
%{_datadir}/applications/okularApplication_djvu.desktop
%{_datadir}/applications/org.kde.mobile.okular_djvu.desktop
%{_datadir}/metainfo/org.kde.okular-djvu.metainfo.xml
%{_datadir}/kservices5/okularDjvu.desktop

#------------------------------------------------

%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description dvi
DVI display support for Okular.

%files dvi -f okular_dvi.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_dvi.so
%{_datadir}/applications/okularApplication_dvi.desktop
%{_datadir}/applications/org.kde.mobile.okular_dvi.desktop
%{_datadir}/metainfo/org.kde.okular-dvi.metainfo.xml
%{_datadir}/kservices5/okularDvi.desktop

#------------------------------------------------

%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular.

%files epub -f okular_epub.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_epub.so
%{_datadir}/applications/okularApplication_epub.desktop
%{_datadir}/applications/org.kde.mobile.okular_epub.desktop
%{_datadir}/metainfo/org.kde.okular-epub.metainfo.xml
%{_datadir}/kservices5/okularEPub.desktop

#------------------------------------------------

%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fax
Fax display support for Okular.

%files fax -f okular_fax.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fax.so
%{_datadir}/applications/okularApplication_fax.desktop
%{_datadir}/applications/org.kde.mobile.okular_fax.desktop
%{_datadir}/metainfo/org.kde.okular-fax.metainfo.xml
%{_datadir}/kservices5/okularFax.desktop

#------------------------------------------------

%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description fb
FeedBooks display support for Okular.

%files fb -f okular_fictionbook.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fb.so
%{_datadir}/applications/okularApplication_fb.desktop
%{_datadir}/applications/org.kde.mobile.okular_fb.desktop
%{_datadir}/metainfo/org.kde.okular-fb.metainfo.xml
%{_datadir}/kservices5/okularFb.desktop

#------------------------------------------------

%package markdown
Summary:	Markdown display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description markdown
Markdown display support for Okular.

%files markdown
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_md.so
%{_datadir}/applications/okularApplication_md.desktop
%{_datadir}/applications/org.kde.mobile.okular_md.desktop
%{_datadir}/metainfo/org.kde.okular-md.metainfo.xml
%{_datadir}/kservices5/okularMd.desktop

#------------------------------------------------

%package mobipocket
Summary:	MobiPocket display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	cmake(QMobipocket)

%description mobipocket
MobiPocket display support for Okular.

%files mobipocket -f okular_mobi.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_mobi.so
%{_datadir}/applications/okularApplication_mobi.desktop
%{_datadir}/applications/org.kde.mobile.okular_mobi.desktop
%{_datadir}/metainfo/org.kde.okular-mobipocket.metainfo.xml
%{_datadir}/kservices5/okularMobi.desktop


#------------------------------------------------
%package kimgio
Summary:	KImgIO display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description kimgio
KImgIO display support for Okular.

%files kimgio -f okular_kimgio.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_kimgio.so
%{_datadir}/applications/okularApplication_kimgio.desktop
%{_datadir}/applications/org.kde.mobile.okular_kimgio.desktop
%{_datadir}/metainfo/org.kde.okular-kimgio.metainfo.xml
%{_datadir}/kservices5/okularKimgio.desktop

#------------------------------------------------

%package ooo
Summary:	OpenOffice.Org/LibreOffice display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description ooo
OpenOffice.org/LibreOffice display support for Okular.

%files ooo -f okular_ooo.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_ooo.so
%{_datadir}/applications/okularApplication_ooo.desktop
%{_datadir}/applications/org.kde.mobile.okular_ooo.desktop
%{_datadir}/metainfo/org.kde.okular-ooo.metainfo.xml
%{_datadir}/kservices5/okularOoo.desktop

#------------------------------------------------

%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular.

%files postscript -f okular_ghostview.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_ghostview.so
%{_datadir}/applications/okularApplication_ghostview.desktop
%{_datadir}/applications/org.kde.mobile.okular_ghostview.desktop
%{_datadir}/metainfo/org.kde.okular-spectre.metainfo.xml
%{_datadir}/kservices5/okularGhostview.desktop

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
%{_datadir}/metainfo/org.kde.okular-tiff.metainfo.xml
%{_datadir}/kservices5/okularTiff.desktop

#------------------------------------------------

%package txt
Summary:	TXT display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description txt
TXT display support for Okular.

%files txt -f okular_txt.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_txt.so
%{_datadir}/applications/org.kde.mobile.okular_txt.desktop
%{_datadir}/applications/okularApplication_txt.desktop
%{_datadir}/metainfo/org.kde.okular-txt.metainfo.xml
%{_datadir}/kservices5/okularTxt.desktop

#------------------------------------------------

%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description xps
XPS display support for Okular.

%files xps -f okular_xps.lang
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_xps.so
%{_datadir}/applications/okularApplication_xps.desktop
%{_datadir}/applications/org.kde.mobile.okular_xps.desktop
%{_datadir}/metainfo/org.kde.okular-xps.metainfo.xml
%{_datadir}/kservices5/okularXps.desktop

#------------------------------------------------

%define okularcore_major 9
%define libokularcore %mklibname Okular5Core %{okularcore_major}

%package -n %{libokularcore}
Summary:	Runtime library for okular
Group:		System/Libraries
Obsoletes:	%{_lib}okularcore1 <= 2:4.10.0
Obsoletes:	%{_lib}okularcore2 <= 2:4.11.0
Obsoletes:	%{_lib}okularcore3 <= 2:4.13.0
Obsoletes:	%{_lib}okularcore4 <= 2:4.14.0
Obsoletes:	%{_lib}okularcore5 <= 2:15.12.1
Obsoletes:	%{_lib}okularcore6 <= 2:15.12.1
Obsoletes:	%{_lib}okularcore7 <= 2:16.06
Obsoletes:	%{_lib}okularcore8 <= 2:18.08

%description -n %{libokularcore}
Runtime library for Okular.

%files -n %{libokularcore}
%{_libdir}/libOkular5Core.so.%{okularcore_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for kdegraphics
Group:		Development/KDE and Qt
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
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang okular --with-html --with-man
%find_lang okular_chm
%find_lang okular_comicbook
%find_lang okular_djvu
%find_lang okular_dvi
%find_lang okular_epub
%find_lang okular_fax
%find_lang okular_fictionbook
%find_lang okular_ghostview
%find_lang okular_kimgio
%find_lang okular_markdown
%find_lang okular_mobi
%find_lang okular_ooo
%find_lang okular_plucker
%find_lang okular_poppler
%find_lang okular_txt
%find_lang okular_xps
%find_lang org.kde.active.documentviewer
