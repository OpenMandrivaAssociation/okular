#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define snapshot %{nil}
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A universal document viewer
Name:		plasma6-okular
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/okular/-/archive/%{gitbranch}/okular-%{gitbranchd}.tar.bz2#/okular-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/okular-%{version}.tar.xz
%endif
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/applications/graphics/okular
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6TextToSpeech)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libmarkdown)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	cmake(KExiv2Qt6)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	pkgconfig(libmarkdown)
Provides:	%{name}-ui = %{EVRD}
Requires:	%{name}-common = %{EVRD}
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
Suggests:	%{name}-tiff = %{EVRD}
Suggests:	%{name}-txt = %{EVRD}
Suggests:	%{name}-xps = %{EVRD}

%description
Okular is a universal document viewer based on KPDF for KDE 6.

Okular combines the excellent functionalities of KPDF with the versatility
of supporting different kind of documents, like PDF, Postscript, DjVu, CHM,
and others.

The document format handlers page has a chart describing in more detail
the supported formats and the features supported in each of them.

%files
%{_bindir}/okular
%{_datadir}/applications/org.kde.okular.desktop
%{_datadir}/metainfo/org.kde.okular.appdata.xml
%{_mandir}/man1/okular.1*

#------------------------------------------------

%package common
Summary:	Files needed by both the desktop and mobile frontends for Okular
Group:		Graphical desktop/KDE

%description common
Files needed by both the desktop and mobile frontends for Okular.

%files common -f okular.lang -f org.kde.active.documentviewer.lang -f okular_markdown.lang
%doc TODO
%{_datadir}/qlogging-categories6/okular.categories
%{_qtdir}/plugins/kf6/parts/okularpart.so
%{_datadir}/okular
%{_datadir}/kconf_update/okular.upd
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config.kcfg/gssettings.kcfg
%{_datadir}/config.kcfg/okular_core.kcfg
%{_datadir}/icons/*/*/*/okular.*

#------------------------------------------------

%package mobile
Summary:	Mobile-friendly alternative UI for Okular
Group:		Graphical desktop/KDE
Provides:	%{name}-ui = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-pdf = %{EVRD}
Requires:	%{name}-postscript = %{EVRD}
Suggests:	%{name}-comicbook = %{EVRD}
Suggests:	%{name}-djvu = %{EVRD}
Suggests:	%{name}-dvi = %{EVRD}
Suggests:	%{name}-epub = %{EVRD}
Suggests:	%{name}-fb = %{EVRD}
Suggests:	%{name}-kimgio = %{EVRD}
Suggests:	%{name}-tiff = %{EVRD}
Suggests:	%{name}-txt = %{EVRD}
Suggests:	%{name}-xps = %{EVRD}

%description mobile
An alternative user interface for Okular, targeting mobile
devices rather than traditional desktops.

%files mobile
%{_bindir}/okularkirigami
%{_datadir}/applications/org.kde.okular.kirigami.desktop
%{_datadir}/metainfo/org.kde.okular.kirigami.appdata.xml
%{_libdir}/qt6/qml/org/kde/okular

#------------------------------------------------

%package pdf
Summary:	PDF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	pkgconfig(poppler-qt6)

%description pdf
PDF display support for Okular.

%files pdf -f okular_poppler.lang
%{_datadir}/config.kcfg/pdfsettings.kcfg
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_poppler.so
%{_datadir}/applications/okularApplication_pdf.desktop
%{_datadir}/applications/org.kde.mobile.okular_pdf.desktop
%{_datadir}/metainfo/org.kde.okular-poppler.metainfo.xml

#------------------------------------------------

%package chm
Summary:	CHM (Microsoft Help) display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	chmlib-devel

%description chm
CHM (Microsoft Help) display support for Okular.

%if 0
# FIXME Not yet supported in Qt6 version
%files chm -f okular_chm.lang
%{_libdir}/qt6/plugins/kf6/kio/kio_msits.so
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_chmlib.so
%{_datadir}/applications/okularApplication_chm.desktop
%{_datadir}/applications/org.kde.mobile.okular_chm.desktop
%{_datadir}/metainfo/org.kde.okular-chm.metainfo.xml
%endif

#------------------------------------------------

%package comicbook
Summary:	ComicBook display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description comicbook
ComicBook display support for Okular.

%files comicbook -f okular_comicbook.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_comicbook.so
%{_datadir}/applications/okularApplication_comicbook.desktop
%{_datadir}/applications/org.kde.mobile.okular_comicbook.desktop
%{_datadir}/metainfo/org.kde.okular-comicbook.metainfo.xml

#------------------------------------------------

%package djvu
Summary:	DjVu display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	pkgconfig(ddjvuapi)

%description djvu
DjVu display support for Okular.

%files djvu -f okular_djvu.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_djvu.so
%{_datadir}/applications/okularApplication_djvu.desktop
%{_datadir}/applications/org.kde.mobile.okular_djvu.desktop
%{_datadir}/metainfo/org.kde.okular-djvu.metainfo.xml

#------------------------------------------------

%package dvi
Summary:	DVI display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description dvi
DVI display support for Okular.

%files dvi -f okular_dvi.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_dvi.so
%{_datadir}/applications/okularApplication_dvi.desktop
%{_datadir}/applications/org.kde.mobile.okular_dvi.desktop
%{_datadir}/metainfo/org.kde.okular-dvi.metainfo.xml

#------------------------------------------------

%package epub
Summary:	EPub display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	ebook-tools-devel

%description epub
EPub display support for Okular.

%files epub -f okular_epub.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_epub.so
%{_datadir}/applications/okularApplication_epub.desktop
%{_datadir}/applications/org.kde.mobile.okular_epub.desktop
%{_datadir}/metainfo/org.kde.okular-epub.metainfo.xml

#------------------------------------------------

%package fax
Summary:	Fax display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description fax
Fax display support for Okular.

%files fax -f okular_fax.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_fax.so
%{_datadir}/applications/okularApplication_fax.desktop
%{_datadir}/applications/org.kde.mobile.okular_fax.desktop
%{_datadir}/metainfo/org.kde.okular-fax.metainfo.xml

#------------------------------------------------

%package fb
Summary:	FeedBooks display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description fb
FeedBooks display support for Okular.

%files fb -f okular_fictionbook.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_fb.so
%{_datadir}/applications/okularApplication_fb.desktop
%{_datadir}/applications/org.kde.mobile.okular_fb.desktop
%{_datadir}/metainfo/org.kde.okular-fb.metainfo.xml

#------------------------------------------------

%package markdown
Summary:	Markdown display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description markdown
Markdown display support for Okular.

%files markdown
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_md.so
%{_datadir}/applications/okularApplication_md.desktop
%{_datadir}/applications/org.kde.mobile.okular_md.desktop
%{_datadir}/metainfo/org.kde.okular-md.metainfo.xml

#------------------------------------------------

%package mobipocket
Summary:	MobiPocket display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	cmake(QMobipocket6)

%description mobipocket
MobiPocket display support for Okular.

%files mobipocket -f okular_mobi.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_mobi.so
%{_datadir}/applications/okularApplication_mobi.desktop
%{_datadir}/applications/org.kde.mobile.okular_mobi.desktop
%{_datadir}/metainfo/org.kde.okular-mobipocket.metainfo.xml

#------------------------------------------------
%package kimgio
Summary:	KImgIO display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description kimgio
KImgIO display support for Okular.

%files kimgio -f okular_kimgio.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_kimgio.so
%{_datadir}/applications/okularApplication_kimgio.desktop
%{_datadir}/applications/org.kde.mobile.okular_kimgio.desktop
%{_datadir}/metainfo/org.kde.okular-kimgio.metainfo.xml

#------------------------------------------------

%package postscript
Summary:	PostScript display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}
BuildRequires:	pkgconfig(libspectre)

%description postscript
PostScript display support for Okular.

%files postscript -f okular_ghostview.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_ghostview.so
%{_datadir}/applications/okularApplication_ghostview.desktop
%{_datadir}/applications/org.kde.mobile.okular_ghostview.desktop
%{_datadir}/metainfo/org.kde.okular-spectre.metainfo.xml

#------------------------------------------------

%package tiff
Summary:	TIFF display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description tiff
TIFF display support for Okular.

%files tiff -f okular_tiff.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_tiff.so
%{_datadir}/applications/okularApplication_tiff.desktop
%{_datadir}/applications/org.kde.mobile.okular_tiff.desktop
%{_datadir}/metainfo/org.kde.okular-tiff.metainfo.xml

#------------------------------------------------

%package txt
Summary:	TXT display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description txt
TXT display support for Okular.

%files txt -f okular_txt.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_txt.so
%{_datadir}/applications/org.kde.mobile.okular_txt.desktop
%{_datadir}/applications/okularApplication_txt.desktop
%{_datadir}/metainfo/org.kde.okular-txt.metainfo.xml

#------------------------------------------------

%package xps
Summary:	XPS display support for Okular
Group:		Graphical desktop/KDE
Requires:	%{name}-ui = %{EVRD}

%description xps
XPS display support for Okular.

%files xps -f okular_xps.lang
%{_libdir}/qt6/plugins/okular_generators/okularGenerator_xps.so
%{_datadir}/applications/okularApplication_xps.desktop
%{_datadir}/applications/org.kde.mobile.okular_xps.desktop
%{_datadir}/metainfo/org.kde.okular-xps.metainfo.xml

#------------------------------------------------

%define okularcore_major 3
%define libokularcore %mklibname Okular6Core

%package -n %{libokularcore}
Summary:	Runtime library for okular
Group:		System/Libraries
Obsoletes:	%{_lib}okularcore1 <= 2:4.10.0
Obsoletes:	%{_lib}okularcore2 <= 2:4.11.0
Obsoletes:	%{_lib}okularcore3 <= 2:4.13.0
Obsoletes:	%{_lib}okularcore4 <= 2:4.14.0
Obsoletes:	%{_lib}okularcore6 <= 2:16.12.1
Obsoletes:	%{_lib}okularcore6 <= 2:16.12.1
Obsoletes:	%{_lib}okularcore7 <= 2:16.06
Obsoletes:	%{_lib}okularcore8 <= 2:18.08
Obsoletes:	%{_lib}okularcore9 <= 2:22.03
Obsoletes:	%{_lib}okularcore10 <= 2:23.08

%description -n %{libokularcore}
Runtime library for Okular.

%files -n %{libokularcore}
%{_libdir}/libOkular6Core.so.%{okularcore_major}*

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
%{_includedir}/okular
%{_libdir}/cmake/Okular6
%{_libdir}/libOkular6Core.so

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n okular-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja \
	-DOKULAR_UI=both

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang okular --with-html --with-man
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
%find_lang okular_poppler
%find_lang okular_tiff
%find_lang okular_txt
%find_lang okular_xps
%find_lang org.kde.active.documentviewer
