#!/usr/bin/env python
# coding: utf-8

# (cuneif)=
# # L0.4: Cuneiform Script
# 
# In the south of Mesopotamia, at the end of the fourth millennium BCE, a writing system based on ideograms was invented for bookkeeping. Today this writing system is known as "cuneiform". The name "cuneiform" derives from the latin word *cuneus* "wedge" and *forme* "form" . It denotes the shape of the strokes. The native designation for the cuneiform script was *tikip santakku* "triangle script". Before the deciphermet of this script they were also called *dactuli pyramidales*, *pyramidales figura* "pyramidal signs". 
# 
# `````{admonition} Good to know 🤓 
# :class: tip
# Thomas Hyde was the first one to name it "cuneiformes": "Istiusmodi enim ductuli pyramidales seu Cuneiformes [...]." (Hyde {cite:year}`hyde_1700`, 526). But he thought that these signs were just ornaments: "Neque ea est Literarum aut Characterum aliqua Scriptura legenda, sed tantum Sculptura ornamenti causa." Hyde {cite:year}`hyde_1700`, *id*.
# 
# `````
# 
# The texts were written on clay, and they just contained personal names and lists of goods. The identification of a language behind these ideograms is problematic, although it is very probable that it was Sumerian[^krebernik_2022] The first understandable texts come from Ur from around the 28th century BCE. They are undoubtedly written in Sumerian. Already in these texts a Semitic name, very likely an Akkadian name, is attested.[^sallaberger_2004] This shows the coexistence of these two languages from almost the beginning of written Mesopotamian history. This form of writing together with the Akkadian language spread throughout Mesopotamia and became dominant in the ancient Near East until the 1st Millennium BCE, when they were gradually replaced by the Aramaic language and its alphabetic script.[^streck_2007] Not only Sumerian and Akkadian used the cuneiform script, but also Hittite, Hurrian, Elamite, Ugaritic and several other smaller languages around the ancient Near East.
# 
# [^krebernik_2022]: Krebernik 2022, p. 1 fn. 1.
# [^sallaberger_2004]: Sallaberger 2004, p. 108.
# [^streck_2007]: Streck 2007, p. 47.
# 
# ## Development
# At the beginning the signs were written, drawing them on wet clay tablets 
# 
# (Picture of a transliteration translation from our corpus)
# 
# 
# At some point in the third millennium, the script was turned 90° clockwise (according to Benjamin Studevent-Hickman in the Sargonic Period, between 2334-2193 BCE in middle chronology terms),[^studevent_2007] the drawing lines were divided in strokes pressed on the wet clay tablet, losing in this way the iconic character and becoming symbolic signs. Following a rebus principle the signs began to represent sounds, but they kept their iconic use, i.e. they could be used for representing those objects for which they were invented (see Fig. #). 
# 
# [^studevent_2007]: Studevent-Hickmann 2007, p. 499.
# 
# The iconic character of the original sign is visible. The Sumerian word for water is /a/. In this use it can be called a logogram, a pictogram or sometimes a sumerogram. It was turned clockwise 90° and became a symbolic sign that could also have a phonetic value. In this case /a/. Over time it acquired new phonetic and logographic values. In this case up to 24 phonetic values and 3 logographic values (if we count the cases where it is the first part of a composite sign, the number of possibilities is even higher). This is representative for all cuneiform signs. They can have more than one phonetic and logographic value.
# 
# ## Cuneiform Signs
# Each sign can consists on following elements:
# 
# | Element | Wedge | 
# | -------- | -------- | 
# | horizontal wedge | <font size="11">𒀸</font> |
# | vertical wedge | <font size="11">𒁹</font> |
# | diagonal wedge | <font size="11">𒀹</font> |
# | winckelhacken | <font size="11">𒌋</font> |
# 
# ## Types of Signs
# We can find three types of functions: 
# 
# - **Logograms**: It represents one or many words. Ocasionally it is also called Sumerogram. In most cases designated by capitals in the transliteration.
# 
#     | Sign | Logogram | Akkadian | Translation |
#     | -------- | :--------: | :---------: |:----:|
#     | <font size="11">𒌓</font> | UTU | *šamaš* |sun
#     | <font size="11">𒌓</font> | U₄ | *umu* |day
#     | <font size="11">𒌓</font> | BABBAR | *peṣû* | white
# 
# - **Phonograms/syllabograms**: It represents syllables or vowels. A sign can have more than one syllabic/vocalic value. Depending on the Language, in Sumerian, they appear in normal script in the transliteration (sometimes sans serif) and in Akkadian, they appear in italics.
# 
#     | Sign | Sign Name |Syllabic writing | 
#     | -------- | :--------: | :----: |
#     | <font size="11">𒆳</font> | KUR |*kur* | 
#     | <font size="11">𒆳</font> | KUR |*šat* |
#     | <font size="11">𒆳</font> | KUR| *mat* |
#     | <font size="11">𒆳</font> | KUR| *lat* |
#     | <font size="11">𒅎</font> | IM |*im*|
#     | <font size="11">𒈾</font> | NA | *na*
# 
# - **Determinative**: It represents a semantic field and is placed before or after a logogram. In printed transliterations it is designated with superscript, but in the digital transliteration it appears in curly brackets.
# 
#     | Sign | Sign Name | Determinativ | Semantic Field | Example | Translation |
#     | -----| :-------: | :----------: | :------------: | :-----: | :---------: |
#     | <font size="11">𒀭</font> | AN | dingir (<sup>d</sup>) | Deities | <sup>d</sup>UTU |
#     | <font size="11">𒄑</font> | GIŠ |ĝeš | Wood objects | <sup>|</sup> | |
#     | <font size="11">𒌑</font> | U₂| u₂ | Plant names | | |
#     | <font size="11">𒆳</font> | KUR| kur | City names | || 
#    
# It is important to note that most of the signs can have two types of functions and some even the three types:
# 
# | Sign | Sign Name | Logogram | Phonogram | Determinativ
# | -------- | -------- | --| ---| ---|
# | <font size="11">𒀭</font> | AN | AN (heaven)|an | dingir
# | <font size="11">𒄑</font> | GIŠ |GIŠ (wood) | is | ĝeš
# | <font size="11">𒆳</font> | KUR| KUR (land) | mat | kur
# | <font size="11">𒀀</font> | A | A (water) | a | -
# | <font size="11">𒆷</font> | LA | LA (plenty) | la | - | 
#     
# Example
# 
# ## Types of Phonograms
# There are four types:
# 
# | Phonogram | Example | Cuneiform |
# | -------- | -------- | --------- |
# | CV[^\*] | ma | <font size="11">𒈠</font>
# | VC | ad | <font size="11">𒀜</font>
# | CVC | lum | <font size="11">𒈝</font>
# | V | a | <font size="11">𒀀</font>
# 
# [^\*]: C = consonant, V = vowel
# 
# ## Orthography
# Words can be written logographic as well as syllabic:
# 
# | Logogram | Cuneiform | Syllabic writing | Cuneiform |
# | -------- | -------- | --------- | ---------- |
# | E₂ | <font size="11">𒂍</font> | *bi-tu-um* | <font size="11">𒁉𒌅𒌝</font> |
# | EN | <font size="11">𒂗</font> | *be-lu-um* | <font size="11">𒁁𒇻𒌝</font> |
# | GAL | <font size="11">𒃲</font> | *ra-bu-um* | <font size="11">𒊏𒁍𒌝</font> |
# 
# ## Number of Signs
# The cuneiform writing, considered from its beginning until the end of its use, has about 1000 signs. Nevertheless, at no period of time were they used in its entirety. It varied from period to period, genres, etc. Besides, the shape of the signs changed geographically as well as diachronically. 
# 
