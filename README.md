# FastHugs
Use fastai-v2 with HuggingFace's pretrained transformers

See this post for a look at the fasthugs demo : http://www.ntentional.com/2020/02/18/fasthugs_demo.html or give the `fasthugs_demo.ipynb` notebook a spin!


## Things You Might Like (❤️ ?)
**FastHugsTokenizer:** A tokenizer wrapper than can be used with fastai-v2’s tokenizer.

**FastHugsModel:** A model wrapper over the HF models, more or less the same to the wrapper’s from HF fastai-v1 articles mentioned below

**Vocab:** A function to extract the vocab depending on the pre-trained transformer (HF hasn’t standardised this processes 😢).

**Padding:** Padding settings for the padding token index and on whether the transformer prefers left or right padding

**Vocab for Albert-base-v2:** .json for Albert-base-v2’s vocab, otherwise this has to be extracted from a SentencePiece model file, which isn’t fun

**Model Splitters**: Functions to split the classification head from the model backbone in line with fastai-v2’s new definition of Learner

## Read these first 👇
This notebook heavily borrows from this notebook , which in turn is based off of this tutorial and accompanying article. Huge thanks to Melissa Rajaram and Maximilien Roberti for these great resources, if you're not familiar with the HuggingFace library please given them a read first as they are quite comprehensive.

## fastai-v2 ✌️2️⃣
This paper introduces the v2 version of the fastai library and you can follow and contribute to v2's progress on the forums. This notebook uses the small IMDB dataset and is based off the fastai-v2 ULMFiT tutorial. Huge thanks to Jeremy, Sylvain, Rachel and the fastai community for making this library what it is. I'm super excited about the additinal flexibility v2 brings. 🎉
