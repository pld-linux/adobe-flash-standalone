%define		rel 1
Summary:	Standalone Flash player (Projector)
Summary(pl.UTF-8):	Odtwarzacz Flash
Name:		adobe-flash-standalone
Version:	11.0.1.152
Release:	%{rel}%{?with_license_agreement:wla}
License:	Free to use, non-distributable
Group:		X11/Applications/Multimedia
Source0:	http://download.macromedia.com/pub/flashplayer/updaters/11/flashplayer_11_sa.i386.tar.gz#/%{name}-%{version}.tgz
# NoSource0-md5:	4d7c80df0614da4cffd46b77ebfaa466
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
