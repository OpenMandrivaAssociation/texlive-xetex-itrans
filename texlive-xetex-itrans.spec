Name:		texlive-xetex-itrans
Version:	55475
Release:	2
Summary:	Itrans input maps for use with XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/itrans
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides maps for use with XeLaTeX with coding done
using itrans. Fontspec maps are provided for Devanagari
(Sanskrit), for Sanskrit in Kannada and for Kannada itself.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/brh-kan.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/brh-kan.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-dvn.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-dvn.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-iast.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-iast.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-kan.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-kan.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-sankan.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-sankan.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-santel.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-santel.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-sdvn.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-sdvn.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-tamil.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-tamil.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-tel.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-itrans/itrans-tel.tec
%doc %{_texmfdistdir}/doc/xelatex/xetex-itrans/README
%doc %{_texmfdistdir}/doc/xelatex/xetex-itrans/itrans-tamil-sample.pdf
%doc %{_texmfdistdir}/doc/xelatex/xetex-itrans/itrans-tamil-sample.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
