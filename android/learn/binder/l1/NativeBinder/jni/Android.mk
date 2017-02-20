LOCAL_PATH := $(call my-dir)

#编译demecore动态库
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := eng
LOCAL_MODULE := libdemocore
JNI_RES_DIR := /opt/android/jni

LOCAL_SRC_FILES := democore/DemoService.cpp democore/IDemoService.cpp
LOCAL_C_INCLUDES := ${JNI_RES_DIR}/include 
LOCAL_C_INCLUDES += ${LOCAL_PATH}/democore
LOCAL_CPPFLAGS   += -DDEBUG -DHAVE_ANDROID_OS  -DHAVE_SYS_UIO_H
LOCAL_LDFLAGS := -L${JNI_RES_DIR}/libs -O2
LOCAL_LDFLAGS += -lcutils -lutils -lbinder -llog

ALL_DEFAULT_INSTALLED_MODULES += ${LOCAL_MODULE}
include $(BUILD_SHARED_LIBRARY)

#编译服务端程序
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := eng
LOCAL_MODULE := DemoServer
LOCAL_SRC_FILES := server/DemoServer.cpp
LOCAL_C_INCLUDES := ${JNI_RES_DIR}/include 
LOCAL_C_INCLUDES += ${LOCAL_PATH}/democore
LOCAL_CPPFLAGS   += -DDEBUG -DHAVE_ANDROID_OS  -DHAVE_SYS_UIO_H
LOCAL_LDFLAGS += -L${JNI_RES_DIR}/libs -O2
LOCAL_LDFLAGS += -llog -lcutils -lutils -lbinder 
LOCAL_SHARED_LIBRARIES += libdemocore
ALL_DEFAULT_INSTALLED_MODULES += $(LOCAL_MODULE)
include $(BUILD_EXECUTABLE)

#编译客户端程序
include $(CLEAR_VARS)
LOCAL_MODULE_TAGS := eng
LOCAL_MODULE := DemoClient
LOCAL_SRC_FILES := client/DemoClient.cpp

LOCAL_C_INCLUDES := ${JNI_RES_DIR}/include 
LOCAL_C_INCLUDES += ${LOCAL_PATH}/democore
LOCAL_CPPFLAGS   += -DDEBUG -DHAVE_ANDROID_OS  -DHAVE_SYS_UIO_H
LOCAL_LDFLAGS += -L${JNI_RES_DIR}/libs -O2
LOCAL_LDFLAGS += -llog -lcutils -lutils -lbinder 
LOCAL_SHARED_LIBRARIES += libdemocore
ALL_DEFAULT_INSTALLED_MODULES += $(LOCAL_MODULE)
include $(BUILD_EXECUTABLE)
