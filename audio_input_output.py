#Reading audio and printing

import cmu_sphinx4
audio_url = ''
transciber =  cmu_sphinx4.Transcriber(audio_url)
for line in transciber.transcript_stream():
	print line
	
	
	