# Read the whole text.
f = open(r'./np3.txt', "r")
text = f.read()

# Read the mask image
modi_coloring = np.array(Image.open('../input/modipic/narendramodi-pti.jpg'))
stopwords = set(STOPWORDS)

# Set up word cloud
wc = WordCloud(max_words=1500, mask=modi_coloring, stopwords=stopwords, max_font_size=35, random_state=42)

# Generate word cloud
wc.generate(text)

# Create coloring from image
image_colors = ImageColorGenerator(modi_coloring)

# Show image
plt.figure(figsize = (15, 15))
plt.axis('off')
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
