# revision 24105
# category Package
# catalog-ctan /macros/xetex/generic/itrans
# catalog-date 2011-09-26 15:47:09 +0200
# catalog-license lppl1.3
# catalog-version 4.0
Name:		texlive-xetex-itrans
Version:	4.0
Release:	1
Summary:	Itrans input maps for use with XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/itrans
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides maps for use with XeLaTeX with coding done
using itrans. Fontspec maps are provided for Devanagari
(Sanskrit), for Sanskrit in Kannada and for Kannada itself.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
