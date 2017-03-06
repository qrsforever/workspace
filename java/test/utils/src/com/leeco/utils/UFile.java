package com.leeco.utils;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

public final class UFile {

	public static boolean saveFile(String fileName, byte[] arys){
		File file = new File(fileName);
		FileOutputStream fos = null;
		try{
			fos = new FileOutputStream(file);
			fos.write(arys);
			fos.flush();
			return true;
		}catch(Exception e){
			System.out.println("save file error:"+e.toString());
		}finally{
			if(fos != null){
				try{
					fos.close();
				}catch(Exception e){
					System.out.println("close file error:"+e.toString());
				}
			}
		}
		return false;
	}

	public static byte[] readFile(String fileName){
		File file = new File(fileName);
		FileInputStream fis = null;
		ByteArrayOutputStream bos = null;
		try{
			fis = new FileInputStream(file);
			bos = new ByteArrayOutputStream();
			byte[] temp = new byte[1024];
	        int size = 0;
	        while ((size = fis.read(temp)) != -1) {
	        	bos.write(temp, 0, size);
	        }
	        return bos.toByteArray();
		}catch(Exception e){
			System.out.println("read file error:"+e.toString());
		}finally{
			if(fis != null){
				try{
					fis.close();
				}catch(Exception e){
					System.out.println("close file error:"+e.toString());
				}
			}
			if(bos != null){
				try{
					bos.close();
				}catch(Exception e){
					System.out.println("close file error:"+e.toString());
				}
			}
		}
		return null;
	}
}
