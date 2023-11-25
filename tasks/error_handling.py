# Create an image_info func with one dict type parameter
# Func waits for a dict that must contain at least two keys:
# - image_id, image_title
# Function must return a string like following:
# "Image 'my cat' has id 5136"
# If at least one of these keys is not in the dict, func must 
# generate a TypeError error
# Call the func and correctly handle the error if it appears

def image_info(**info: dict) -> str:
    try:
        image_title = info["image_title"]
        image_id = info["image_id"]
        # without error:
        # image_title = info.get("image_title")
        # image_id = info.get("image_id")
        return f"Image '{image_title}' has id {image_id}"
    except KeyError as e:
        raise TypeError(f"Missing required key: {e}")

# Test case 1
info1 = {
    "image_title": "my cat",
    "image_id": 5136,
    "image_size": "100x100",
}

try:
    result = image_info(**info1)
    print(result)
except TypeError as e:
    print(f"Error: {e}")

