#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-calibrator
Version  : 1.2.6
Release  : 4
URL      : https://cran.r-project.org/src/contrib/calibrator_1.2-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/calibrator_1.2-6.tar.gz
Summary  : Bayesian calibration of complex computer codes
Group    : Development/Tools
License  : GPL-2.0
Requires: R-cubature
Requires: R-emulator
BuildRequires : R-cubature
BuildRequires : R-emulator
BuildRequires : clr-R-helpers

%description
Kennedy and O'Hagan 2001.  The package includes routines to find the
 hyperparameters and parameters; see the help page for stage1() for a
 worked example using the toy dataset.  A tutorial is provided in the
 calex.Rnw vignette; and a suite of especially simple one dimensional
 examples appears in inst/doc/one.dim/.

%prep
%setup -q -c -n calibrator

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530465831

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530465831
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrator
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrator
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library calibrator
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library calibrator|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/calibrator/CITATION
/usr/lib64/R/library/calibrator/DESCRIPTION
/usr/lib64/R/library/calibrator/INDEX
/usr/lib64/R/library/calibrator/Meta/Rd.rds
/usr/lib64/R/library/calibrator/Meta/data.rds
/usr/lib64/R/library/calibrator/Meta/features.rds
/usr/lib64/R/library/calibrator/Meta/hsearch.rds
/usr/lib64/R/library/calibrator/Meta/links.rds
/usr/lib64/R/library/calibrator/Meta/nsInfo.rds
/usr/lib64/R/library/calibrator/Meta/package.rds
/usr/lib64/R/library/calibrator/Meta/vignette.rds
/usr/lib64/R/library/calibrator/NAMESPACE
/usr/lib64/R/library/calibrator/R/calibrator
/usr/lib64/R/library/calibrator/R/calibrator.rdb
/usr/lib64/R/library/calibrator/R/calibrator.rdx
/usr/lib64/R/library/calibrator/data/toys.rda
/usr/lib64/R/library/calibrator/doc/calex.R
/usr/lib64/R/library/calibrator/doc/calex.Rnw
/usr/lib64/R/library/calibrator/doc/calex.pdf
/usr/lib64/R/library/calibrator/doc/index.html
/usr/lib64/R/library/calibrator/doc/one.dim/Ed_theta_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/READ.ME
/usr/lib64/R/library/calibrator/doc/one.dim/calex_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/data_maker_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/design_maker_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/extractor_maker_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/h1_h2_maker_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/params_maker_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/phi_fun_1d.R
/usr/lib64/R/library/calibrator/doc/one.dim/phi_maker_1d.R
/usr/lib64/R/library/calibrator/help/AnIndex
/usr/lib64/R/library/calibrator/help/aliases.rds
/usr/lib64/R/library/calibrator/help/calibrator.rdb
/usr/lib64/R/library/calibrator/help/calibrator.rdx
/usr/lib64/R/library/calibrator/help/paths.rds
/usr/lib64/R/library/calibrator/html/00Index.html
/usr/lib64/R/library/calibrator/html/R.css
