# import the necessary packages
from flask import Flask, render_template, redirect, url_for, request,session,Response
import numpy as np
import cv2
import sys
import os
from twilio.rest import Client
from firebase import firebase
import json


firebase1 = firebase.FirebaseApplication('https://heart-3eccd-default-rtdb.firebaseio.com', None)



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC565174843fde27746ea872eb1eafb38b'
auth_token = '7b777fb52d820dc63cb4f792c66d6b51'
client = Client(account_sid, auth_token)

app = Flask(__name__)

app.secret_key = '1234'
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('camera'))
	return render_template('login.html', error=error)
	
@app.route('/camera', methods=['GET', 'POST'])
def camera():
	return render_template('camera.html')

def get_frame():
	# Helper Methods
	def buildGauss(frame, levels):     #image pyramid of different resolution downward
		pyramid = [frame]
		for level in range(levels):
			frame = cv2.pyrDown(frame)
			pyramid.append(frame)
		return pyramid
	def reconstructFrame(pyramid, index, levels): #image pyramid of different resolution upward
		filteredFrame = pyramid[index]
		for level in range(levels):
			filteredFrame = cv2.pyrUp(filteredFrame)
		filteredFrame = filteredFrame[:videoHeight, :videoWidth]
		return filteredFrame

	# Webcam Parameters
	webcam = None
	if len(sys.argv) == 2:
		webcam = cv2.VideoCapture(sys.argv[1])
	else:
		webcam = cv2.VideoCapture(0)   #port depend on number of camera
	realWidth = 500
	realHeight = 500
	videoWidth = 250
	videoHeight = 250
	videoChannels = 3       #RGB
	videoFrameRate = 15
	webcam.set(3, realWidth)
	webcam.set(4, realHeight)


	# Color Magnification Parameters
	levels = 3
	alpha = 170
	minFrequency = 1.0
	maxFrequency = 2.0
	bufferSize = 150
	bufferIndex = 0

	# Output Display Parameters
	font = cv2.FONT_HERSHEY_SIMPLEX
	loadingTextLocation = (20, 30)
	bpmTextLocation = (videoWidth//2 + 5, 30)
	fontScale = 1
	fontColor = (255,255,255)
	lineType = 2
	boxColor = (0, 255, 0)
	boxWeight = 3

	# Initialize Gaussian Pyramid
	firstFrame = np.zeros((videoHeight, videoWidth, videoChannels))
	firstGauss = buildGauss(firstFrame, levels+1)[levels]
	videoGauss = np.zeros((bufferSize, firstGauss.shape[0], firstGauss.shape[1], videoChannels))
	fourierTransformAvg = np.zeros((bufferSize))

	# Bandpass Filter for Specified Frequencies
	frequencies = (1.0*videoFrameRate) * np.arange(bufferSize) / (1.0*bufferSize)
	#print(frequencies)     #0.0 to 14.9
	mask = (frequencies >= minFrequency) & (frequencies <= maxFrequency)  # band pass filter (1Hz to 2Hz as HR = 72bpm)

	# Heart Rate Calculation Variables
	bpmCalculationFrequency = 15    #Framerate=15
	bpmBufferIndex = 0
	bpmBufferSize = 10
	bpmBuffer = np.zeros((bpmBufferSize))

	i = 0
	faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	while True:
		ret, frame = webcam.read()
		if ret == False:
			break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
			gray,
	
			scaleFactor=1.2,
			minNeighbors=5
			,     
	   		minSize=(20, 20)
		)

		totalFace = len(faces)		

		detectionFrame = frame[int(videoHeight/2):int(realHeight-videoHeight/2), int(videoWidth/2):int(realWidth-videoWidth/2), :]

		# Construct Gaussian Pyramid
		videoGauss[bufferIndex] = buildGauss(detectionFrame, levels+1)[levels]
		fourierTransform = np.fft.fft(videoGauss, axis=0)

		# Bandpass Filter
		fourierTransform[mask == False] = 0

		# Grab a Pulse
		if bufferIndex % bpmCalculationFrequency == 0:     #after every 15 frames
			i = i + 1
			for buf in range(bufferSize):
				fourierTransformAvg[buf] = np.real(fourierTransform[buf]).mean()
			hz = frequencies[np.argmax(fourierTransformAvg)]
			bpm = 60.0 * hz
			bpmBuffer[bpmBufferIndex] = bpm
			bpmBufferIndex = (bpmBufferIndex + 1) % bpmBufferSize

		# Amplify
		filtered = np.real(np.fft.ifft(fourierTransform, axis=0))
		filtered = filtered * alpha

		# Reconstruct Resulting Frame
		filteredFrame = reconstructFrame(filtered, bufferIndex, levels)
		outputFrame = detectionFrame + filteredFrame
		outputFrame = cv2.convertScaleAbs(outputFrame)

		bufferIndex = (bufferIndex + 1) % bufferSize
               
		frame[int(videoHeight/2):int(realHeight-videoHeight/2), int(videoWidth/2):int(realWidth-videoWidth/2), :] = outputFrame
		cv2.rectangle(frame, (int(videoWidth/2) , int(videoHeight/2)), (int(realWidth-videoWidth/2), int(realHeight-videoHeight/2)), boxColor, boxWeight)
		if(totalFace>0):
			if i > bpmBufferSize:
				with open('p1.csv','a') as fd:
					fd.write(str(bpmBuffer.mean()))

				#data = {'p1':bpmBuffer.mean()}
				#data = json.dumps(data)
				res = firebase1.put('https://heart-3eccd-default-rtdb.firebaseio.com','p1',str(bpmBuffer.mean()))
				cv2.putText(frame, "BPM: %d" % bpmBuffer.mean(), bpmTextLocation, font, fontScale, fontColor, lineType)
				if(bpmBuffer.mean()>110 or bpmBuffer.mean()<60):
					message = client.messages \
						.create(
							body="Patient of Bed 1-abnormal Heart Beats ...Emergency treatment needed",
							from_='+12168103133',
							to='+918421525880'
						)
			
			else:
				cv2.putText(frame, "Calculating BPM...", loadingTextLocation, font, fontScale, fontColor, lineType)
		else:
			cv2.putText(frame, "Face Not Found..", loadingTextLocation, font, fontScale, fontColor, lineType)



		imgencode=cv2.imencode('.jpg',frame)[1]
		stringData=imgencode.tostring()
		yield (b'--frame\r\n'
			b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

	webcam.release()
	cv2.destroyAllWindows()




@app.route('/video_stream')
def video_stream():
	 
	 return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')


# No caching at all for API endpoints.
@app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	return response


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
