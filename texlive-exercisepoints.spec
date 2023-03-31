Name:		texlive-exercisepoints
Version:	49590
Release:	2
Summary:	A LaTeX package to count exercises and points
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exercisepoints
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisepoints.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisepoints.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can be used to facilitate exercise counting and
exercise point counting in a LaTeX-document. It counts the
number of exercises and it sums all the points of the exercises
in a document. Especially for exams it is also common to have
an overview of all exercises and their maximal points. This is
also supported by this package by providing a macro to retrieve
the points of each exercise.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/exercisepoints
%doc %{_texmfdistdir}/doc/latex/exercisepoints

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
