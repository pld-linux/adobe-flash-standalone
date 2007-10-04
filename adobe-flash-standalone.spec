#
%define		_ver_major	9
%define		_ver_minor	0
%define		_ver_patch	48
%define		_ver_serial	0
%define		_rel 1
Summary:	Standalone Flash player
Summary(pl.UTF-8):	Odtwarzacz Flash
Name:		adobe-flash-standalone
Version:	%{_ver_major}.%{_ver_minor}.%{_ver_patch}.%{_ver_serial}
Release:	%{_rel}%{?with_license_agreement:wla}
License:	Free to use, non-distributable
Group:		X11/Applications/Multimedia
Source0:	http://download.macromedia.com/pub/flashplayer/updaters/9/flash_player_9_linux_dev.tar.gz
# NoSource0-md5:	cd0ca45c56f81f94e806125d39374c07
URL:		http://www.adobe.com/products/flashplayer/
# apparently dlopened by player
Requires:	libasound.so.2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/adobe

%description
Adobe(R) Flash(R) Player 9 for Linux - the next-generation client
runtime for engaging with Flash content and applications on Linux.

%description -l pl.UTF-8
Adobe(R) Flash(R) Player - środowisko nowej generacji do obsługi
treści i aplikacji we Flashu pod Linuksem.

%prep
%setup -q -n flash_player_%{_ver_major}_linux_dev
tar xf standalone/release/flashplayer.tar.gz

%install
rm -rf $RPM_BUILD_ROOT

install -D flashplayer $RPM_BUILD_ROOT%{_bindir}/flashplayer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
