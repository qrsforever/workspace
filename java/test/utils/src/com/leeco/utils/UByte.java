
package com.leeco.utils;

public final class UByte {

    /**
     * @param addr
     * @param align
     * @return
     */
    public static int align(int addr, int align) {
        if (align > addr) {
            return addr;
        }
        int offset = addr % align;
        return addr + (align - offset);
    }

    /**
     * @param bytes
     * @return
     */
    public static String bytes2HexString(byte[] bytes) {
        StringBuilder result = new StringBuilder();
        for (int i = bytes.length - 1; i >= 0; i--) {
            String hex = Integer.toHexString(bytes[i]);
            if (hex.length() < 2) {
                result.append("0" + hex);
            } else {
                result.append(hex);
            }
            result.append(" ");
        }
        return result.toString();
    }

    /**
     * @param res
     * @param start
     * @param count
     * @return
     */
    public static byte[] copyBytes(byte[] res, int start, int count) {
        if (res == null) {
            return null;
        }
        byte[] result = new byte[count];
        for (int i = 0; i < count; i++) {
            result[i] = res[start + i];
        }
        return result;
    }

    /**
     * @param res
     * @return
     */
    public static int byte2Int(byte[] res) {
        int targets = (res[0] & 0xff) | ((res[1] << 8) & 0xff00) | ((res[2] << 24) >>> 8)
                | (res[3] << 24);
        return targets;
    }

    public static long byte2Long(byte[] b) {
        long s = 0;
        long s0 = b[0] & 0xff;
        long s1 = b[1] & 0xff;
        long s2 = b[2] & 0xff;
        long s3 = b[3] & 0xff;
        long s4 = b[4] & 0xff;
        long s5 = b[5] & 0xff;
        long s6 = b[6] & 0xff;
        long s7 = b[7] & 0xff;
        s1 <<= 8;
        s2 <<= 16;
        s3 <<= 24;
        s4 <<= 32;
        s5 <<= 40;
        s6 <<= 48;
        s7 <<= 56;
        s = s0 | s1 | s2 | s3 | s4 | s5 | s6 | s7;
        return s;
    }

    public static short byte2Short(byte[] b) {
        short s = 0;
        short s0 = (short) (b[0] & 0xff);
        short s1 = (short) (b[1] & 0xff);
        s1 <<= 8;
        s = (short) (s0 | s1);
        return s;
    }

    public static byte[] long2ByteAry(long number) {
        long temp = number;
        byte[] b = new byte[8];
        for (int i = 0; i < b.length; i++) {
            b[i] = new Long(temp & 0xff).byteValue();
            temp = temp >> 8;
        }
        return b;
    }

    public static byte[] int2Byte(int number) {
        int temp = number;
        byte[] b = new byte[4];
        for (int i = 0; i < b.length; i++) {
            b[i] = new Integer(temp & 0xff).byteValue();
            temp = temp >> 8;
        }
        return b;
    }

    public static byte[] short2Byte(short number) {
        int temp = number;
        byte[] b = new byte[2];
        for (int i = 0; i < b.length; i++) {
            b[i] = new Integer(temp & 0xff).byteValue();
            temp = temp >> 8;
        }
        return b;
    }

    public static byte[] replaceByteAry(byte[] src, int rep_index, byte[] copyByte) {
        for (int i = rep_index; i < rep_index + copyByte.length; i++) {
            src[i] = copyByte[i - rep_index];
        }
        return src;
    }

    public static byte[] reverseBytes(byte[] bytes) {
        if (bytes == null || (bytes.length % 2) != 0) {
            return bytes;
        }
        int i = 0;
        int offset = bytes.length / 2;
        while (i < (bytes.length / 2)) {
            byte tmp = bytes[i];
            bytes[i] = bytes[offset + i];
            bytes[offset + i] = tmp;
            i++;
        }
        return bytes;
    }
}
