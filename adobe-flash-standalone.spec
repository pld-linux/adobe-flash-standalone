%define		rel 1
Summary:	Standalone Flash player (Projector)
Summary(pl.UTF-8):	Odtwarzacz Flash
Name:		adobe-flash-standalone
Version:	10.3.181.34
Release:	%{rel}%{?with_license_agreement:wla}
License:	Free to use, non-distributable
Group:		X11/Applications/Multimedia
Source0:	http://download.macromedia.com/pub/flashplayer/updaters/10/flashplayer_10_sa.tar.gz#/%{name}-%{version}.tgz
# NoSource0-md5:	a315c5508d049060558b70d5654ff0c3
NoSource:	0
URL:		http://www.adobe.com/support/flashplayer/downloads.html
# apparently dlopened by player
Requires:	libasound.so.2
Requires:	libcurl.so.4
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/adobe

%description
Adobe(R) Flash(R) Standalone Player (aka Projector) for Linux - the
next-generation client runtime for engaging with Flash content and
applications on Linux.

%description -l pl.UTF-8
Adobe(R) Flash(R) Player - środowisko nowej generacji do obsługi
treści i aplikacji we Flashu pod Linuksem.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p flashplayer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashplayer
