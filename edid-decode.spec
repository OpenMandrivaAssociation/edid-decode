%define git	20120926

Summary:	EDID parse tool
Name:		edid-decode
Version:	20170207
Release:	1
License:	MIT
Group:		System/X11
Url:		http://cgit.freedesktop.org/xorg/app/edid-decode/
# git clone git://anongit.freedesktop.org/xorg/app/edid-decode
# tar c -j --exclude=.git --exclude=.gitignore -f edid-decode-%{git}.tar.bz2 edid-decode
Source0:	%{name}-%{git}.tar.bz2
# (cjw) add a basic man page
Source1:	edid-decode.1
# (cjw) use CFLAGS to compile source file
Patch1:		edid-decode-makefile.patch
# (cjw) fix string parsing
Patch2:		edid-decode-extract-string.patch

%description
The edid-decode tool parses a given EDID from a file or stdin and
shows the contents on stdout. It handles both the regular video info
and the audio info often provided by HDMI displays.

%prep
%setup -q -n %{name}
%patch1 -p1 -b .cleanup
%patch2 -p1 -b .strings

%build
%make CFLAGS="%{optflags}"

%install
%makeinstall_std
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

