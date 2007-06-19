%define name	ocamlduce
%define version	3.10.0
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A merger between OCaml and CDuce
URL:		http://caml.inria.fr
License:	QPL & LGPL
Group:		Development/Other
Source0:	http://gallium.inria.fr/~frisch/ocamlduce/download/%{name}-%{version}.tar.gz
Patch0:		ocamlduce-3.10.0-destdir.patch
BuildRequires:	libx11-devel ncurses-devel tcl tcl-devel tk tk-devel emacs-bin db4-devel
BuildRequires:	ocaml ocamlfind
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OCamlDuce is a merger between OCaml and CDuce. It comes as a modified
version of OCaml which integrates CDuce features: XML expressions,
regular expression types and patterns, iterators. The licensing conditions
for OCaml and CDuce apply to the files directly derived from these projects.
Other files are distributed under a choice of any of two licenses used for
OCaml (with the same exceptions).

%prep
%setup -q
%patch0 -p1 -b .destdir

%build
make all
make opt

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/*
%dir %{_libdir}/ocaml/site-lib/ocamlduce
%{_libdir}/ocaml/site-lib/ocamlduce/*

%changelog
