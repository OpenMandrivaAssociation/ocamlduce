Name:           ocamlduce
Version:        3.12.0.0
Release:        %mkrel 1
Summary:        A merger between OCaml and CDuce
License:        QPL & LGPL & MIT
Group:          Development/Other
URL:            https://ocamlduce.forge.ocamlcore.org/
Source0:        http://forge.ocamlcore.org/frs/download.php/225/ocamlduce-%{version}.tar.gz
Patch1:         ocamlduce-3.11.1.0.src-as-dir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.12.0
BuildRequires:  ocaml-sources
BuildRequires:  ocaml-findlib

%description
OCamlDuce is a merger between OCaml and CDuce. It comes as a modified
version of OCaml which integrates CDuce features: XML expressions,
regular expression types and patterns, iterators. The licensing conditions
for OCaml and CDuce apply to the files directly derived from these projects.
Other files are distributed under a choice of any of two licenses used for
OCaml (with the same exceptions).

%prep
%setup -q
%patch1 -p1

%build
make prepare OCAML_SOURCE=/usr/src/ocaml/ OCAML_SRCDIR=ocaml
(cd ocaml/ && ./configure -bindir %{_bindir} -libdir %{_libdir}/ocaml -mandir %{_mandir}/man1 \
           && make -f Makefile.ocamlduce world.opt)

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
cd ocaml/ && make installbyte installopt -f Makefile.ocamlduce \
               LIBDIR=%{buildroot}%{_libdir}/ocaml \
               BINDIR=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_bindir}/*
%dir %{_libdir}/ocaml/ocamlduce
%{_libdir}/ocaml/ocamlduce/*

