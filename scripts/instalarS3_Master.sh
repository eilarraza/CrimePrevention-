apt-get update
apt-get upgrade
#yum -y install libcurl libcurl-devel
sudo apt-get remove fuse
sudo apt-get install build-essential libcurl4-openssl-dev libxml2-dev mime-support
cd /usr/src/
wget http://downloads.sourceforge.net/project/fuse/fuse-2.X/2.9.4/fuse-2.9.4.tar.gz
tar xzf fuse-2.9.4.tar.gz
cd fuse-2.9.4
./configure --prefix=/usr/local
make && make install
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
ldconfig
modprobe fuse

cd /usr/src/
wget https://s3fs.googlecode.com/files/s3fs-1.74.tar.gz
tar xzf s3fs-1.74.tar.gz
cd s3fs-1.74
./configure --prefix=/usr/local
make && make install

echo AKIAILPF44AI6FPDD43A:5NOWefTzLSQ9AC3oTafPAGz5d+KMROCoPffhE78v > ~/.passwd-s3fs
chmod 600 ~/.passwd-s3fs

mkdir /tmp/cache
cd /tmp/cache
cd /
mkdir /s3mnt3
cd /
chmod 777 /tmp/cache

#fusermount -u /s3mnt s3fs -o
#allow_other s3archivos /s3mnt
#allow_other databritanica /s3mnt3
s3fs -o use_cache=/tmp/cache databritanica /s3mnt3
