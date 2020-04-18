package Musify.components;

import java.io.File;
import it.sauronsoftware.jave.AudioAttributes;
import it.sauronsoftware.jave.Encoder;
import it.sauronsoftware.jave.EncoderException;
import it.sauronsoftware.jave.EncodingAttributes;

/**
 * Converts song file quality.
 */
public class SongQualityConverter {
    private static final Integer lowBitrate = 128000; // Minimal bitrate
    private static final Integer mediumBitrate = 256000; // Medium bitrate
    private static final Integer channels = 2; // 2 for stereo, 1 for mono
    private static final Integer samplingRate = 44100; // For good quality.

    /**
     * Creates an instance.
     */
    public SongQualityConverter() {
    }

    /**
     * Generates a new song file with different attributes, based on an existent one.
     * @param source Song file to base on
     * @param target New song file destination path
     * @param withLowQuality true if the new song quality should be the lowest; false if 
     * it should be between the lowest and the highest.
     */
    public void generateSongFile(File source, File target, boolean withLowQuality) {
        AudioAttributes audioAttributes = new AudioAttributes();
        EncodingAttributes encoderAttributes = new EncodingAttributes();
        Encoder encoder = new Encoder();
        if (withLowQuality) {
            audioAttributes.setBitRate(lowBitrate);
        } else {
            audioAttributes.setBitRate(mediumBitrate);
        }
        audioAttributes.setChannels(channels);
        audioAttributes.setSamplingRate(samplingRate);
        encoderAttributes.setAudioAttributes(audioAttributes);
        encoderAttributes.setFormat("mp3");
        try {
            encoder.encode(source, target, encoderAttributes);
        } catch (EncoderException encoderException) {
            System.out.println("Encoding Failed -> " + encoderException.getMessage());
        } catch (Exception exception) {
            System.out.println("Exception -> " + exception.getMessage());
        }
    }
}
