Summary:	A document formatting system
Name:		groff
Version:	1.21
Release:	6
Epoch:		1
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
# Source0-md5:	8b8cd29385b97616a0f0d96d0951c5bf
Source1:	%{name}-trofftops.sh
Source2:	groff-nroff
URL:		http://www.gnu.org/software/groff/
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
Requires:	coreutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Groff is a document formatting system. Groff takes standard text and
formatting commands as input and produces formatted output. The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size,
bold type, italic type, the number and size of columns on a page, and
more. You should install groff if you want to use it as a document
formatting system. Groff can also be used to format man pages. If you
are going to use groff with the X Window System, you'll also need to
install the groff-gxditview package.

%package perl
Summary:	Parts of the groff formatting system that require Perl
Group:		Applications/Publishing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perl
groff-perl contains the parts of the groff text processor package that
require Perl. These include the afmtodit font processor used to create
PostScript font files, the grog utility that can be used to
automatically determine groff command-line options, and the
troff-to-ps print filter.

%prep
%setup -q

sed -i "s|/bin/sed|/usr/bin/sed|g" font/devps/generate/symbol.sed

%build
%configure \
	--without-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/trofftops
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/nroff

ln -sf s.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gs.tmac
ln -sf mse.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gmse.tmac
ln -sf m.tmac	$RPM_BUILD_ROOT%{_datadir}/groff/%{version}/tmac/gm.tmac
ln -sf eqn	$RPM_BUILD_ROOT%{_bindir}/geqn
ln -sf indxbib	$RPM_BUILD_ROOT%{_bindir}/gindxbib
ln -sf lookbib	$RPM_BUILD_ROOT%{_bindir}/glookbib
ln -sf neqn	$RPM_BUILD_ROOT%{_bindir}/gneqn
ln -sf nroff	$RPM_BUILD_ROOT%{_bindir}/gnroff
ln -sf troff	$RPM_BUILD_ROOT%{_bindir}/gtroff
ln -sf tbl	$RPM_BUILD_ROOT%{_bindir}/gtbl
ln -sf pic	$RPM_BUILD_ROOT%{_bindir}/gpic
ln -sf refer	$RPM_BUILD_ROOT%{_bindir}/grefer
ln -sf soelim	$RPM_BUILD_ROOT%{_bindir}/gsoelim

echo ".so eqn.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/geqn.1
echo ".so indxbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gindxbib.1
echo ".so lookbib.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glookbib.1
echo ".so neqn.1" >    $RPM_BUILD_ROOT%{_mandir}/man1/gneqn.1
echo ".so nroff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gnroff.1
echo ".so pic.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gpic.1
echo ".so refer.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/grefer.1
echo ".so soelim.1" >  $RPM_BUILD_ROOT%{_mandir}/man1/gsoelim.1
echo ".so tbl.1" >     $RPM_BUILD_ROOT%{_mandir}/man1/gtbl.1
echo ".so troff.1" >   $RPM_BUILD_ROOT%{_mandir}/man1/gtroff.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc BUG-REPORT ChangeLog NEWS PROBLEMS PROJECTS README TODO
%attr(755,root,root) %{_bindir}/addftinfo
%attr(755,root,root) %{_bindir}/eqn
%attr(755,root,root) %{_bindir}/eqn2graph
%attr(755,root,root) %{_bindir}/geqn
%attr(755,root,root) %{_bindir}/gindxbib
%attr(755,root,root) %{_bindir}/glookbib
%attr(755,root,root) %{_bindir}/gneqn
%attr(755,root,root) %{_bindir}/gnroff
%attr(755,root,root) %{_bindir}/gpic
%attr(755,root,root) %{_bindir}/grefer
%attr(755,root,root) %{_bindir}/grn
%attr(755,root,root) %{_bindir}/grodvi
%attr(755,root,root) %{_bindir}/groff
%attr(755,root,root) %{_bindir}/groffer
%attr(755,root,root) %{_bindir}/grolbp
%attr(755,root,root) %{_bindir}/grolj4
%attr(755,root,root) %{_bindir}/grops
%attr(755,root,root) %{_bindir}/grotty
%attr(755,root,root) %{_bindir}/gsoelim
%attr(755,root,root) %{_bindir}/gtbl
%attr(755,root,root) %{_bindir}/gtroff
%attr(755,root,root) %{_bindir}/hpftodit
%attr(755,root,root) %{_bindir}/indxbib
%attr(755,root,root) %{_bindir}/lkbib
%attr(755,root,root) %{_bindir}/lookbib
%attr(755,root,root) %{_bindir}/neqn
%attr(755,root,root) %{_bindir}/nroff
%attr(755,root,root) %{_bindir}/pfbtops
%attr(755,root,root) %{_bindir}/pic
%attr(755,root,root) %{_bindir}/pic2graph
%attr(755,root,root) %{_bindir}/post-grohtml
%attr(755,root,root) %{_bindir}/pre-grohtml
%attr(755,root,root) %{_bindir}/refer
%attr(755,root,root) %{_bindir}/soelim
%attr(755,root,root) %{_bindir}/tbl
%attr(755,root,root) %{_bindir}/tfmtodit
%attr(755,root,root) %{_bindir}/troff
%attr(755,root,root) %{_bindir}/chem
%attr(755,root,root) %{_bindir}/gdiffmk
%attr(755,root,root) %{_bindir}/grap2graph
%attr(755,root,root) %{_bindir}/pdfroff
%attr(755,root,root) %{_bindir}/preconv
%attr(755,root,root) %{_bindir}/roff2dvi
%attr(755,root,root) %{_bindir}/roff2html
%attr(755,root,root) %{_bindir}/roff2pdf
%attr(755,root,root) %{_bindir}/roff2ps
%attr(755,root,root) %{_bindir}/roff2text
%attr(755,root,root) %{_bindir}/roff2x

%dir %{_libdir}/groff
%dir %{_libdir}/groff/groffer
%attr(755,root,root) %{_libdir}/groff/groffer/split_env.sh
%attr(755,root,root) %{_libdir}/groff/groffer/version.sh

%{_datadir}/groff
%{_mandir}/man1/addftinfo.1*
%{_mandir}/man1/chem.1*
%{_mandir}/man1/eqn.1*
%{_mandir}/man1/eqn2graph.1*
%{_mandir}/man1/gdiffmk.1*
%{_mandir}/man1/geqn.1*
%{_mandir}/man1/gindxbib.1*
%{_mandir}/man1/glookbib.1*
%{_mandir}/man1/gneqn.1*
%{_mandir}/man1/gnroff.1*
%{_mandir}/man1/gpic.1*
%{_mandir}/man1/grap2graph.1*
%{_mandir}/man1/grefer.1*
%{_mandir}/man1/grn.1*
%{_mandir}/man1/grodvi.1*
%{_mandir}/man1/groff.1*
%{_mandir}/man1/groffer.1*
%{_mandir}/man1/grohtml.1*
%{_mandir}/man1/grolbp.1*
%{_mandir}/man1/grolj4.1*
%{_mandir}/man1/grops.1*
%{_mandir}/man1/grotty.1*
%{_mandir}/man1/gsoelim.1*
%{_mandir}/man1/gtbl.1*
%{_mandir}/man1/gtroff.1*
%{_mandir}/man1/hpftodit.1*
%{_mandir}/man1/indxbib.1*
%{_mandir}/man1/lkbib.1*
%{_mandir}/man1/lookbib.1*
%{_mandir}/man1/neqn.1*
%{_mandir}/man1/nroff.1*
%{_mandir}/man1/pdfroff.1*
%{_mandir}/man1/pfbtops.1*
%{_mandir}/man1/pic.1*
%{_mandir}/man1/pic2graph.1*
%{_mandir}/man1/preconv.1*
%{_mandir}/man1/refer.1*
%{_mandir}/man1/roff2dvi.1*
%{_mandir}/man1/roff2html.1*
%{_mandir}/man1/roff2pdf.1*
%{_mandir}/man1/roff2ps.1*
%{_mandir}/man1/roff2text.1*
%{_mandir}/man1/roff2x.1*
%{_mandir}/man1/soelim.1*
%{_mandir}/man1/tbl.1*
%{_mandir}/man1/tfmtodit.1*
%{_mandir}/man1/troff.1*
%{_mandir}/man5/*
%{_mandir}/man7/[!m]*

%{_infodir}/*info*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afmtodit
%attr(755,root,root) %{_bindir}/grog
%attr(755,root,root) %{_bindir}/mmroff
%attr(755,root,root) %{_bindir}/trofftops
%attr(755,root,root) %{_libdir}/groff/groffer/func.pl
%attr(755,root,root) %{_libdir}/groff/groffer/man.pl
%attr(755,root,root) %{_libdir}/groff/groffer/perl_test.pl
%{_mandir}/man1/afmtodit.*
%{_mandir}/man1/grog.*
%{_mandir}/man1/mmroff.*

