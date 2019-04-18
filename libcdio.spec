#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A8DE5008275EC21 (rocky@panix.com)
#
Name     : libcdio
Version  : 2.1.0
Release  : 6
URL      : https://mirrors.kernel.org/gnu/libcdio/libcdio-2.1.0.tar.bz2
Source0  : https://mirrors.kernel.org/gnu/libcdio/libcdio-2.1.0.tar.bz2
Source99 : https://mirrors.kernel.org/gnu/libcdio/libcdio-2.1.0.tar.bz2.sig
Summary  : Portable CD-ROM I/O library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: libcdio-bin = %{version}-%{release}
Requires: libcdio-lib = %{version}-%{release}
Requires: libcdio-license = %{version}-%{release}
Requires: libcdio-man = %{version}-%{release}
BuildRequires : pkgconfig(ncurses)

%description
The libcdio package contains a library for CD-ROM and CD image
access. Applications wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM or of the specific details of
various CD-image formats may benefit from using this library.

%package bin
Summary: bin components for the libcdio package.
Group: Binaries
Requires: libcdio-license = %{version}-%{release}

%description bin
bin components for the libcdio package.


%package dev
Summary: dev components for the libcdio package.
Group: Development
Requires: libcdio-lib = %{version}-%{release}
Requires: libcdio-bin = %{version}-%{release}
Provides: libcdio-devel = %{version}-%{release}
Requires: libcdio = %{version}-%{release}

%description dev
dev components for the libcdio package.


%package doc
Summary: doc components for the libcdio package.
Group: Documentation
Requires: libcdio-man = %{version}-%{release}

%description doc
doc components for the libcdio package.


%package lib
Summary: lib components for the libcdio package.
Group: Libraries
Requires: libcdio-license = %{version}-%{release}

%description lib
lib components for the libcdio package.


%package license
Summary: license components for the libcdio package.
Group: Default

%description license
license components for the libcdio package.


%package man
Summary: man components for the libcdio package.
Group: Default

%description man
man components for the libcdio package.


%prep
%setup -q -n libcdio-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555630061
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1555630061
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcdio
cp COPYING %{buildroot}/usr/share/package-licenses/libcdio/COPYING
cp test/copying-rr.gpl %{buildroot}/usr/share/package-licenses/libcdio/test_copying-rr.gpl
cp test/copying.gpl %{buildroot}/usr/share/package-licenses/libcdio/test_copying.gpl
cp test/data/copying.iso %{buildroot}/usr/share/package-licenses/libcdio/test_data_copying.iso
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cd-drive
/usr/bin/cd-info
/usr/bin/cd-read
/usr/bin/cdda-player
/usr/bin/iso-info
/usr/bin/iso-read
/usr/bin/mmc-tool

%files dev
%defattr(-,root,root,-)
/usr/include/cdio++/cdio.hpp
/usr/include/cdio++/cdtext.hpp
/usr/include/cdio++/device.hpp
/usr/include/cdio++/devices.hpp
/usr/include/cdio++/disc.hpp
/usr/include/cdio++/enum.hpp
/usr/include/cdio++/iso9660.hpp
/usr/include/cdio++/mmc.hpp
/usr/include/cdio++/read.hpp
/usr/include/cdio++/track.hpp
/usr/include/cdio/audio.h
/usr/include/cdio/bytesex.h
/usr/include/cdio/bytesex_asm.h
/usr/include/cdio/cd_types.h
/usr/include/cdio/cdio.h
/usr/include/cdio/cdio_config.h
/usr/include/cdio/cdtext.h
/usr/include/cdio/device.h
/usr/include/cdio/disc.h
/usr/include/cdio/ds.h
/usr/include/cdio/dvd.h
/usr/include/cdio/ecma_167.h
/usr/include/cdio/iso9660.h
/usr/include/cdio/logging.h
/usr/include/cdio/memory.h
/usr/include/cdio/mmc.h
/usr/include/cdio/mmc_cmds.h
/usr/include/cdio/mmc_hl_cmds.h
/usr/include/cdio/mmc_ll_cmds.h
/usr/include/cdio/mmc_util.h
/usr/include/cdio/posix.h
/usr/include/cdio/read.h
/usr/include/cdio/rock.h
/usr/include/cdio/sector.h
/usr/include/cdio/track.h
/usr/include/cdio/types.h
/usr/include/cdio/udf.h
/usr/include/cdio/udf_file.h
/usr/include/cdio/udf_time.h
/usr/include/cdio/utf8.h
/usr/include/cdio/util.h
/usr/include/cdio/version.h
/usr/include/cdio/xa.h
/usr/lib64/libcdio++.so
/usr/lib64/libcdio.so
/usr/lib64/libiso9660++.so
/usr/lib64/libiso9660.so
/usr/lib64/libudf.so
/usr/lib64/pkgconfig/libcdio++.pc
/usr/lib64/pkgconfig/libcdio.pc
/usr/lib64/pkgconfig/libiso9660++.pc
/usr/lib64/pkgconfig/libiso9660.pc
/usr/lib64/pkgconfig/libudf.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcdio++.so.1
/usr/lib64/libcdio++.so.1.0.0
/usr/lib64/libcdio.so.19
/usr/lib64/libcdio.so.19.0.0
/usr/lib64/libiso9660++.so.0
/usr/lib64/libiso9660++.so.0.0.0
/usr/lib64/libiso9660.so.11
/usr/lib64/libiso9660.so.11.0.0
/usr/lib64/libudf.so.0
/usr/lib64/libudf.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcdio/COPYING
/usr/share/package-licenses/libcdio/test_copying-rr.gpl
/usr/share/package-licenses/libcdio/test_copying.gpl
/usr/share/package-licenses/libcdio/test_data_copying.iso

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cd-drive.1
/usr/share/man/man1/cd-info.1
/usr/share/man/man1/cd-read.1
/usr/share/man/man1/iso-info.1
/usr/share/man/man1/iso-read.1
