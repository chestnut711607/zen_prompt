
import streamlit as st
import random

st.set_page_config(page_title="禅意美学图片提示词生成器", page_icon="🍵", layout="centered")

st.title("🍵 禅意美学图片提示词生成器")
st.caption("输入一个关键词，自动生成适合海报设计的禅意摄影图提示词。")

SUBJECT_MAP = {
    "流水": ["flowing water", "mountain stream", "quiet river", "stone creek"],
    "石头": ["solitary stone", "moss-covered rock", "zen garden stone", "river stone"],
    "竹林": ["bamboo grove", "misty bamboo forest", "quiet bamboo path"],
    "茶": ["solitary tea cup", "simple clay teapot", "traditional tea setting"],
    "禅茶": ["solitary tea cup on a wooden table", "clay teapot with rising steam"],
    "莲花": ["lotus flower", "still pond with lotus", "lotus with morning dew"],
    "山": ["misty mountain", "distant mountain peak", "quiet mountain landscape"],
    "云": ["sea of clouds", "soft drifting clouds", "misty sky"],
    "树": ["ancient tree", "solitary tree", "old tree in mist"],
    "庭院": ["quiet zen courtyard", "traditional oriental courtyard"],
    "家庭": ["family walking quietly", "parent and child under soft light", "three generations beneath an old tree"],
}

LIGHTS = [
    "soft morning light",
    "gentle diffused sunlight",
    "overcast natural light",
    "soft golden hour light",
    "subtle window light",
]

MOODS = [
    "stillness",
    "inner peace",
    "quiet contemplation",
    "mindfulness",
    "tranquility",
    "emotional stillness",
]

SPACES = [
    "vast negative space",
    "large blank area",
    "minimal composition",
    "sparse visual elements",
    "empty foreground",
    "breathing room",
]

AESTHETICS = [
    "oriental zen aesthetics",
    "wabi-sabi philosophy",
    "poetic atmosphere",
    "natural textures",
    "soft gray and muted earth tones",
]

PHOTO_STYLE = [
    "fine art photography",
    "museum quality",
    "cinematic natural lighting",
    "editorial visual style",
    "ultra realistic photography",
    "Hasselblad medium format",
    "masterpiece",
    "8k",
]

POSTER = [
    "poster design friendly",
    "large typography area",
    "copy space",
    "clean layout",
]

def match_subject(keyword):
    for key, values in SUBJECT_MAP.items():
        if key in keyword:
            return random.choice(values)
    return keyword

def generate_prompt(keyword, poster=True, vertical=True):
    subject = match_subject(keyword)

    prompt_parts = [
        f"A zen-inspired fine art photography scene featuring {subject}",
        random.choice(LIGHTS),
        random.choice(MOODS),
        *random.sample(SPACES, 4),
        *random.sample(AESTHETICS, 3),
        *random.sample(PHOTO_STYLE, 6),
    ]

    if poster:
        prompt_parts.extend(POSTER)

    if vertical:
        prompt_parts.append("vertical composition, 2:3 aspect ratio")

    return ",\n".join(prompt_parts)

keyword = st.text_input("请输入画面关键词", placeholder="例如：流水、石头、竹林、禅茶、家庭、莲花、山峰")

col1, col2 = st.columns(2)
with col1:
    poster_mode = st.checkbox("用于海报设计", value=True)
with col2:
    vertical_mode = st.checkbox("竖版 2:3", value=True)

if st.button("生成提示词", type="primary"):
    if not keyword.strip():
        st.warning("请先输入一个关键词。")
    else:
        prompt = generate_prompt(keyword.strip(), poster_mode, vertical_mode)
        st.subheader("生成结果")
        st.code(prompt, language="text")

        st.subheader("中文理解")
        st.write(f"这是一张以 **{keyword}** 为主体的禅意美学摄影图，画面留白较多，气质安静、克制、适合用于文化类、东方美学类、品牌海报类视觉设计。")

st.divider()
st.caption("提示：你可以把生成结果复制到 Midjourney、即梦、GPT 图像、Flux、Stable Diffusion 等工具中使用。")
