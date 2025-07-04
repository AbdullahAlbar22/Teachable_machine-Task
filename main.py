from keras.layers import TFSMLayer
import numpy as np
from PIL import Image

# ✅ Load the model
layer = TFSMLayer('/content/model.savedmodel', call_endpoint='serving_default')
print("Model loaded!")

# ✅ Load image
img = Image.open('/content/a7.jpg').resize((224, 224))
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# ✅ Predict
predictions = layer(img_array)
print("Raw predictions dict:", predictions)

# ✅ Extract tensor
pred_tensor = list(predictions.values())[0]  # OR predictions['outputs'] if you know the key
print("Raw prediction tensor:", pred_tensor.numpy())

# ✅ Map to class names
class_names = ['Bananna', 'Apple']
predicted_class = class_names[np.argmax(pred_tensor)]
print("Predicted Class:", predicted_class)