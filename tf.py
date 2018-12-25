import cv2

def read_cam(cam, mirror=False):
	_, img = cam.read()
	if mirror: 
		img = cv2.flip(img, 1)
	return img

def main():
	cam = cv2.VideoCapture(0)
	while cam.isOpened():
		img = read_cam(cam, True)
		img = cv2.resize(img, (640, 360), interpolation=cv2.INTER_CUBIC)
		cv2.imshow("123", img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cam.release()
	cv2.destroyAllWindows()
		

if __name__ == '__main__':
	main()