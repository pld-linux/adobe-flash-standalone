%define		ver_major	10
%define		ver_minor	0
%define		ver_patch	15
%define		ver_serial	3
%define		rel 1
Summary:	Standalone Flash player
Summary(pl.UTF-8):	Odtwarzacz Flash
Name:		adobe-flash-standalone
Version:	%{ver_major}.%{ver_minor}.%{ver_patch}.%{ver_serial}
Release:	%{rel}%{?with_license_agreement:wla}
License:	Free to use, non-distributable
Group:		X11/Applications/Multimedia
Source0:	http://download.macromedia.com/pub/flashplayer/updaters/10/flash_player_10_linux_dev.tar.gz
# NoSource0-md5:	
URL:		http://www.adobe.com/products/flashplayer/
# apparently dlopened by player
Requires:	libasound.so.2
Requires:	libcurl.so.4
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/adobe

%description
Adobe(R) Flash(R) Player for Linux - the next-generation client
runtime for engaging with Flash content and applications on Linux.

%description -l pl.UTF-8
Adobe(R) Flash(R) Player - środowisko nowej generacji do obsługi
treści i aplikacji we Flashu pod Linuksem.

%prep
%setup -q -n flash_player_%{ver_major}_linux_dev
tar xf standalone/release/flashplayer.tar.gz

%install
rm -rf $RPM_BUILD_ROOT

install -D flashplayer $RPM_BUILD_ROOT%{_bindir}/flashplayer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashplayer
