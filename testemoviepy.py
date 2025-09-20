from moviepy.editor import TextClip, CompositeVideoClip

texto = TextClip("Teste MoviePy", fontsize=70, color='white').set_duration(3)
video = CompositeVideoClip([texto]).set_duration(3)
video.write_videofile("teste.mp4", fps=24)
