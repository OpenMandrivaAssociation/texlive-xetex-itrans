%global tl_name xetex-itrans
%global tl_revision 55475

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2
Release:	%{tl_revision}.1
Summary:	Itrans input maps for use with XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/itrans
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-itrans.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides maps for use with XeLaTeX with coding done using
itrans. Fontspec maps are provided for Devanagari (Sanskrit), for
Sanskrit in Kannada and for Kannada itself.

