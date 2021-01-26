# Read the whole text.
f = open(r'../input/ambedkarkibaate/ambedkarspeech.txt.txt', "r")
text = f.read()

# Create mask
img_mask = img.copy()
img_mask[img_mask.sum(axis=2) == 0] = 255

# Edge detection in the image
edges = np.mean([gaussian_gradient_magnitude(img[:, :, i] / 255., 2) for i in range(3)], axis=0)
img_mask[edges > .08] = 255

# Set up word cloud
wc = WordCloud(max_words=2000, mask=img_mask, max_font_size=40, random_state=42)

# Generate word cloud
wc.generate(text)

# Create coloring from image
image_colors = ImageColorGenerator(img)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(15, 15))
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")

plt.figure(figsize=(15, 15))
plt.axis('off')
plt.imshow(edges)
