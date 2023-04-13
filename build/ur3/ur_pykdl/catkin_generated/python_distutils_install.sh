#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/susyreyesm/ros/ur3c_ws/src/ur3/ur_pykdl"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/susyreyesm/ros/ur3c_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/susyreyesm/ros/ur3c_ws/install/lib/python2.7/dist-packages:/home/susyreyesm/ros/ur3c_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/susyreyesm/ros/ur3c_ws/build" \
    "/usr/bin/python2" \
    "/home/susyreyesm/ros/ur3c_ws/src/ur3/ur_pykdl/setup.py" \
     \
    build --build-base "/home/susyreyesm/ros/ur3c_ws/build/ur3/ur_pykdl" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/susyreyesm/ros/ur3c_ws/install" --install-scripts="/home/susyreyesm/ros/ur3c_ws/install/bin"