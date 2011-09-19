### RPM external swig 2.0.4
## INITENV SET SWIG_HOME %i
## INITENV SET SWIG_LIB  %i/share/swig/%realversion

Source: http://downloads.sourceforge.net/sourceforge/swig/swig/%n-%realversion.tar.gz

%build
./configure --without-pcre --prefix=%i \
            CC="`which gcc`" CXX="`which c++`" LD="`which c++`"
make %makeprocesses
%install
make install
case %cmsos in
  osx*) strip -x %i/bin/{swig,ccache-swig} ;;
  *) strip %i/bin/{swig,ccache-swig} ;;
esac
