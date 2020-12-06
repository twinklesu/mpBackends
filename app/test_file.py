import tensorflow as tf
import tensorflow_hub as hub
import requests
from urllib import request
from PIL import Image
from io import BytesIO


def compare_my_pet(Found_url, Mypet_url):
    CHANNELS = 3  # number of image channels (RGB)

    def build_graph(hub_module_url, target_image_path, Mypet_url):
        module = hub.Module(hub_module_url)
        height, width = hub.get_expected_image_size(module)

        # Copied a method of https://github.com/GoogleCloudPlatform/cloudml-samples/blob/bf0680726/flowers/trainer/model.py#L181
        # and fixed for all type images (not only jpeg)
        def decode_and_resize(image_str_tensor):
            """Decodes jpeg string, resizes it and returns a uint8 tensor."""
            # image = tf.image.decode_image(image_str_tensor, channels=CHANNELS)
            # # Note resize expects a batch_size, but tf_map supresses that index,
            # # thus we have to expand then squeeze.  Resize returns float32 in the
            # # range [0, uint8_max]
            image = tf.expand_dims(image_str_tensor, 0)
            image = tf.compat.v1.image.resize_bilinear(
                image, [height, width], align_corners=False)
            image = tf.squeeze(image, [0])
            image = tf.cast(image, dtype=tf.uint8)
            return image

        def to_img_feature(images):
            """Extract the feature of image vectors"""
            outputs = module(images, signature="image_feature_vector")
            return outputs

        # Step 2) Extract image features of the target image.

        target_image = decode_and_resize(target_image_path)
        target_image = tf.image.convert_image_dtype(target_image, dtype=tf.float32)
        target_image = tf.expand_dims(target_image, 0)
        target_image = to_img_feature(target_image)

        # Step 3) Extract image features of input images.
        input_images = []
        for my_img in Mypet_url:
            input_image = decode_and_resize(my_img)
            input_image = tf.image.convert_image_dtype(input_image, dtype=tf.float32)
            input_image = tf.expand_dims(input_image, 0)
            input_image = to_img_feature(input_image)
            input_images.append(input_image)

        similarities_1 = []
        for input_image in input_images:
            # Step 4) Compare cosine_similarities of the target image and the input images.
            dot = tf.tensordot(target_image, tf.transpose(input_image), 1)
            similarity = dot / (tf.norm(target_image, axis=1) * tf.norm(input_image, axis=1))
            similarity = tf.reshape(similarity, [-1])
            similarities_1.append(similarity)

        return similarities_1

    def get_image(data2, data1):

        target_post_id = data2['result'][0][0]
        target_image_url = data2['result'][0][1]
        res = request.urlopen(target_image_url).read()
        target_img = Image.open(BytesIO(res))

        input_image_list = []
        user_list = []
        user_list.append(target_post_id)

        # user_list.appennd(target_post_id)
        # r = requests.get(input_url)
        # data = r.json()
        for u in data1['result']:
            temp = []
            user_id = u[1]
            pet_name = u[2]
            res = request.urlopen(u[0]).read()
            img = Image.open(BytesIO(res))
            temp.append(user_id)
            temp.append(pet_name)
            user_list.append(temp)
            input_image_list.append(img)

        return target_img, input_image_list, user_list

    # url 2개 집어넣기
    target_img_path, input_img_paths, user_list = get_image(Found_url, Mypet_url)

    hub_module_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_96/feature_vector/1"
    with tf.Graph().as_default():
        similarity = build_graph(hub_module_url, target_img_path, input_img_paths)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            # Inference similarities
            similarities = []

            for i in similarity:
                similarities.append(sess.run(i))

    for i in range(len(similarities)):
        user_list[i + 1].append(similarities[i])

    final = []
    for i in range(len(user_list)):
        if i == 0:
            final.append("post id : ")
            final.append(user_list[i])

            final.append(" similarity")
            final.append("\n")

        else:
            final.append("owner is ")
            final.append(user_list[i][0])
            final.append(". pet name is ")
            final.append(user_list[i][1])
            final.append(" similarity = ")
            final.append(str(float(user_list[i][2])))
            final.append("\n")

    final_result = ','.join(final)
    c = final_result.replace(',', '')
    c = c.replace(' \n', '\n')

    return c