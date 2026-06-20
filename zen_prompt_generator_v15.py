
import streamlit as st
import random

st.set_page_config(
    page_title="禅意美学图片提示词生成器 V1.5",
    page_icon="🍃",
    layout="centered"
)

st.title("🍃 禅意美学图片提示词生成器 V1.5")
st.caption("输入一个关键词，自动生成留白多、静心、禅意、适合海报设计的 AI 图片提示词。")

SUBJECT_MAP = {
    "流水": ["flowing water", "mountain stream", "quiet river", "stone creek"],
    "水": ["still water", "flowing water", "quiet lake", "mountain stream"],
    "石头": ["solitary stone", "moss-covered stone", "zen garden stone", "river stone"],
    "石": ["solitary stone", "moss-covered rock", "river stone"],
    "竹林": ["bamboo grove", "misty bamboo forest", "quiet bamboo path"],
    "竹": ["bamboo grove", "fresh bamboo leaves", "bamboo forest in morning light"],
    "莲花": ["lotus flower", "still pond with lotus", "lotus with morning dew"],
    "莲": ["lotus flower", "quiet lotus pond"],
    "山": ["misty mountain", "distant mountain peak", "quiet mountain landscape"],
    "云": ["sea of clouds", "soft drifting clouds", "open sky with clouds"],
    "树": ["ancient tree", "solitary tree", "old tree in soft morning light"],
    "庭院": ["quiet oriental courtyard", "zen courtyard", "traditional courtyard in morning light"],

    "茶": ["solitary tea cup", "simple clay teapot", "traditional tea setting"],
    "禅茶": ["solitary tea cup on a wooden table", "clay teapot with rising steam"],
    "香": ["incense burner", "soft incense smoke", "quiet incense ritual"],
    "读书": ["open book beside tea", "quiet reading corner", "book on wooden table"],
    "书": ["open book in soft window light", "book beside a tea cup"],

    "家庭": ["family walking quietly in nature", "three generations beneath an ancient tree"],
    "亲子": ["parent and child walking along a quiet path", "parent and child planting a young tree"],
    "陪伴": ["small family figures walking in a vast landscape", "two people sitting quietly beneath a tree"],
    "团圆": ["three generations gathered beneath a large tree", "family reunion in warm evening light"],

    "学堂": ["small mindfulness academy hidden among bamboo groves", "quiet learning courtyard in morning light"],
    "小院": ["small oriental courtyard surrounded by greenery", "mindfulness courtyard in bamboo forest"],
    "法务": ["glowing root network beneath a bamboo forest", "bamboo forest with connected roots underground"],
    "合规": ["glowing roots supporting small courtyards", "orderly bamboo grove with luminous root system"],
    "生态": ["living ecosystem with bamboo, water and soft sunlight", "interconnected natural landscape"],
    "公益": ["young tree growing in morning sunlight", "river flowing through a warm green landscape"],
}

CONCEPT_MAP = {
    "智慧": ["morning light passing through ancient trees", "a quiet path leading toward distant mountains"],
    "自在": ["open sky above distant mountains", "sea of clouds with vast negative space"],
    "成长": ["young tree growing in soft golden sunlight", "seedling emerging from rich soil"],
    "希望": ["sunrise over a quiet green landscape", "new leaves glowing in morning light"],
    "安定": ["ancient tree standing in a peaceful open landscape", "quiet courtyard in soft light"],
    "觉察": ["single tea cup with rising steam in soft window light", "still water reflecting the sky"],
    "传承": ["three generations beneath an ancient tree", "old tree and young sapling growing together"],
    "共生": ["interconnected forest and river ecosystem", "bamboo forest with glowing root network"],
    "信任": ["bridge connecting two quiet courtyards", "warm light connecting small houses in mist"],
    "长期": ["ancient tree with deep roots", "mountain landscape in early morning sunlight"],
    "治理": ["orderly bamboo forest with glowing underground roots", "small courtyards connected by subtle light paths"],
    "秩序": ["bamboo standing independently in clean rhythmic composition", "raked sand garden with a single stone"],
}

STYLE_RULES = {
    "academy": ["MPI", "法务", "合规", "治理", "秩序", "静心生态", "静心学堂", "静心小院", "学堂", "小院"],
    "family": ["家庭", "亲子", "陪伴", "团圆", "传承"],
    "life": ["成长", "希望", "公益", "教育", "生态", "共生"],
    "tea": ["茶", "禅茶", "香", "读书", "书", "独处"],
    "culture": ["智慧", "自在", "觉察", "读书会", "文化", "课程", "讲座"],
    "wabi": ["石头", "石", "枯山水", "孤独", "空"],
}

STYLE_CONFIG = {
    "wabi": {
        "name": "侘寂禅意",
        "colors": ["soft gray tones", "warm beige", "muted earth tones", "natural stone colors", "low saturation palette"],
        "moods": ["stillness", "silence", "quiet contemplation", "emptiness", "wabi-sabi philosophy"],
    },
    "tea": {
        "name": "茶禅",
        "colors": ["warm wood tones", "soft beige", "muted green", "gentle tea brown", "soft window light palette"],
        "moods": ["slow living", "present moment awareness", "inner clarity", "quiet contemplation", "gentle warmth"],
    },
    "life": {
        "name": "生命禅意",
        "colors": ["fresh bamboo green", "lotus green", "warm golden sunlight", "soft white clouds", "light jade tones"],
        "moods": ["hope", "growth", "harmony", "living energy", "peaceful awakening"],
    },
    "family": {
        "name": "家庭禅意",
        "colors": ["warm sunlight", "soft green tones", "warm white", "gentle earth colors", "soft golden atmosphere"],
        "moods": ["quiet companionship", "sense of belonging", "gentle connection", "peaceful happiness", "emotional stillness"],
    },
    "academy": {
        "name": "静心生态",
        "colors": ["fresh bamboo green", "warm morning gold", "soft white clouds", "light jade tones", "gentle luminous green"],
        "moods": ["stability", "trust", "responsibility", "long-term vision", "harmony and order", "interconnectedness"],
    },
    "culture": {
        "name": "文化禅意",
        "colors": ["soft ink gray", "warm paper white", "muted green", "natural wood tones", "gentle golden light"],
        "moods": ["wisdom", "inner clarity", "quiet learning", "cultural depth", "mindfulness"],
    },
}

LIGHTS = [
    "soft morning light",
    "gentle diffused sunlight",
    "warm golden hour light",
    "subtle window light",
    "morning mist illuminated by sunlight",
]

NEGATIVE_SPACE = [
    "vast negative space",
    "large blank area",
    "minimal composition",
    "sparse visual elements",
    "empty foreground",
    "breathing room",
    "clean visual balance",
]

AESTHETICS = [
    "oriental zen aesthetics",
    "poetic atmosphere",
    "natural textures",
    "minimalist oriental aesthetics",
    "quiet and contemplative atmosphere",
]

PHOTO_STYLE = [
    "fine art photography",
    "museum quality",
    "editorial visual style",
    "cinematic natural lighting",
    "ultra realistic photography",
    "Hasselblad medium format",
    "masterpiece",
    "8k",
]

POSTER_TERMS = [
    "poster design friendly",
    "large typography area",
    "copy space",
    "clean layout",
    "premium cultural poster design",
]

COMPOSITION_RULES = {
    "山": "mountain placed in the lower third, large blank sky above",
    "云": "wide open sky composition, subject placed low in the frame",
    "茶": "tea cup placed in the lower right corner, large empty space above",
    "禅茶": "tea setting placed asymmetrically, large blank area for title typography",
    "竹": "bamboo placed on one side of the frame, vertical rhythm and quiet negative space",
    "竹林": "bamboo path receding into mist, strong vertical composition",
    "石": "single stone placed off-center, empty sand or ground surrounding it",
    "石头": "solitary stone placed off-center with abundant blank space",
    "家庭": "small family figures seen from a distance, vast landscape surrounding them",
    "亲子": "parent and child as small figures in the lower third, open sky above",
    "法务": "bamboo forest above ground, glowing root network visible beneath the earth",
    "合规": "small courtyards connected by luminous roots, balanced and orderly composition",
    "学堂": "small academy courtyard hidden in bamboo forest, large blank sky area",
    "小院": "quiet courtyard placed in lower third, soft mist and blank space above",
}

def detect_subject(keyword: str):
    for key in sorted(SUBJECT_MAP.keys(), key=len, reverse=True):
        if key in keyword:
            return random.choice(SUBJECT_MAP[key]), key

    for key in sorted(CONCEPT_MAP.keys(), key=len, reverse=True):
        if key in keyword:
            return random.choice(CONCEPT_MAP[key]), key

    return keyword, keyword

def detect_style(keyword: str):
    priority = ["academy", "family", "life", "tea", "culture", "wabi"]
    for style in priority:
        for word in STYLE_RULES[style]:
            if word in keyword:
                return style
    return "life"

def detect_composition(keyword: str, matched_key: str):
    for key in sorted(COMPOSITION_RULES.keys(), key=len, reverse=True):
        if key in keyword or key == matched_key:
            return COMPOSITION_RULES[key]
    return "main subject placed asymmetrically within the frame, large blank area reserved for typography"

def generate_prompt(keyword, poster=True, vertical=True, style_override="自动识别"):
    subject, matched_key = detect_subject(keyword)
    style_key = detect_style(keyword)

    if style_override != "自动识别":
        style_name_to_key = {v["name"]: k for k, v in STYLE_CONFIG.items()}
        style_key = style_name_to_key.get(style_override, style_key)

    config = STYLE_CONFIG[style_key]
    composition = detect_composition(keyword, matched_key)

    prompt_parts = [
        f"A zen-inspired fine art photography scene featuring {subject}",
        composition,
        random.choice(LIGHTS),
        *random.sample(NEGATIVE_SPACE, 5),
        *random.sample(config["moods"], min(4, len(config["moods"]))),
        *random.sample(config["colors"], min(4, len(config["colors"]))),
        *random.sample(AESTHETICS, 4),
        *random.sample(PHOTO_STYLE, 7),
    ]

    if poster:
        prompt_parts.extend(POSTER_TERMS)

    if vertical:
        prompt_parts.append("vertical composition, 2:3 aspect ratio")

    return ",\n".join(prompt_parts), config["name"], subject, composition

keyword = st.text_input(
    "请输入关键词",
    placeholder="例如：流水、石头、竹林、禅茶、家庭、成长、智慧、希望、共生"
)

col1, col2 = st.columns(2)
with col1:
    poster_mode = st.checkbox("用于海报设计", value=True)
with col2:
    vertical_mode = st.checkbox("竖版 2:3", value=True)

style_options = ["自动识别"] + [STYLE_CONFIG[k]["name"] for k in STYLE_CONFIG]
style_override = st.selectbox("禅意风格", style_options)

if st.button("生成提示词", type="primary"):
    if not keyword.strip():
        st.warning("请先输入一个关键词。")
    else:
        prompt, style_name, subject, composition = generate_prompt(
            keyword.strip(),
            poster=poster_mode,
            vertical=vertical_mode,
            style_override=style_override
        )

        st.success("已生成禅意美学图片提示词")

        st.subheader("识别结果")
        c1, c2 = st.columns(2)
        c1.metric("禅意风格", style_name)
        c2.metric("视觉主体", subject)

        st.write(f"**构图策略：** {composition}")

        st.subheader("AI 图片提示词")
        st.code(prompt, language="text")

        st.download_button(
            "下载提示词 TXT",
            data=prompt,
            file_name="zen_image_prompt_v15.txt",
            mime="text/plain"
        )

st.divider()

with st.expander("V1.5 优化内容"):
    st.write("1. 保留 V1：用户只输入一个关键词。")
    st.write("2. 新增：侘寂禅意、茶禅、生命禅意、家庭禅意、文化禅意、静心生态。")
    st.write("3. 新增：抽象概念映射，例如“智慧、成长、自在、希望、共生、法务”。")
    st.write("4. 新增：根据关键词自动匹配构图方式。")
    st.write("5. 默认更偏向温暖、生命力、光明的禅意，而不是灰色棕色的枯寂感。")

st.caption("适用于 Midjourney、即梦、GPT 图像、Flux、Stable Diffusion 等 AI 绘图工具。")
