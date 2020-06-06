package Musify.components;

import java.io.File;

/**
 * Song quality converter executor.
 */
public class SongQualityMain {

    // Directories accord to Musify gRPC Server file (musify_service_server.py) execution location.
    private static final String LOW_QUALITY_SONGS_FOLDER = System.getProperty("user.dir") + "/../../storage/songs/lowquality/";
    private static final String MEDIUM_QUALITY_SONGS_FOLDER = System.getProperty("user.dir") + "/../../storage/songs/mediumquality/";

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("No source file.");
            return;
        }
        SongQualityConverter converter = new SongQualityConverter();
        File source = new File(args[0]);
        File lowQualityTarget = new File(LOW_QUALITY_SONGS_FOLDER + source.getName());
        File mediumQualityTarget = new File(MEDIUM_QUALITY_SONGS_FOLDER + source.getName());

        converter.generateSongFile(source, lowQualityTarget, true);
        converter.generateSongFile(source, mediumQualityTarget, false);
    }
}
