for s in {256,128,64,32,16}; do
	ffmpeg -i play-next-button-green-icon_512.bmp -filter:v "scale=-1:$s" play-next-button-green-icon_$s.png && mv play-next-button-green-icon_$s.png play-next-button-green-icon_$s.bmp
done
