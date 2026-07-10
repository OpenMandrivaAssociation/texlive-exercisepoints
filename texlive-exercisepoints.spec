%global tl_name exercisepoints
%global tl_revision 49590

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.3
Release:	%{tl_revision}.1
Summary:	A LaTeX package to count exercises and points
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exercisepoints
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisepoints.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercisepoints.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can be used to facilitate exercise counting and exercise
point counting in a LaTeX-document. It counts the number of exercises
and it sums all the points of the exercises in a document. Especially
for exams it is also common to have an overview of all exercises and
their maximal points. This is also supported by this package by
providing a macro to retrieve the points of each exercise.

