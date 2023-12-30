from PIL import Image
from ultralytics import YOLO

'''
Required Library's
PIL, ultralytics
'''

#Pretrained model of the YoloV8 project, we can train a model by ourself to suit our own needs.
model = YOLO("yolov8n.pt")

results = model("gr.png") # put here image to get a result.

#Turn the result into an image using PIL.
for r in results:
    im_array = r.plot()
    im = Image.fromarray(im_array[..., ::-1])
    im.show()
    im.save("results.jpg")

'''
This is a poc that shows an already built Neural Network
this is built for camera, which is good for us because like camera, stock graph is updated live on every ms
so the only thing left to do is to choose which graph patterns we need, create a dataset based on those patterns
and than train, validated and test,
and we pretty much done with a Convolutional Neural Network
'''