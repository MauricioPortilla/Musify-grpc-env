package Musify.components;

import java.io.File;

public class SongQualityMain {

    private static final String LOW_QUALITY_SONGS_FOLDER = "/home/vagrant/Musify/storage/songs/lowquality/";
    private static final String MEDIUM_QUALITY_SONGS_FOLDER = "/home/vagrant/Musify/storage/songs/mediumquality/";

    public static void main(String[] args) {
        if (args[0] == null) {
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
