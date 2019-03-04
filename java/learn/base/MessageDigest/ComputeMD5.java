import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class ComputeMD5{

	public static String getMD5String(String rawString){
        String[] hexArray = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"};
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(rawString.getBytes());
            byte[] rawBit = md.digest();
            String outputMD5 = " ";
            for(int i = 0; i<3; i++){
                outputMD5 = outputMD5+hexArray[rawBit[i]>>>4& 0x0f];
                outputMD5 = outputMD5+hexArray[rawBit[i]& 0x0f];
            }
            return outputMD5.trim();
        }catch(NoSuchAlgorithmException e){
            System.out.println("error");
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String[] args){
		System.out.println(getMD5String(args[0]));
	}
}
