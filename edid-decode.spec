Summary:	EDID parse tool
Name:		edid-decode
Version:	20210201
Release:	1
License:	MIT
Group:		System/X11
Url:		https://git.linuxtv.org/edid-decode.git/
# git clone https://git.linuxtv.org//edid-decode.git/ && cd edid-decode
# git archive --prefix=edid-decode-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../edid-decode-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.xz

%description
The edid-decode tool parses a given EDID from a file or stdin and
shows the contents on stdout. It handles both the regular video info
and the audio info often provided by HDMI displays.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
